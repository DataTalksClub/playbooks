#!/usr/bin/env python3
"""Create a clip manifest CSV from transcript-post-miner post-ideas JSON."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}$")


def clean_filename(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value[:80] or "clip"


def read_ideas(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ideas = data.get("ideas", [])
    if not isinstance(ideas, list):
        raise SystemExit(f"`ideas` must be a list in {path}")
    return ideas


def manifest_rows(ideas: list[dict[str, Any]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, idea in enumerate(ideas, start=1):
        clip = idea.get("clip") or {}
        if not clip.get("recommended"):
            continue
        start = str(clip.get("start", "")).strip()
        end = str(clip.get("end", "")).strip()
        if not TIMESTAMP_RE.match(start) or not TIMESTAMP_RE.match(end):
            raise SystemExit(
                f"Invalid clip timestamps for {idea.get('id') or index}: {start!r} - {end!r}"
            )
        idea_id = str(idea.get("id") or f"idea_{index:03d}")
        title = str(clip.get("title") or idea.get("title") or idea_id).strip()
        rows.append(
            {
                "idea_id": idea_id,
                "title": title,
                "clip_start": start,
                "clip_end": end,
                "clip_quality": str(clip.get("quality", "")).strip(),
                "clip_reason": str(clip.get("reason", "")).strip(),
                "output_file": f"{idea_id}-{clean_filename(title)}.mp4",
            }
        )
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create clip-manifest.csv from transcript-post-miner post-ideas.json.",
    )
    parser.add_argument("post_ideas_json", type=Path, help="Path to post-ideas.json")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output CSV path. Defaults to clip-manifest.csv next to post-ideas.json.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ideas_path = args.post_ideas_json.expanduser().resolve()
    if not ideas_path.is_file():
        raise SystemExit(f"Post ideas JSON not found: {ideas_path}")
    output = args.output or ideas_path.with_name("clip-manifest.csv")
    if not output.is_absolute():
        output = Path.cwd() / output
    rows = manifest_rows(read_ideas(ideas_path))
    fieldnames = [
        "idea_id",
        "title",
        "clip_start",
        "clip_end",
        "clip_quality",
        "clip_reason",
        "output_file",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"Wrote {len(rows)} clip rows to {output}")


if __name__ == "__main__":
    main()
