---
platform: x
---

How function calling works in 4 steps:

1. You define tools with schemas

You describe each function: name, purpose, parameters, and types.

The LLM uses these schemas to decide which tool to call and how.

2. The LLM proposes tool calls

When the model needs to act, it returns a function call request with arguments.

It never executes code directly. It proposes: "I want to call write_file with these arguments."

3. Your system executes the function

You run the function in your code, capture the output (success, error, file content), and send results back to the LLM.

This is where the actual action happens.

4. The LLM integrates the results

The model processes the output and continues the conversation.

It can chain additional tool calls or present the final result to the user.

This loop continues until the task is complete.

For coding agents, this means:

- Reading existing code
- Modifying files
- Running tests
- Checking results
- Making adjustments

The LLM orchestrates it, and your system executes it.

I wrote a complete guide on building a coding agent that creates Django apps using function calling.

Get it here: https://maven.com/alexey-grigorev/o/0a9e5c

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents
