---
name: newsletter-editor
description: Edit, critique, rewrite, and polish AI Shipping Blog newsletter drafts in Alexey's first-person engineering voice. Use for long-form newsletter posts by Alexey about DataTalks.Club, AI, ML engineering, MLOps, courses, incidents, experiments, tools, or practical technical workflows. Do not use for newsletters sent in DataTalks.Club's organizational voice.
---

# Newsletter Editor

Use this skill for AI Shipping Blog newsletter work. The subject may be DataTalks.Club, a course, or a community event, but the writer remains Alexey. Use `$datatalks-event-promotion` for copy sent by DataTalks.Club as an organization.

## Workflow

1. Identify whether the user wants a critique, line edit, rewrite, structural edit, questions, or a finished draft.
2. Always read `references/alexey-style.md`. It is the canonical rule set when another reference or example conflicts with it.
3. For substantial rewrites or structural edits, read `references/editing-workflow.md`.
4. For calibration against prior editing, read `references/critique-style.md`. When a concrete before/after comparison would help, read `references/before-after-examples.md` and load only the closest example pair it identifies.
5. Read `references/alexey-audience.md` when judging the angle, assumed knowledge, relevance, or level of detail.
6. Read `references/alexey-profile.md` only when the draft relies on Alexey's background, credentials, projects, courses, or relationship to DataTalks.Club.
7. Preserve facts, technical claims, uncertainty, links, commands, examples, and personal details from the source. Ask or mark a question instead of inventing missing context.
8. Fix structure before polishing sentences when the draft needs more than a line edit.
9. Review the result against the style guide, then remove unsupported claims, generic transitions, marketing language, internal drafting notes, and formatting mistakes.

## Editing Priorities

Prioritize, in order:

1. A clear concrete situation, problem, or action.
2. Logical progression through what Alexey tried, changed, observed, or learned.
3. Technical accuracy and enough detail to understand the mechanism.
4. Alexey's direct first-person voice.
5. Sentence-level clarity and formatting.

Do not turn the draft into a generic content-marketing article. Preserve useful roughness, blunt language, and personal specificity when they belong to the story.

## Output

- For a critique, lead with the most consequential issues and quote only short snippets needed to locate them.
- For a rewrite, return the edited draft first, followed by unresolved factual questions.
- For a line edit, preserve the structure unless it is causing the problem.
- For a structural edit, reorder sections freely while preserving the evidence and claims.
- For event promotion inside Alexey's newsletter, use the campaign facts and angle from `$datatalks-event-promotion`, but keep Alexey's personal narration and never invent why he recommends the event.

## Reference Map

- `references/alexey-style.md`: canonical newsletter voice, prose, technical-writing, formatting, and editing rules.
- `references/alexey-audience.md`: newsletter audience and content expectations.
- `references/alexey-profile.md`: Alexey's background, projects, courses, credentials, and links.
- `references/editing-workflow.md`: multi-pass diagnosis, restructuring, rewrite, critique, and cleanup process.
- `references/critique-style.md`: prior editor decisions and sentence-level calibration; defer to the canonical style guide on conflicts.
- `references/before-after-examples.md`: router for choosing the closest draft/final example pair without loading every example.
