"""Parse a Telegram Desktop HTML export into JSONL, keeping messages from 2026 onward.

Usage: python parse_export.py <export_dir> <out_jsonl> [--since 2026-01-01]
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

DATE_RE = re.compile(r"(\d{2})\.(\d{2})\.(\d{4}) (\d{2}):(\d{2}):(\d{2})")
REPLY_RE = re.compile(r"go_to_message(\d+)")


def parse_ts(title: str):
    m = DATE_RE.search(title)
    if not m:
        return None
    d, mo, y, h, mi, s = map(int, m.groups())
    return datetime(y, mo, d, h, mi, s)


def parse_duration(text: str):
    # "00:54", "1:23:45", "12s", "1m 23s"
    t = text.strip()
    if ":" in t:
        parts = [int(p) for p in t.split(":")]
        sec = 0
        for p in parts:
            sec = sec * 60 + p
        return sec
    m = re.match(r"(?:(\d+)m)?\s*(?:(\d+)s)?", t)
    if m and (m.group(1) or m.group(2)):
        return int(m.group(1) or 0) * 60 + int(m.group(2) or 0)
    return None


def parse_media(a_tag):
    """Extract media info from an <a class='media ...'> tag or an <img class='photo'>."""
    classes = a_tag.get("class", [])
    href = a_tag.get("href", "")
    title_el = a_tag.select_one(".title")
    title = title_el.get_text(" ", strip=True) if title_el else ""
    status_el = a_tag.select_one(".status")
    status = status_el.get_text(" ", strip=True) if status_el else ""
    if "media_voice_message" in classes:
        return {"type": "voice", "path": href, "duration_sec": parse_duration(status)}
    if "media_photo" in classes or "media_video_message" in classes:
        kind = "video_note" if "media_video_message" in classes else "photo"
        return {"type": kind, "path": href, "duration_sec": parse_duration(status)}
    if "media_file" in classes:
        return {"type": "file", "path": href, "title": title, "status": status}
    if "media_sticker" in classes:
        return {"type": "sticker", "path": href, "emoji": title}
    if href:
        return {"type": "link_media", "path": href, "title": title}
    return None


def parse_page(soup, page_name, out_f, since, stats):
    current_sender = None
    for msg in soup.select("div.message"):
        classes = msg.get("class", [])
        if "service" in classes:
            continue
        msg_id = msg.get("id", "").replace("message", "")
        date_div = msg.select_one(".date")
        ts = parse_ts(date_div.get("title", "")) if date_div else None
        if ts is None:
            continue

        from_el = msg.select_one(".from_name")
        if from_el:
            current_sender = from_el.get_text(" ", strip=True).rstrip(",")
        sender = current_sender

        body = msg.select_one(".body")

        # forwarded messages: inner .forwarded holds original author
        forwarded = None
        fwd = msg.select_one(".forwarded")
        if fwd:
            fwd_from = fwd.select_one(".from_name")
            if fwd_from:
                forwarded = fwd_from.get_text(" ", strip=True)

        reply_to = None
        reply_el = msg.select_one(".reply_to a")
        if reply_el:
            m = REPLY_RE.search(reply_el.get("href", ""))
            if m:
                reply_to = int(m.group(1))

        media = []
        for a in msg.select("a.media"):
            info = parse_media(a)
            if info:
                media.append(info)
        for img in msg.select("img.photo"):
            media.append({"type": "photo", "path": img.get("src", "")})

        text_el = msg.select_one(".text")
        text = ""
        if text_el:
            text = text_el.get_text("\n", strip=True)

        if ts < since:
            stats["before_cutoff"] += 1
            # keep sender chain accurate for later messages
            continue

        rec = {
            "id": int(msg_id) if msg_id.isdigit() else msg_id,
            "ts": ts.isoformat(timespec="seconds"),
            "page": page_name,
            "sender": sender,
            "text": text,
            "media": media,
        }
        if reply_to:
            rec["reply_to"] = reply_to
        if forwarded:
            rec["forwarded_from"] = forwarded
        out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        stats["kept"] += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export_dir")
    ap.add_argument("out_jsonl")
    ap.add_argument("--since", default="2026-01-01")
    args = ap.parse_args()

    since = datetime.fromisoformat(args.since)
    export = Path(args.export_dir)
    pages = sorted(
        export.glob("messages*.html"),
        key=lambda p: (
            int(re.search(r"messages(\d*)", p.stem).group(1) or 1)
        ),
    )
    stats = {"kept": 0, "before_cutoff": 0}
    with open(args.out_jsonl, "w", encoding="utf-8") as out_f:
        for page in pages:
            soup = BeautifulSoup(page.read_text(encoding="utf-8"), "lxml")
            parse_page(soup, page.name, out_f, since, stats)
            print(f"{page.name}: cumulative kept={stats['kept']} skipped={stats['before_cutoff']}", file=sys.stderr)

    print(json.dumps(stats))


if __name__ == "__main__":
    main()
