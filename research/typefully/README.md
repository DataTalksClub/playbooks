# Typefully Social Export

This folder stores Typefully posts from Alexey social media that mention:

- `zoomcamp`
- `free course`

Run the exporter from the repo root:

```bash
TYPEFULLY_API_KEY=... python3 research/typefully/scripts/download_posts.py \
  --social-set-id TYPEFULLY_SOCIAL_SET_ID \
  --limit 50 \
  --hydrate-details
```

If you do not know the social set ID, let the script discover it:

```bash
TYPEFULLY_API_KEY=... python3 research/typefully/scripts/download_posts.py \
  --social-set-name-match alexey \
  --limit 50 \
  --hydrate-details
```

The default endpoint is:

```text
/v2/social-sets/{social_set_id}/drafts
```

Use `--hydrate-details` when you need full post text. Without it, Typefully's list endpoint returns preview snippets only.

If Typefully uses a different read endpoint for the account, pass it explicitly:

```bash
TYPEFULLY_API_KEY=... python3 research/typefully/scripts/download_posts.py \
  --social-set-id TYPEFULLY_SOCIAL_SET_ID \
  --endpoint "/v2/social-sets/{social_set_id}/posts"
```

The exporter writes:

- `raw/typefully-raw-*.json`: raw paginated API responses.
- `filtered/typefully-matches-*.json`: normalized matching records.
- `filtered/typefully-matches-*.csv`: spreadsheet-friendly matching records.
- `filtered/typefully-matches-*.md`: human-readable post digest.
- `manifest.json`: latest export summary and file pointers.

Raw and timestamped filtered exports are ignored by Git. Promote a reviewed export to `typefully-examples.json`, `typefully-examples.csv`, and `typefully-examples.md` when it should become shared research.

Do not commit or store the Typefully API key in this repo.

## Full Export

`all-posts/` holds every post on Alexey's account, not only the course-related ones. Match on any text to skip the term filter:

```bash
set -a && . ./.env && set +a
python3 research/typefully/scripts/download_posts.py \
  --social-set-id 188312 \
  --hydrate-details \
  --term " " \
  --limit 50 \
  --max-pages 100 \
  --output-dir research/typefully/all-posts
```

The raw and filtered files are gitignored; `all-posts/manifest.json` records the latest run. The analysis of this export is in `.claude/skills/social-content-studio/references/alexey-content-sources.md`.
