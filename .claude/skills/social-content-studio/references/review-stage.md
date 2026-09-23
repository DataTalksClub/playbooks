# Review Stage

The review runs after the copy is written and `scripts/check_posts.py` passes, and before the user approves anything. It checks what a script cannot: whether every claim is true to the source, whether it is attributed to the right person, and whether the post follows its profile's voice.

Run it in a separate agent from the writer (the `post-reviewer` subagent in Claude Code, or a fresh session in Codex). The reviewer sees only the finished post and its sources, never the writer's reasoning, so it cannot inherit the writer's assumptions.

## Inputs

Review a whole run in one pass, and read only what a check needs. Reading every transcript in full is the most expensive thing this stage can do.

- Read once per run: `source/source.json` (names, roles, links, transcript caveats), and the style reference of each owner present in the run.
- Read per post: `post.json`, the copy files, and the briefs in `../../briefs/` named by `source_moments[].excerpt_path`. The briefs already hold the raw excerpts, so they answer most questions.
- Only when a brief does not settle a claim, pull the surrounding lines from `source/transcript-context.md` with `grep -n` plus `sed -n` on the timestamp. Do not read `full_transcript.json` or a whole context file into the conversation.

## What to check

1. **Claims.** Go through the factual claims in the copy: what was built, what was said, numbers, product capabilities, results. Find the line that supports each one. Mark it `supported`, `unsupported` (no line says it), `overstated` (the line says less, for example "in some cases" became "often"), or `unclear`.
2. **Attribution.** The transcript has no speaker labels. For every claim tied to a person, decide who said it from context (who was presenting, who asked the question, who answers). A first-person statement in Alexey's post must be something Alexey said in the recording; if the speaker is unclear, it is an error, not a guess.
3. **Status of what was shown.** Something that was asked for, planned, or failed on screen must not be described as working. Future features must read as future.
4. **Voice.** Alexey's posts: first person only for his own experience, no invented opinions or motives. "We" about a DataTalks.Club event he hosted is his normal framing, so do not flag it; check individual claims and opinions instead. DataTalks.Club posts: organizational voice, no first-person singular, "we" only as the host.
5. **CTA.** The recording link is given a reason tied to the post's idea, and the repo or other required links are present.
6. **Transcript caveats.** Names and terms in `source.json` caveats (misheard names, unverified spellings) must not leak into the copy.

## Output

Write the result into the post's `review.json` under `reviewer`, keeping `lint` untouched. Do not edit the copy files; the writer applies fixes.

Keep the record short: list a claim only when its verdict is not `supported`, plus the few claims the post rests on. Never write a line-by-line table of every sentence.

```json
{
  "reviewer": {
    "reviewed": "YYYY-MM-DD",
    "claims": [
      {
        "claim": "The reviewer is a Codex agent",
        "source": "00:30:35-00:30:53",
        "speaker": "Louis",
        "verdict": "supported"
      }
    ],
    "findings": [
      {
        "severity": "error",
        "issue": "Says the 60-second polling picked up new issues; at 00:57:57 it did not.",
        "suggestion": "Say Louis asked the manager to poll every 60 seconds.",
        "status": "open"
      }
    ],
    "summary": "One sentence."
  }
}
```

- `severity`: `error` for anything false, misattributed, or against the voice rules; `warn` for weaker wording or style. Do not raise style nits that `check_posts.py` already covers (length, banned phrases, links).
- `status`: the reviewer writes `open`. The writer sets `fixed` after changing the copy, or `wont_fix` with a reason in `suggestion` when the user decides to keep it.
- `check_posts.py` fails a post while any `error` finding is `open`.

## After review

1. The writer fixes the copy for each `open` finding and marks it `fixed`.
2. Run `scripts/check_posts.py` again.
3. Hand the posts to the user. The user sets `status: approved` in `post.json` for the posts that are ready; only approved posts are uploaded.
