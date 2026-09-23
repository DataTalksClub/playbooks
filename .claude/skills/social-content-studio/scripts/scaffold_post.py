#!/usr/bin/env python3
"""Create a post folder in a content run with the files its owner's profile needs.

Writes post.json, empty copy files with frontmatter (linkedin.md, plus x.md when
the profile has a separate X thread), and a review.json stub. With --clip it
adds the clip to clips/clip-manifest.json for the video-clip-cutter skill.
The writer then fills in the copy; check_posts.py validates the result.

Example:
  python3 .claude/skills/social-content-studio/scripts/scaffold_post.py content-runs/<run> \\
    --owner alexey --idea idea_001 --topic "Build the agent team one layer at a time" \\
    --angle "..." --cta "Watch the recording; explore the repo" \\
    --moment "00:10:43-00:11:18=Goal of the workflow" --clip 00:39:23-00:40:11
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

from post_common import load_json, load_profiles, profile_for, timestamp_seconds, write_json


RANGE = re.compile(r"^(\d{1,2}:\d{2}:\d{2})-(\d{1,2}:\d{2}:\d{2})(?:=(.*))?$")


def parse_range(value: str) -> tuple[str, str, str]:
    match = RANGE.match(value.strip())
    if not match:
        raise SystemExit(f"Bad range '{value}'. Use HH:MM:SS-HH:MM:SS, optionally followed by =note.")
    start, end, note = match.group(1), match.group(2), (match.group(3) or "").strip()
    if timestamp_seconds(end) <= timestamp_seconds(start):
        raise SystemExit(f"Range '{value}' ends before it starts.")
    return start, end, note


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:60] or "clip"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a post folder with the files its profile needs.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--owner", required=True, help="Profile key from references/profiles.json, for example alexey or datatalksclub.")
    parser.add_argument("--idea", default="", help="Upstream idea ID, for example idea_001.")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--angle", default="")
    parser.add_argument("--cta", default="")
    parser.add_argument("--moment", action="append", default=[], help="Transcript moment HH:MM:SS-HH:MM:SS=note. Repeatable.")
    parser.add_argument("--clip", action="append", default=[], help="Clip segment HH:MM:SS-HH:MM:SS. Repeat for a multi-part clip.")
    parser.add_argument("--no-visual", action="store_true", help="Skip the carousel and image even if the profile has a visual draft.")
    args = parser.parse_args()

    run_dir = args.run_dir.expanduser().resolve()
    profiles = load_profiles()
    profile = profile_for(args.owner, profiles, run_dir)
    prefix = profile.get("post_prefix") or args.owner
    existing = sorted(int(p.name.rsplit("_", 1)[1]) for p in (run_dir / "posts").glob(f"{prefix}_*") if p.name.rsplit("_", 1)[1].isdigit())
    post_id = f"{prefix}_{(existing[-1] + 1 if existing else 1):03d}"
    post_dir = run_dir / "posts" / post_id
    post_dir.mkdir(parents=True)

    source_path = run_dir / "source" / "source.json"
    source = load_json(source_path) if source_path.exists() else {}
    copy_files = sorted(set((profile.get("copy") or {}).values()))
    files = {key: f"{key}.md" for key in copy_files}
    files["review"] = "review.json"
    for key in copy_files:
        platform = key if key == "x" else ", ".join(p for p, src in profile["copy"].items() if src == key)
        (post_dir / f"{key}.md").write_text(f"---\npost_id: {post_id}\nplatform: {platform}\nstatus: draft\n---\n\n", encoding="utf-8")

    excerpt = f"../../briefs/{args.idea}.md" if args.idea and (run_dir / "briefs" / f"{args.idea}.md").exists() else ""
    media: dict[str, str] = {}
    clip: dict[str, Any] = {"recommended": False}
    if args.clip:
        segments = [{"start": s, "end": e} for s, e, _ in map(parse_range, args.clip)]
        output = f"{post_id.replace('_', '-')}-{slugify(args.topic)}.mp4"
        clip = {
            "recommended": True,
            "clip_id": f"clip_{post_id}",
            "segments": segments,
            "manifest_path": "../../clips/clip-manifest.json",
            "path": f"../../clips/{output}",
            "duration_seconds": sum(timestamp_seconds(s["end"]) - timestamp_seconds(s["start"]) for s in segments),
        }
        media["clip"] = clip["path"]
        manifest_path = run_dir / "clips" / "clip-manifest.json"
        manifest_path.parent.mkdir(exist_ok=True)
        manifest = load_json(manifest_path) if manifest_path.exists() else {
            "input": source.get("local_video", ""), "output_dir": str(manifest_path.parent), "clips": []
        }
        manifest["clips"].append({"output": output, **({"parts_prefix": clip["clip_id"]} if len(segments) > 1 else {}), "segments": segments})
        write_json(manifest_path, manifest)
    if "visual" in (profile.get("variants") or {}) and not args.no_visual:
        media["carousel"] = "linkedin-carousel/carousel.pdf"
        media["image"] = "twitter-resource/twitter-resource.png"

    today = date.today().isoformat()
    post = {
        "post_id": post_id,
        "idea_id": args.idea,
        "source_id": source.get("source_id", ""),
        "owner": args.owner,
        "platforms": list((profile.get("copy") or {}).keys()),
        "status": "draft",
        "topic": args.topic,
        "created": today,
        "updated": today,
        "angle": args.angle,
        "cta": args.cta,
        "source_moments": [{"start": s, "end": e, "note": n, "excerpt_path": excerpt} for s, e, n in map(parse_range, args.moment)],
        "clip": clip,
        "media": media,
        "files": files,
        "scheduling": {"ready_for_queue": False, "preferred_publish_at": "", "external_id": ""},
    }
    write_json(post_dir / "post.json", post)
    write_json(post_dir / "review.json", {"post_id": post_id, "lint": None, "reviewer": None})
    print(post_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
