#!/usr/bin/env python3
"""Mechanical checks for content-run posts, per the owner's profile in references/profiles.json.

Checks copy files, X thread markers and per-post limits (URLs count as 23),
banned phrases, required links from source/source.json, transcript timestamps,
media files and clip length, and unresolved reviewer findings. Writes the
result to each post's review.json under `lint` and exits 1 on any error.

Run after writing and before upload; scripts/typefully_drafts.py runs it too.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

from post_common import (
    banned_phrases,
    draft_variants,
    load_json,
    load_profiles,
    media_duration,
    post_copy,
    post_media,
    profile_for,
    strip_frontmatter,
    timestamp_seconds,
    write_json,
    x_length,
)

X_STANDARD_VIDEO_SECONDS = 140


def check_post(post_path: Path, run: dict[str, Any], source: dict[str, Any], profiles: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    post_dir = post_path.parent
    post = load_json(post_path)
    post_id = str(post.get("post_id"))
    if post_id != post_dir.name:
        errors.append(f"post_id '{post_id}' does not match folder '{post_dir.name}'")
    for field in ["post_id", "owner", "status", "topic", "files"]:
        if not post.get(field):
            errors.append(f"post.json is missing `{field}`")
    status = str(post.get("status"))
    allowed = {"draft", "needs_review", "approved", "ready", "scheduled", "published", "rejected", "archived"}
    if status not in allowed:
        errors.append(f"status '{status}' is not one of {sorted(allowed)}")
    owner = str(post.get("owner") or "")
    if not owner:
        return errors + ["no owner in post.json"], warnings
    profile = profile_for(owner, profiles, post_path)

    for key, name in (post.get("files") or {}).items():
        if key in ("linkedin", "x") and (post_dir / name).exists():
            meta, _ = strip_frontmatter((post_dir / name).read_text(encoding="utf-8"))
            if meta.get("post_id") and meta["post_id"] != post_id:
                errors.append(f"{name}: frontmatter post_id '{meta['post_id']}' does not match '{post_id}'")

    try:
        copy = post_copy(post_dir, post, profile)
    except (ValueError, FileNotFoundError) as exc:
        return errors + [str(exc)], warnings

    limit = profile.get("x_post_limit")
    if limit and "x" in copy:
        for index, text in enumerate(copy["x"], 1):
            numbered = f"{index}/{len(copy['x'])}\n\n{text}" if len(copy["x"]) > 1 else text
            length = x_length(numbered)
            if length > limit:
                errors.append(f"x post {index}/{len(copy['x'])} is {length} characters (limit {limit}, URLs count as 23)")
        if len(copy["x"]) == 1 and x_length(copy["x"][0]) > limit:
            errors.append("x copy is a single post over the limit; write it as an N/M thread")

    all_text = "\n".join(text for texts in copy.values() for text in texts)
    for phrase in banned_phrases(profile):
        if re.search(rf"(?<![\w-]){re.escape(phrase)}(?![\w-])", all_text, re.I):
            errors.append(f"banned phrase: '{phrase}'")
    if profile.get("warn_on_em_dash") and "—" in all_text:
        warnings.append("em dash found (style: avoid unless essential)")

    shared: dict[str, list[str]] = {}
    for platform, texts in copy.items():
        shared.setdefault("\n".join(texts), []).append(platform)
    for name, url in (source.get("links") or {}).items():
        for text, platforms in shared.items():
            if url not in text:
                errors.append(f"{'/'.join(platforms)} copy is missing the {name} link: {url}")

    duration = float(source.get("duration_seconds") or 0)
    for moment in post.get("source_moments") or []:
        try:
            start, end = timestamp_seconds(moment["start"]), timestamp_seconds(moment["end"])
        except (KeyError, ValueError):
            errors.append(f"source moment has a bad timestamp: {moment}")
            continue
        if end <= start or (duration and end > duration + 1):
            errors.append(f"source moment {moment['start']}-{moment['end']} is outside the recording")
        excerpt = moment.get("excerpt_path")
        if excerpt and not (post_dir / excerpt).exists():
            errors.append(f"excerpt file not found: {excerpt}")

    for kind, relative in post_media(post).items():
        path = post_dir / relative
        if not path.is_file():
            errors.append(f"{kind} file not found: {relative}")
            continue
        if kind == "clip" and limit:
            seconds = media_duration(path)
            if seconds and seconds > X_STANDARD_VIDEO_SECONDS:
                warnings.append(f"clip is {seconds:.0f}s; check X's video limit for accounts without Premium")
    variants = [name for name, _ in draft_variants(post_dir, post, profile)]
    if variants == ["text"] and post_media(post):
        warnings.append("media is listed but no draft variant is complete; the upload would be text-only")

    review_path = post_dir / "review.json"
    if review_path.exists():
        reviewer = load_json(review_path).get("reviewer") or {}
        open_findings = [f for f in reviewer.get("findings") or [] if f.get("status", "open") == "open" and f.get("severity") == "error"]
        if open_findings:
            errors.append(f"{len(open_findings)} open reviewer finding(s) marked error in review.json")
        if not reviewer:
            warnings.append("no reviewer pass recorded in review.json")
    return errors, warnings


def check_run(run_dir: Path, *, write: bool = True, only: set[str] | None = None) -> dict[str, tuple[list[str], list[str]]]:
    run = load_json(run_dir / "run.json") if (run_dir / "run.json").exists() else {}
    source_path = run_dir / "source" / "source.json"
    source = load_json(source_path) if source_path.exists() else {}
    profiles = load_profiles()
    results: dict[str, tuple[list[str], list[str]]] = {}
    for post_path in sorted(run_dir.glob("posts/*/post.json")):
        if only is not None and post_path.parent.name not in only:
            continue
        errors, warnings = check_post(post_path, run, source, profiles)
        results[post_path.parent.name] = (errors, warnings)
        if write:
            review_path = post_path.parent / "review.json"
            review = load_json(review_path) if review_path.exists() else {"post_id": post_path.parent.name}
            review["lint"] = {"checked": date.today().isoformat(), "errors": errors, "warnings": warnings}
            write_json(review_path, review)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Check content-run posts against their profile rules.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--no-write", action="store_true", help="Do not update review.json.")
    args = parser.parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    results = check_run(run_dir, write=not args.no_write)
    if not results:
        raise SystemExit(f"No posts found in {run_dir}")
    failed = 0
    for post_id, (errors, warnings) in results.items():
        status = "FAIL" if errors else "ok"
        print(f"{status:4} {post_id}")
        for message in errors:
            print(f"     error: {message}")
        for message in warnings:
            print(f"     warn:  {message}")
        failed += bool(errors)
    print(f"{len(results) - failed}/{len(results)} posts pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
