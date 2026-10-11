"""Render team-emails-2026.jsonl into readable digests for analysis.

Outputs (in data/):
  email-threads-digest.txt  - all threads chronological, bodies trimmed to ~1500 chars
  email-by-grace.txt        - every message authored by Grace (full authored body)
  email-by-valeriia.txt     - every message authored by Valeriia (full authored body)
  email-thread-index.txt    - one line per thread: id, dates, participants, msg count
  email-stats.txt           - volume per month per author, top counterparties
"""
import json
import os
import re
from collections import Counter, defaultdict

BASE = r"C:\Users\User\git\playbooks\team\telegram-analysis"
SRC = os.path.join(BASE, "data", "team-emails-2026.jsonl")

GMAIL_Q = re.compile(r"^On\b[^\n]{2,300}\bwrote:\s*$|^On\b[^\n]{2,300}\s*\r?\n\s*wrote:\s*$", re.M)
OUTLOOK_Q = re.compile(r"^From: .+\r?\nSent: .+\s*$", re.M)
SEP_Q = re.compile(r"^-{3,}\s*(Forwarded message|Original Message)\s*-{3,}\s*$", re.M | re.I)
GT_Q = re.compile(r"^> ?", re.M)
HTML_Q = re.compile(r"<blockquote", re.I)


def authored(body):
    """Return the part of the body the sender actually wrote (strip quoted reply chain)."""
    if not body:
        return ""
    cut = len(body)
    for rx in (GMAIL_Q, OUTLOOK_Q, SEP_Q, GT_Q, HTML_Q):
        m = rx.search(body)
        if m:
            cut = min(cut, m.start())
    return body[:cut].rstrip()


def short_date(iso):
    return iso[:10]


def hhmm(iso):
    return iso[11:16]


def person(s):
    """'Grace Lordel Domisiw <grace@datatalks.club>' -> 'Grace Lordel Domisiw <grace@datatalks.club>' (keep as-is)"""
    return (s or "").replace("\r", " ").replace("\n", " ").strip()


def classify(m, authored_body):
    frm = (m.get("from") or "").lower()
    if "grace@datatalks.club" in frm:
        return "grace"
    if "valeriia" in frm:
        return "valeriia"
    if "alexey" in frm or "alexey.s.grigoriev" in frm:
        return "alexey"
    return "other"


def main():
    msgs = []
    seen = set()
    dupes = 0
    empty_body = 0
    with open(SRC, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = json.loads(line)
            key = (m.get("threadId"), m.get("messageId"))
            if key in seen:
                dupes += 1
                continue
            seen.add(key)
            if not (m.get("body") or "").strip():
                empty_body += 1
            msgs.append(m)

    for m in msgs:
        m["_authored"] = authored(m.get("body") or "")
        if not m["_authored"].strip() and (m.get("snippet") or "").strip():
            m["_authored"] = "[body missing; snippet:] " + m["snippet"]
        m["_who"] = classify(m, m["_authored"])

    msgs.sort(key=lambda m: m["date"])
    threads = defaultdict(list)
    for m in msgs:
        threads[m["threadId"]].append(m)

    def atts(m):
        out = []
        for a in m.get("attachments") or []:
            sz = a.get("size") or 0
            out.append(f"{a.get('filename','?')} ({a.get('mimeType','?')}, {sz//1024}KB)")
        return out

    # ---------- 1. threads digest ----------
    with open(os.path.join(BASE, "data", "email-threads-digest.txt"), "w", encoding="utf-8") as f:
        for tid in sorted(threads, key=lambda t: threads[t][0]["date"]):
            ms = threads[tid]
            subj = ms[0]["subject"] or "(no subject)"
            subj = re.sub(r"^(re|fwd|fw):\s*", "", subj, flags=re.I)
            f.write(f"##### THREAD {tid}: {subj}\n")
            f.write(f"[{len(ms)} msgs, {short_date(ms[0]['date'])} -> {short_date(ms[-1]['date'])}]\n")
            for m in ms:
                f.write(f"\n[{short_date(m['date'])} {hhmm(m['date'])}] From: {person(m['from'])} | To: {person(m['to'])}")
                cc = person(m.get("cc") or "")
                if cc:
                    f.write(f" | Cc: {cc}")
                f.write("\n")
                a = atts(m)
                if a:
                    f.write("Attachments: " + "; ".join(a) + "\n")
                body = m["_authored"]
                if len(body) > 1500:
                    body = body[:1500].rstrip() + "\n[[...truncated...]]"
                f.write(body + "\n")
            f.write("\n\n")

    # ---------- 2/3. per-author files ----------
    for who, fname in (("grace", "email-by-grace.txt"), ("valeriia", "email-by-valeriia.txt")):
        with open(os.path.join(BASE, "data", fname), "w", encoding="utf-8") as f:
            n = 0
            for m in msgs:
                if m["_who"] != who:
                    continue
                n += 1
                f.write("=" * 78 + "\n")
                f.write(f"[{short_date(m['date'])} {hhmm(m['date'])}] THREAD {m['threadId']}: {m['subject']}\n")
                f.write(f"To: {person(m['to'])} | Cc: {person(m.get('cc') or '')}\n")
                a = atts(m)
                if a:
                    f.write("Attachments: " + "; ".join(a) + "\n")
                f.write("-" * 78 + "\n")
                f.write((m["_authored"] or "").strip() + "\n\n")
            print(f"{fname}: {n} messages")

    # ---------- 4. thread index ----------
    with open(os.path.join(BASE, "data", "email-thread-index.txt"), "w", encoding="utf-8") as f:
        for tid in sorted(threads, key=lambda t: threads[t][0]["date"]):
            ms = threads[tid]
            subj = ms[0]["subject"] or "(no subject)"
            people = []
            for m in ms:
                for p in re.findall(r"<([^>]+)>", (m.get("from") or "") + " " + (m.get("to") or "")):
                    if p not in people:
                        people.append(p)
            whos = Counter(m["_who"].split("(")[0] for m in ms)
            f.write(f"{short_date(ms[0]['date'])} {tid} [{len(ms)}m g{whos.get('grace',0)}/v{whos.get('valeriia',0)}/a{whos.get('alexey',0)}] {subj[:80]}\n")
            f.write(f"    participants: {', '.join(people[:12])}\n")

    # ---------- 5. stats ----------
    with open(os.path.join(BASE, "data", "email-stats.txt"), "w", encoding="utf-8") as f:
        f.write(f"messages: {len(msgs)} (deduped {dupes}), threads: {len(threads)}, empty bodies: {empty_body}\n\n")
        per = defaultdict(Counter)
        for m in msgs:
            per[m["date"][:7]][m["_who"]] += 1
        f.write("messages per month per author:\n")
        for mo in sorted(per):
            c = per[mo]
            f.write(f"  {mo}: total {sum(c.values()):3d} | grace {c['grace']:3d} | valeriia {c['valeriia']:3d} | alexey {c['alexey']:3d} | other {c['other']:3d}\n")
        f.write("\ntop external senders (non-dtc):\n")
        ext = Counter(m["from"] for m in msgs if m["_who"] == "other")
        for s, c in ext.most_common(60):
            f.write(f"  {c:3d}  {s}\n")
        f.write("\nthreads containing grace / valeriia / alexey msgs:\n")
        g = sum(1 for t in threads.values() if any(m["_who"] == "grace" for m in t))
        v = sum(1 for t in threads.values() if any(m["_who"] == "valeriia" for m in t))
        a = sum(1 for t in threads.values() if any(m["_who"] == "alexey" for m in t))
        f.write(f"  grace in {g}, valeriia in {v}, alexey in {a} of {len(threads)} threads\n")

    print("done")


if __name__ == "__main__":
    main()
