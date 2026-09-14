---
post_id: post_001
platform: x
status: draft
---

1/6

When building an agent app, the first milestone is not "make the agent perfect".

It is: make the whole path work.

2/6

For the workshop app, that meant:

- Simple tool call loop
- FastAPI backend
- Frontend
- Docker image
- Deployment that responds

3/6

We did not start with a vector database.

We did not add structured outputs first.

We did not build full conversation memory first.

Those are useful, but they add complexity.

4/6

This matters even more with streaming.

Structured outputs plus streaming plus tool events can make the first version much harder to reason about.

5/6

Once the vertical slice works, you have something real to improve:

- Better retrieval
- Traces
- Evaluation
- Tests
- Auth
- Deployment guardrails

6/6

Build the smallest deployable agent first.

Then make it better.

Recording: https://youtu.be/h84rcRezNM4
