---
platform: x
date: 2026-02-24
url: "https://x.com/Al_Grigor/status/2026263333452865956"
media: "image"
analytics:
  likes: 3
  reposts: 0
  comments: 2
  impressions: 621
  engagements: 29
  detail_expands: 7
  profile_visits: 2
---

Developer cheatsheet to turn a chatbot into a coding agent:

1) Chatbot vs agent decision

Decide upfront whether you actually need an agent. Agents are only worth it when you need actions like file I/O, code execution, or search.

2) Tool schema definition

Define concrete tools with strict schemas describing names, parameters, and constraints, and expose only what the agent should be allowed to do.

3) Tool execution loop

Implement a loop where the model proposes tool calls, your system executes them, and the results are fed back into the conversation state.

4) Project-scoped editing tools

Provide file and shell access scoped to a project root, with guardrails to prevent unsafe commands and accidental damage.

5) Project template scaffolding

Start each run from a clean template copied into a fresh directory so all agent edits remain isolated and reproducible.

6) System prompt as documentation

Use the system prompt to document the tech stack, file structure, and rules, and require the model to plan before acting.

Use this as a checklist when building a tool-using coding agent on top of your preferred stack and LLM API.

Want a detailed step-by-step tutorial? Download my guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Learn to build AI agents and apply new knowledge to create 8+ projects from scratch on the AI Engineering Buildcamp.

Register here:
