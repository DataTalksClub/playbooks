---
platform: x
---

Every coding agent needs these 5 tools:

1. read_file(filepath)

Lets the agent inspect existing code before making changes.

Without this, the agent is blind to the current state of your project.

2. write_file(filepath, content)

Creates or modifies files in the project.

This is how the agent makes actual changes to your codebase.

3. see_file_tree(folder)

Shows the project structure: directories, files, and their organization.

The agent uses this to understand where to create new files and how the project is laid out.

4. execute_bash_command(command)

Runs shell commands: tests, migrations, package installations, or any terminal operation.

The agent can verify its changes work correctly.

5. search_in_files(pattern)

Finds specific code or references across multiple files.

Critical for understanding how different parts of the codebase connect.

With these 5 functions, an agent can:
- Analyze your project
- Create new features
- Modify existing code
- Run tests
- Fix bugs
- Deliver working applications

I built a coding agent that creates Django apps from a single prompt using exactly these tools.

Cost: less than $1 per project with gpt-4o-mini.

The complete implementation is in my new guide: https://maven.com/alexey-grigorev/o/0a9e5c

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents
