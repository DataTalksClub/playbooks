---
post_id: post_005
platform: linkedin
status: draft
---

Next DataTalksClub workshop:

Running Durable Agents in Production

With Nicholas Lotz
Tuesday, June 16
4:30 PM - 6:00 PM GMT+2
YouTube

If you already built a basic agent loop, you probably saw the next set of questions quickly.

Where do you store state?

How do you recover after a failed tool call?

How do you wait for human approval?

How do you debug the exact step that failed?

This workshop is about the code and infrastructure around the loop.

We will cover:

- Why in-process agent loops fail in production
- How to persist workflow state outside the agent process
- How to resume after process death, deploys, and failures
- How to retry tool calls without losing execution history or duplicating side effects
- How to add human approval steps that write pending state and resume later
- How to inspect traces for LLM calls, tool calls, timing, token usage, errors, and retry attempts
- How durable execution fits with RAG, evaluation, monitoring, and production AI systems

By the end, you should have a clearer mental model for the execution layer you need around the agent loop.

Register here: [registration link]
