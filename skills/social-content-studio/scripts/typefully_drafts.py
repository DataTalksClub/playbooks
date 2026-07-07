#!/usr/bin/env python3
"""Create Typefully v2 drafts from Social Content Studio post artifacts."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


API_BASE_URL = "https://api.typefully.com"


def strip_markdown_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def parse_social_set_ids(values: list[str]) -> list[str]:
    ids: list[str] = []
    for value in values:
        for item in value.split(","):
            item = item.strip()
            if item:
                ids.append(item)
    if not ids:
        raise SystemExit("At least one --social-set-id is required.")
    return ids


def read_api_key(args: argparse.Namespace) -> str:
    if args.api_key_stdin:
        api_key = sys.stdin.readline().strip()
    else:
        api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise SystemExit(
            f"Missing API key. Set {args.api_key_env} or pass --api-key-stdin."
        )
    return api_key


def api_request(
    *,
    method: str,
    url: str,
    api_key: str,
    body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = None
    headers = {"Authorization": f"Bearer {api_key}"}
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            response_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed with {exc.code}: {error_body}") from exc
    if not response_body:
        return {}
    parsed = json.loads(response_body)
    if not isinstance(parsed, dict):
        raise RuntimeError(f"Expected JSON object from {url}, got {type(parsed).__name__}")
    return parsed


def platform_payload(post_dir: Path, post: dict[str, Any]) -> dict[str, Any]:
    files = post.get("files") or {}
    platforms: dict[str, Any] = {}
    for platform in post.get("platforms") or []:
        draft_file = files.get(platform)
        if not draft_file:
            continue
        draft_path = post_dir / draft_file
        if not draft_path.exists():
            raise FileNotFoundError(f"Missing {platform} draft file: {draft_path}")
        platforms[platform] = {
            "enabled": True,
            "posts": [{"text": strip_markdown_frontmatter(draft_path)}],
        }
    if not platforms:
        raise ValueError(f"No platform drafts found in {post_dir}")
    return platforms


def draft_payload(post_dir: Path, post: dict[str, Any]) -> dict[str, Any]:
    title_parts = [str(post.get("post_id") or post_dir.name)]
    if post.get("topic"):
        title_parts.append(str(post["topic"]))
    return {
        "draft_title": " - ".join(title_parts),
        "platforms": platform_payload(post_dir, post),
    }


def find_post_records(run_dir: Path, include_statuses: set[str]) -> list[Path]:
    records: list[Path] = []
    for path in sorted(run_dir.glob("posts/*/post.json")):
        post = load_json(path)
        if str(post.get("status")) in include_statuses:
            records.append(path)
    return records


def existing_typefully_entries(post: dict[str, Any]) -> list[dict[str, Any]]:
    entries = post.get("typefully_drafts") or []
    if not isinstance(entries, list):
        return []
    return [entry for entry in entries if isinstance(entry, dict)]


def already_created(post: dict[str, Any], social_set_id: str) -> bool:
    for entry in existing_typefully_entries(post):
        if str(entry.get("social_set_id")) == str(social_set_id) and entry.get("draft_id"):
            return True
    return False


def update_post_record(
    post_path: Path,
    post: dict[str, Any],
    social_set_id: str,
    response: dict[str, Any],
) -> None:
    entries = existing_typefully_entries(post)
    entries.append(
        {
            "social_set_id": str(social_set_id),
            "draft_id": response.get("id"),
            "status": response.get("status"),
            "private_url": response.get("private_url", ""),
            "share_url": response.get("share_url", ""),
            "created_at": response.get("created_at", ""),
            "updated_at": response.get("updated_at", ""),
        }
    )
    post["typefully_drafts"] = entries
    post_path.write_text(json.dumps(post, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create Typefully API v2 drafts from a content-run folder."
    )
    parser.add_argument("run_dir", type=Path, help="Content run directory.")
    parser.add_argument(
        "--social-set-id",
        action="append",
        required=True,
        help="Typefully social set ID. Can be repeated or comma-separated.",
    )
    parser.add_argument(
        "--status",
        action="append",
        default=["draft"],
        help="Post status to upload. Defaults to draft. Can be repeated.",
    )
    parser.add_argument(
        "--api-key-env",
        default="TYPEFULLY_API_KEY",
        help="Environment variable containing the Typefully API key.",
    )
    parser.add_argument(
        "--api-key-stdin",
        action="store_true",
        help="Read the Typefully API key from stdin instead of an environment variable.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned requests without creating drafts.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Create drafts even when this post already has a draft for a social set.",
    )
    parser.add_argument(
        "--base-url",
        default=API_BASE_URL,
        help="Typefully API base URL.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"Run directory not found: {run_dir}")

    social_set_ids = parse_social_set_ids(args.social_set_id)
    include_statuses = {status.strip() for status in args.status if status.strip()}
    records = find_post_records(run_dir, include_statuses)
    if not records:
        raise SystemExit(f"No post records with statuses {sorted(include_statuses)} in {run_dir}")

    api_key = "" if args.dry_run else read_api_key(args)
    created: list[dict[str, Any]] = []
    skipped = 0

    for post_path in records:
        post = load_json(post_path)
        payload = draft_payload(post_path.parent, post)
        for social_set_id in social_set_ids:
            if not args.force and already_created(post, social_set_id):
                print(f"skip existing: {post.get('post_id')} social_set={social_set_id}")
                skipped += 1
                continue
            endpoint = f"{args.base_url.rstrip('/')}/v2/social-sets/{social_set_id}/drafts"
            if args.dry_run:
                print(json.dumps({"url": endpoint, "payload": payload}, indent=2, ensure_ascii=False))
                continue
            response = api_request(method="POST", url=endpoint, api_key=api_key, body=payload)
            update_post_record(post_path, post, social_set_id, response)
            created.append(
                {
                    "post_id": post.get("post_id"),
                    "social_set_id": str(social_set_id),
                    "draft_id": response.get("id"),
                    "private_url": response.get("private_url", ""),
                    "share_url": response.get("share_url", ""),
                }
            )
            print(
                f"created: {post.get('post_id')} social_set={social_set_id} "
                f"draft_id={response.get('id')}"
            )
            time.sleep(0.2)

    summary_path = run_dir / "queue" / "typefully-drafts.json"
    if not args.dry_run:
        existing: list[Any] = []
        if summary_path.exists():
            try:
                loaded = json.loads(summary_path.read_text(encoding="utf-8"))
                if isinstance(loaded, list):
                    existing = loaded
            except json.JSONDecodeError:
                existing = []
        summary_path.write_text(
            json.dumps(existing + created, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(f"created={len(created)} skipped={skipped} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
