---
post_id: post_002
platform: linkedin
status: draft
---

Setting up tool calling for your agent is a big step.

But it does not mean the agent is ready for production.

It means the agent can call a function with a schema.

Once you put it in a real workflow, you need to answer smaller questions:

- Where is the state stored?
- Do you save the tool input and output for each step?
- What happens if the tool call times out?
- Can you retry without creating a duplicate ticket, payment, message, or database write?
- Can the workflow wait for approval and continue tomorrow?
- Can you resume after a deploy?

This is what we will cover in the DataTalksClub workshop "Running Durable Agents in Production" with Nicholas Lotz.

We will focus on the pieces around the agent loop that are easy to miss at first:

- Server-side state instead of process-local memory
- Per-step execution history
- Retry policies, timeouts, and idempotency for tool calls
- Timeouts and recovery paths
- Human approval steps that can wait without keeping a worker alive
- Traces for debugging prompts, model calls, tool calls, timing, token usage, and failures

The useful outcome is practical: you can explain what ran, what failed, what was retried, and where the workflow should continue.

Tuesday, June 16
4:30 PM - 6:00 PM GMT+2
YouTube

Register here: [registration link]
