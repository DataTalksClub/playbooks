---
platform: x
---

The difference between a chatbot and an agent comes down to one thing: function calling.

A chatbot generates text based on its training. It can't take actions.

An agent can invoke tools to perform actions and bring results back into the conversation.

Here's a simple example:

-> Without function calling:
You ask: "Tell me a joke about Alexey"
The model generates a joke directly from its training.

-> With function calling:
You ask: "Tell me a joke"
The model sees it has access to a make_joke(name) function.
It asks: "What's your name?"
You reply: "Alexey"
The model calls make_joke("Alexey")
Your system executes the function and returns the result.
The model presents the joke to you.

The LLM never executes code directly. It proposes calls; your system runs them.

This is what transforms a chatbot into an agent.

For a coding agent, the tools become more powerful:

- read_file() to inspect code
- write_file() to modify projects
- execute_bash_command() to run tests
- see_file_tree() to understand structure

I recently published a guide on building your own coding agent that creates Django apps from a single prompt.

It covers:

- Function calling mechanics
- Tool schemas and descriptions
- System prompt engineering
- Complete implementation

Read it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents
