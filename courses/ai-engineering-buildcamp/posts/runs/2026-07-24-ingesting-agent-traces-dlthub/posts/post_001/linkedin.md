---
post_id: post_001
platform: linkedin
status: draft
---

Your coding agent is already producing a dataset.

When you use tools like Claude Code, Codex, Copilot, or other local coding agents, they store metadata about your sessions: token usage, models, inputs, outputs, cache, project traces, and tool calls.

This is useful data.

You can ask questions like:

- How many tokens did I use last month?
- Which models did I use the most?
- Which projects generated the most activity?
- Did any secrets appear in my logs?

The hard part is that the raw files are usually JSON or JSONL, and they are not pleasant to inspect manually.

In Alena Astrakhantseva's workshop, we went from local agent traces to an ingestion pipeline and a dashboard:

- Read local trace files
- Load them with dlt
- Store them in DuckDB
- Explore usage by day, model, and project
- Turn unreadable logs into something you can query

This is a nice framing for agent observability:

Start with traces as data.

Then build the ingestion layer, schema, validation, and reports around them.

Recording:
https://youtube.com/live/A0LmmZf-ggM
