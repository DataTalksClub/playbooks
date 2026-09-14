---
post_id: post_003
platform: x
status: draft
---

1/5

Agent traces rarely arrive as clean analytics tables.

They arrive as deeply nested JSON.

Messages, usage, cache, models, tool calls, project metadata, inputs, outputs.

2/5

In Alena's workshop, the first dlt pipeline loaded local coding-agent traces and created 78 tables.

That number makes sense once you see how nested the source data is.

3/5

Then the pipeline was adjusted.

Some fields stayed as JSON columns instead of becoming separate tables.

The schema went from 78 tables to 40.

4/5

This is the practical part of agent observability:

Design a trace schema that is queryable enough for dashboards and flexible enough for messy payloads.

5/5

Workshop recording:
https://youtube.com/live/A0LmmZf-ggM
