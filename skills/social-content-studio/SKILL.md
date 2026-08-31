---
name: social-content-studio
description: Create, critique, revise, and save structured social media post artifacts for Alexey. Use when drafting LinkedIn/X posts in Alexey's voice, adapting source material into Alexey-style posts, reviewing copy for Alexey's audience, preparing Alexey course/community announcements, turning transcript or video ideas into post files, or producing machine-readable records for later scheduling, clipping, API publishing, or file-based editing. Do not use for posts published by DataTalks.Club as an organization.
---

# Social Content Studio

This skill is for Alexey's accounts. DataTalks.Club may be the subject of his post, but that does not make it a DataTalks.Club account post. Use `$datatalks-event-promotion` for copy published in DataTalks.Club's organizational voice.

## Core Workflow

1. Identify the content owner, platform, goal, source material, and whether the user wants a draft, a critique, a revision, variants, or saved post files.
2. For Alexey content, read `references/alexey-profile.md`, `references/alexey-audience.md`, and `references/alexey-style.md`.
3. If examples are needed for calibration, read `references/alexey-good-posts.md`.
4. Draft in Alexey's voice using the user's source material. Preserve factual claims and links exactly unless the user asks for rewriting or verification.
5. Run an internal reviewer pass before finalizing. Check audience fit, specificity, evidence, structure, hook, and style rules.
6. Revise the strongest version using the reviewer pass. If useful, provide 2-3 variants with clearly different angles.
7. If the user asks to save drafts, create post files in the user's current project or requested folder, never inside the skill directory.
8. For multi-post, transcript, video, clip, scheduling, or automation workflows, use artifact mode by default and read `references/output-formats.md`.
9. For saved Alexey post artifacts, generate LinkedIn carousel and X/Twitter resource media by default with `$alexey-carousel-generator` after the post files are saved, unless the user explicitly asks for text-only posts.

## Artifact Mode

Use artifact mode when the user asks for saved files, reusable outputs, a pipeline, a batch of posts, scheduling/API handoff, or posts connected to transcript/video clips.

In artifact mode:

1. Create or use a content-run folder outside the skill directory. Prefer `content-runs/<YYYY-MM-DD-slug>/` unless the user gives another folder.
2. Keep chat output brief. Treat files as the source of truth.
3. Store one folder per post under `posts/<post_id>/`.
4. Save human-editable platform drafts as Markdown, such as `linkedin.md` and `x.md`.
5. Save machine-readable metadata in each `post.json`.
6. Preserve stable IDs from upstream tools: `idea_id`, `source_id`, and `clip_id` when available.
7. Link posts to transcript evidence with `source_moments` and `excerpt_path`.
8. Link posts to generated or planned video clips with the `clip` object.
9. Save the reviewer pass in `review.json` when creating structured records.
10. Validate generated records with `scripts/validate_post_records.py` when practical.
11. When the user asks to send drafts to Typefully, use `scripts/typefully_drafts.py` and avoid storing API keys in files.
12. For Alexey posts, generate `linkedin-carousel.json` and `twitter-resource.json` in each post folder, render them there, and record the rendered paths in `post.json.files` unless the user explicitly asks to skip media.

Use these scripts when helpful:

- `scripts/create_content_run.py`: create a standard run folder and `run.json`.
- `scripts/validate_post_records.py`: validate `posts/*/post.json`.
- `scripts/export_social_queue.py`: export `ready` posts to `queue/social-queue.jsonl` for scheduling/API handoff.
- `scripts/typefully_drafts.py`: create Typefully API v2 drafts from `posts/*` artifacts.

Do not parse chat output for downstream automation when files can be written instead.

## Typefully Handoff

Use Typefully API v2 for publishing handoff. Draft creation is scoped to a Typefully social set:

```text
POST /v2/social-sets/{social_set_id}/drafts
```

The script `scripts/typefully_drafts.py` reads each post folder, builds the `platforms` payload from `linkedin.md` and `x.md`, creates one Typefully draft per requested social set, and writes returned draft IDs/URLs back into each `post.json`.

Run a dry run before creating drafts:

```bash
scripts/typefully_drafts.py <content-run> --social-set-id 12345 --dry-run
```

For real API calls, pass the API key through `TYPEFULLY_API_KEY` or `--api-key-stdin`. Do not write the API key into `run.json`, `post.json`, queue files, or shell scripts.

## Automatic Writer-Reviewer-Editor Loop

Run this loop by default for new posts:

1. Writer: create the first draft from the source material and Alexey references.
2. Reviewer: critique the draft against the reviewer checklist.
3. Editor: rewrite the draft using the critique.
4. Final check: remove banned phrases, filler transitions, hype, unnecessary hashtags, and unsupported claims.

Do not require the user to manually ask for critique after drafting. Show the final revised version first unless the user asks to see the critique. When helpful, include a short "What I changed" note after the final post.

## Drafting Rules

- Prefer short paragraphs, direct openings, and practical engineering framing.
- Use concrete mechanisms and measurable outcomes when discussing AI, ML, agents, MLOps, or software systems.
- Keep links from the source material intact.
- Do not invent dates, enrollment details, prices, results, testimonials, or metrics.
- Use hashtags only if the user explicitly asks for them.
- Use no more than 3 emojis, and only when they help with event, list, or emphasis formatting.
- Avoid em dashes unless essential.
- Avoid filler intros and corporate polish. Start with the useful point.

## Reviewer Pass

Review every substantial draft using this checklist:

- Audience: Does it serve data scientists, ML engineers, data engineers, MLOps professionals, AI engineers, software engineers, or adjacent tech professionals?
- Value: Does it give practical insight, a useful breakdown, an evidence-backed opinion, or a clear announcement?
- Specificity: Are the claims concrete enough to be credible?
- Voice: Does it sound like Alexey: straightforward, expert, conversational, and practical?
- AI language: Does it use terms like evaluation, metrics, traces, failure modes, tool schemas, observability, reliability, reproducibility, latency, and cost where relevant?
- Risk: Are any claims unverifiable, overstated, or potentially misleading?
- Style rules: Does it avoid banned phrases, filler transitions, hype, unnecessary hashtags, and throat-clearing?
- CTA: Is the next step clear when a next step is needed?

Return critiques as concise bullets, then provide a revised version.

## Saving Post Files

When the user asks to store generated posts, save them in the user's current project or requested folder.

For one-off human editing, Markdown alone is acceptable. For multi-post, transcript, video, clip, scheduling, or automation workflows, use the structured artifact formats in `references/output-formats.md`.

Use Markdown for human editing:

```markdown
---
owner: alexey
platform: linkedin
status: draft
topic: short topic
created: YYYY-MM-DD
---

# Post

Draft text here.

# Notes

- Angle:
- CTA:
- Source material:
```

Use JSON when the user wants structured records for later tooling:

```json
{
  "owner": "alexey",
  "platform": "linkedin",
  "status": "draft",
  "topic": "",
  "created": "YYYY-MM-DD",
  "post": "",
  "notes": {
    "angle": "",
    "cta": "",
    "source_material": ""
  }
}
```

Prefer the richer `post.json` schema from `references/output-formats.md` when a post needs links to ideas, source transcript excerpts, clips, review results, or scheduling state.

## Transcript And Clip Handoff

When receiving briefs from `transcript-post-miner`, preserve the upstream `idea_id`, source timestamps, raw transcript excerpt path, and clip recommendation in the saved post record.

When a post needs a video clip:

- Keep every final clip shorter than 600 seconds.
- Store planned clip metadata in `post.json`.
- Put clip-cutting instructions in `clips/clip-manifest.json` so `video-clip-cutter` can create the media.
- After cutting clips, update `clip.path` in the related `post.json`.

Do not collapse the relationship into prose notes only. The post-to-idea-to-clip relationship must be available in structured fields.

## Reference Map

- `references/alexey-profile.md`: background, credentials, projects, courses, and links.
- `references/alexey-audience.md`: target audience and content expectations.
- `references/alexey-style.md`: voice, formatting, vocabulary, and banned patterns.
- `references/alexey-good-posts.md`: examples for style calibration.
- `references/output-formats.md`: artifact-mode folder layout, post records, review records, and queue export format.
