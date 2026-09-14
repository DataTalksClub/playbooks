---
post_id: post_003
platform: x
status: draft
---

1/7

AI coding agents are very good at creating tests that look like tests.

That is not the same as creating useful tests.

2/7

In the workshop, the agent generated tests for the investment coach bot.

Some were basically checking:

- imports work
- method names exist
- certain words appear in prompts

3/7

This gives false confidence.

The repository looks responsible:

"Look, we have tests."

But the tests do not tell us if the agent behaves correctly.

4/7

For an AI agent, I would rather test:

- expected tool calls
- forbidden advice is absent
- answer is useful
- no endless tool loop

5/7

That is why I spent time cleaning tests before cleaning the rest of the code.

Tests are the thing we trust when we change the system.

6/7

Sloppy implementation code is bad.

Sloppy tests are worse because they can make bad code look safe.

7/7

With AI-generated code, reviewing tests is not optional.

It is part of owning the system.

Recording: https://youtu.be/aPq-y5PO9m4
