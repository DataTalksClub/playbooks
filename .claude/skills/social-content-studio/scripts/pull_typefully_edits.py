#!/usr/bin/env python3
"""Pull the current text of a run's Typefully drafts and compare it with what was generated.

Read-only: makes only GET requests. For every draft recorded in post.json
`typefully_drafts`, saves the Typefully version next to the post and writes
`edits.md` in the run folder with a diff per platform. Those diffs are the
input for updating the style references (see SKILL.md, "Learn from edits").

Run it after the posts are published, or any time after editing in Typefully.
"""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from post_common import join_x_thread, load_json, load_profiles, post_copy, profile_for, write_json
from typefully_drafts import API_BASE_URL, api_request, read_api_key


def typefully_text(platform_data: dict[str, Any]) -> str | None:
    posts = [post.get("text", "") for post in platform_data.get("posts") or [] if isinstance(post, dict)]
    return join_x_thread(posts) if posts else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull Typefully draft text and diff it against the generated copy.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--api-key-env", default="TYPEFULLY_API_KEY")
    parser.add_argument("--api-key-stdin", action="store_true")
    parser.add_argument("--base-url", default=API_BASE_URL)
    args = parser.parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    api_key = read_api_key(args)
    base_url = args.base_url.rstrip("/")
    profiles = load_profiles()

    sections: list[str] = []
    changed = unchanged = 0
    for post_path in sorted(run_dir.glob("posts/*/post.json")):
        post = load_json(post_path)
        entries = [e for e in post.get("typefully_drafts") or [] if isinstance(e, dict) and e.get("draft_id")]
        if not entries:
            continue
        profile = profile_for(str(post.get("owner")), profiles, post_path)
        generated = {platform: join_x_thread(texts) for platform, texts in post_copy(post_path.parent, post, profile).items()}
        out_dir = post_path.parent / "typefully"
        out_dir.mkdir(exist_ok=True)
        for entry in entries:
            url = f"{base_url}/v2/social-sets/{entry['social_set_id']}/drafts/{entry['draft_id']}"
            try:
                draft = api_request(method="GET", url=url, api_key=api_key)
            except RuntimeError as exc:
                print(f"skip {post['post_id']} draft {entry['draft_id']}: {exc}")
                continue
            variant = entry.get("variant", "clip")
            write_json(out_dir / f"{variant}-{entry['draft_id']}.json", draft)
            entry.update(
                {
                    "status": draft.get("status"),
                    "published_at": draft.get("published_at"),
                    "published_urls": {k: v for k, v in draft.items() if k.endswith("_published_url") and v},
                    "pulled_at": date.today().isoformat(),
                }
            )
            for platform, data in (draft.get("platforms") or {}).items():
                if not isinstance(data, dict) or not data.get("enabled") or platform not in generated:
                    continue
                final = typefully_text(data)
                if final is None:
                    continue
                (out_dir / f"{variant}-final-{platform}.md").write_text(final + "\n", encoding="utf-8")
                if final.strip() == generated[platform].strip():
                    unchanged += 1
                    continue
                changed += 1
                diff = difflib.unified_diff(
                    generated[platform].splitlines(), final.splitlines(), "generated", "typefully", lineterm="", n=1
                )
                sections.append(
                    f"## {post['post_id']} / {variant} / {platform} ({post.get('owner')}, {draft.get('status')})\n\n```diff\n"
                    + "\n".join(diff)
                    + "\n```\n"
                )
        write_json(post_path, post)

    header = (
        f"# Typefully edits: {run_dir.name}\n\nPulled {date.today().isoformat()}. "
        f"{changed} platform version(s) edited, {unchanged} unchanged.\n\n"
        "Look for patterns across posts, then update the owning style reference "
        "(alexey-style.md, datatalks-style.md, or the platform reference) rather than fixing single posts.\n\n"
    )
    (run_dir / "edits.md").write_text(header + ("\n".join(sections) or "No edits.\n"), encoding="utf-8")
    print(f"edited={changed} unchanged={unchanged} report={run_dir / 'edits.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
