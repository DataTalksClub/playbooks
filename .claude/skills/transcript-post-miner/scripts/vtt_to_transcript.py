#!/usr/bin/env python3
"""Convert a WebVTT transcript (for example a Zoom recording transcript) into full_transcript.json.

Writes `full_transcript.json` ({"text", "segments": [{start, end, speaker, text}]}),
the same shape as the YouTube fetcher and `transcribe_local.py`, plus a `speaker`
field on each segment, so the rest of the transcript-post-miner workflow is
unchanged.

    python3 .claude/skills/transcript-post-miner/scripts/vtt_to_transcript.py TRANSCRIPT.vtt \
      --output content-runs/<run>/source --video RECORDING.mp4

- Reads speakers from Zoom's `Name: text` cue prefix or a WebVTT `<v Name>` tag.
- --video compares the transcript end with the video duration and warns when
  they differ by more than a few seconds, which means clip timestamps from the
  transcript would not match the video.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

TIMING = re.compile(r"^\s*(\S+)\s+-->\s+(\S+)")
VOICE = re.compile(r"^<v(?:\.[^ >]*)?\s+([^>]+)>(.*)$")
ZOOM_SPEAKER = re.compile(r"^([^:]{1,60}):\s+(.*)$")
TAG = re.compile(r"</?[^>]+>")


def seconds(value: str) -> float:
    parts = value.replace(",", ".").split(":")
    if len(parts) == 2:
        parts.insert(0, "0")
    hours, minutes, secs = parts
    return int(hours) * 3600 + int(minutes) * 60 + float(secs)


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout
    return float(out.strip())


def parse_vtt(source: str) -> list[dict]:
    cues: list[tuple[str, str, str]] = []
    for block in re.split(r"\n\s*\n", source.replace("\r\n", "\n").strip()):
        lines = block.strip().split("\n")
        timing_index = next((i for i, line in enumerate(lines) if TIMING.match(line)), None)
        if timing_index is None:
            continue  # WEBVTT header, NOTE, STYLE, or REGION block
        start, end = TIMING.match(lines[timing_index]).groups()
        cues.append((start, end, " ".join(line.strip() for line in lines[timing_index + 1 :])))

    # Zoom writes "Name: text" on every cue. Only read that prefix as a speaker when
    # the file has no <v> tags and most cues have it, so a plain "Step 1: ..." caption
    # is not taken for a name.
    plain = [TAG.sub("", text).strip() for _, _, text in cues]
    has_voices = any(VOICE.match(text) for _, _, text in cues)
    zoom_style = not has_voices and sum(bool(ZOOM_SPEAKER.match(text)) for text in plain) > len(cues) / 2

    segments: list[dict] = []
    for (start, end, raw), text in zip(cues, plain):
        speaker = ""
        voice = VOICE.match(raw)
        if voice:
            speaker, text = voice.group(1).strip(), TAG.sub("", voice.group(2)).strip()
        elif zoom_style and ZOOM_SPEAKER.match(text):
            speaker, text = [part.strip() for part in ZOOM_SPEAKER.match(text).groups()]
        if text:
            segments.append({"start": round(seconds(start), 2), "end": round(seconds(end), 2),
                             "speaker": speaker, "text": text})
    return segments


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert a WebVTT transcript into full_transcript.json.")
    parser.add_argument("vtt", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="Folder for full_transcript.json.")
    parser.add_argument("--video", type=Path, help="The matching recording, to check that the timestamps line up.")
    args = parser.parse_args()

    vtt = args.vtt.expanduser().resolve()
    if not vtt.is_file():
        raise SystemExit(f"Transcript not found: {vtt}")
    segments = parse_vtt(vtt.read_text(encoding="utf-8-sig"))
    if not segments:
        raise SystemExit(f"No cues found in {vtt}")

    transcript_end = max(s["end"] for s in segments)
    transcript = {"text": " ".join(s["text"] for s in segments), "segments": segments,
                  "method": f"vtt {vtt.name}", "duration_seconds": round(transcript_end)}
    if args.video:
        video_seconds = duration(args.video.expanduser())
        transcript["duration_seconds"] = round(video_seconds)
        gap = video_seconds - transcript_end
        if gap < -1 or gap > 5:
            print(f"warning: transcript ends at {transcript_end:.1f}s but the video is {video_seconds:.1f}s long; "
                  "timestamps may not match the video", file=sys.stderr)
        else:
            print(f"video check: transcript ends {gap:.1f}s before the end of the video "
                  f"(video duration_seconds {round(video_seconds)})")

    out = args.output.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    (out / "full_transcript.json").write_text(json.dumps(transcript, indent=1, ensure_ascii=False), encoding="utf-8")
    speakers = Counter(s["speaker"] or "(no speaker)" for s in segments)
    print(f"wrote {out / 'full_transcript.json'}: {len(segments)} segments; "
          + ", ".join(f"{name} {count}" for name, count in speakers.most_common()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
