#!/usr/bin/env python3
"""Validate Social Content Studio post records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


POST_STATUSES = {
    "draft",
    "needs_review",
    "approved",
    "ready",
    "scheduled",
    "published",
    "rejected",
    "archived",
}
TIMESTAMP_RE = re.compile(r"^(?:(\d{1,2}):)?([0-5]?\d):([0-5]\d)(?:\.\d{1,3})?$")
REQUIRED_FIELDS = {
    "post_id",
    "owner",
    "platforms",
    "status",
    "topic",
    "created",
    "angle",
    "source_moments",
    "files",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("post.json must contain a JSON object")
    return data


def validate_timestamp(value: Any, field: str) -> str | None:
    if not value:
        return None
    if not isinstance(value, str) or not TIMESTAMP_RE.match(value):
        return f"{field} has invalid timestamp: {value!r}"
    return None


def validate_post(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [f"{path}: {exc}"]

    missing = sorted(REQUIRED_FIELDS - set(data))
    for field in missing:
        errors.append(f"{path}: missing required field {field!r}")

    status = data.get("status")
    if status not in POST_STATUSES:
        errors.append(f"{path}: invalid status {status!r}")

    platforms = data.get("platforms")
    if not isinstance(platforms, list) or not all(isinstance(item, str) for item in platforms):
        errors.append(f"{path}: platforms must be a list of strings")

    source_moments = data.get("source_moments")
    if not isinstance(source_moments, list):
        errors.append(f"{path}: source_moments must be a list")
    else:
        for index, moment in enumerate(source_moments, start=1):
            if not isinstance(moment, dict):
                errors.append(f"{path}: source_moments[{index}] must be an object")
                continue
            for key in ["start", "end"]:
                error = validate_timestamp(moment.get(key), f"source_moments[{index}].{key}")
                if error:
                    errors.append(f"{path}: {error}")

    files = data.get("files")
    if isinstance(files, dict):
        for platform in platforms if isinstance(platforms, list) else []:
            draft_file = files.get(platform)
            if draft_file and not (path.parent / draft_file).exists():
                errors.append(f"{path}: missing draft file for {platform}: {draft_file}")
    elif "files" in data:
        errors.append(f"{path}: files must be an object")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate post.json records.")
    parser.add_argument(
        "path",
        type=Path,
        help="A post.json file or a content run directory containing posts/*/post.json.",
    )
    return parser.parse_args()


def find_post_records(path: Path) -> list[Path]:
    path = path.expanduser()
    if path.is_file():
        return [path]
    return sorted(path.glob("posts/*/post.json"))


def main() -> int:
    args = parse_args()
    records = find_post_records(args.path)
    if not records:
        raise SystemExit(f"No post records found at {args.path}")

    all_errors: list[str] = []
    for record in records:
        all_errors.extend(validate_post(record))

    if all_errors:
        for error in all_errors:
            print(error)
        return 1

    print(f"Validated {len(records)} post record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
