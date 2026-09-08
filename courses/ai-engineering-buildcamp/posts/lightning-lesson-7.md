---
platform: x
date: 2026-02-11
url: "https://x.com/Al_Grigor/status/2021600160074379649"
---

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large FAQ for a Data Engineering course hosted on GitHub: 300+ questions, written by students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents
