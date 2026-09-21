---
issue: 285
send_date: 2026-07-13
status: sent
subject: "🛠️ Free workshop: Build an AI Agent with Guardrails | DataTalks.Club Weekly"
preview_text: "Learn how to stop an AI agent from answering off-topic requests or making unsafe promises."
mailchimp_title: "Weekly email #285 (July 13, 2026) – not sponsored"
archive_url: https://mailchi.mp/datatalks.club/weekly-285
source: Mailchimp export (plain-text version, as sent)
---

## Build an AI Agent with Guardrails

You learned how to build and evaluate LLM applications during LLM Zoomcamp, but the course does not cover guardrails.

Use this workshop to build an agent for the Data Engineering Zoomcamp FAQ and add guardrails around its inputs and outputs.

- Check whether requests match the agent’s topic and purpose
- Detect unsafe promises and policy violations in responses
- Run multiple guardrails concurrently to limit added latency

The tutorial uses Python, Pydantic, minsearch, and the OpenAI Python SDK, with no agent framework required.

[Read the workshop tutorial](https://aishippinglabs.com/workshops/agent-with-guardrails)

_Sponsored content_

## LLM Zoomcamp: Module 5

This week in LLM Zoomcamp: Module 5, Monitoring.

We build:

- A Streamlit chat app with RAG
- Metric capture for LLM calls and cost
- PostgreSQL storage for conversations
- User feedback with thumbs up and thumbs down
- Automatic relevance evaluation with a built-in judge
- Streamlit and Grafana dashboards
- A Docker Compose setup for running everything together

You’ll focus on what your LLM application is doing after deployment to determine what to improve next.

[Start Module 5](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring)

## Upcoming events

- [July 21, 12:30 PM: Engineering Your Own AI Assistant](https://luma.com/s5snn8xy) – Paul Iustin breaks down the practical realities of agentic AI engineering for the individual developer.
- [July 21, 4:30 PM: Tracking and personalizing AI agents with Snowplow and the Vercel AI SDK](https://luma.com/vz9iv4f2) – Instrument a Next.js agentic application with behavioral tracking across and feed real-time user context from Snowplow Signals back into the agent's system prompt
- [August 3, 12:30 PM: Engineering AI-Powered Data Products](https://luma.com/si2n1g9b) – Radovan Bacovic shares his insights from over 20 years in the data world on navigating today's data landscape.
- [August 3, 4:30 PM: Running Durable Agents in Production](https://luma.com/wz20rm8n) – Turn a working agent loop into a durable production workflow that can pause, recover, retry, and keep a full execution history.

## Tracking and personalizing AI agents with Snowplow and the Vercel AI SDK

Your agent can see the chat history but not what the user is doing in the product. If you want the agent to respond based on the user's current session, you need to capture that context and make it available to the model.

This workshop shows how to do that with a Next.js travel chatbot.

The approach:

1. Track client behavior (page views, clicks, filters)
2. Track server-side events (purchases, bookings)
3. Track agent decisions (tool calls, outcomes)
4. Validate events against schemas in real time
5. Compute session attributes with Snowplow Signals
6. Inject those attributes into the system prompt

You'll set up the pipeline, add tracking at each layer, and use live session data to shape the agent's responses.

[Register here](https://luma.com/vz9iv4f2)

## Running Durable Agents in Production

Most agents run cleanly in a demo and then break the first time something goes wrong in production. The agent logic was never the hard part. Keeping it running reliably is.

In this workshop, Nicholas Lotz shows how to turn a working agent loop into a durable production workflow that can pause, recover, retry, and keep a full execution history.

You'll learn how to:

- Persist agent state outside the running process, so a crash doesn't lose progress
- Resume execution after crashes or interrupted deployments
- Retry flaky tool calls with timeouts and recovery logic
- Add human approval steps and more!

By the end, you'll understand the execution layer that separates a clever agent demo from a reliable agent service.

[Register here](https://luma.com/wz20rm8n)

## Alexey on Data Newsletter: PyPI Release Pipeline for Python Libraries

In the latest newsletter edition, Alexey shared his workflow for creating Python libraries and releasing them to PyPI.

Read the full edition to learn about:

- Starting a library and choosing a name
- Publishing the first version
- Releasing through CI
- Automating the process with agents

[Read here](https://alexeyondata.substack.com/p/my-pypi-release-pipeline-for-python)
