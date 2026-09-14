---
post_id: post_006
platform: x
status: draft
---

1/6

My practical agent workflow has three roles:

PM, engineer, QA.

The PM grooms. The engineer implements. QA checks the result.

2/6

If QA passes, the issue moves forward.

If QA fails, the issue goes back to the engineer with specific failures.

3/6

This is a workflow graph:

Pick issue -> groom -> implement -> test -> pass or loop back.

The orchestrator runs the process instead of doing every step itself.

4/6

Loop engineering helps with persistence.

I can set a goal like:

"Work through the MVP backlog."

Then the agent keeps moving through the pile.

5/6

There is a cost.

PM + engineer + QA uses more tokens than one implementation prompt.

6/6

The benefit is quality.

The tester often finds things the implementation agent missed.

Workshop:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
