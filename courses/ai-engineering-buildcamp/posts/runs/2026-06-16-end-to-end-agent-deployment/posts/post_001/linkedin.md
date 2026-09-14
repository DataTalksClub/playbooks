---
post_id: post_001
platform: linkedin
status: draft
---

When building an agent app, the first goal is not to design the perfect agent.

The first goal is to make the whole path work:

- A simple tool call loop
- A backend endpoint
- A frontend that can ask questions
- A Docker image
- A deployment that actually responds

In the workshop, we started with a small RAG FAQ agent. No vector database at first. No complicated framework. No structured outputs in the first version.

Structured outputs are useful. Conversation memory is useful. A better retrieval layer is useful.

But each of them adds another layer of complexity, especially when streaming is involved.

So the first milestone was simple: make the thing work end to end.

Once that vertical slice is running, you have a real system to improve. You can add better retrieval, traces, tests, structured outputs, auth, and more careful evaluation.

Before that, you are still guessing.

Full recording: https://youtu.be/h84rcRezNM4
