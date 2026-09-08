---
platform: x
date: 2026-03-02
url: "https://x.com/Al_Grigor/status/2028530825499984181?s=20"
media: "image"
analytics:
  likes: 4
  reposts: 0
  comments: 1
  impressions: 526
  engagements: 26
  detail_expands: 6
  profile_visits: 2
---

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents
