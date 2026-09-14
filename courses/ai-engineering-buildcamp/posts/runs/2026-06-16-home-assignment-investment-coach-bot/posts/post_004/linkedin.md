---
post_id: post_004
platform: linkedin
status: draft
---

For AI agents, checking the final answer is not enough.

You also need to check how the agent got there.

In the workshop, we built a small investment coaching bot. A user asks a question, the agent calls tools, fetches company data, and produces an answer.

When evaluating this, I want to know two things:

1. Is the answer acceptable?

2. Was the path acceptable?

The second part is easy to miss.

An answer can look fine while the agent:

- called the wrong tool
- skipped the data source
- made too many tool calls
- looped on the same action
- answered from general knowledge instead of fetched data

This is why I like evaluating the trajectory.

Trajectory means the sequence of steps before the final response:

- tool calls
- inputs to the tools
- returned data
- reasoning path visible through the calls

For the investment bot, a good eval scenario can include:

- user input
- expected answer properties
- expected tool behavior
- final answer
- collected trajectory
- LLM judge or deterministic checks

Output-only evals tell you whether the answer looks good.

Trajectory evals tell you whether the agent behaved like the system you meant to build.

For agents, both matter.

Recording: https://youtu.be/aPq-y5PO9m4
