---
post_id: post_005
platform: x
status: draft
---

1/5

Agent observability starts with ingestion.

Your traces may live in local files, Logfire, Langfuse, platform APIs, internal loggers, or vendor APIs.

2/5

Each source can have a different shape.

Tool calls, model usage, sessions, spans, inputs, outputs, and metadata are not always represented the same way.

3/5

So the first job is data engineering:

Collect traces. Load them somewhere queryable. Preserve the fields you need. Validate the shape.

4/5

Then you can ask useful questions:

Which models are used? Which tools are called? Which sessions fail? Which projects generate the most usage?

5/5

Alena Astrakhantseva showed this with dlt and agent traces:

https://youtube.com/live/A0LmmZf-ggM
