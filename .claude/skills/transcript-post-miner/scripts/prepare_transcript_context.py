#!/usr/bin/env python3
"""Create timestamped Markdown windows from a full_transcript.json file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def format_ts(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def load_segments(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    segments = data.get("segments", [])
    if not isinstance(segments, list):
        raise SystemExit(f"`segments` must be a list in {path}")
    return [
        {
            "start": float(seg.get("start", 0.0)),
            "end": float(seg.get("end", seg.get("start", 0.0))),
            "text": str(seg.get("text", "")).replace("\n", " ").strip(),
        }
        for seg in segments
        if str(seg.get("text", "")).strip()
    ]


def make_windows(
    segments: list[dict[str, Any]],
    *,
    window_seconds: int,
    overlap_seconds: int,
) -> list[tuple[float, float, list[dict[str, Any]]]]:
    if not segments:
        return []
    start = segments[0]["start"]
    duration_end = max(seg["end"] for seg in segments)
    windows: list[tuple[float, float, list[dict[str, Any]]]] = []
    cursor = start
    step = max(1, window_seconds - overlap_seconds)
    while cursor < duration_end:
        end = min(duration_end, cursor + window_seconds)
        items = [seg for seg in segments if cursor <= seg["start"] < end]
        if items:
            windows.append((cursor, end, items))
        cursor += step
    return windows


def render_markdown(
    transcript_path: Path,
    segments: list[dict[str, Any]],
    windows: list[tuple[float, float, list[dict[str, Any]]]],
) -> str:
    duration = max((seg["end"] for seg in segments), default=0.0)
    lines = [
        "# Transcript Context",
        "",
        f"Source: {transcript_path}",
        f"Duration: {format_ts(duration)}",
        f"Segments: {len(segments)}",
        "",
        "Use these windows to mine social post ideas across the full transcript. Ideas may span multiple windows.",
        "",
    ]
    for index, (start, end, items) in enumerate(windows, start=1):
        lines.extend(
            [
                f"## Window {index:03d}: {format_ts(start)} - {format_ts(end)}",
                "",
            ]
        )
        for seg in items:
            lines.append(
                f"[{format_ts(seg['start'])} - {format_ts(seg['end'])}] {seg['text']}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert full_transcript.json into timestamped Markdown windows.",
    )
    parser.add_argument("transcript_json", type=Path, help="Path to full_transcript.json")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output Markdown path. Defaults to transcript-context.md next to the transcript.",
    )
    parser.add_argument(
        "--window-seconds",
        type=int,
        default=600,
        help="Window size in seconds (default: 600).",
    )
    parser.add_argument(
        "--overlap-seconds",
        type=int,
        default=30,
        help="Window overlap in seconds (default: 30).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    transcript_path = args.transcript_json.expanduser().resolve()
    if not transcript_path.is_file():
        raise SystemExit(f"Transcript not found: {transcript_path}")
    if args.window_seconds <= 0:
        raise SystemExit("--window-seconds must be positive")
    if args.overlap_seconds < 0 or args.overlap_seconds >= args.window_seconds:
        raise SystemExit("--overlap-seconds must be >= 0 and smaller than --window-seconds")

    segments = load_segments(transcript_path)
    windows = make_windows(
        segments,
        window_seconds=args.window_seconds,
        overlap_seconds=args.overlap_seconds,
    )
    output = args.output or transcript_path.with_name("transcript-context.md")
    if not output.is_absolute():
        output = Path.cwd() / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(transcript_path, segments, windows), encoding="utf-8")
    print(f"Wrote {len(windows)} transcript windows to {output}")


if __name__ == "__main__":
    main()
