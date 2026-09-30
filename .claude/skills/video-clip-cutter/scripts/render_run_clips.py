#!/usr/bin/env python3
"""Transcribe and render the captioned versions of every clip in a content run.

For each post whose cut clip exists (rejected and archived posts are skipped):
- transcribes the clip once (clips/captions/<clip>.words.json and .txt);
- renders the horizontal version, and the vertical version when post.json has `clip.title`;
- records the paths in post.json: `clip.transcript`, `media.clip_horizontal`, `media.clip_vertical`.

The style is the post's owner, looked up in references/clip-styles.json. Posts whose
owner has no style are transcribed but not rendered. From source/source.json:
Whisper is primed with the speaker, host, title, and `caption_names`, and
`caption_fixes` ({"heard": "meant"}) corrects misheard phrases in every clip.

    uv run --with mlx-whisper --with pillow python3 \
      .claude/skills/video-clip-cutter/scripts/render_run_clips.py content-runs/<run> [--transcribe-only]

Use --transcribe-only right after cutting, so whoever writes the posts and clip
titles can read exactly what each clip says.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from render_social_clip import captions_paths, load_style, render, transcribe


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Transcribe and render captioned clips for a content run.")
    parser.add_argument("run", type=Path, help="Content run folder, for example content-runs/2026-09-22-switch-...")
    parser.add_argument("--post", action="append", default=[], help="Only this post ID. Repeatable.")
    parser.add_argument("--format", choices=["vertical", "horizontal"], action="append", help="Only this format. Repeatable.")
    parser.add_argument("--transcribe-only", action="store_true", help="Write clip transcripts; render nothing.")
    parser.add_argument("--names", default="", help="Extra names and terms to prime Whisper.")
    parser.add_argument("--retranscribe", action="store_true", help="Ignore existing words files.")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def whisper_names(source: dict[str, Any], extra: str) -> str:
    speakers = source.get("speakers") or ([source["speaker"]] if source.get("speaker") else [])
    names = [s.get("name", "") if isinstance(s, dict) else str(s) for s in speakers]
    names += [source.get("host", ""), source.get("title", ""), *source.get("caption_names", []), extra]
    return ", ".join(n for n in names if n)


def relative(path: Path, post_dir: Path) -> str:
    return os.path.relpath(path, post_dir)


def main() -> int:
    args = parse_args()
    run_dir = args.run.expanduser().resolve()
    source_path = run_dir / "source" / "source.json"
    source = load_json(source_path) if source_path.exists() else {}
    names, fixes = whisper_names(source, args.names), source.get("caption_fixes") or {}
    formats = args.format or ["horizontal", "vertical"]
    problems: list[str] = []

    for post_path in sorted(run_dir.glob("posts/*/post.json")):
        post_dir = post_path.parent
        post = load_json(post_path)
        post_id, clip_info = post["post_id"], post.get("clip") or {}
        if args.post and post_id not in args.post:
            continue
        if post.get("status") in ("rejected", "archived"):
            continue
        if not clip_info.get("recommended") or not clip_info.get("path"):
            continue
        clip = (post_dir / clip_info["path"]).resolve()
        if not clip.is_file():
            problems.append(f"{post_id}: clip not cut yet ({clip_info['path']})")
            continue

        transcribe(clip, names, retranscribe=args.retranscribe, fixes=fixes)
        clip_info["transcript"] = relative(captions_paths(clip)[1], post_dir)
        print(f"{post_id}: transcript {clip_info['transcript']}")

        if not args.transcribe_only:
            owner = post.get("owner", "")
            try:
                load_style(owner)
            except KeyError:
                problems.append(f"{post_id}: no clip style for owner {owner!r}; transcribed only")
                formats_for_post = []
            else:
                formats_for_post = formats
            media = post.setdefault("media", {})
            for fmt in formats_for_post:
                if fmt == "vertical" and not clip_info.get("title"):
                    problems.append(f"{post_id}: no clip.title in post.json; vertical version skipped")
                    continue
                output = render(clip, owner, fmt, title=clip_info.get("title", ""), label=clip_info.get("label", ""),
                                names=names, fixes=fixes)
                media[f"clip_{fmt}"] = relative(output, post_dir)
                print(f"{post_id}: {fmt} {media[f'clip_{fmt}']}")
        write_json(post_path, post)

    for problem in problems:
        print(f"warning: {problem}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
