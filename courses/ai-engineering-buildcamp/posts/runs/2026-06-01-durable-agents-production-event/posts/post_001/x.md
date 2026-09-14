---
post_id: post_001
platform: x
status: draft
---

1/5

An agent investigates a failed payment.

It checks logs, calls Stripe, drafts a reply, then waits for approval.

Then the worker restarts.

Where should the agent continue from?

Workshop: [registration link]

2/5

This is where many agent demos become fragile.

The useful work already happened, yet the workflow still needs to remember:

- Which step was next
- Which tools ran
- Which approval was pending

3/5

The problem is ordinary production behavior:

Deploys happen.
Workers restart.
Tools time out.
People approve things later.

The agent workflow has to survive that.

4/5

Nicholas Lotz will cover this in Running Durable Agents in Production:

- Durable workflow state
- Recovery after failure
- Tool call retries
- Human approvals
- Execution traces

5/5

Running Durable Agents in Production
with Nicholas Lotz

Jun 16, 4:30-6:00 PM GMT+2
YouTube

Register: [registration link]
