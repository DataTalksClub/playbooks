# Multi-Pass Editing Workflow

Use this workflow for newsletter drafts unless the user asks for a narrow line edit.

Do the passes internally. Do not expose every pass unless the user asks to see the process. For normal edit requests, return the edited draft plus short notes for unresolved questions.

If the draft is under-specified, structurally messy, or the best final shape is not obvious, pause after Pass 1 and propose the likely final structure with focused questions before rewriting. This is especially useful for long drafts, system-evolution posts, multi-project posts, incident writeups, or drafts produced from voice notes.

## Pass 1: Diagnose the Article

Before rewriting, identify:

- The real story type: build log, system evolution, incident, multi-project survey, course/community update, workflow story, or technical explainer.
- The core constraint: what made the work necessary now?
- The sequence: what existed before, what broke or became insufficient, what Alexey tried, what changed, and what the result was.
- The reader promise: what the reader will understand by the end.
- Missing facts: numbers, failure details, before/after signals, links, screenshots, commands, or who did what.

If the draft starts with a thesis or a description of the article, replace it with context or action. The final versions usually open with the situation, not with "In this article I want to share..."

## Optional Checkpoint: Structure and Questions

Use this checkpoint when the draft would benefit from user input before a full rewrite.

Return:

1. The likely final article shape.
2. The main structural edits you would make.
3. The 3-7 questions that would most improve the final version.

Good questions ask for concrete material, not opinions:

- What changed that made the old approach stop working?
- What was the first version and what exactly was wrong with it?
- What did you change in the next version?
- What signal showed that the new version worked?
- Which example is the strongest one to keep?
- Is this a one-off experiment or something you now use regularly?
- Who else was involved and should be credited?

Avoid asking questions that can be solved by editing. Ask only for missing facts, missing constraints, or choices that affect the article's structure.

## Pass 2: Restructure

Edit the architecture before editing sentences.

Common structural moves from the examples:

- Add a concrete opening and a short preview list for long articles.
- Group related tool sections under one larger workflow section.
- Split long systems into stages when the story is about evolution over time.
- For multi-project posts, establish the shared method first, then show numbered cases.
- Move background before tool details when the reader needs to understand why the tool exists.
- Move broad conceptual discussion after the concrete example, not before it.
- Cut source lists, placeholder notes, and internal comments from final prose.
- Keep captions close to the image they explain, but do not let captions carry the main argument.

Ask of every section:

- What problem appears here?
- What did Alexey do?
- What changed because of it?
- What concrete signal shows it worked or failed?

If a section cannot answer these, merge it, cut it, or turn it into a short aside.

## Pass 3: Rewrite for Alexey's Voice

Rewrite after the structure is stable.

Use:

- First person for Alexey's actions.
- Plain statements with concrete verbs.
- Practical trade-offs: "good enough", "I paused it", "I do not have time", "it works the way I need it to".
- Personal specifics when they explain the constraint.
- Numbers and concrete signals when they are available.

Avoid:

- Article meta: "This article covers", "In this section", "The result is".
- Corporate abstractions: "seamless", "friction" when "painful" or "too slow" is more Alexey.
- Explaining the obvious after the concrete sentence already shows it.
- Turning every idea into a heading.
- Leaving repeated source footnotes from generated drafts.

Sentence-level moves:

- Fuse adjacent short sentences when they are one thought.
- Split overloaded sentences when they hide the action.
- Lead with "When" or "If" when the condition frames the action.
- Put the useful or softer clause at the end when a sentence pivots.
- Replace formal colon lists with natural phrasing when the list is not important.
- Keep bullets when the content is genuinely a sequence, recipe, role list, or checklist.

## Pass 4: Critique the Edited Draft

After rewriting, critique your own edit before returning it.

Look for:

- A missing or weak opening constraint.
- A section that explains a tool without saying why Alexey needed it.
- A section that has a result but no signal.
- A transition that summarizes what the reader just read.
- A list that should be prose, or prose that should be a list.
- Too many examples in one section.
- Technical detail that proves knowledge but does not move the story.
- A broad conclusion instead of a concrete landing.
- Removed personal details that should have stayed.
- Added claims that were not in the source.

If you find a major issue, revise again. If the issue needs Alexey's input, mark it as a question.

## Pass 5: Final Cleanup

Before returning:

- Remove frontmatter unless the user asks to keep it.
- Remove source sections, draft notes, and placeholder comments unless needed for the publishing workflow.
- Check heading levels and title.
- Check that bullets start uppercase.
- Check body bold and dash rules from `alexey-style.md`.
- Check links and code blocks for obvious breakage.
- Check names: DataTalks.Club, Valeriia, Alexey, course names, tools, repos.
- Keep unresolved questions short and actionable.

## Output Formats

For an edit:

1. Edited draft.
2. `Open questions` only if needed.
3. Very short note about the main structural change if useful.

For a critique:

1. Biggest structural issues.
2. Voice issues.
3. Missing facts/questions.
4. Suggested edit plan.

For a staged workflow request:

1. First provide diagnosis and edit plan.
2. Then produce the rewrite.
3. Then critique the rewrite.
4. Then provide a final cleaned version.
