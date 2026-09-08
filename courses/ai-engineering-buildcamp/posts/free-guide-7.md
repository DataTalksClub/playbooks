---
platform: x
date: 2026-02-18
url: "https://x.com/Al_Grigor/status/2024031163095130324"
media: "image"
analytics:
  likes: 26
  reposts: 3
  comments: 1
  impressions: 815
  engagements: 74
  detail_expands: 19
  profile_visits: 2
---

Free 25+ pages guide on building your own coding agent with Python, Jupyter, and Django

What it covers:

1. Decide: chatbot or agent

- Chatbot: text in -> text out
- Agent: loops with tool calls + stateful history

2. Define tool schemas

- Start with concrete functions: read_file, write_file, see_file_tree, execute_bash_command.
- Describe them using JSON schema (name, description, parameters).

3. Implement the tool loop

- Send messages + tools -> model.
- If it returns function_call, dispatch to Python.
- Append function_call + function_call_output back into the history.

4. Add project-editing tools

- Bind tools to a project_dir (sandbox).
- Block dangerous commands (e.g., runserver).
- Skip .venv, __pycache__, node_modules.

5. Scaffold a template repo

- Clone a minimal Django template.
- Copy it per project, then let the agent refactor and extend it.

6. Write a real system prompt

- Explain the stack, file tree, and constraints.
- Tell the model to plan first, then call tools to execute.

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

This guide is a preview of what we do during the AI Engineering Buildcamp.

During the course, you'll learn to build AI agents and apply new knowledge to create 8+ projects from scratch.

Read the details here: https://maven.com/alexey-grigorev/from-rag-to-agents
