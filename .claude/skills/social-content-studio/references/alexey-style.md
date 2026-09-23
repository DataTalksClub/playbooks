# Alexey Style

## Voice

Use a straightforward, expert, practical voice.

The writing should feel conversational but not casual to the point of vagueness. It should sound like an experienced engineer explaining what matters, why it matters, and what to do next.

Prefer:

- Short paragraphs
- Clear bullets when they help scanning
- Direct claims
- Concrete mechanisms
- Practical examples
- Specific outcomes
- Engineering vocabulary

Avoid:

- Corporate tone
- Generic motivational language
- Overly formal phrasing
- Excessive superlatives
- Hype
- Anthropomorphic descriptions of AI systems

## AI and Engineering Vocabulary

When discussing AI agents and production AI systems, prefer concrete terms such as:

- evaluation
- metrics
- traces
- failure modes
- tool schemas
- observability
- reliability
- reproducibility
- latency
- cost
- retries
- rate limits
- guardrails
- monitoring
- structured outputs
- versioning
- regression tests

Avoid vague descriptions like:

- magic
- intelligent assistant that understands everything
- thinks like a human
- autonomous teammate
- unlocks potential

## Formatting Rules

- Use short paragraphs.
- Use bullets for concrete lists, course modules, outcomes, or step-by-step learning paths.
- Do not use listicle formatting unless the content naturally needs a list.
- Do not use hashtags unless specifically requested.
- Use at most 3 emojis per post, and only for events, lists, or emphasis as in source material.
- Avoid em dashes unless essential.
- Keep links visible and easy to find.
- Do not split URLs unless preserving a source post exactly.
- Start bullets with an uppercase letter.
- Use straight quotes and apostrophes.

## X, LinkedIn, And Substack Share One Post

Alexey has X Premium. By default, his LinkedIn, X, and Substack Notes copy is the same post: write `linkedin.md` only, and the Typefully handoff sends that text to all three platforms in one draft. Do not write a separate `x.md` or reshape the post into a thread unless the user asks for one.

## X / Twitter Threads

Use this section only when the user asks for an X thread for Alexey.

The thread should promote the event, not teach the full lesson.

Thread structure:

- Tweet 1: Start with one concrete production situation or practitioner problem. Make the reader understand the pain quickly. Include the event link when possible.
- Tweet 2: Continue directly from tweet 1. Add enough context to make the problem clear.
- Middle tweets: Show why the problem matters in practice. Use concrete examples, but do not turn the thread into a full tutorial.
- Final tweet: Name the event, speaker, date/time, platform, and registration link.

Each thread should have one clear idea. Do not combine multiple unrelated agent problems in one thread.

For event announcement threads:

- Show the problem.
- Name the gap or failure mode.
- Say that the workshop will cover the solution.
- Leave enough curiosity for the event.

Avoid over-teaching in event promo threads. Do not give away the whole implementation. Mention concrete details only when they make the problem clearer, such as workflow state, retries, approval state, traces, tool inputs, or tool outputs.

Avoid abstract hooks. Do not start from general categories like "durable execution matters" or "agents need observability". Start from a concrete scenario:

- An agent investigates a failed payment and the worker restarts.
- A tool call creates a support ticket, times out, and may be retried.
- A refund needs human approval, but the approval arrives hours later.
- An agent gives a wrong answer after using several tools.

Avoid the contrast formula "it's not this, it's that" and similar patterns:

- "The hard part is not X. It is Y."
- "It is not about X. It is about Y."
- "Not only X, but also Y."

Use direct phrasing instead:

- "A production agent has to survive deploys, timeouts, restarts, and late approvals."
- "A retry can create a duplicate ticket when the first request already succeeded."
- "The workflow needs to remember which approval is pending."

## Patterns From Published Edits

These come from comparing drafts with the versions Valeriia published (2026-09-23, Switch workshop run). Write this way from the start.

**Open with the lesson, not the event.** Move the takeaway to the first line and use the event as the evidence that follows.

- Draft: "Louis Amaudruz built a multi-agent workflow live at our DataTalks.Club workshop. A few things broke along the way."
- Published: "When a multi-agent workflow stalls, check permissions and handoffs between agents before blaming the model." then "Here are several examples from our latest workshop with Louis:"

**Refer to the event as ours, loosely.** "our latest workshop", "one of our latest workshops", "our DataTalksClub workshop" (Alexey writes DataTalksClub without the dot), rather than "the Switch workshop" or the full event title.

**"We" is fine for workshop work.** "In one of our latest workshops, we built agents that work on GitHub issues" is Alexey's own framing as host. Keep individual claims and opinions attributed to whoever made them, but do not rewrite the collective "we" of an event into "Louis built".

**Introduce the guest inline instead of narrating the question.** "Here's an answer from Louis, our guest at the workshop: ..." rather than "I asked Louis Amaudruz about this during the Switch workshop."

**Drop quote scaffolding.** State the line plainly instead of "His summary:" plus quotation marks. Cut sentences that only re-attribute a point already credited.

**Give a numbered item its own line.** The number and a short label on one line, a blank line, then the explanation as its own paragraph. Do not pack the label and the explanation into one line.

**Break long paragraphs.** A sentence that adds a distinct beat gets its own paragraph, for example "He said no." after the question it answers.

**Bullets have no trailing periods.**

**Tighten wording.** "If it all lands in Slack" over "If all of it lands in Slack"; "check the zip archive" over "go check the zip archive"; drop "with him", "exactly", and similar filler.

## Banned Phrases

Do not use:

- game-changer
- the best part
- at the end of the day
- unlock potential
- at its core
- the idea is simple
- in today's landscape
- seamless
- robust
- transformative
- delve
- leverage
- In addition
- Furthermore
- In conclusion
- That said

## Avoid Throat-Clearing

Do not start with:

- I've been thinking about...
- Here's the thing...
- In today's world...
- Many people ask me...
- As you may know...

Start with the concrete point instead.
