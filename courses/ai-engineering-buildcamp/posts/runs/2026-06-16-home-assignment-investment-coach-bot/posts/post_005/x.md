---
post_id: post_005
platform: x
status: draft
---

1/7

One of the best moments in the workshop was when the bot broke.

2/7

We had the investment coach working in the CLI.

Then we wrapped it as a Telegram bot.

It started responding. Monitoring showed activity. Things looked fine.

3/7

Then one query made the agent keep calling the same search tool again and again.

Not ideal.

But very useful.

4/7

Now we had a real eval case.

Not a theoretical one.

The system showed us a failure mode.

5/7

The fix is not only:

"Add a limit."

The fix is:

- add a tool-call limit
- return gracefully
- add a regression test
- add an eval scenario

6/7

Example assertion:

"The agent should not make more than 5 tool calls for this question."

Then check the trajectory.

7/7

This is practical agent evaluation:

Use the system.
Observe failures.
Encode them.

Every weird demo failure is a future test case.

Recording: https://youtu.be/aPq-y5PO9m4
