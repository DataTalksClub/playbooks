---
post_id: post_001
platform: linkedin
status: draft
---

A pattern I see with agent demos:

You build something that works in a notebook or a small app.

It plans the next step, calls a tool, gets a result, and continues.

Then you try to run it as a workflow.

Normal things start to matter:

- The process restarts
- You deploy a new version while the task is still running
- A tool call fails on step 6
- Someone needs to approve the next action and replies later
- You need to see the exact input and output for the failed step

If all state is in memory, there is not much to inspect or resume.

You need a place to store the run ID, current step, tool inputs, tool outputs, errors, retries, and approval state.

This is the part many demos skip because nothing fails during the demo.

On Tuesday, June 16, Nicholas Lotz will run a DataTalksClub workshop on Running Durable Agents in Production.

We will look at how to structure agents as durable workflows:

- Persisting state outside the agent process
- Resuming after failures
- Retrying tool calls safely
- Waiting for human approval without losing context
- Inspecting execution traces
- Deploying multi-agent apps to real infrastructure

Useful if you are building agents for RAG, workflow automation, customer operations, data tasks, or internal tools and want to understand what has to live outside the agent loop.

Tuesday, June 16
4:30 PM - 6:00 PM GMT+2
YouTube

Register here: [registration link]
