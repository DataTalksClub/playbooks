# First Week Nudges

Use these during the first week, after the Telegram start/module announcements have already been posted.

## Setup Check-In

How is the setup going?

If you already started Module 1, reply in this thread with one of these:

- Setup done.
- I am blocked on environment setup.
- I can run the examples, but I do not understand part of the workflow yet.
- I have not started yet.

If you are blocked, include your OS, the command you ran, and the error message. Screenshots are fine, but text logs are easier to search.

Environment setup:
https://datatalks.club/docs/courses/ai-dev-tools-zoomcamp/environment-setup/

## First Workflow Design Prompt

Module 1 starts before implementation: make the work explicit enough that an agent can execute it and another agent can verify it.

What did you define before asking a coding agent to implement anything?

Useful details to share:

- The product requirement or user problem.
- The technology stack and why you can review it.
- One focused backlog task and its acceptance criteria.
- Important constraints or boundaries.
- Context you added to `AGENTS.md` or another project document.
- How independent QA will decide whether the task passes.

Reply with one decision that made the task clearer or easier to verify.

## Getting Unstuck Prompt

If an implementation almost works, define the condition that is still failing before starting another agent run.

Try this loop:

1. Write the checkable condition the task must satisfy.
2. Run the relevant app, test, or verification command.
3. Capture the evidence for what failed.
4. Return the focused task to implementation with that evidence.
5. Repeat until the condition passes or a human decision is needed.
6. Run independent QA against the original acceptance criteria.
7. Review the result before accepting or committing it.

If you are stuck in this loop, post the command, error, and what changed between attempts.

## Homework Start Nudge

For Homework 1, start small.

The goal is not to create a perfect app on the first try. The goal is to practice the workflow:

- Write the requirement and acceptance criteria.
- Break the work into focused backlog tasks.
- Give the agent the required project context.
- Implement one task at a time.
- Verify the result independently against the acceptance criteria.
- Return failed tasks to implementation with concrete evidence.
- Review and document what you accepted.

If you want feedback, share your repo and the part you want someone to look at.

## Quiet Channel Nudge

Quick check:

What was the first thing that confused you in Module 1?

It can be a requirement, backlog task, acceptance criterion, agent role, piece of context, QA check, setup step, or command. Short answers are useful. If several people mention the same thing, we can clarify it for everyone.
