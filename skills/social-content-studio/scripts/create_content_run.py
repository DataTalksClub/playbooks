#!/usr/bin/env python3
"""Create a Social Content Studio content-run folder."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "content-run"


def parse_platforms(value: str) -> list[str]:
    platforms = [item.strip().lower() for item in value.split(",") if item.strip()]
    return platforms or ["linkedin"]


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a content run folder.")
    parser.add_argument("title", help="Short title for the run.")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path("content-runs"),
        help="Parent directory for content runs. Defaults to content-runs.",
    )
    parser.add_argument("--owner", default="alexey", help="Content owner.")
    parser.add_argument(
        "--platforms",
        default="linkedin",
        help="Comma-separated default platforms, for example linkedin,x.",
    )
    parser.add_argument("--source-type", default="", help="Source type, for example youtube.")
    parser.add_argument("--source-title", default="", help="Source title.")
    parser.add_argument("--source-url", default="", help="Source URL.")
    parser.add_argument("--video-id", default="", help="YouTube video ID when available.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    today = date.today().isoformat()
    slug = slugify(args.title)
    run_id = f"{today}-{slug}"
    run_dir = (args.base_dir.expanduser() / run_id).resolve()

    for relative in ["source", "ideas", "briefs", "posts", "clips", "queue"]:
        (run_dir / relative).mkdir(parents=True, exist_ok=True)

    source_id = slugify(args.video_id or args.source_title or args.title)
    if args.video_id:
        source_id = f"youtube_{source_id}"

    run_record = {
        "run_id": run_id,
        "created": today,
        "owner": args.owner,
        "default_platforms": parse_platforms(args.platforms),
        "status": "drafting",
        "source": {
            "source_id": source_id,
            "type": args.source_type,
            "title": args.source_title,
            "url": args.source_url,
            "video_id": args.video_id,
            "transcript_path": "",
            "duration_seconds": 0,
        },
    }
    write_json(run_dir / "run.json", run_record)
    write_json(run_dir / "source" / "source.json", run_record["source"])
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
