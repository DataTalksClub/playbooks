---
post_id: post_005
platform: linkedin
status: draft
---

One of the best moments in the workshop was when the bot broke.

We had the investment coach working in the CLI.

Then we wrapped it as a Telegram bot.

It started responding. We could see activity in monitoring. Everything looked fine.

Then a query made the agent keep calling the same search tool again and again.

This is exactly the kind of bug I want to find during a workshop.

Because now we have a real eval case.

Not a theoretical one.

The fix is not only:

"Add a limit."

The fix is:

- add a tool-call limit
- return a graceful "I do not know" answer
- add a regression test
- add an eval scenario
- verify the trajectory stops

For example:

"The agent should not make more than 5 tool calls for this question."

This is the practical side of agent evaluation.

You do not invent all scenarios upfront.

You use the system, observe failures, and encode them so they do not come back.

Every weird demo failure is a future test case.

Recording: https://youtu.be/aPq-y5PO9m4
