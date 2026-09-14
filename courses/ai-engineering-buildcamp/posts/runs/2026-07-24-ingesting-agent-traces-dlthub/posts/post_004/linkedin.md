---
post_id: post_004
platform: linkedin
status: draft
---

A useful mental model for coding agents:

Skills describe what to do.

Tools do the repeated work.

In the workshop, Alena and I discussed this while building dlt pipelines with an agent.

A skill can be a markdown file that tells the agent:

- When to use a file-system pipeline
- When to use a REST API pipeline
- How to debug a pipeline
- How to inspect the data
- Which validation steps matter

A tool is executable code or a deterministic function:

- Read a file
- Count rows
- Read a table
- Run the pipeline
- Inspect schema
- Query the destination

This distinction matters when building AI engineering workflows.

If the agent has only natural language instructions, it may rebuild the same logic again and again.

If the agent has reusable tools, the model can focus on planning, choosing the right workflow, and interpreting results.

In this workshop, the dlt workbench used this pattern:

Skills routed the agent to the right workflow.

Tools handled the repeated data operations.

That is a much better foundation than asking a model to invent a new ingestion pipeline from scratch each time.

Recording:
https://youtube.com/live/A0LmmZf-ggM
