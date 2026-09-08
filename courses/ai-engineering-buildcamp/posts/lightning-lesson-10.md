---
platform: x
url: "https://x.com/Al_Grigor/status/2016421020513788090"
---

When building agents, what is the difference between skills and commands?
They look similar, but they serve different roles.

1. Commands are explicit. You can think of them as user-driven shortcuts

🔸 The user knows exactly what should happen
🔸 The user triggers it directly, for example /kit
🔸 The agent simply executes the instruction

2. Skills are implicit

🔸 The user describes a task in natural language
🔸 The agent decides whether a skill applies
🔸 The agent loads and uses the skill autonomously

The user never says, "Use this skill"

Skills encode operational knowledge. They tell the agent how to do something, so it doesn't have to guess.

3. The key distinction is who makes the decision:

🔸 Commands: the user decides
🔸 Skills: the agent decides

Commands are best when the intent is precise.

Skills are better when you want reusable, predictable agent behavior across tasks and projects.

If you want to go deeper, I've shared a free workshop on implementing skills from scratch:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up. Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents