# Test, Containerize, and Deploy an AI-Assisted App

- **Instructor:** Alexey Grigorev
- **Date:** Monday, August 10, 2026
- **Time:** 14:00 Europe/Berlin
- **Location:** YouTube
- **Registration:** {{ workshop_3_luma_url }}

## About Event

This is the 3rd workshop in our series to update the AI Dev Tools Zoomcamp content.

This workshop updates [Module 3: Test, Containerize, and Deploy an AI-Assisted App](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/03-deployment?utm_source=luma).

The previous workshop ended with an application that runs on your machine. In this hands-on session, Alexey Grigorev will take it the rest of the way: proven by tests that exercise the real stack, packaged in containers, checked automatically on every pull request, and deployed at a public URL.

Each of those steps is something AI tools are good at drafting and bad at owning. A generated `Dockerfile` that builds isn't the same as one that builds the right thing. A green pipeline that skips the tests is worse than no pipeline at all.

## What You'll Learn

- How to write integration tests that exercise the API, the database, and the frontend together
- How to set up and tear down a test database, and when to recreate it instead of rolling back
- How to test against the OpenAPI spec instead of against the implementation
- How to check that an AI-generated test suite actually catches anything, by breaking the code on purpose
- How to containerize the app with a multi-stage build that compiles the frontend and serves it from the backend image
- How to move from SQLite to Postgres without rewriting the application code
- How to keep secrets and environment configuration out of the image
- How to set up CI so linting, tests, and the container build run on every pull request
- How to read a failing pipeline log and feed it back to the agent
- How to deploy to a platform such as Render, Fly.io, Railway, or Cloud Run
- How to handle managed databases, migrations, health checks, logs, and rollback
- How to connect the pipeline to the deployment so merging to the main branch is what ships
- Why a deploy that succeeded isn't the same as an app that works

By the end, you'll know how to take an AI-assisted application from your laptop to a public URL that redeploys automatically when the tests pass.

Like the other workshops, this will be a live demo with practical tips and time for Q&A.

## All Events in This Series

- [AI-Native Developer Workflow: Using AI Tools Without Losing Control](https://www.youtube.com/watch?v=VUJxJGpaDEs)
- [Build and Ship an AI-Assisted Full-Stack App](https://www.youtube.com/watch?v=x9dq5nBpDg8)
- [Test, Containerize, and Deploy an AI-Assisted App]({{ workshop_3_luma_url }})
- [Open-Source AI Tools for Security, Audit, and DevOps](https://luma.com/ycsfxigi)
- [Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents](https://luma.com/ap4l3qlj)
- [AI Dev Tools Zoomcamp 2026 Pre-Course Live Q&A](https://luma.com/a8qa5s2s)
- [AI Dev Tools Zoomcamp 2026 Course Launch](https://luma.com/tsiusx8s)

## Thinking About Joining AI Dev Tools Zoomcamp?

This workshop covers the updated content for [Module 3](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/03-deployment?utm_source=luma) of [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp?utm_source=luma), our free course on using AI tools in practical software development workflows.

The course covers AI-assisted planning, coding, review, testing, deployment, coding agent capabilities, MCP, skills, plugins, security, audit, DevOps, and a complete final project.

The new cohort of AI Dev Tools Zoomcamp starts on August 31, 2026. You can join it by [registering here](https://courses.datatalks.club/register/ai-dev-tools/?utm_source=luma).

## About the Speaker

Alexey Grigorev is the Founder of DataTalks.Club and creator of the Zoomcamp series.

Alexey is a software and ML engineer with over 10 years in engineering and 6+ years in machine learning. He has deployed large-scale ML systems at companies like OLX Group and Simplaex, authored several technical books, including Machine Learning Bookcamp, and is a Kaggle Master with a 1st place finish in the NIPS'17 Criteo Challenge.

[DataTalks.Club](http://datatalks.club/?utm_source=luma) is the place to talk about data. [Join our Slack community](https://datatalks.club/slack.html?utm_source=luma)!
