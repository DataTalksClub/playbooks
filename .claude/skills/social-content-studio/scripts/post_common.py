"""Shared helpers for content-run post records: profiles, copy, threads, and media.

Used by scaffold_post.py, check_posts.py, typefully_drafts.py, and pull_typefully_edits.py
so every stage reads a post the same way.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
PROFILES_PATH = Path(__file__).resolve().parent.parent / "references" / "profiles.json"
THREAD_MARKER = re.compile(r"^[ \t]*(\d+)/(\d+)[ \t]*$", re.MULTILINE)
URL = re.compile(r"https?://\S+")
X_URL_LENGTH = 23


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_profiles(path: Path = PROFILES_PATH) -> dict[str, dict[str, Any]]:
    return load_json(path).get("profiles") or {}


def profile_for(owner: str, profiles: dict[str, dict[str, Any]], where: Path) -> dict[str, Any]:
    if owner not in profiles:
        raise SystemExit(f"{where}: owner '{owner}' is not in {PROFILES_PATH.name} (known: {', '.join(sorted(profiles))})")
    return profiles[owner]


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = text.strip()
    meta: dict[str, str] = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
            return meta, parts[2].strip()
    return meta, text


def read_draft(path: Path) -> str:
    return strip_frontmatter(path.read_text(encoding="utf-8"))[1]


def split_x_thread(text: str, source: Path) -> list[str]:
    """Split an x.md body on `N/M` marker lines into one text per post.

    A body without markers is a single post. Markers must run 1..M with a
    consistent total, so a typo cannot silently merge or drop tweets.
    """
    markers = list(THREAD_MARKER.finditer(text))
    if not markers:
        return [text]
    if text[: markers[0].start()].strip():
        raise ValueError(f"{source}: text before the first thread marker")
    count = len(markers)
    numbers = [int(m.group(1)) for m in markers]
    totals = {int(m.group(2)) for m in markers}
    if numbers != list(range(1, count + 1)) or totals != {count}:
        found = ", ".join(m.group(0).strip() for m in markers)
        raise ValueError(f"{source}: thread markers must run 1/{count}..{count}/{count}, found: {found}")
    posts: list[str] = []
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < count else len(text)
        chunk = text[marker.end() : end].strip()
        if not chunk:
            raise ValueError(f"{source}: thread post {marker.group(0).strip()} is empty")
        posts.append(chunk)
    return posts


def join_x_thread(posts: list[str]) -> str:
    """Inverse of split_x_thread, used to compare Typefully threads with x.md."""
    if len(posts) == 1:
        return posts[0]
    return "\n\n".join(f"{i}/{len(posts)}\n\n{text}" for i, text in enumerate(posts, 1))


def x_length(text: str) -> int:
    """Length as X counts it: every URL is 23 characters."""
    return len(URL.sub("x" * X_URL_LENGTH, text))


def post_copy(post_dir: Path, post: dict[str, Any], profile: dict[str, Any]) -> dict[str, list[str]]:
    """{platform: [post texts]} for every platform in the profile's copy map.

    Platforms fed by the same file get identical copy. Only a dedicated x.md is
    split into a thread; long-form copy reused on X stays one post.
    """
    files = post.get("files") or {}
    copy: dict[str, list[str]] = {}
    for platform, source in (profile.get("copy") or {}).items():
        if not files.get(source):
            raise ValueError(f"{post_dir / 'post.json'}: profile copies {platform} from files.{source}, which post.json does not list")
        path = post_dir / files[source]
        if not path.exists():
            raise FileNotFoundError(f"Missing {platform} draft file: {path}")
        text = read_draft(path)
        copy[platform] = split_x_thread(text, path) if platform == "x" and source == "x" else [text]
    return copy


def post_media(post: dict[str, Any]) -> dict[str, str]:
    """{kind: relative path} for the post's media (clip, carousel, image)."""
    media = dict(post.get("media") or {})
    clip = post.get("clip") or {}
    if "clip" not in media and clip.get("recommended") and clip.get("path"):
        media["clip"] = clip["path"]
    return media


def draft_variants(post_dir: Path, post: dict[str, Any], profile: dict[str, Any]) -> list[tuple[str, dict[str, list[Path]]]]:
    """Typefully drafts to create for this post: [(variant, {platform: [media paths]})].

    A variant is used only when every media file it needs exists. A post with
    no usable variant gets one text-only draft covering all copy platforms.
    """
    media = post_media(post)
    variants: list[tuple[str, dict[str, list[Path]]]] = []
    for name, mapping in (profile.get("variants") or {}).items():
        plan: dict[str, list[Path]] = {}
        usable = True
        for platform, kind in mapping.items():
            if kind in (None, "none"):
                plan[platform] = []
                continue
            if kind not in media or not (post_dir / media[kind]).is_file():
                usable = False
                break
            plan[platform] = [(post_dir / media[kind]).resolve()]
        if usable:
            variants.append((name, plan))
    if not variants:
        variants.append(("text", {platform: [] for platform in profile.get("copy") or {}}))
    return variants


def banned_phrases(profile: dict[str, Any]) -> list[str]:
    """Profile phrases plus bullets parsed from the style file section named in `banned_phrases_from`."""
    phrases = list(profile.get("banned_phrases") or [])
    reference = profile.get("banned_phrases_from")
    if reference:
        file_part, _, heading = reference.partition("#")
        text = (REPO_ROOT / file_part).read_text(encoding="utf-8")
        match = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
        if match:
            phrases += [line[2:].strip() for line in match.group(1).splitlines() if line.startswith("- ")]
    return phrases


def media_duration(path: Path) -> float | None:
    try:
        output = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
            capture_output=True, text=True, timeout=30, check=True,
        ).stdout.strip()
        return float(output)
    except (OSError, subprocess.SubprocessError, ValueError):
        return None


def timestamp_seconds(value: str) -> float:
    parts = [float(part) for part in value.split(":")]
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds
