# Curriculum and Outcomes

## Course summary

AI Dev Tools Zoomcamp is a free hands-on course about using AI coding tools in real software development workflows.

The course is not about training models or building RAG applications. It is about the new day-to-day of software work: using chat tools, coding assistants, AI IDEs, coding agents, MCP, tests, CI/CD, deployment, and automation without giving up engineering discipline.

Learners finish with a complete deployed application and a clearer workflow for using AI tools to plan, build, review, test, and ship code.

## Modules

### Module 1: Introduction to Vibe Coding / AI Tools Overview

What learners study:

- The landscape of AI-assisted software development tools
- Chat-based tools, coding assistants, AI IDEs, project bootstrappers, and agents
- How different tools behave when asked to build the same simple app
- Where AI-generated code helps and where it creates risk

What learners practice:

- Building a Snake game with different AI tools
- Comparing outputs from tools like ChatGPT, Claude, Claude Code, GitHub Copilot, Cursor, Bolt, Lovable, and similar assistants
- Reading, reviewing, and debugging generated code
- Thinking critically about tool choice instead of chasing every new product

Marketing angle:

This module gives learners a grounded map of the AI coding tool space. It turns "vibe coding" from a vague trend into something they can test, compare, and use with judgment.

### Module 2: End-to-End Project (Snake)

What learners study:

- How to use AI tools across a full application workflow
- Frontend/backend collaboration through OpenAPI specs
- How AGENTS.md and repo instructions guide coding agents
- Testing, database integration, containerization, deployment, and CI/CD

What learners practice:

- Building a frontend with Lovable, React, and tests
- Generating and using OpenAPI specs from frontend needs
- Creating a FastAPI backend that follows the API contract
- Adding SQLAlchemy, SQLite or Postgres, unit tests, integration tests, Docker Compose, Render deployment, and GitHub Actions

Marketing angle:

This is the "AI tools in the real world" module. Learners see how AI can help across the whole lifecycle, not just produce isolated snippets.

### Module 3: Model Context Protocol

What learners study:

- MCP clients, servers, tools, resources, and prompts
- Stdio and HTTPS communication modes
- How AI tools connect to external context and actions
- Local vs remote MCP servers, security, and permissions

What learners practice:

- Running a Python MCP server
- Calling MCP tools with JSON-RPC
- Using MCP Inspector
- Configuring MCP clients in VS Code, Codex, Cursor, Antigravity, and similar tools
- Trying workflows such as repo triage, PR summaries, scripted edits, data queries, and publishing posts

Marketing angle:

MCP is becoming one of the key pieces of AI developer tooling. This module helps learners understand it by building and using it, not just reading about it.

### Module 4: Build an AI Coding Agent (Django)

What learners study:

- How coding agents are structured
- OpenAI Responses API and function calling
- Tool definitions for file reading, file writing, command execution, search, and file-tree inspection
- How developer prompts guide an agent inside a real codebase

What learners practice:

- Building a coding agent that scaffolds and extends projects
- Using a Django template as the base project
- Running an agent with ToyAIKit
- Exploring OpenAI Agents SDK, PydanticAI, and Z.ai as alternative agent frameworks
- Creating and modifying a Django app through an agent workflow

Marketing angle:

This module goes behind the curtain. Learners stop treating coding agents as magic and start understanding how they are built, constrained, and evaluated.

### Module 5: AI for Testing, CI/CD and DevOps

What learners study:

- AI-assisted PR reviews and summaries
- Change-risk hints and automated test generation
- Coverage gates, LLM evals, regression checks, and release automation
- Secure AI usage around secrets, data redaction, OSS policy, artifact retention, and audit

What learners practice:

- Creating CI workflows that use AI for PR summaries and test suggestions
- Adding regression checks and coverage expectations
- Drafting release notes and changelogs
- Thinking through deployment runbooks, incident postmortems, and on-call copilots

Marketing angle:

This module connects AI tools to engineering quality. The message is not "let AI write everything"; it is "use AI to make review, testing, delivery, and operations more reliable."

### Module 6: Automation with Low-Code and No-Code AI (n8n)

What learners study:

- Where low-code and no-code automation fit in a developer workflow
- How n8n can connect tools, content, data, and AI steps
- Practical automation patterns for technical and career workflows

What learners practice:

- Installing n8n
- Building AI-powered workflows
- Creating LinkedIn posts
- Tailoring a CV for a specific position

Marketing angle:

This module shows that AI development is not only code inside an IDE. Some useful workflows are better expressed as automations that connect existing tools.

## Tools and technologies

Canonical list is in `course.yaml`.

Use this section to explain why these tools matter.

The tools in the course fall into a few practical groups:

- AI assistants and coding agents: ChatGPT, Claude, Gemini, DeepSeek, Claude Code, GitHub Copilot, Cursor, OpenAI Codex, Gemini CLI, Antigravity, and related tools help learners explore, generate, edit, and review code.
- App-building tools: Lovable, Bolt, React, TypeScript, JavaScript, FastAPI, Python, SQLAlchemy, SQLite, Postgres, and Django give learners realistic frontend/backend surfaces to practice on.
- Agent and context tooling: Model Context Protocol, MCP Inspector, Context7, OpenAI Responses API, ToyAIKit, OpenAI Agents SDK, and PydanticAI help learners understand how AI tools connect to files, APIs, docs, and actions.
- Engineering workflow tools: GitHub Codespaces, GitHub CLI, GitHub Actions, Docker, Docker Compose, Render, PR Agent, and CodeRabbit connect AI-assisted coding to review, testing, deployment, and delivery.
- Automation tools: n8n, Hashnode, Notion, and similar workflow tools show how AI can support non-IDE tasks such as content, documentation, and career workflows.

The tool list is intentionally broad because the course is about learning how to evaluate and use AI developer tools, not memorizing one vendor-specific workflow.

## Homework

In the 2025 cohort, there were 3 graded homework assignments. They were designed as small but realistic builds: each one asks learners to use AI tools, inspect the result, iterate when things fail, and submit working code in GitHub.

The homework reinforces the main behavior the course wants to teach: do not just accept generated code. Learners should inspect it, test it, improve it, document it, and make it reproducible.

### Homework 1: Introduction to AI-Assisted Development

Learners build a Django TODO application with AI assistance. The app supports creating, editing, and deleting TODOs, assigning due dates, and marking tasks as resolved.

What learners practice:

- Asking an AI assistant to install Django and create a project/app
- Understanding where Django settings, models, views, templates, and tests live
- Running migrations
- Implementing app logic and templates
- Asking AI to generate tests, then running and fixing them
- Committing the work to GitHub

Why it matters:

This homework is deliberately approachable. Learners do not need to know Django before starting. The point is to practice using AI as a guide while still understanding each step enough to answer questions and debug the result.

### Homework 2: End-to-End Application Development

Learners build a real-time collaborative coding interview platform with AI assistance. The app lets users create a session link, share it with candidates, edit code together, see real-time updates, highlight syntax, and execute code safely in the browser.

What learners practice:

- Prompting AI to create a full frontend/backend application
- Optionally following the course workflow: frontend, OpenAPI specs, backend
- Writing integration tests for client/server interaction
- Creating a README with run and test commands
- Running frontend and backend together with `concurrently`
- Adding syntax highlighting for JavaScript and Python
- Running Python in the browser with WASM
- Containerizing the app
- Deploying the app and sharing a demo

Why it matters:

This homework turns AI-assisted coding into a real product workflow. Learners practice the messy middle: tests, client/server integration, local dev commands, containerization, deployment, and demoing the result.

### Homework 3: Model Context Protocol

Learners build their own MCP server, similar in spirit to Context7. The server can scrape web content, make documentation searchable, and expose tools to an AI assistant.

What learners practice:

- Creating a new Python project with `uv`
- Installing and running FastMCP
- Understanding MCP transport
- Building a tool that retrieves web pages through Jina Reader
- Integrating the MCP server with an AI assistant
- Downloading documentation from a GitHub repo
- Indexing Markdown/MDX files with `minsearch`
- Creating a search function and exposing it as an MCP tool

Why it matters:

This homework helps learners understand how AI assistants become more useful when connected to tools and context. They build a small documentation search engine and wire it into their own assistant workflow.

Homework is not required for the certificate, but it helps learners build the habits they need for the final project.

## Final project

The final project is a complete application of the learner's choice, built end to end with AI tools.

Expected project shape:

- A clear problem and expected system functionality
- A frontend
- A backend
- An OpenAPI spec or equivalent contract between frontend and backend
- A database or persistent storage
- Unit and/or integration tests
- Dockerfile or Docker Compose setup
- Public deployment or clear proof of deployment
- README with setup, run, test, and deployment instructions
- Documentation of how AI tools, prompts, workflows, AGENTS.md, or MCP were used

The project can use any tech stack. Python or Django are not required. Optional additions include an ML component, an MCP server, or CI/CD deployment automation.

## Portfolio outcome

The portfolio outcome is a complete deployed application that shows a learner can use AI tools responsibly across a real development workflow.

Strong portfolio projects should demonstrate:

- Product thinking: the app solves a clear problem
- Architecture: frontend, backend, API contract, and persistence make sense together
- AI workflow: the learner can explain which tools were used and why
- Engineering quality: tests, containers, CI/CD, and documentation are present
- Reproducibility: another person can run, review, and evaluate the project

This is the main promise of the course: learners do not just say they "used AI to code." They can show a working application and explain the engineering workflow behind it.

## Certificate path

Certificate is available during a live cohort.

To earn it, learners need to:

- Pass the final project
- Complete 3 peer reviews
- Meet the cohort deadlines and project requirements

Self-paced learners can use the materials and build the project for practice or portfolio work, but certificates are tied to live cohort participation.

## What learners can say after finishing

Examples:

- "I can use AI coding tools without blindly trusting generated code."
- "I can build a full-stack application with AI assistance and still keep the architecture understandable."
- "I can turn frontend needs into an OpenAPI contract and use it to build a backend."
- "I can guide coding agents with repo instructions, prompts, and review loops."
- "I can configure and use MCP tools to connect AI assistants to external context and actions."
- "I can add tests, CI checks, containers, and deployment to an AI-assisted project."
- "I can document how AI tools were used in a project so another engineer can review the work."
- "I can compare AI developer tools and choose a workflow based on the task, not hype."
