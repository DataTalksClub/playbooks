---
post_id: post_004
platform: linkedin
status: draft
---

Moving an agent app from FastAPI to Lambda is mostly about replacing the web layer.

The agent loop did not need to change much.
The search tool did not need to change much.
The frontend did not need to change much.

The part that changed was the layer that receives HTTP requests and sends responses back.

With FastAPI, the framework handles routing:

- `GET /`
- Static files
- `POST /ask`
- `POST /ask/stream`
- Response headers
- Request parsing

With Lambda, you are closer to the raw request.

The handler has to inspect the method and path, route to the right function, parse the body, and return the correct response.

Streaming adds another constraint.

For a normal Lambda response, buffering is fine. For an agent UI, waiting until the whole answer is ready is not what we want. We want server-sent events to arrive while the agent is working.

That is why the workshop used a custom Lambda runtime and a Function URL with response streaming.

The useful lesson: most of the application can stay the same, but deployment targets define the shape of the web adapter.

Full workshop materials: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Recording: https://youtu.be/zoAvc8VU6Qs
