---
post_id: post_004
platform: x
status: draft
---

1/7

For AI agents, checking the final answer is not enough.

You also need to check how the agent got there.

2/7

In the workshop, the investment bot:

- receives a question
- calls tools
- fetches company data
- produces an answer

The answer is only one artifact.

3/7

An answer can look fine while the agent:

- called the wrong tool
- skipped data
- made too many calls
- looped
- answered from general knowledge

4/7

That is why I like evaluating the trajectory.

Trajectory = the sequence of tool calls and intermediate steps before the final response.

5/7

A useful eval scenario can include:

- user input
- expected answer properties
- expected tool behavior
- final answer
- collected trajectory
- judge/checks

6/7

Output evals ask:

"Does the answer look good?"

Trajectory evals ask:

"Did the agent behave like the system we meant to build?"

7/7

For agents, both matter.

Especially when tool use is the product.

Recording: https://youtu.be/aPq-y5PO9m4
