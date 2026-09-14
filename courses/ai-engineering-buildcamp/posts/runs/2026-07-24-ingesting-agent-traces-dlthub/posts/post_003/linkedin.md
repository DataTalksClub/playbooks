---
post_id: post_003
platform: linkedin
status: draft
---

Agent traces rarely look like analytics tables.

They look like deeply nested JSON.

That detail matters.

In Alena Astrakhantseva's workshop, the first dlt pipeline loaded local coding-agent traces and created 78 tables.

At first this may look surprising. Why so many tables?

Because the raw traces are nested:

- Messages
- Inputs
- Outputs
- Usage
- Cache
- Models
- Tool calls
- Project/session metadata

When you load this into a relational database, the ingestion layer has to decide how much to normalize.

Flatten everything too aggressively and you get schema pollution.

Keep too much as raw JSON and the data becomes harder to query.

The interesting part of the demo was that the agent adjusted the pipeline: some fields stayed as JSON columns, and the schema went from 78 tables to 40.

This is a good practical lesson for agent observability.

The problem is not only "collect traces".

The problem is designing a useful shape for trace data:

- Queryable enough for dashboards
- Flexible enough for messy nested payloads
- Stable enough to maintain as agent tools change

Recording:
https://youtube.com/live/A0LmmZf-ggM
