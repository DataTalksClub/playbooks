---
post_id: post_002
platform: linkedin
status: draft
---

An agent UI should not sit silently while the backend is working.

If the user asks a question and nothing changes for 20 seconds, the app feels broken. Even if the agent is doing useful work.

For agent apps, I like showing the work as it happens:

- The response streaming in
- The tool call being made
- The tool input
- The tool result
- Long tool output collapsed by default

This is not just a UX detail.

It makes the system easier to debug. It shows whether retrieval happened. It shows whether the agent called the right tool. It shows what data came back before the final answer was written.

In the workshop, the first frontend waited until the final answer was ready. It technically worked, but it was hard to see what was happening.

The better version streamed events from the FastAPI backend to the frontend and showed tool calls in the interface.

For production agent apps, this is one of the simplest observability improvements you can make.

Full recording: https://youtu.be/h84rcRezNM4
