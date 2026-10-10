"""Extract long Telegram channel posts without inferring their human author.

Run: uv run --with beautifulsoup4 python research/telegram/scripts/extract_announcements.py <export-root>
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

CHANNELS = {
    'AI Dev Tools Zoomcamp': ('ai-dev-tools-zoomcamp', 'aidevtoolszoomcamp'),
    'ML Zoomcamp announcements': ('ml-zoomcamp', 'mlzoomcamp'),
    'LLM Zoomcamp': ('llm-zoomcamp', 'llm_zoomcamp'),
    'Data Engineering Zoomcamp': ('de-zoomcamp', 'dezoomcamp'),
    'MLOps Zoomcamp announcements': ('mlops-zoomcamp', 'dtc_courses'),
}
root = Path(__file__).resolve().parents[3]
records, exports = [], []
for path in sorted(Path(sys.argv[1]).glob('*/messages.html')):
    raw = path.read_bytes()
    soup = BeautifulSoup(raw.decode('utf-8'), 'html.parser')
    channel = soup.select_one('.page_header .text').get_text(strip=True)
    course, username = CHANNELS[channel]
    sender = channel
    total = 0
    for message in soup.select('.message.default'):
        author = message.select_one('.body > .from_name')
        if author:
            sender = author.get_text(strip=True)
        node = message.select_one('.body > .text')
        date = message.select_one('.body > .date')
        if not node or not date:
            continue
        total += 1
        links = list(dict.fromkeys(a['href'] for a in node.select('a[href]')))
        for br in node.select('br'):
            br.replace_with('\n')
        text = node.get_text().strip()
        stamp = date['title']
        year = int(stamp.split(' ')[0].split('.')[-1])
        length = len(text)
        # Recent medium-length operational posts are useful alongside long posts.
        if length < 700 and not (year >= 2025 and length >= 450):
            continue
        mid = message['id'].removeprefix('message')
        records.append(dict(course=course, channel=channel, exported_sender=sender,
                            human_author='unverified', message_id=int(mid), date=stamp,
                            characters=length, selection='long' if length >= 700 else 'recent-medium',
                            source_file=f'{path.parent.name}/messages.html',
                            public_url=f'https://t.me/{username}/{mid}', text=text, links=links))
    exports.append(dict(channel=channel, source_file=f'{path.parent.name}/messages.html',
                        sha256=hashlib.sha256(raw).hexdigest(), text_messages=total))
out = root / 'research/telegram'
out.mkdir(parents=True, exist_ok=True)
(out / 'announcements-2026-10-10.json').write_text(json.dumps(dict(
    exported_on='2026-10-10', author_caveat='Channel export does not identify Valeriia. Human authorship is unverified.',
    exports=exports, messages=records), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
for course in CHANNELS.values():
    slug = course[0]
    subset = [r for r in records if r['course'] == slug]
    parts = ['# Historical Telegram announcement sources',
             'Extracted from the supplied October 10, 2026 Telegram HTML exports. Visible message text is preserved, including historical mistakes. These are source examples, not current drafts.',
             'The exports name the channel as sender. Valeriia’s authorship cannot be verified. Selection: at least 700 characters, plus posts from 2025 onward with at least 450 characters. Shorter posts were not extracted.',
             'Machine-readable source and export hashes: `research/telegram/announcements-2026-10-10.json`. Do not reuse historical dates, status, certificate rules, learner counts, or links without checking current cohort sources.']
    for r in subset:
        parts.extend([f"## Message {r['message_id']} — {r['date']}",
                      f"Source: {r['public_url']} | {r['characters']} characters | {r['selection']} | human author unverified",
                      '```text\n'+r['text']+'\n```'])
        parts.append('Source links:\n\n'+'\n'.join('- '+link for link in r['links']) if r['links'] else 'No links in this message.')
    target = root / f'courses/{slug}/copy-bank/telegram/historical-announcements-2026-10-10.md'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n\n'.join(parts)+'\n', encoding='utf-8')
print(json.dumps(dict(selected=len(records), by_course=dict(Counter(r['course'] for r in records))),indent=2))
