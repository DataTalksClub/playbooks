---
post_id: post_004
platform: linkedin
status: draft
---

When your agent fails, "the model did something weird" does not help much.

You need to answer specific questions:

- Which step was running?
- Which tool was called?
- What arguments did we send to the tool?
- What did the tool return?
- Was this a timeout, a bad input, a rate limit, or an LLM decision?
- How long did each step take?
- How much did it cost?
- Can we retry safely?
- Can we resume from the failed step?

Without traces and per-step history, you are mostly reading logs and guessing.

For an agent workflow, I would want to see the run ID, step ID, prompt version, model response, tool name, tool arguments, tool response, latency, token usage, error, and retry count.

On June 16, Nicholas Lotz will run a DataTalksClub workshop on Running Durable Agents in Production.

We will talk about the execution layer around the agent loop: state, retries, recovery, human approvals, observability, and deployment.

If you are working on agents for RAG, automation, data workflows, customer operations, or internal tools, these traces are what help you debug the system when the answer is wrong or the workflow stops halfway.

Tuesday, June 16
4:30 PM - 6:00 PM GMT+2
YouTube

Register here: [registration link]
