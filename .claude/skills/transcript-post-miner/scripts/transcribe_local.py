#!/usr/bin/env python3
"""Transcribe a local video on this machine with Whisper, when YouTube has no captions.

Writes `full_transcript.json` ({"text", "segments": [{start, end, text}]}), the
same shape as the YouTube fetcher, so the rest of the transcript-post-miner
workflow is unchanged.

- Runs mlx-whisper (Apple Silicon) through `uv`, so nothing needs installing:
    uv run --with mlx-whisper python3 .claude/skills/transcript-post-miner/scripts/transcribe_local.py VIDEO --output DIR
- Transcribes in chunks and saves each chunk as it finishes; a rerun skips
  finished chunks, so a crash or interruption never loses work.
- --names seeds Whisper with the speaker and product names from the event
  source, which fixes most misspellings (for example "Louis", not "Luis").
- Drops Whisper's repetition loops over silence (the same short line many
  times in a row) and reports how many segments were dropped.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, capture_output=True)


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout
    return float(out.strip())


def drop_loops(segments: list[dict], min_repeats: int = 4) -> tuple[list[dict], int]:
    """Remove runs of the same short text repeated min_repeats+ times (Whisper loops)."""
    kept: list[dict] = []
    dropped = 0
    i = 0
    while i < len(segments):
        j = i
        key = segments[i]["text"].strip().lower().rstrip(".")
        while j + 1 < len(segments) and segments[j + 1]["text"].strip().lower().rstrip(".") == key:
            j += 1
        run_length = j - i + 1
        if run_length >= min_repeats and len(key) <= 40:
            dropped += run_length
        else:
            kept.extend(segments[i : j + 1])
        i = j + 1
    return kept, dropped


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe a local video with Whisper, chunked and resumable.")
    parser.add_argument("video", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="Folder for full_transcript.json and chunk checkpoints.")
    parser.add_argument("--names", default="", help="Comma-separated names and terms to prime Whisper, for example 'Louis Amaudruz, Switch, SandboxAQ'.")
    parser.add_argument("--model", default="mlx-community/whisper-large-v3-turbo")
    parser.add_argument("--chunk-minutes", type=float, default=10)
    parser.add_argument("--language", default="en")
    args = parser.parse_args()

    try:
        import mlx_whisper  # noqa: PLC0415
    except ImportError:
        raise SystemExit("mlx-whisper is not available. Run through: uv run --with mlx-whisper python3 " + " ".join(sys.argv))

    out = args.output.expanduser().resolve()
    chunks_dir = out / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    total = duration(args.video)
    step = args.chunk_minutes * 60
    prompt = f"{args.names}." if args.names else None

    segments: list[dict] = []
    index = 0
    start = 0.0
    while start < total - 1:
        done = chunks_dir / f"chunk_{index:03d}.json"
        if not done.exists():
            audio = chunks_dir / f"chunk_{index:03d}.wav"
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(step), "-i", str(args.video),
                 "-vn", "-ac", "1", "-ar", "16000", str(audio)])
            result = mlx_whisper.transcribe(str(audio), path_or_hf_repo=args.model, language=args.language, initial_prompt=prompt)
            chunk = [{"start": round(s["start"] + start, 2), "end": round(s["end"] + start, 2), "text": s["text"].strip()}
                     for s in result["segments"] if s["text"].strip()]
            done.write_text(json.dumps(chunk, ensure_ascii=False), encoding="utf-8")
            audio.unlink()
            print(f"chunk {index}: {len(chunk)} segments ({start / 60:.0f}-{min(start + step, total) / 60:.0f} min)", flush=True)
        segments.extend(json.loads(done.read_text(encoding="utf-8")))
        index += 1
        start += step

    segments, dropped = drop_loops(segments)
    transcript = {"text": " ".join(s["text"] for s in segments), "segments": segments,
                  "method": f"local {args.model}", "duration_seconds": round(total)}
    (out / "full_transcript.json").write_text(json.dumps(transcript, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out / 'full_transcript.json'}: {len(segments)} segments, dropped {dropped} repeated-loop segments")
    return 0


if __name__ == "__main__":
    sys.exit(main())
