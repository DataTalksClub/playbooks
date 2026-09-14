---
post_id: post_003
platform: linkedin
status: draft
---

AI coding agents are very good at creating tests that look like tests.

That is not the same as creating useful tests.

In the workshop, the agent generated tests for the investment coach bot.

Some of them were basically checking:

- imports work
- method names exist
- certain words appear in instructions

This gives false confidence.

It makes the repository look responsible:

"Look, we have tests."

But the tests do not tell us whether the agent behaves correctly.

For an AI agent, I would rather test things like:

- when the user asks a company question, does the agent call the expected tools?
- does the answer avoid forbidden financial advice?
- does the answer contain something useful, not only a data dump?
- does the agent stop instead of looping forever?

This is why I spent time cleaning the tests before cleaning the code.

Sloppy implementation code is not great.

But sloppy tests are more dangerous because they become the thing we trust.

With AI-generated code, reviewing tests is not optional.

It is part of owning the system.

Recording: https://youtu.be/aPq-y5PO9m4
