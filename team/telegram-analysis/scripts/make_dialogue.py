"""Render parsed JSONL + voice transcripts into a readable dialogue file.

Usage: python make_dialogue.py <in_jsonl> <transcripts_jsonl> <out_txt>
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def load_transcripts(path):
    t = {}
    if path and Path(path).exists():
        for line in open(path, encoding="utf-8"):
            rec = json.loads(line)
            t[rec["file"]] = rec.get("text", "")
    return t


def fmt_dur(sec):
    if not sec:
        return "?"
    m, s = divmod(int(sec), 60)
    return f"{m}:{s:02d}" if m else f"{s}s"


def main():
    in_jsonl, transcripts_path, out_txt = sys.argv[1:4]
    transcripts = load_transcripts(transcripts_path)
    recs = [json.loads(l) for l in open(in_jsonl, encoding="utf-8")]

    out = open(out_txt, "w", encoding="utf-8")
    last_date = None
    for r in recs:
        ts = datetime.fromisoformat(r["ts"])
        date = ts.strftime("%Y-%m-%d")
        if date != last_date:
            out.write(f"\n===== {date} =====\n")
            last_date = date
        parts = []
        reply = f" [re #{r['reply_to']}]" if r.get("reply_to") else ""
        fwd = f" [fwd from {r['forwarded_from']}]" if r.get("forwarded_from") else ""
        for m in r.get("media", []):
            if m["type"] == "voice":
                fname = m["path"].split("/")[-1]
                tr = transcripts.get(fname)
                if tr is None:
                    parts.append(f"(VOICE {fmt_dur(m.get('duration_sec'))} — not transcribed)")
                elif not tr.strip():
                    parts.append(f"(VOICE {fmt_dur(m.get('duration_sec'))} — [silence/no speech])")
                else:
                    lang_hint = ""
                    parts.append(f"(VOICE {fmt_dur(m.get('duration_sec'))}) {tr.strip()}{lang_hint}")
            elif m["type"] == "photo":
                parts.append("[photo]")
            elif m["type"] == "video_note":
                parts.append(f"[video note {fmt_dur(m.get('duration_sec'))}]")
            elif m["type"] == "file":
                parts.append(f"[file: {m.get('title') or m['path'].split('/')[-1]}]")
            elif m["type"] == "sticker":
                parts.append(f"[sticker {m.get('emoji', '')}]")
        text = r["text"].strip()
        body = " + ".join([p for p in parts if p])
        if text:
            body = (body + "\n    " + text) if body else text
        if not body:
            body = "(empty)"
        time_s = ts.strftime("%H:%M")
        out.write(f"[{time_s}] {r['sender']}{reply}{fwd}: {body}\n")
    out.close()
    print(f"wrote {out_txt}")


if __name__ == "__main__":
    main()
