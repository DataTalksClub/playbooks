---
post_id: post_002
platform: linkedin
status: draft
---

Prompting over raw agent logs is useful for one-off exploration.

It gets expensive when you repeat it.

In the workshop, Alena showed a simple example:

Ask a coding agent to read all local traces and answer:

"How many tokens did I use last month?"

The agent can do it. It reads the files, aggregates the data, and gives you an answer.

Then you change the question:

"What about the last six months?"

Now the agent may need to read and aggregate the same logs again. Some cache may help, but the workflow still spends time and tokens on work that should become reusable.

This is where a data pipeline changes the workflow.

Instead of repeatedly asking an agent to scan raw logs:

- Ingest the traces once
- Normalize the structure
- Store them in a queryable destination
- Refresh the data on a schedule
- Build a dashboard on top

Now token usage, model usage, project activity, and cost patterns become normal analytics questions.

For personal use, this helps you understand your own consumption.

For teams, it becomes a way to see how coding agents are actually used across projects.

Recording:
https://youtube.com/live/A0LmmZf-ggM
