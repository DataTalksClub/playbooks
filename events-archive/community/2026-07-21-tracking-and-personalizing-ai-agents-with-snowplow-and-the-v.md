# Tracking and personalizing AI agents with Snowplow and the Vercel AI SDK

- **Type:** Workshop
- **Date:** Tuesday, July 21, 2026
- **Time:** 17:00 Europe/Berlin
- **Instructor:** Jordan Peck, James Borlase
- **Luma:** https://luma.com/vz9iv4f2
- **Related course:** LLM Zoomcamp (adjacent, not part of the series)

## About Event

AI agents usually rely on the conversation as their main source of context.

But users also interact with the rest of the product. They open pages, change filters, compare options, and take actions before asking the agent a question.

This creates two practical challenges:

1.   The agent may respond without important context from the current user session.

2.   The engineering team may have limited visibility into what the user did, what the application recorded, and how the agent responded.

In this hands-on workshop, we will show how to address both problems using a Next.js travel chatbot example.

We will use data from three layers: client-side user activity, server-side application events, agent actions and decisions to compute live session attributes and pass them into the agent's system prompt.

During the workshop, you'll learn how to:

*   Set up a pipeline

*   Validate events against schemas in real time

*   Track user, application, and agent activity

*   Capture agent actions and decisions as structured events

*   Compute live session attributes from a behavioral event stream

*   Add those attributes to the agent's system prompt

*   Adapt responses based on what the user is doing in the product

You'll understand:

*   How behavioral data can improve agent responses

*   How to add observability beyond basic chat logs

*   How to connect product analytics with agent traces

*   How to structure events so they can support debugging, evaluation, and personalization

*   How to implement real-time context without building the entire data pipeline from scratch

By the end of the workshop, you will have a practical example of how to connect behavioral tracking, agent observability, and real-time personalization in one application.

## About the speakers:

**Jordan Peck** is Director of Field Engineering at Snowplow, working with the company's most complex and strategic customers to solve behavioral data challenges. He helps engineering and data teams get Snowplow pipelines into production and extract value from event streams to power real-time agentic use cases.

**James Borlase** is a Senior Product Manager at Snowplow, specializing in event tracking, data strategy, and advanced analytics. With a background in analytics leadership at Sessions, Google, and Serato, he has built data-driven solutions in machine learning, real-time personalization, product analytics, and marketing measurement.

* * *

This workshop is hosted by DataTalks.Club with support from [Snowplow](https://snowplow.io/?utm_source=luma).

[DataTalks.Club](http://datatalks.club/?utm_source=luma) is the place to talk about data. [Join our Slack community](https://datatalks.club/slack.html?utm_source=luma)!
