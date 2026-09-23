---
name: social-content-studio
description: Create, critique, revise, and save structured social media post artifacts for Alexey. Use when drafting LinkedIn/X posts in Alexey's voice, adapting source material into Alexey-style posts, reviewing copy for Alexey's audience, preparing Alexey course/community announcements, turning transcript or video ideas into post files, or producing machine-readable records for later scheduling, clipping, API publishing, or file-based editing. Do not use for posts published by DataTalks.Club as an organization.
---

# Social Content Studio

This skill is for Alexey's accounts. DataTalks.Club may be the subject of his post, but that does not make it a DataTalks.Club account post. Use the `datatalks-event-promotion` skill for copy published in DataTalks.Club's organizational voice.

## Core Workflow

1. Identify the content owner, platform, goal, source material, and whether the user wants a draft, a critique, a revision, variants, or saved post files.
2. For Alexey content, read `references/alexey-profile.md`, `references/alexey-audience.md`, and `references/alexey-style.md`.
3. If examples are needed for calibration, read `references/alexey-good-posts.md`.
4. Draft in Alexey's voice using the user's source material. Preserve factual claims and links exactly unless the user asks for rewriting or verification.
5. Run an internal reviewer pass before finalizing. Check audience fit, specificity, evidence, structure, hook, and style rules. In artifact mode, the independent review in `references/review-stage.md` follows.
6. Revise the strongest version using the reviewer pass. If useful, provide 2-3 variants with clearly different angles.
7. If the user asks to save drafts, create post files in the user's current project or requested folder, never inside the skill directory.
8. For multi-post, transcript, video, clip, scheduling, or automation workflows, use artifact mode by default and read `references/output-formats.md`.
9. For saved Alexey post artifacts, generate LinkedIn carousel and X/Twitter resource media by default with the `alexey-carousel-generator` skill after the post files are saved, unless the user explicitly asks for text-only posts. They become the post's `visual` Typefully draft, next to the `clip` draft.

## Artifact Mode

Use artifact mode when the user asks for saved files, reusable outputs, a pipeline, a batch of posts, scheduling/API handoff, or posts connected to transcript/video clips. Keep chat output brief; files are the source of truth, and downstream tools never parse chat output.

One content run holds everything made from one source (a recording, an event, a launch), for every owner. Each post records its `owner`, and `references/profiles.json` holds the machine-readable rules per owner: which draft file feeds which platform, X limits, media variants, banned phrases, and the Typefully social set. The prose voice rules stay in each owner's style reference. Which owner gets which post for a recording is set in the `datatalks-event-promotion` skill, `references/stage-2-post-event.md`.

### Pipeline

1. **Run.** `scripts/create_content_run.py` creates `content-runs/<YYYY-MM-DD-slug>/`. Put the source facts in `source/source.json`, including `links` (every URL each post must carry, such as the recording and repo) and transcript caveats.
2. **Ideas.** For recordings, the `transcript-post-miner` skill writes the shortlist and `briefs/<idea_id>.md` with raw excerpts. The user approves ideas, owners, and media per idea before writing.
3. **Scaffold.** `scripts/scaffold_post.py <run> --owner <profile> --idea ... --topic ... --moment ... --clip ...` creates `posts/<prefix>_NNN/` with `post.json`, empty copy files for that profile, a `review.json` stub, and the clip entry in `clips/clip-manifest.json`. Do not hand-write post records.
4. **Write.** Fill the copy files. Alexey: `linkedin.md` only; it is the copy for LinkedIn, X, and Substack. DataTalks.Club: `linkedin.md` plus an `x.md` thread, written with the `datatalks-event-promotion` skill.
5. **Media.** Cut clips with the `video-clip-cutter` skill from `clips/clip-manifest.json`. For Alexey posts with a visual draft, render the carousel and image with the `alexey-carousel-generator` skill. Paths are listed in `post.json.media` (`clip`, `carousel`, `image`).
6. **Check.** `scripts/check_posts.py <run>` checks the post records, copy files, thread markers, X limits (URLs count as 23), banned phrases, required links, transcript timestamps, media files, and open reviewer findings. It writes results to `review.json.lint` and exits 1 on any error. Fix and rerun until it passes.
7. **Review.** Run the review in a separate agent (the `post-reviewer` subagent), following `references/review-stage.md`. It writes claim-by-claim findings to `review.json.reviewer`. Fix every `error` finding, mark it `fixed`, and rerun the check.
8. **Approve.** Hand the posts to the user. The user sets `status: approved` in `post.json` for posts that are ready.
9. **Upload.** With the user's permission for that upload, run `scripts/typefully_drafts.py <run>`; see Typefully Handoff below.
10. **Learn from edits.** After the posts are published, run `scripts/pull_typefully_edits.py <run>`. It saves the Typefully version of each post and writes `edits.md` with a diff per platform. When edits show a pattern, update the owning style reference so the next run starts closer to the final version.

Scripts:

- `scripts/create_content_run.py`: create a run folder and `run.json`.
- `scripts/scaffold_post.py`: create a post folder from the owner's profile.
- `scripts/check_posts.py`: mechanical checks before review and upload.
- `scripts/typefully_drafts.py`: create Typefully drafts.
- `scripts/pull_typefully_edits.py`: pull published text back and diff it (read-only).

## Typefully Handoff

`scripts/typefully_drafts.py` creates Typefully drafts for approved posts (`POST /v2/social-sets/{social_set_id}/drafts`) and records each draft in `post.json.typefully_drafts`. Typefully manages platforms inside one draft, so never create one draft per platform.

- **Drafts per post.** One draft per media variant in the owner's profile:
  - Alexey: a `clip` draft (clip on LinkedIn, X, and Substack) and a `visual` draft (carousel PDF on LinkedIn, resource image on X). Both use the same `linkedin.md` copy.
  - DataTalks.Club: one `clip` draft with `linkedin.md` on LinkedIn and the `x.md` thread on X.
  - A variant is created only when every media file it needs exists; a post with no media gets one text-only draft.
- **Accounts.** The social set comes from the post's owner in `references/profiles.json`. The script refuses owners without a `typefully_social_set_id` and stops if `--social-set-id` disagrees. `--list-social-sets` lists IDs (read-only).
- **Threads.** A dedicated `x.md` is split on its `N/M` lines, one Typefully post per tweet. Copy reused from `linkedin.md` stays one post.
- **Gate.** Only `status: approved` posts are uploaded unless `--status` says otherwise, and the script runs `check_posts.py` first and stops on errors (`--skip-checks` overrides).
- **Media.** Files upload in parallel and the script waits until Typefully has processed each one (`--media-timeout`, default 900s). Each draft is then created once with its media and never patched, so editing a draft in Typefully cannot conflict with an upload.
- **Failures and reruns.** A draft whose media fails is not created, and the run exits 1 while the other drafts are still created. Media IDs are saved under `post.json.typefully_media_uploads`, and variants that already have a draft are skipped, so rerunning the same command creates only what is missing. `--post`, `--variant`, and `--platform` narrow a run; `--force` re-creates.

Always dry-run first:

```bash
python3 .claude/skills/social-content-studio/scripts/typefully_drafts.py <content-run> --dry-run
```

For real API calls, pass the API key through `TYPEFULLY_API_KEY` or `--api-key-stdin`. Do not write the API key into `run.json`, `post.json`, queue files, or shell scripts.

## Writer-Reviewer-Editor Loop

Run this loop by default for new posts, without being asked: draft from the source material, critique it against `references/alexey-style.md` and the checks below, then rewrite. Show the final version first; add a short "What I changed" note when useful.

Critique each draft for: audience fit, practical value, specific and supported claims, Alexey's voice, concrete AI/engineering vocabulary, overstated or unverifiable claims, style rules, and a clear next step. In artifact mode the mechanical half of this is `scripts/check_posts.py` and the independent half is `references/review-stage.md`, so do not repeat them by hand.

## Drafting Rules

- Prefer short paragraphs, direct openings, and practical engineering framing.
- Use concrete mechanisms and measurable outcomes when discussing AI, ML, agents, MLOps, or software systems.
- Keep links from the source material intact.
- Do not invent dates, enrollment details, prices, results, testimonials, or metrics.
- Use hashtags only if the user explicitly asks for them.
- Use no more than 3 emojis, and only when they help with event, list, or emphasis formatting.
- Avoid em dashes unless essential.
- Avoid filler intros and corporate polish. Start with the useful point.

## Saving Post Files

Save drafts in the user's current project or requested folder, never inside the skill directory. A single ad-hoc draft can be one Markdown file with `owner`, `platform`, `status`, `topic`, and `created` in the frontmatter. Anything with several posts, transcripts, clips, or an upload uses the content-run formats in `references/output-formats.md`.

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
- `references/profiles.json`: per-owner rules read by the scripts (copy per platform, X limits, media variants, banned phrases, Typefully social set).
- `references/review-stage.md`: the independent review procedure and `review.json.reviewer` format.
