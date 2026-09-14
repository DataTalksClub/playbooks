# Transcript Post Ideas

Source: How to Work with AI Coding Agents: Spec-Driven Development, Context and Loop Engineering, Workflows

## 1. One-Shot Prompting Makes The Agent Decide Your Product

Priority: 5/5
Platform fit: LinkedIn strong, X strong
Confidence: high

Post angle:
A short prompt like "implement a weekly feedback tool" gives the agent too much room. It will choose the product shape, stack, interface, and scope. In the demo, the one-shot version produced a working CLI, but not the retrospective workflow Alexey actually wanted.

Why it is worth posting:
This is a clear, practical correction to vague "AI can build apps" advice. The lesson is not that agents are bad. The lesson is that underspecified prompts push product decisions into the model.

Source moments:
- 00:16:34 - 00:17:38: Alexey explains that a vague one-shot prompt makes the agent fill gaps and choose assumptions.
- 00:30:18 - 00:31:36: The one-shot result is a different app: a CLI for weekly project health, not the intended team retrospective tool.

Clip recommendation:
Use 00:16:34 - 00:17:38.

Clip reason:
This segment explains the problem crisply and stands alone without needing the demo UI.

Writing brief:
Write a LinkedIn/X post for engineers explaining why one-shot coding-agent prompts often produce the wrong product, even when the code works. Emphasize specification before implementation.

## 2. Specification Starts As A Conversation

Priority: 5/5
Platform fit: LinkedIn strong, X good
Confidence: high

Post angle:
Alexey uses a chat assistant before opening the coding agent. The job is not code generation. It is scoping: ask one question at a time, keep output short, decide who the users are, what workflow matters, what is anonymous, when feedback is revealed, and what is out of scope.

Why it is worth posting:
Many practitioners jump directly into the coding agent. This post shows a repeatable front-end to the process: turn a vague idea into a project-level spec before writing code.

Source moments:
- 00:18:01 - 00:20:20: Alexey prompts ChatGPT to help scope the project, ask one question at a time, and keep output short.
- 00:20:22 - 00:29:59: The vague idea is turned into an MVP with feedback cycles, anonymity, voting, action items, roles, screens, and exclusions.

Clip recommendation:
Use 00:19:06 - 00:20:20.

Clip reason:
The excerpt shows the exact scoping prompt and the "one question at a time" interaction pattern.

Writing brief:
Write a post explaining how to use a chat assistant as a scoping partner before coding. Include the one-question-at-a-time pattern and why it prevents walls of text.

## 3. Technology Choice Is Architecture Work

Priority: 4/5
Platform fit: LinkedIn strong, X good
Confidence: high

Post angle:
After the product spec, Alexey asks the coding agent for multiple stack options, then challenges them. He chooses Django mostly because he can read and maintain it quickly. The lesson: even with agents, the architect still owns trade-offs, familiarity, hosting constraints, background jobs, APIs, and dependency choices.

Why it is worth posting:
This is a useful counterweight to "just let the agent pick the stack." Agents can propose options, but humans still need to decide what they can operate.

Source moments:
- 00:35:42 - 00:41:15: Alexey separates conceptual scoping from technical stack selection and chooses Django because he knows it well.
- 00:43:01 - 00:46:40: He descopes architecture choices and recommends challenging every line of the technology decision.

Clip recommendation:
Use 00:39:45 - 00:41:15.

Clip reason:
This excerpt has the clearest practical decision: choose a stack you can read, review, and maintain.

Writing brief:
Write a post about the human architect role in AI-assisted development. Focus on trade-offs, familiarity, and challenging agent-suggested stack choices.

## 4. Context Engineering Is Mostly Documentation Discipline

Priority: 5/5
Platform fit: LinkedIn strong, X strong
Confidence: high

Post angle:
Context engineering for coding agents is not mystical. In the demo, it is mostly AGENTS.md, process.md, role files, and pointers to focused docs. The goal is to stop every new session from rediscovering project rules, commands, tools, and workflows.

Why it is worth posting:
This is a concrete version of a buzzword. Alexey's audience can copy the pattern immediately: a small root context file plus task-specific docs.

Source moments:
- 01:00:35 - 01:05:59: Alexey explains that each new session needs project context and introduces AGENTS.md / CLAUDE.md.
- 01:07:35 - 01:12:16: He trims AGENTS.md and explains linking to process/testing/UI docs instead of dumping everything into one file.

Clip recommendation:
Use 01:02:26 - 01:03:45.

Clip reason:
This segment defines context engineering in practical coding-agent terms.

Writing brief:
Write a post explaining context engineering as repo documentation discipline. Mention AGENTS.md, process.md, and routing agents to focused docs only when needed.

## 5. Feature Specs Need Acceptance Criteria And Out-Of-Scope Items

Priority: 5/5
Platform fit: LinkedIn strong, X strong
Confidence: high

Post angle:
Project-level specs are not enough. Each feature needs grooming: a goal, concrete acceptance criteria, and explicit out-of-scope items. The acceptance criteria should be checkable: someone should be able to point at the screen and say yes or no.

Why it is worth posting:
This maps product management practice directly onto coding-agent work. It reduces ambiguity before the implementation agent starts.

Source moments:
- 01:12:29 - 01:14:09: Alexey explains why vague GitHub issues still leave too much room for assumptions.
- 01:16:27 - 01:18:05: He creates a PM role and emphasizes checkable acceptance criteria.
- 01:21:50 - 01:23:56: A groomed authentication issue shows concrete criteria and out-of-scope items.

Clip recommendation:
Use 01:16:27 - 01:18:05.

Clip reason:
This gives a clean explanation of the PM/grooming role and why acceptance criteria matter.

Writing brief:
Write a post about feature-level specifications for coding agents. Use the PM/grooming analogy and emphasize checkable acceptance criteria plus out-of-scope sections.

## 6. PM, Engineer, QA Is A Practical Agent Workflow

Priority: 5/5
Platform fit: LinkedIn strong, X strong
Confidence: high

Post angle:
Alexey turns the coding process into a small workflow graph: PM grooms the issue, engineer implements it, QA checks acceptance criteria, and failed work loops back to the engineer. The orchestrator launches these roles instead of doing everything in one session.

Why it is worth posting:
This makes "loop engineering" and "graph engineering" concrete. It also explains why quality improves but token usage increases.

Source moments:
- 01:27:15 - 01:30:15: Alexey explains goals/loops as a way to keep an agent working through a pile of issues.
- 01:35:29 - 01:41:46: He defines PM, engineer, QA, and the workflow graph with pass/fail looping.
- 01:52:37 - 01:53:30: He notes the quality/token trade-off of using PM, implementation, and testing roles.

Clip recommendation:
Use 01:37:27 - 01:39:11.

Clip reason:
This segment explains the PM-engineer-QA graph and pass/fail loop clearly.

Writing brief:
Write a post explaining agent workflows as a PM-engineer-QA loop. Mention acceptance criteria, QA verdicts, failed work looping back, and the token-versus-quality trade-off.
