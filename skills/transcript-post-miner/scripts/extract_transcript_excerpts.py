#!/usr/bin/env python3
"""Extract raw transcript excerpts for approved social post briefs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def ts_to_seconds(value: str) -> int:
    parts = value.strip().split(":")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError(f"Expected HH:MM:SS timestamp, got {value!r}")
    hours, minutes, seconds = [int(part) for part in parts]
    return hours * 3600 + minutes * 60 + seconds


def load_segments(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    segments = data.get("segments", [])
    if not isinstance(segments, list):
        raise SystemExit(f"`segments` must be a list in {path}")
    return segments


def excerpt(segments: list[dict[str, Any]], start: int, end: int) -> str:
    parts: list[str] = []
    for segment in segments:
        segment_start = float(segment.get("start", 0.0))
        if start <= segment_start < end:
            text = str(segment.get("text", "")).replace("\n", " ").strip()
            if text:
                parts.append(text)
    return " ".join(parts).strip()


def parse_range(value: str) -> tuple[str, str, int, int]:
    if "-" not in value:
        raise argparse.ArgumentTypeError("Range must look like HH:MM:SS-HH:MM:SS")
    start_s, end_s = [part.strip() for part in value.split("-", 1)]
    start = ts_to_seconds(start_s)
    end = ts_to_seconds(end_s)
    if end <= start:
        raise argparse.ArgumentTypeError("Range end must be after start")
    return start_s, end_s, start, end


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract raw transcript excerpts from full_transcript.json.",
    )
    parser.add_argument("transcript_json", type=Path, help="Path to full_transcript.json")
    parser.add_argument(
        "--range",
        action="append",
        required=True,
        dest="ranges",
        help="Timestamp range as HH:MM:SS-HH:MM:SS. Can be provided multiple times.",
    )
    parser.add_argument("--title", default="Transcript Excerpts", help="Markdown title.")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    transcript_path = args.transcript_json.expanduser().resolve()
    if not transcript_path.is_file():
        raise SystemExit(f"Transcript not found: {transcript_path}")
    segments = load_segments(transcript_path)
    lines = [f"# {args.title}", "", f"Source: {transcript_path}", ""]
    for raw_range in args.ranges:
        start_s, end_s, start, end = parse_range(raw_range)
        lines.extend(
            [
                f"## {start_s} - {end_s}",
                "",
                excerpt(segments, start, end),
                "",
            ]
        )
    output_text = "\n".join(lines).rstrip() + "\n"
    if args.output:
        output = args.output.expanduser()
        if not output.is_absolute():
            output = Path.cwd() / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(output_text, encoding="utf-8")
        print(f"Wrote transcript excerpts to {output}")
    else:
        print(output_text, end="")


if __name__ == "__main__":
    main()
