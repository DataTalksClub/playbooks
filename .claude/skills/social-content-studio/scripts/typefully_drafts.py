#!/usr/bin/env python3
"""Create Typefully v2 drafts from content-run posts.

Each post becomes one Typefully draft per media variant in its owner's profile
(references/profiles.json). Every draft holds all of the profile's platforms:
Typefully manages platforms inside a draft, so never create one draft per platform.

- Alexey: `clip` draft (clip on LinkedIn, X, Substack) and `visual` draft
  (carousel PDF on LinkedIn, resource image on X), both with linkedin.md copy.
- DataTalks.Club: `clip` draft with linkedin.md on LinkedIn and the x.md thread on X.

Media is uploaded and processed before any draft exists. Each draft is then
created once, complete, and never patched, so edits made in Typefully are never
overwritten. A draft whose media fails is not created; rerunning the same
command reuses finished uploads and creates only the missing drafts.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from check_posts import check_run
from post_common import (
    PROFILES_PATH,
    draft_variants,
    load_json,
    load_profiles,
    post_copy,
    profile_for,
    write_json,
)


API_BASE_URL = "https://api.typefully.com"


def read_api_key(args: argparse.Namespace) -> str:
    if args.api_key_stdin:
        api_key = sys.stdin.readline().strip()
    else:
        api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise SystemExit(f"Missing API key. Set {args.api_key_env} or pass --api-key-stdin.")
    return api_key


def api_request(*, method: str, url: str, api_key: str, body: dict[str, Any] | None = None) -> Any:
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
    return json.loads(response_body)


def put_file(upload_url: str, path: Path) -> None:
    """PUT raw bytes to a presigned upload URL with no extra headers.

    Typefully's presigned URLs are signed without Content-Type, and urllib adds
    one to every body, so this uses http.client directly.
    """
    parsed = urllib.parse.urlsplit(upload_url)
    connection_class = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection
    connection = connection_class(parsed.netloc, timeout=300)
    target = parsed.path + (f"?{parsed.query}" if parsed.query else "")
    try:
        connection.request("PUT", target, body=path.read_bytes(), headers={"Content-Length": str(path.stat().st_size)})
        response = connection.getresponse()
        body = response.read().decode("utf-8", errors="replace")
    finally:
        connection.close()
    if response.status not in (200, 201, 204):
        raise RuntimeError(f"Upload of {path.name} failed with {response.status}: {body[:500]}")


def media_status(base_url: str, api_key: str, social_set_id: str, media_id: str) -> dict[str, Any]:
    response = api_request(method="GET", url=f"{base_url}/v2/social-sets/{social_set_id}/media/{media_id}", api_key=api_key)
    return response if isinstance(response, dict) else {}


def upload_and_wait(
    *, base_url: str, api_key: str, social_set_id: str, path: Path, cached_media_id: str | None, timeout: float, poll_interval: float
) -> dict[str, Any]:
    """Upload one file (or reuse a cached upload) and wait until Typefully has processed it.

    Runs in a worker thread and never raises: the result says whether the media is ready.
    """
    media_id = cached_media_id
    try:
        if media_id:
            try:
                status = media_status(base_url, api_key, social_set_id, media_id).get("status")
            except RuntimeError:
                status = None
            if status == "ready":
                return {"media_id": media_id, "status": "ready", "reused": True}
            if status in (None, "failed"):
                media_id = None
        if not media_id:
            response = api_request(
                method="POST",
                url=f"{base_url}/v2/social-sets/{social_set_id}/media/upload",
                api_key=api_key,
                body={"file_name": path.name},
            )
            media_id = response.get("media_id") if isinstance(response, dict) else None
            upload_url = response.get("upload_url") if isinstance(response, dict) else None
            if not media_id or not upload_url:
                raise RuntimeError(f"Unexpected media/upload response: {response}")
            put_file(upload_url, path)
        deadline = time.monotonic() + timeout
        while True:
            data = media_status(base_url, api_key, social_set_id, media_id)
            status = data.get("status")
            if status == "ready":
                return {"media_id": media_id, "status": "ready", "reused": False}
            if status == "failed":
                return {"media_id": media_id, "status": "failed", "error": str(data.get("error_reason") or "processing failed")}
            if time.monotonic() >= deadline:
                return {"media_id": media_id, "status": "timeout", "error": f"not ready after {timeout:.0f}s (status={status!r})"}
            time.sleep(poll_interval)
    except Exception as exc:  # noqa: BLE001 - reported per file, the run continues
        return {"media_id": media_id, "status": "failed", "error": str(exc)}


def cache_key(post_path: Path, path: Path) -> str:
    """Media path relative to the post folder, so the cache survives moving the run."""
    return os.path.relpath(path, post_path.parent)


def cached_upload(post_path: Path, post: dict[str, Any], social_set_id: str, path: Path) -> str | None:
    for entry in post.get("typefully_media_uploads") or []:
        if (
            isinstance(entry, dict)
            and entry.get("social_set_id") == social_set_id
            and entry.get("path") == cache_key(post_path, path)
            and entry.get("size") == path.stat().st_size
            and entry.get("media_id")
        ):
            return str(entry["media_id"])
    return None


def record_upload(post_path: Path, post: dict[str, Any], social_set_id: str, path: Path, result: dict[str, Any]) -> None:
    key = cache_key(post_path, path)
    entries = [
        entry
        for entry in post.get("typefully_media_uploads") or []
        if not (isinstance(entry, dict) and entry.get("social_set_id") == social_set_id and entry.get("path") == key)
    ]
    entries.append(
        {
            "social_set_id": social_set_id,
            "path": key,
            "size": path.stat().st_size,
            "media_id": result.get("media_id"),
            "status": result.get("status"),
            "error": result.get("error", ""),
        }
    )
    post["typefully_media_uploads"] = entries
    write_json(post_path, post)


def uploaded_platforms(post: dict[str, Any], social_set_id: str, variant: str) -> set[str]:
    uploaded: set[str] = set()
    for entry in post.get("typefully_drafts") or []:
        if not isinstance(entry, dict) or str(entry.get("social_set_id")) != social_set_id or not entry.get("draft_id"):
            continue
        if entry.get("variant", variant) != variant:
            continue
        uploaded.update(entry.get("platforms") or [])
    return uploaded


def list_social_sets(args: argparse.Namespace) -> int:
    """Print the account's social sets (read-only GET) to fill in profiles.json."""
    api_key = read_api_key(args)
    payload = api_request(method="GET", url=f"{args.base_url.rstrip('/')}/v2/social-sets?limit=50", api_key=api_key)
    records = payload.get("results", payload) if isinstance(payload, dict) else payload
    if not isinstance(records, list):
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    for record in records:
        if isinstance(record, dict):
            labels = [str(record[key]) for key in ["name", "username", "display_name", "handle"] if record.get(key)]
            print(f"{record.get('id', '?')}\t{' / '.join(labels)}")
    return 0


def split_values(values: list[str] | None) -> set[str]:
    return {item.strip() for value in values or [] for item in value.split(",") if item.strip()}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create Typefully API v2 drafts from a content-run folder.")
    parser.add_argument("run_dir", type=Path, nargs="?", help="Content run directory.")
    parser.add_argument("--post", action="append", help="Only these post IDs, for example alexey_001. Repeat or comma-separate.")
    parser.add_argument("--variant", action="append", help="Only these variants, for example clip or visual.")
    parser.add_argument("--platform", action="append", help="Only these platforms. Defaults to all platforms of each variant.")
    parser.add_argument("--status", action="append", help="Post status to upload. Defaults to approved. Repeat or comma-separate.")
    parser.add_argument(
        "--social-set-id",
        help="Optional cross-check. The social set comes from each post's owner in references/profiles.json; the run stops if this disagrees.",
    )
    parser.add_argument("--api-key-env", default="TYPEFULLY_API_KEY", help="Environment variable containing the Typefully API key.")
    parser.add_argument("--api-key-stdin", action="store_true", help="Read the Typefully API key from stdin.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned drafts without calling the API.")
    parser.add_argument("--force", action="store_true", help="Create drafts even when this variant already has one.")
    parser.add_argument("--no-media", action="store_true", help="Create one text-only draft per post.")
    parser.add_argument("--skip-checks", action="store_true", help="Upload even if check_posts.py reports errors.")
    parser.add_argument("--media-timeout", type=float, default=900, help="Seconds to wait for each file to process (default: 900).")
    parser.add_argument("--media-workers", type=int, default=3, help="Files uploaded in parallel (default: 3).")
    parser.add_argument("--list-social-sets", action="store_true", help="List the account's social sets (read-only) and exit.")
    parser.add_argument("--base-url", default=API_BASE_URL, help="Typefully API base URL.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.list_social_sets:
        return list_social_sets(args)
    if args.run_dir is None:
        raise SystemExit("run_dir is required.")
    run_dir = args.run_dir.expanduser().resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"Run directory not found: {run_dir}")

    profiles = load_profiles()
    base_url = args.base_url.rstrip("/")
    include_statuses = split_values(args.status) or {"approved"}
    include_posts = split_values(args.post) or None
    include_variants = split_values(args.variant) or None
    include_platforms = split_values(args.platform) or None

    records = [
        path
        for path in sorted(run_dir.glob("posts/*/post.json"))
        if (include_posts is None or path.parent.name in include_posts) and str(load_json(path).get("status")) in include_statuses
    ]
    if not records:
        raise SystemExit(f"No posts with statuses {sorted(include_statuses)} in {run_dir}. Approve posts first or pass --status.")

    results = check_run(run_dir, write=not args.dry_run, only={path.parent.name for path in records})
    failing = {post_id: errors for post_id, (errors, _) in results.items() if errors}
    if failing and not args.skip_checks:
        for post_id, errors in failing.items():
            print(f"check failed: {post_id}: " + "; ".join(errors))
        raise SystemExit("Fix the errors above (scripts/check_posts.py) or pass --skip-checks.")

    # Plan every draft first, so a bad file stops the run before any upload.
    drafts: list[dict[str, Any]] = []
    skipped = 0
    for post_path in records:
        post = load_json(post_path)
        owner = str(post.get("owner") or "")
        profile = profile_for(owner, profiles, post_path)
        social_set_id = str(profile["typefully_social_set_id"]) if profile.get("typefully_social_set_id") not in (None, "") else None
        if args.social_set_id and social_set_id and args.social_set_id != social_set_id:
            raise SystemExit(
                f"{post_path}: owner '{owner}' maps to social set {social_set_id} in {PROFILES_PATH.name}, "
                f"but --social-set-id {args.social_set_id} was passed. Refusing to upload."
            )
        if not social_set_id and not args.dry_run:
            raise SystemExit(f"{post_path}: no typefully_social_set_id for '{owner}' in {PROFILES_PATH} (see --list-social-sets).")
        copy = post_copy(post_path.parent, post, profile)
        variants = [("text", {p: [] for p in copy})] if args.no_media else draft_variants(post_path.parent, post, profile)
        for variant, plan in variants:
            if include_variants is not None and variant not in include_variants:
                continue
            platforms = [p for p in plan if p in copy and (include_platforms is None or p in include_platforms)]
            already = set() if args.force or not social_set_id else uploaded_platforms(post, social_set_id, variant)
            to_send = [p for p in platforms if p not in already]
            if not to_send:
                if platforms:
                    print(f"skip existing: {post.get('post_id')} [{variant}] platforms={','.join(platforms)}")
                    skipped += 1
                continue
            drafts.append(
                {"path": post_path, "post": post, "owner": owner, "social_set_id": social_set_id, "variant": variant,
                 "platforms": to_send, "copy": copy, "plan": {p: plan[p] for p in to_send}}
            )

    def payload_for(draft: dict[str, Any], media_ids: dict[str, list[str]]) -> dict[str, Any]:
        post = draft["post"]
        platforms: dict[str, Any] = {}
        for platform in draft["platforms"]:
            posts: list[dict[str, Any]] = [{"text": text} for text in draft["copy"][platform]]
            if media_ids.get(platform):
                posts[0]["media_ids"] = media_ids[platform]
            platforms[platform] = {"enabled": True, "posts": posts}
        title = f"[{draft['owner']}] {post.get('post_id')} ({draft['variant']})"
        if post.get("topic"):
            title += f" - {post['topic']}"
        return {"draft_title": title[:512], "platforms": platforms}

    if args.dry_run:
        for draft in drafts:
            media = {p: [str(path) for path in paths] for p, paths in draft["plan"].items() if paths}
            target = draft["social_set_id"] or f"<no social set for {draft['owner']}>"
            print(json.dumps({"url": f"{base_url}/v2/social-sets/{target}/drafts", "variant": draft["variant"], "media": media,
                              "payload": payload_for(draft, {})}, indent=2, ensure_ascii=False))
        print(f"drafts planned={len(drafts)} skipped={skipped} dry_run=True")
        return 0

    api_key = read_api_key(args)

    # Upload all media in parallel before any draft exists.
    users: dict[tuple[str, Path], list[dict[str, Any]]] = {}
    for draft in drafts:
        for paths in draft["plan"].values():
            for path in paths:
                users.setdefault((draft["social_set_id"], path), [])
                if draft not in users[(draft["social_set_id"], path)]:
                    users[(draft["social_set_id"], path)].append(draft)
    uploads: dict[tuple[str, Path], dict[str, Any]] = {}
    if users:
        print(f"uploading {len(users)} media file(s), up to {args.media_workers} at a time...")
        with ThreadPoolExecutor(max_workers=max(1, args.media_workers)) as pool:
            futures = {
                pool.submit(
                    upload_and_wait,
                    base_url=base_url,
                    api_key=api_key,
                    social_set_id=social_set_id,
                    path=path,
                    cached_media_id=next(
                        (m for d in users[(social_set_id, path)] if (m := cached_upload(d["path"], d["post"], social_set_id, path))), None
                    ),
                    timeout=args.media_timeout,
                    poll_interval=10,
                ): (social_set_id, path)
                for social_set_id, path in users
            }
            for future in as_completed(futures):
                key = futures[future]
                uploads[key] = result = future.result()
                for draft in users[key]:
                    record_upload(draft["path"], draft["post"], key[0], key[1], result)
                note = " (reused)" if result.get("reused") else ""
                print(f"media {result['status']}: {key[1].name}{note} {result.get('error', '')}".rstrip())

    created: list[dict[str, Any]] = []
    failed: list[str] = []
    summary_path = run_dir / "queue" / "typefully-drafts.json"
    for draft in drafts:
        post, label, social_set_id = draft["post"], f"{draft['post'].get('post_id')} [{draft['variant']}]", draft["social_set_id"]
        files = list(dict.fromkeys(path for paths in draft["plan"].values() for path in paths))
        not_ready = [f"{p.name}: {uploads[(social_set_id, p)].get('error') or uploads[(social_set_id, p)]['status']}"
                     for p in files if uploads[(social_set_id, p)]["status"] != "ready"]
        if not_ready:
            print(f"NOT CREATED: {label} - media not ready: {'; '.join(not_ready)}. Rerun to retry.")
            failed.append(label)
            continue
        media_ids = {p: [uploads[(social_set_id, path)]["media_id"] for path in paths] for p, paths in draft["plan"].items() if paths}
        endpoint = f"{base_url}/v2/social-sets/{social_set_id}/drafts"
        try:
            response = api_request(method="POST", url=endpoint, api_key=api_key, body=payload_for(draft, media_ids))
            if not isinstance(response, dict):
                raise RuntimeError(f"Expected JSON object from {endpoint}")
        except RuntimeError as exc:
            print(f"NOT CREATED: {label} - {exc}. Rerun to retry.")
            failed.append(label)
            continue
        entry = {
            "social_set_id": social_set_id, "variant": draft["variant"], "platforms": draft["platforms"],
            "draft_id": response.get("id"), "status": response.get("status"),
            "private_url": response.get("private_url", ""), "share_url": response.get("share_url", ""),
            "created_at": response.get("created_at", ""),
        }
        post.setdefault("typefully_drafts", []).append(entry)
        write_json(draft["path"], post)
        created.append({"post_id": post.get("post_id"), "owner": draft["owner"], **entry})
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        existing = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else []
        summary_path.write_text(json.dumps(existing + [created[-1]], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"created: {label} platforms={','.join(draft['platforms'])} media={sum(len(v) for v in media_ids.values())} draft_id={response.get('id')}")
        time.sleep(0.2)

    print(f"created={len(created)} skipped={skipped} failed={len(failed)}")
    if failed:
        print(f"Not created: {', '.join(failed)}. Nothing was created for them in Typefully; rerun the same command to retry.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
