---
owner: "alexey"
date: "2026-07-29"
platform: "Alexey Newsletter"
status: "draft"
event: "Workshop 2: Build and Ship an AI-Assisted Full-Stack App"
sequence_slot: "Educational post"
created: "2026-07-22"
---

# Newsletter Section

## Keep the project state outside the chat

When I use an AI coding tool for a larger project, I do not want the important decisions to live only in the conversation.

The chat is useful for the current task. The repository needs to preserve the state of the project after that task is finished.

For an end-to-end application, this state is spread across several artifacts:

- The product spec describes what we are building
- Acceptance criteria describe the behavior we need to verify
- The API contract describes how the frontend and backend communicate
- Tests preserve the behavior that already works
- Docker and deployment files describe how the application runs

Once I review and accept an output, it becomes context for the next task. The backend follows the API contract. The tests follow the acceptance criteria. The deployment follows the runtime assumptions recorded in the project.

This makes errors easier to locate. When the application behaves incorrectly, I can compare the implementation with an explicit decision instead of trying to remember what I meant several prompts ago.

I will demonstrate this process in Workshop 2 of AI Dev Tools Zoomcamp by taking one application from idea to deployment.

Monday, August 3
3:00 PM to 4:30 PM GMT+2

RSVP: https://luma.com/50kvfku2

# Notes

- Angle: Store accepted project decisions in repository artifacts instead of relying on chat history.
- CTA: RSVP for Workshop 2.
- Source material: `copy-bank/events/02-2026-08-03-build-and-ship-ai-assisted-full-stack-app.md`.
