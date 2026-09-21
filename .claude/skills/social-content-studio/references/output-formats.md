# Output Formats

Use these formats when Social Content Studio should produce reusable artifacts instead of chat-only drafts.

## Content Run Layout

Create one run folder per source, campaign, or batch:

```text
content-runs/<YYYY-MM-DD-slug>/
  run.json
  source/
    source.json
    transcript.json
  ideas/
    post-ideas.json
  briefs/
    idea_001.md
  posts/
    post_001/
      post.json
      linkedin.md
      x.md
      review.json
  clips/
    clip-manifest.json
    post_001.mp4
  queue/
    social-queue.jsonl
```

Only create folders that are needed for the task. Do not put run output inside the skill directory.

## Run Record

Store run-level metadata in `run.json`:

```json
{
  "run_id": "2026-05-28-agent-evals",
  "created": "2026-05-28",
  "owner": "alexey",
  "default_platforms": ["linkedin"],
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

For X threads, store the thread in `x.md` as numbered tweets separated by blank lines:

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

## Queue Export

Use JSON Lines for scheduling handoff. Each line should represent one platform draft that is ready to publish:

```json
{"post_id":"post_001","platform":"linkedin","status":"ready","body_path":"posts/post_001/linkedin.md","clip_path":"clips/post_001.mp4","preferred_publish_at":""}
```

The queue is an interchange format, not the source of truth. The source of truth is still each post folder.
