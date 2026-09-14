---
post_id: post_003
platform: x
status: draft
---

1/7

For a small agent app, you often do not need separate frontend and backend containers.

One Docker image can be enough.

2/7

In the workshop app:

- FastAPI backend
- Vanilla JS frontend
- Docker deployment target

We packaged it as one service.

3/7

The Dockerfile used a multi-stage build:

1. Build frontend in a Node.js stage
2. Copy static files into the backend image
3. Let FastAPI serve API + frontend

4/7

This keeps Node.js out of the runtime image.

The final container only needs the backend runtime and the generated frontend assets.

5/7

It also simplifies deployment:

- One container
- One service
- One place to test env vars

6/7

There was still a real bug.

The app worked outside Docker, then failed inside Docker because the API key was not passed in the expected format.

7/7

Lesson: test the app inside the container before deploying.

Especially secrets and environment variables.

Recording: https://youtu.be/h84rcRezNM4
