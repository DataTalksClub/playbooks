#!/usr/bin/env python3
"""Render carousel media for content-run post folders and update post.json."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


CAROUSEL_ROOT = Path("/Users/valeria/carousel-automation")
RENDER_JS = CAROUSEL_ROOT / "src" / "render.js"


def find_post_dirs(path: Path) -> list[Path]:
    path = path.resolve()
    if (path / "post.json").exists():
        return [path]
    if (path / "posts").is_dir():
        return sorted(p for p in (path / "posts").iterdir() if (p / "post.json").exists())
    if path.name == "posts" and path.is_dir():
        return sorted(p for p in path.iterdir() if (p / "post.json").exists())
    raise SystemExit(f"No post folders found at {path}")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def run_render(content_json: Path, flag: str, output_dir: Path) -> None:
    cmd = ["node", str(RENDER_JS), str(content_json), flag, "--output", str(output_dir)]
    subprocess.run(cmd, cwd=CAROUSEL_ROOT, check=True)


def update_post_record(post_dir: Path, rendered: dict[str, str]) -> None:
    post_json = post_dir / "post.json"
    if not post_json.exists():
        return
    record = load_json(post_json)
    files = record.setdefault("files", {})
    files.update(rendered)
    write_json(post_json, record)


def render_post_dir(post_dir: Path, *, linkedin: bool, twitter: bool) -> list[str]:
    outputs: list[str] = []
    rendered_fields: dict[str, str] = {}

    linkedin_json = post_dir / "linkedin-carousel.json"
    if linkedin and linkedin_json.exists():
        out_dir = post_dir / "linkedin-carousel"
        run_render(linkedin_json, "--square", out_dir)
        expected_pdf = out_dir / "carousel.pdf"
        expected_first = out_dir / "frame-01.png"
        if not expected_pdf.exists() or not expected_first.exists():
            raise RuntimeError(f"LinkedIn render missing expected output in {out_dir}")
        rendered_fields["linkedin_carousel"] = "linkedin-carousel.json"
        rendered_fields["linkedin_carousel_output"] = "linkedin-carousel"
        outputs.append(str(out_dir))

    twitter_json = post_dir / "twitter-resource.json"
    if twitter and twitter_json.exists():
        out_dir = post_dir / "twitter-resource"
        run_render(twitter_json, "--twitter", out_dir)
        expected = out_dir / "twitter-resource.png"
        if not expected.exists():
            raise RuntimeError(f"Twitter render missing expected output: {expected}")
        rendered_fields["twitter_resource"] = "twitter-resource.json"
        rendered_fields["twitter_resource_image"] = "twitter-resource/twitter-resource.png"
        outputs.append(str(expected))

    if rendered_fields:
        update_post_record(post_dir, rendered_fields)

    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Post folder, posts folder, or content-run folder")
    parser.add_argument("--skip-linkedin", action="store_true", help="Do not render linkedin-carousel.json")
    parser.add_argument("--skip-twitter", action="store_true", help="Do not render twitter-resource.json")
    args = parser.parse_args()

    all_outputs: list[str] = []
    for raw_path in args.paths:
        for post_dir in find_post_dirs(Path(raw_path)):
            outputs = render_post_dir(
                post_dir,
                linkedin=not args.skip_linkedin,
                twitter=not args.skip_twitter,
            )
            all_outputs.extend(outputs)

    if not all_outputs:
        print("No media JSON files found to render.", file=sys.stderr)
        return 1

    print("Rendered media:")
    for output in all_outputs:
        print(f"- {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
