#!/usr/bin/env python3
"""Export sent DataTalks.Club Weekly issues from Mailchimp into newsletter/issues/.

Read-only: this script only sends GET requests. It never creates, edits,
schedules, or sends campaigns.

For each sent "Weekly email #N" campaign it writes:
  newsletter/issues/<YYYY-MM-DD>-weekly-<N>/issue.md   text as sent, with links
  newsletter/issues/<YYYY-MM-DD>-weekly-<N>/stats.json opens, clicks, clicks per slot
If that folder holds a draft (status: draft), the draft is kept as draft.md so
the sent text can be compared with what was drafted.

It also rewrites newsletter/performance.md, a summary across the exported issues.

Usage (from the repository root, with MAILCHIMP_API_KEY in the environment or .env):
  python3 .claude/skills/dtc-newsletter/scripts/mailchimp_export.py --last 12
"""

import argparse
import base64
import json
import os
import re
import statistics
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ISSUES = ROOT / "newsletter" / "issues"
LIST_ID = "97178021aa"  # "DataTalks" audience
TITLE_RE = re.compile(r"Weekly email #(\d+)")
HEADING_RE = re.compile(r"^\*\* (.+)\n-{20,}\n", re.M)
LINK_LINE_RE = re.compile(r"^(.+?) \((https?://[^)\s]+)\)\s*$")
URL_RE = re.compile(r"^https?://\S+$")
LIST_RE = re.compile(r"^(\* |\d+\. )")
INLINE_LINK_RE = re.compile(r"^(.+?) \((https?://[^)\s]+)\)\s*(.*)$")
FOOTER_MARKERS = ("DataTalks.Club is the place to talk about data", "\n=====")


def api_key():
    key = os.environ.get("MAILCHIMP_API_KEY")
    env = ROOT / ".env"
    if not key and env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("MAILCHIMP_API_KEY="):
                key = line.split("=", 1)[1].strip()
    if not key:
        raise SystemExit("Set MAILCHIMP_API_KEY in the environment or in .env at the repository root.")
    return key


def get(key, path, **params):
    dc = key.rsplit("-", 1)[1]
    url = f"https://{dc}.api.mailchimp.com/3.0/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    token = base64.b64encode(f"x:{key}".encode()).decode()
    request = urllib.request.Request(url, headers={"Authorization": f"Basic {token}"}, method="GET")
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def split_slots(plain_text):
    """Return [(heading, body_text)] for the slots between the header and the footer."""
    cut = min((i for i in (plain_text.find(m) for m in FOOTER_MARKERS) if i > 0), default=len(plain_text))
    text = plain_text[:cut]
    matches = list(HEADING_RE.finditer(text))
    slots = []
    for i, match in enumerate(matches):
        heading = match.group(1).strip()
        if heading.startswith("DataTalks.Club Weekly"):
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        slots.append((heading, text[match.end():end].strip()))
    return slots


def slot_markdown(heading, body):
    """Convert one plain-text slot to the issue.md block format. Returns (markdown, urls, sponsored)."""
    lines = [line.rstrip() for line in body.splitlines()]
    urls, out, sponsored = [], [], False
    if lines and URL_RE.match(lines[0].strip()):
        urls.append(lines.pop(0).strip())  # linked heading image or title
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        link = LINK_LINE_RE.match(stripped.lstrip("* ").strip())
        if stripped.startswith("Sponsored content") and link:
            sponsored = True
            urls.append(link.group(2))
            out.append(("label", "_Sponsored content_"))
        elif LIST_RE.match(stripped):
            marker = "- " if stripped.startswith("* ") else LIST_RE.match(stripped).group(1)
            item = stripped[len(LIST_RE.match(stripped).group(1)):].strip()
            inline = INLINE_LINK_RE.match(item)
            if inline:
                urls.append(inline.group(2))
                rest = f" {inline.group(3)}" if inline.group(3) else ""
                item = f"[{inline.group(1)}]({inline.group(2)}){rest}"
            out.append(("bullet", marker + item))
        elif link and len(link.group(1)) <= 60:
            urls.append(link.group(2))
            out.append(("para", f"[{link.group(1)}]({link.group(2)})"))
        else:
            urls.extend(re.findall(r"\((https?://[^)\s]+)\)", stripped))
            out.append(("para", stripped))

    parts = [f"## {heading}"]
    previous = None
    for kind, text in out:
        parts.append(text if (kind == "bullet" and previous == "bullet") else "\n" + text)
        previous = kind
    return "\n".join(parts).strip(), urls, sponsored


def slot_type(heading, sponsored):
    h = heading.lower()
    if sponsored:
        return "promo (sponsored)"
    if "zoomcamp" in h and ("module" in h or "project" in h or "homework" in h):
        return "zoomcamp"
    if h.startswith("upcoming events"):
        return "events list"
    if h.startswith("book of the week"):
        return "book of the week"
    if "alexey on data" in h:
        return "alexey on data"
    if "recording" in h or h.startswith("workshop notes"):
        return "recording or notes"
    if h.endswith("cohort"):
        return "course registration"
    if "live events" in h:
        return "course event series"
    return "event detail / other"


def export_issue(key, campaign):
    number = int(TITLE_RE.search(campaign["settings"]["title"]).group(1))
    date = campaign["send_time"][:10]
    folder = ISSUES / f"{date}-weekly-{number}"
    folder.mkdir(parents=True, exist_ok=True)

    content = get(key, f"campaigns/{campaign['id']}/content", fields="plain_text")
    clicks = get(key, f"reports/{campaign['id']}/click-details", count=200,
                 fields="urls_clicked.url,urls_clicked.total_clicks,urls_clicked.unique_clicks")
    url_clicks = defaultdict(lambda: [0, 0])
    for item in clicks.get("urls_clicked", []):
        url_clicks[item["url"]][0] += item["total_clicks"]
        url_clicks[item["url"]][1] += item["unique_clicks"]

    blocks, slot_stats = [], []
    for heading, body in split_slots(content.get("plain_text", "")):
        markdown, urls, sponsored = slot_markdown(heading, body)
        blocks.append(markdown)
        counted = {u for u in urls if "datatalks.club/support" not in u}
        slot_stats.append({
            "heading": heading,
            "type": slot_type(heading, sponsored),
            "clicks": sum(url_clicks[u][0] for u in counted),
            "unique_clicks_summed": sum(url_clicks[u][1] for u in counted),
        })

    settings, summary = campaign["settings"], campaign.get("report_summary", {})
    issue = folder / "issue.md"
    if issue.exists() and "status: draft" in issue.read_text():
        issue.rename(folder / "draft.md")
    front = [
        "---",
        f"issue: {number}",
        f"send_date: {date}",
        "status: sent",
        f"subject: {json.dumps(settings.get('subject_line', ''), ensure_ascii=False)}",
        f"preview_text: {json.dumps(settings.get('preview_text', ''), ensure_ascii=False)}",
        f"mailchimp_title: {json.dumps(settings.get('title', ''), ensure_ascii=False)}",
        f"archive_url: {campaign.get('long_archive_url') or campaign.get('archive_url', '')}",
        "source: Mailchimp export (plain-text version, as sent)",
        "---",
    ]
    issue.write_text("\n".join(front) + "\n\n" + "\n\n".join(blocks) + "\n")

    stats = {
        "issue": number,
        "send_date": date,
        "subject": settings.get("subject_line", ""),
        "open_rate": summary.get("open_rate"),
        "click_rate": summary.get("click_rate"),
        "unique_opens": summary.get("unique_opens"),
        "subscriber_clicks": summary.get("subscriber_clicks"),
        "sponsored_label_clicks": sum(v[0] for u, v in url_clicks.items() if "datatalks.club/support" in u),
        "slots": slot_stats,
        "note": "Slot clicks sum every link position in the slot (heading, title, button), so unique_clicks_summed can count one person more than once.",
    }
    (folder / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n")
    return stats


def write_performance(all_stats):
    all_stats = sorted(all_stats, key=lambda s: s["issue"], reverse=True)
    cell = lambda v: str(v).replace("|", "\\|")
    pct = lambda v: f"{v * 100:.1f}%" if isinstance(v, (int, float)) else "n/a"
    lines = [
        "# DataTalks.Club Weekly performance",
        "",
        "Generated by `.claude/skills/dtc-newsletter/scripts/mailchimp_export.py` from Mailchimp reports. Open rates are inflated by Apple Mail Privacy Protection, so compare issues with each other rather than reading them as absolute numbers. Slot clicks add up every link position in a slot, and a link that appears in two slots (an event in a detail slot and in the Upcoming events list) counts toward both.",
        "",
        "## Issues",
        "",
        "| # | Date | Subject | Open rate | Click rate | Most clicked slot |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for s in all_stats:
        top = max(s["slots"], key=lambda x: x["clicks"], default=None)
        top_text = f"{cell(top['heading'])} ({top['clicks']})" if top else "n/a"
        lines.append(f"| {s['issue']} | {s['send_date']} | {cell(s['subject'])} | {pct(s['open_rate'])} | {pct(s['click_rate'])} | {top_text} |")

    by_type = defaultdict(list)
    for s in all_stats:
        for slot in s["slots"]:
            by_type[slot["type"]].append(slot["clicks"])
    lines += ["", "## Clicks by slot type", "", "| Slot type | Appearances | Median clicks | Max clicks |", "| --- | --- | --- | --- |"]
    for kind, values in sorted(by_type.items(), key=lambda kv: -statistics.median(kv[1])):
        lines.append(f"| {kind} | {len(values)} | {statistics.median(values):.0f} | {max(values)} |")
    (ROOT / "newsletter" / "performance.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--last", type=int, default=12, help="Number of most recent weekly issues to export (default 12)")
    args = parser.parse_args()

    key = api_key()
    campaigns = get(key, "campaigns", status="sent", list_id=LIST_ID, sort_field="send_time", sort_dir="DESC",
                    count=max(50, args.last * 3),
                    fields="campaigns.id,campaigns.send_time,campaigns.settings,campaigns.report_summary,"
                           "campaigns.archive_url,campaigns.long_archive_url")["campaigns"]
    weekly = [c for c in campaigns if TITLE_RE.search(c["settings"].get("title") or "")][: args.last]
    all_stats = []
    for campaign in weekly:
        stats = export_issue(key, campaign)
        all_stats.append(stats)
        print(f"#{stats['issue']} {stats['send_date']}: {len(stats['slots'])} slots")
    write_performance(all_stats)
    print(f"Wrote newsletter/performance.md from {len(all_stats)} issues.")


if __name__ == "__main__":
    main()
