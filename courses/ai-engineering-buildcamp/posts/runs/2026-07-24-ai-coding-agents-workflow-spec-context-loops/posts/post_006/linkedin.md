---
post_id: post_006
platform: linkedin
status: draft
---

My practical agent workflow has three roles:

PM, engineer, QA.

The PM grooms the issue.

The engineer implements it.

The QA checks the result against the acceptance criteria.

If QA passes, the issue can move forward.

If QA fails, the issue goes back to the engineer with specific failures.

This is what people now call graph engineering, but the concept is familiar from software teams.

It is a workflow:

1. Pick an issue
2. Groom it if needed
3. Implement it
4. Test it against acceptance criteria
5. Loop failed work back to implementation
6. Close the issue only when the criteria pass

The orchestrator is the main agent session.

It does not do all the work itself.

It launches the right role at the right time and keeps the process moving.

Loop engineering helps with persistence.

Instead of babysitting the agent, I set a goal such as:

"Work through the MVP backlog."

The loop keeps nudging the agent to continue until the goal is done.

There is a trade-off.

This uses more tokens than a single implementation prompt.

But the quality is better because the tester often finds things the implementation agent missed.

For user-facing features, that trade-off is usually worth it.

Workshop recording:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
