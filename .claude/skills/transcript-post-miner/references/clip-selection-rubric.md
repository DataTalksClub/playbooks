# Clip Selection Rubric

Use clips as support for social posts, not as an automatic output for every idea.

## Recommend A Clip When

- A 30-120 second segment contains a clean standalone explanation.
- The speaker makes a clear claim, gives a memorable example, or walks through a concrete decision.
- The clip has a natural start and end.
- The clip does not require extensive setup from earlier in the video.
- The clip can act as a hook while the post adds structure and takeaway.

## Prefer Text-Only When

- The idea is synthesized from several transcript moments.
- The strongest content is a list, framework, or comparison spread over time.
- The clip depends heavily on slides, code, UI navigation, or missing visual context.
- The clip would need too much trimming to become coherent.
- The transcript has useful ideas but no quotable or self-contained spoken segment.

## Clip Range Guidelines

- Default target: 45-90 seconds.
- Acceptable range: 30-120 seconds.
- Start at the first sentence that introduces the useful idea.
- End after the takeaway, example, or decision point.
- Avoid starting with "so", "basically", repeated context, or mid-sentence fragments when possible.
- Avoid ending before the speaker completes the thought.

## Clip Output

For every recommended clip, provide:

- `clip_start`
- `clip_end`
- `clip_title`
- `clip_reason`
- `clip_quality`: high, medium, or low
- `trim_notes`: start/end guidance for manual editing

If no clip is recommended, explain why in one sentence.
