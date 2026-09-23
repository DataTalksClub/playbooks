# Output Formats

Use these formats when Social Content Studio should produce reusable artifacts instead of chat-only drafts.

## Content Run Layout

Create one run folder per source, campaign, or batch, shared by every owner. Do not split a source into one run per owner: each post records its `owner`, and post IDs carry the profile's `post_prefix` from `profiles.json` (`alexey_001`, `dtc_001`).

```text
content-runs/<YYYY-MM-DD-slug>/
  run.json                 "owners": ["alexey", "datatalksclub"]
  source/
    source.json            facts, links every post must carry, transcript caveats
    full_transcript.json
  post-ideas.md
  briefs/
    idea_001.md            raw transcript excerpts per idea
  posts/
    alexey_001/
      post.json
      linkedin.md          Alexey: one copy for LinkedIn, X, and Substack
      review.json          lint (check_posts.py) and reviewer (review stage)
      linkedin-carousel/   visual draft media
      twitter-resource/
      typefully/           pulled Typefully versions (pull_typefully_edits.py)
    dtc_001/
      post.json
      linkedin.md
      x.md                 DataTalks.Club X thread
      review.json
  clips/
    clip-manifest.json
    alexey-001-<slug>.mp4
  queue/
    typefully-drafts.json   created drafts, written by typefully_drafts.py
  edits.md                 diffs between generated and published copy
```

Create posts with `scripts/scaffold_post.py`, which writes the right files for the owner. Only create folders that are needed for the task. Do not put run output inside the skill directory.

## Run Record

Store run-level metadata in `run.json`:

```json
{
  "run_id": "2026-05-28-agent-evals",
  "created": "2026-05-28",
  "owners": ["alexey", "datatalksclub"],
  "status": "drafting",
  "source": {
    "source_id": "youtube_abc123",
    "type": "youtube",
    "title": "",
    "url": "",
    "video_id": "",
    "transcript_path": "source/transcript.json",
    "duration_seconds": 0
  }
}
```

Allowed run `status` values:

- `drafting`
- `reviewing`
- `ready`
- `scheduled`
- `published`
- `archived`

## Post Record

Every post folder must contain a `post.json` record:

```json
{
  "post_id": "post_001",
  "idea_id": "idea_001",
  "source_id": "youtube_abc123",
  "owner": "alexey",
  "platforms": ["linkedin", "x"],
  "status": "draft",
  "topic": "",
  "created": "2026-05-28",
  "updated": "2026-05-28",
  "angle": "",
  "cta": "",
  "source_moments": [
    {
      "start": "00:05:50",
      "end": "00:07:30",
      "note": "",
      "excerpt_path": "../../briefs/idea_001.md"
    }
  ],
  "clip": {
    "recommended": true,
    "clip_id": "clip_001",
    "manifest_path": "../../clips/clip-manifest.json",
    "path": "../../clips/post_001.mp4",
    "duration_seconds": 100
  },
  "files": {
    "linkedin": "linkedin.md",
    "x": "x.md",
    "review": "review.json"
  },
  "scheduling": {
    "ready_for_queue": false,
    "preferred_publish_at": "",
    "external_id": ""
  }
}
```

Allowed post `status` values:

- `draft`
- `needs_review`
- `approved`
- `ready`
- `scheduled`
- `published`
- `rejected`
- `archived`

## Platform Draft Markdown

Use one Markdown file per platform for human editing:

```markdown
---
post_id: post_001
platform: linkedin
status: draft
---

Draft text here.
```

Keep the Markdown body clean enough to paste or send to a publishing API without extra extraction logic.

For Alexey, `linkedin.md` is the shared copy for LinkedIn, X, and Substack Notes. List `"platforms": ["linkedin", "x", "substack"]` in `post.json` with only `files.linkedin`; the Typefully handoff reuses that file for X and Substack. Write `x.md` only when a separate X thread is requested, or for DataTalks.Club.

For X threads, store the thread in `x.md` as numbered tweets separated by blank lines. The Typefully handoff splits on the `N/M` lines, so keep them on their own line and numbered `1/M` through `M/M`:

```markdown
---
post_id: post_001
platform: x
status: draft
---

1/5

First tweet text with the hook and, for event promos, the registration link when possible.

2/5

Second tweet text that continues the same idea.
```

Keep each numbered tweet under 280 characters. For event announcements, each thread should have one clear problem-led idea and should point to the event for the solution rather than becoming a full tutorial.

## Review Record

Store the writer-reviewer-editor loop in `review.json` when saving structured posts:

```json
{
  "post_id": "post_001",
  "checks": {
    "audience_fit": "pass",
    "specificity": "pass",
    "voice": "pass",
    "unsupported_claims": "pass",
    "style_rules": "pass",
    "cta": "pass"
  },
  "notes": [],
  "changed": []
}
```

Use `pass`, `warn`, or `fail` for check values.

In artifact mode, `review.json` also holds two machine-written blocks, and these replace self-assessed `checks` for content runs:

- `lint`: written by `scripts/check_posts.py` (`checked`, `errors`, `warnings`).
- `reviewer`: written by the independent review in `review-stage.md` (`claims` with the transcript source and speaker for each claim, and `findings` with `severity` and `status`).

## Media

`post.json.media` lists the post's media by kind, with paths relative to the post folder:

```json
"media": {
  "clip": "../../clips/alexey-001-issue-hub.mp4",
  "carousel": "linkedin-carousel/carousel.pdf",
  "image": "twitter-resource/twitter-resource.png"
}
```

The owner's `variants` in `profiles.json` decide which Typefully drafts these become. For Alexey: a `clip` draft on every platform, and a `visual` draft with the carousel on LinkedIn and the image on X.
