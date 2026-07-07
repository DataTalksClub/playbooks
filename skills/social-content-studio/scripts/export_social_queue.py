#!/usr/bin/env python3
"""Export ready Social Content Studio posts to a JSONL scheduling queue."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def markdown_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text


def run_relative_path(value: str, post_dir: Path, run_dir: Path) -> str:
    if not value:
        return ""
    path = Path(value)
    if not path.is_absolute():
        path = post_dir / path
    try:
        return str(path.resolve(strict=False).relative_to(run_dir))
    except ValueError:
        return str(path)


def queue_items(run_dir: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for post_record in sorted(run_dir.glob("posts/*/post.json")):
        post = load_json(post_record)
        scheduling = post.get("scheduling") or {}
        if post.get("status") != "ready" and not scheduling.get("ready_for_queue"):
            continue

        files = post.get("files") or {}
        clip = post.get("clip") or {}
        for platform in post.get("platforms") or []:
            draft_name = files.get(platform)
            if not draft_name:
                continue
            draft_path = post_record.parent / draft_name
            if not draft_path.exists():
                raise ValueError(f"Missing draft file: {draft_path}")
            clip_path = run_relative_path(str(clip.get("path") or ""), post_record.parent, run_dir)
            items.append(
                {
                    "post_id": post.get("post_id"),
                    "idea_id": post.get("idea_id", ""),
                    "platform": platform,
                    "status": post.get("status"),
                    "topic": post.get("topic", ""),
                    "body_path": str(draft_path.relative_to(run_dir)),
                    "body": markdown_body(draft_path),
                    "clip_path": clip_path,
                    "preferred_publish_at": scheduling.get("preferred_publish_at", ""),
                    "external_id": scheduling.get("external_id", ""),
                }
            )
    return items


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export ready posts to social-queue.jsonl.")
    parser.add_argument("run_dir", type=Path, help="Content run directory.")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSONL path. Defaults to queue/social-queue.jsonl inside the run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"Run directory does not exist: {run_dir}")

    output = args.output or run_dir / "queue" / "social-queue.jsonl"
    if not output.is_absolute():
        output = Path.cwd() / output
    output.parent.mkdir(parents=True, exist_ok=True)

    items = queue_items(run_dir)
    with output.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Wrote {len(items)} queue item(s) to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
