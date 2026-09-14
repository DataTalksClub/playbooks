---
post_id: post_002
platform: linkedin
status: draft
---

For agent projects, I like starting with a CLI.

Even when the final product is supposed to be a Telegram bot.

In the workshop, the assignment was to build an investment coaching bot. The tempting first step is obvious:

Create the Telegram bot.

But I started with a terminal app.

Why?

Because at the beginning I do not care about Telegram yet.

I care about the core loop:

- user asks a question
- agent decides what tools to call
- tools fetch company data
- agent produces an answer
- answer respects the safety boundary

The CLI makes this much easier to inspect.

When the agent answers, I can ask:

- Did it call the tools?
- Did it just recite the prompt?
- Did it dump raw API data?
- Did it start with useful analysis?
- Did it avoid personalized financial advice?

Only after this loop works does it make sense to add Telegram.

This is a general pattern I use with agents:

Build the boring interface first.

Then add the nicer interface.

The boring interface is usually where debugging is cheapest.

Recording: https://youtu.be/aPq-y5PO9m4
