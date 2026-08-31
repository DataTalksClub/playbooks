# Telegram Module Announcement Template

Use this template for weekly module announcements in a course Telegram announcement channel. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

Telegram is a short-update platform. A module announcement should tell learners what changed this week and what to click next. Keep details in the linked course materials, not in the Telegram post.

Recommended length: 500-900 characters for the default version. Use the compact version for reminder posts.

## Template

{{ course_short_name }}: Module {{ module_number }} starts

This week: {{ module_title }}.

You will:

- {{ module_highlight_1 }}
- {{ module_highlight_2 }}
- {{ module_highlight_3 }}

Materials:
{{ module_url }}

Course platform:
{{ course_platform_url }}

{{#if homework_available}}
Homework {{ homework_number }}:
{{ homework_url }}

Submit:
{{ homework_submission_url }}

Deadline: {{ homework_deadline }}
{{/if}}

{{#unless homework_available}}
No graded homework this week. Use the module materials and keep working on {{ project_or_practice_focus }}.
{{/unless}}

Questions: ask in {{ slack_channel_name }} on Slack.
{{ slack_invite_url }}

FAQ:
{{ faq_url }}

## Compact Version

{{ course_short_name }}: Module {{ module_number }} starts

This week: {{ module_title }}.

Materials:
{{ module_url }}

{{#if homework_available}}
Homework: {{ homework_url }}
Submit: {{ homework_submission_url }}
Deadline: {{ homework_deadline }}
{{/if}}

Questions: {{ slack_channel_name }} on Slack
{{ slack_invite_url }}

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ course_short_name }}` | Short course name used in announcements. |
| `{{ module_number }}` | Module number or week number. |
| `{{ module_title }}` | Official module title. |
| `{{ module_short_description }}` | Optional one-sentence context. Usually omit for Telegram unless the title is unclear. |
| `{{ module_highlight_1 }}` to `{{ module_highlight_3 }}` | Concrete things learners will practice. Use 2 to 3 bullets. |
| `{{ module_url }}` | Module materials URL. |
| `{{ course_platform_url }}` | Course platform URL. |
| `{{ course_playlist_url }}` | Optional playlist URL. Include only when it is the primary action. |
| `{{ homework_available }}` | Boolean or template condition for whether graded homework exists. |
| `{{ homework_number }}` | Homework number. |
| `{{ homework_url }}` | Homework instructions URL. |
| `{{ homework_submission_url }}` | Submission form URL. |
| `{{ homework_deadline }}` | Human-readable deadline with timezone if relevant. |
| `{{ project_or_practice_focus }}` | What learners should keep working on if there is no homework. |
| `{{ slack_channel_name }}` | Course Slack channel name. |
| `{{ slack_invite_url }}` | Community workspace invite URL from `urls.slack_invite`. |
| `{{ faq_url }}` | Course FAQ URL. |
| `{{ course_working_principle }}` | Optional one-line reminder. Use only when there is room. |

## Editing Rules

- Keep the title to one line.
- Keep the default post under 900 characters when possible.
- Use 2 to 3 bullets, not 5.
- Keep links visible and on their own lines.
- Include only the links needed this week.
- Do not include the playlist unless it is the main place to watch the module.
- Start each highlight with a concrete action when possible.
- Keep homework details separate from general materials.
- Remove no-homework fallback text when homework exists.
- Remove homework fields when there is no homework.
- Send questions to Slack, not Telegram.
- Avoid long reminders. Link to the FAQ instead.
- Use silent posting for non-urgent reminders when appropriate.
- Replace placeholders before publishing.
