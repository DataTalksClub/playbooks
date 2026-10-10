# Telegram announcement sources

The supplied `Downloads/channels` exports contain five course announcement channels. The October 10, 2026 extraction contains 138 candidates: 32 AI Dev Tools, 35 ML, 34 LLM, 27 Data Engineering, and 10 MLOps posts.

Selection includes posts with at least 700 visible characters and recent posts from 2025 onward with at least 450 characters. The second group keeps useful module and project updates that are shorter than the longest posts. This is a length-based candidate set, not an editorial endorsement. Short posts, photos, reactions, and service messages are excluded.

The exports identify channels as senders, not Valeriia. Human authorship remains unverified; the user approved using longer announcements as candidates. Export timestamps are preserved exactly, including their UTC offset. Do not treat that export offset as the intended timezone for a future course deadline.

## Files

- [Machine-readable extraction](announcements-2026-10-10.json): visible text, original links, message IDs, selection reasons, sender fields, and SHA-256 hashes of the five source HTML files.
- [AI Dev Tools examples](../../courses/ai-dev-tools-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md).
- [ML examples](../../courses/ml-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md).
- [LLM examples](../../courses/llm-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md).
- [Data Engineering examples](../../courses/de-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md).
- [MLOps examples](../../courses/mlops-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md).
- [ML Zoomcamp 2026 drafts](../../courses/campaigns/ml-zoomcamp-2026/copy-bank/telegram/README.md).

The source digests preserve visible wording, including mistakes. Original link targets appear below each message because Telegram exports sometimes show different text for a link. Public message URLs are derived from the known course-channel usernames and message IDs; they have not all been opened individually.

## Re-extract

Run from the playbooks repository:

```powershell
uv run --with beautifulsoup4 python research/telegram/scripts/extract_announcements.py C:\Users\User\Downloads\channels
```

The script writes this dated extraction and the five course digests. Read the source examples for structure and topic selection. Verify every date, deadline, availability claim, registration link, certificate rule, and learner count before adapting one for a new cohort.
