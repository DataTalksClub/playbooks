# Slack Module Interaction Nudge Template

Use this after the module announcement has already reached Slack from Telegram automation. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

Do not duplicate the announcement. Slack has a different job: get learners to reply, compare progress, share blockers, and help each other. Keep the post short, ask one concrete question, and tell people to reply in the thread.

## Template

Module {{ module_number }} discussion thread:

{{ interaction_question }}

Reply in this thread with:

- {{ reply_field_1 }}:
- {{ reply_field_2 }}:
- {{ reply_field_3 }}:

Short answers are useful. If you are stuck, include the exact command, error, screenshot, repo link, or example you are looking at.

Helpful link:
{{ primary_help_link }}

## Blocker Check-In

Module {{ module_number }} blocker check:

What is the first thing blocking you right now?

Reply in this thread with:

- Area:
- What you tried:
- Error or unclear part:
- Link, screenshot, or command:

If you can help someone else, reply to their message in the thread.

## Show-Your-Work Prompt

Module {{ module_number }} progress thread:

Share one thing you built, fixed, tested, or understood this week.

Reply in this thread with:

- What I worked on:
- What changed:
- Link or screenshot:
- What I want feedback on:

Small updates are good. A half-working project with a clear question is easier to help with than a silent project.

## Tool Or Concept Comparison Prompt

Module {{ module_number }} comparison thread:

{{ comparison_question }}

Reply in this thread with:

- Tool, concept, or approach:
- Task:
- What worked:
- What failed or needed review:

Please keep it concrete. "It worked well" is less useful than "it generated the API route, but the tests failed until I fixed the schema".

## End-Of-Week Check-In

Weekly check-in:

What did you finish this week, and what is still unclear?

Reply in this thread with:

- Finished:
- Stuck on:
- Next step:

If you are behind, that is fine. A clear next step is more useful than trying to catch up on everything at once.

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ module_number }}` | Module or week number. |
| `{{ interaction_question }}` | One discussion question tied to the module. |
| `{{ reply_field_1 }}` to `{{ reply_field_3 }}` | Structured reply fields. Use 3 to 4 fields at most. |
| `{{ primary_help_link }}` | One support link: FAQ, setup guide, homework, or project guide. |
| `{{ comparison_question }}` | Concrete comparison question for tools, concepts, techniques, or project choices. |

## Editing Rules

- Do not repeat the Telegram announcement.
- Ask one question per Slack post.
- Ask people to reply in the thread.
- Give a tiny reply format so answering feels easy.
- Prefer prompts that ask for artifacts: command, error, repo, screenshot, short result, or next step.
- Keep the post under 1200 characters when possible.
- Use one link, not a link list.
- Do not use Slack for broadcast-only copy if Telegram already sent the broadcast.
- Post blocker checks early in the week and progress/share prompts later in the week.
- When the channel is quiet, ask for the smallest possible reply.
