---
post_id: post_002
platform: x
status: draft
---

1/6

An agent UI should not stay silent while the backend is working.

If nothing changes for 20 seconds, the app feels broken.

Even when the agent is doing useful work.

2/6

For agent apps, I like showing:

- Streaming answer text
- Tool calls
- Tool inputs
- Tool results
- Long outputs collapsed by default

3/6

This is not only UX.

It is observability.

You can see whether retrieval happened, whether the right tool was called, and what data came back before the final answer.

4/6

In the workshop, the first frontend waited until the final response was ready.

It worked, but it was hard to know what was happening.

5/6

The better version streamed events from FastAPI to the frontend and showed tool activity as it happened.

This makes debugging much easier.

6/6

If you build agent products, expose the important events.

Users and developers both need to see progress.

Recording: https://youtu.be/h84rcRezNM4
