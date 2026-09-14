---
post_id: post_002
platform: x
status: draft
---

1/6

For agent projects, I like starting with a CLI.

Even when the final product is supposed to be a Telegram bot.

2/6

In the workshop, the assignment was an investment coaching bot.

The tempting first step:

Create the Telegram bot.

I started with a terminal app instead.

3/6

At the beginning, I care about the core loop:

- user question
- tool selection
- data fetch
- answer
- safety boundary

4/6

The CLI makes debugging easier.

Did the agent call tools?

Did it dump raw API data?

Did it start with useful analysis?

Did it avoid financial advice?

5/6

Only after the loop works does it make sense to add Telegram.

Otherwise you debug the agent, the data, and the UI at the same time.

6/6

My agent-project rule:

Build the boring interface first.

Then add the nicer interface.

Recording: https://youtu.be/aPq-y5PO9m4
