---
post_id: post_001
platform: x
status: draft
---

1/6

Small agent tools do not always need an always-on server.

For tools you use once a day or once a week, AWS Lambda can be a better fit.

2/6

In the previous workshop, we deployed the FAQ agent as a containerized web app.

That worked, but it still meant running a service somewhere.

3/6

Lambda changes the cost model.

The function wakes up on invocation.

If nobody uses the app, there is no always-on server to pay for.

4/6

In this workshop, the same agent app served:

- Frontend
- Agent API
- Streaming responses

through a Lambda Function URL.

5/6

Lambda is not always better.

It is useful when the workload is occasional: internal tools, personal agents, small workflows, and experiments.

6/6

For steady public traffic, a normal web service can be simpler.

For low-traffic agent tools, serverless is worth considering.

Recording: https://youtu.be/zoAvc8VU6Qs
