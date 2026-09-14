---
post_id: post_003
platform: linkedin
status: draft
---

Adding a human approval step to an agent looks small in code.

Usually it looks like this:

1. The agent prepares an action.
2. A person reviews it.
3. The agent continues.

But now you have a workflow that may need to wait.

What happens if approval takes two hours or two days?

What happens if the worker process restarts?

What happens if the deployment finishes while the workflow is waiting?

What happens if the approver rejects the step and the agent needs to compensate or choose a different path?

At that point, approval is not just a button in the UI.

It is part of the execution model.

The workflow needs to write something like "pending approval" to storage, keep the workflow ID, store the proposed action, and resume from that step when the approval event arrives.

It should not depend on one live Python process still being there when the person replies.

On June 16, Nicholas Lotz will join DataTalksClub for a workshop on Running Durable Agents in Production.

We will cover human-in-the-loop workflows, retries, timeouts, traces, failure recovery, and deployment patterns for agents that need to run outside a demo.

Tuesday, June 16
4:30 PM - 6:00 PM GMT+2
YouTube

Register here: [registration link]
