---
platform: x
url: "https://x.com/Al_Grigor/status/2015333850130575586"
---

What are skills in AI agents?

In one of the workshops, I demo a GitHub Fetch skill.

The task seems simple: retrieve files from a GitHub repository. But without this skill, the agent must guess how to:

- Interact with GitHub
- Choose the right commands
- Navigate the repository structure

A skill provides a reusable set of instructions that guides the agent through tasks step by step.

Specifically, the GitHub Fetch skill instructs the agent on:

- Using the gh CLI
- Listing repository contents
- Navigating directories
- Downloading specific files

With these validated instructions, skills minimize reasoning errors by encoding operational knowledge.

In the demo, we used this skill to fetch two commands from a GitHub repo:

- /kid generates a wild project idea
- /parent implements it as code

These commands are stored in GitHub, and the agent uses the GitHub Fetch skill to automatically retrieve them.

Skills offer benefits like:

- Making behavior predictable
- Avoiding repeated prompts
- Reusing hard-won instructions
- Scaling beyond one-off demos

I teach how to build production-ready AI agents in my AI Bootcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

The next cohort starts tomorrow: https://maven.com/alexey-grigorev/from-rag-to-agents