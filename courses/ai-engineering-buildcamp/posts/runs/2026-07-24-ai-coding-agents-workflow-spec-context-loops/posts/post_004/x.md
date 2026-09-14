---
post_id: post_004
platform: x
status: draft
---

1/5

Context engineering for coding agents is mostly documentation discipline.

The agent needs to know the project, commands, process, task tracker, roles, and relevant docs.

2/5

You can repeat this in every prompt.

Or you can put the context in the repo.

In the workshop, I used `AGENTS.md` as the root context file.

3/5

Keep the root file short.

It should be a map, not a manual.

Point to `docs/process.md`, testing docs, UI docs, and role files.

4/5

Then the agent can load the context needed for the current task instead of carrying everything all the time.

This saves tokens and reduces confusion.

5/5

Practical context engineering:

Put durable project knowledge where the agent can find it.

Workshop:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
