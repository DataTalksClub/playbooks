---
post_id: post_004
platform: x
status: draft
---

1/7

Moving an agent app from FastAPI to Lambda is mostly about replacing the web layer.

The agent loop can stay mostly the same.

2/7

In the workshop, these parts stayed close to the previous version:

- Agent loop
- Search tool
- Renderer abstraction
- Frontend

3/7

The changed part was the HTTP adapter.

FastAPI handles routing, request parsing, static files, and response headers for you.

4/7

Lambda is lower-level.

The handler needs to inspect method/path, route the request, parse the body, and return the response.

5/7

Streaming adds another constraint.

For an agent UI, buffering the whole answer is not enough.

We want SSE events while the agent is working.

6/7

That is why the workshop used a custom Lambda runtime and a Function URL with response streaming.

7/7

The deployment target defines the web adapter.

Most of the agent logic can stay the same.

Recording: https://youtu.be/zoAvc8VU6Qs
