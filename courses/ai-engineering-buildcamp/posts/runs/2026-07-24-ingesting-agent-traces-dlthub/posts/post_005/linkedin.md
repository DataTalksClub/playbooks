---
post_id: post_005
platform: linkedin
status: draft
---

Agent observability starts with ingestion.

When you build your own agents, traces may live in many places:

- Local files
- Logfire
- Langfuse
- Platform APIs
- Internal logging systems
- Vendor APIs for coding assistants

Each source can have a different structure.

One system may expose tool calls in one shape. Another may store model usage differently. Another may have deeper nesting around sessions, spans, inputs, outputs, or metadata.

This is why agent observability quickly becomes a data engineering problem.

First you need to collect the traces.

Then you need to load them into a destination where you can ask useful questions:

- Which models are used most?
- Which tools are called?
- How much usage does each project generate?
- Which sessions fail?
- Where are performance issues?
- What should be monitored over time?

In Alena Astrakhantseva's workshop, we simulated this with a REST API that returns fake agent logs, then used dlt to ingest the data and build a report.

The same pattern applies when the source is Logfire, Anthropic API, local trace files, or another logger.

Collect traces.

Structure them.

Validate them.

Build reports that help you understand how the agent behaves.

Recording:
https://youtube.com/live/A0LmmZf-ggM
