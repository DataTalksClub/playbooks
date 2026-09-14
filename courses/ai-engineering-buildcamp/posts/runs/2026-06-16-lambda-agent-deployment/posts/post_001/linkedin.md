---
post_id: post_001
platform: linkedin
status: draft
---

Small agent tools do not always need an always-on server.

In the previous workshop, we deployed the FAQ agent as a containerized web app. That worked, but it still meant having a service running somewhere.

For tools that are used once a day, once a week, or only when you need them, AWS Lambda is a good deployment option.

The difference is the cost model:

- Railway, Render, Fly.io, or an EC2-style setup gives you a service that exists all the time
- Lambda wakes up when it is invoked
- If nobody uses the app, there is no always-on server to pay for

In the workshop, we took the same agent app and deployed it as a Lambda Function URL.

It still served the frontend.
It still handled the agent API.
It still streamed responses back to the browser.

The interesting part is not that Lambda is always better. It is not.

The useful distinction is workload shape.

If the app is a public product with steady traffic, a normal web service can be simpler.

If it is a small internal tool, a personal agent, or a rarely used workflow, Lambda can fit well.

Full workshop materials: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Recording: https://youtu.be/zoAvc8VU6Qs
