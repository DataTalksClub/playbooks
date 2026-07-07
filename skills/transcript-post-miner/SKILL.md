---
name: transcript-post-miner
description: Mine long video transcripts for high-quality LinkedIn/X post ideas and short clip recommendations before writing social posts. Use when Codex is given a YouTube URL or video ID, full transcript, YouTube transcript JSON, workshop recording transcript, chaptered video transcript, or asks to fetch a YouTube transcript and find topics, angles, post briefs, clips, highlights, or social content opportunities from a long video. Especially useful when chapter-by-chapter post generation is too narrow and ideas may span multiple transcript sections.
---

# Transcript Post Miner

## Overview

Use this skill to turn a long transcript into a reviewable set of social post opportunities. The goal is not to summarize chapters. The goal is to identify the strongest standalone ideas across the whole recording, anchor each idea in transcript evidence, and recommend whether a short video clip should accompany the post.

This skill usually runs before `social-content-studio`: first mine and validate ideas, then hand approved briefs to the social writing skill.

## Workflow

1. Identify the input format:
   - YouTube URL or 11-character video ID
   - `full_transcript.json` with `text` and `segments` fields from `short-video-automation`
   - a raw timestamped transcript
   - chapter files plus a full transcript
2. If the input is a YouTube URL or video ID, fetch the transcript first using the workflow in `references/youtube-transcript-fetching.md`.
3. If a transcript path is provided or created, inspect its size and shape. For `full_transcript.json`, prefer using `scripts/prepare_transcript_context.py` to create timestamped windows for review.
4. Read the transcript globally before deciding on post ideas. Do not treat chapters as fixed boundaries.
5. Mine 8-15 candidate ideas by looking for teachable claims, frameworks, mistakes, trade-offs, demos, strong explanations, practical processes, and surprising distinctions.
6. Anchor every idea to transcript moments. Reject ideas that cannot be supported by specific timestamps.
7. Assess whether each idea needs a clip:
   - recommend a clip only when a short excerpt works as a standalone hook or proof point
   - recommend text-only when the idea is distributed across the transcript or needs synthesis
8. Present a shortlist for user approval before writing posts unless the user explicitly asks to write immediately.
9. For approved ideas, create explicit handoff briefs before writing. Each brief must include the topic, timestamps, raw transcript excerpts, post angle, clip recommendation, and writing brief.
10. Pass the handoff briefs, including the raw transcript excerpts, to `social-content-studio` for LinkedIn and X drafts.

## Resource Guide

Read references only as needed:

- `references/idea-selection-rubric.md`: how to score and filter post opportunities.
- `references/clip-selection-rubric.md`: how to choose clip ranges and when to avoid clips.
- `references/output-formats.md`: Markdown and JSON schemas for idea lists, writing briefs, and clip manifests.
- `references/youtube-transcript-fetching.md`: how to fetch `full_transcript.json` from a YouTube URL or video ID using the local `short-video-automation` script.

Use scripts when helpful:

- `scripts/prepare_transcript_context.py`: convert `full_transcript.json` into timestamped Markdown windows.
- `scripts/extract_transcript_excerpts.py`: extract raw transcript excerpts for approved ideas and timestamp ranges.
- `scripts/create_clip_manifest.py`: convert approved idea JSON into a CSV for clip production.

## Idea Mining Rules

- Prefer ideas that are useful without watching the full video.
- Prefer ideas that connect multiple transcript moments into a stronger argument.
- Preserve the speaker's actual claims. Do not invent examples, metrics, tools, or conclusions.
- Separate the post angle from the clip recommendation. A good post does not always need a clip.
- Use chapters as navigational hints only. An idea may span chapters, skip chapters, or come from a small moment inside a chapter.
- Favor practical engineering substance over generic motivation.
- Include both LinkedIn and X fit when relevant.
- Keep the output reviewable. It should help the user decide what to write, not bury them in exhaustive transcript notes.

## Output Expectations

Default to a Markdown shortlist with:

- idea title
- platform fit
- post angle
- why it is worth posting
- source moments with timestamps
- clip recommendation
- writing brief
- priority score

When the user wants automation, also create `post-ideas.json` using the schema in `references/output-formats.md`.

## Handoff To Social Writing

After the user approves ideas, invoke or recommend `social-content-studio` with each approved handoff brief. The handoff must include raw transcript excerpts for the relevant timestamp ranges, not only summaries or timestamp labels. The writer should create final LinkedIn and/or X copy from the approved angle and the provided excerpts, not from the whole transcript again unless more context is needed.
