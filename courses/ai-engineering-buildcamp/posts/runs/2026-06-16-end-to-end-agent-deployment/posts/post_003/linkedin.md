---
post_id: post_003
platform: linkedin
status: draft
---

For a small agent app, you often do not need separate frontend and backend containers.

In the workshop, we had:

- A FastAPI backend
- A vanilla JavaScript frontend
- A Docker deployment target

The simple setup was one Docker image.

The Dockerfile used a multi-stage build:

1. Build the frontend in a Node.js stage
2. Copy the generated static files into the backend image
3. Let FastAPI serve both the API and the frontend assets

This keeps Node.js out of the runtime image. The final container only needs the backend runtime and the built frontend files.

It also makes deployment simpler. One service. One container. One set of environment variables to check.

Of course, this is not always the right architecture. If the frontend is large, owned by another team, or deployed independently, separate services make sense.

But for a small agent app, one container is often enough.

One small lesson from the demo: always test secrets and environment variables inside the container. The app worked outside Docker, then failed inside Docker because the API key was not passed in the expected format.

That is exactly the kind of issue you want to catch before deployment.

Full recording: https://youtu.be/h84rcRezNM4
