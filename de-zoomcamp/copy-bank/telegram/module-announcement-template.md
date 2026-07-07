AI Dev Tools Zoomcamp: Module {{ module_number }} starts

This week we start Module {{ module_number }}: {{ module_title }}.

{{ module_short_description }}

In this module, you will:

- {{ module_highlight_1 }}
- {{ module_highlight_2 }}
- {{ module_highlight_3 }}
- {{ module_highlight_4 }}
- {{ module_highlight_5 }}

Materials:
{{ module_url }}

Course platform:
{{ course_platform_url }}

Course playlist:
https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43

{{#if homework_available}}
Homework {{ homework_number }}:
{{ homework_url }}

Submission form:
{{ homework_submission_url }}

Deadline:
{{ homework_deadline }}

Submission forms close automatically after the deadline.
{{/if}}

{{#unless homework_available}}
There is no graded homework documented for this module in the course notes we have.

Use this week to go through the materials, run the examples, and keep moving on your final project.

If this cohort adds homework for this module:
{{ homework_submission_url }}

Deadline, if added:
{{ homework_deadline }}
{{/unless}}

Questions:
Ask in the course-ai-dev-tools-zoomcamp Slack channel.

Slack:
https://datatalks.club/slack.html

FAQ:
https://datatalks.club/faq/ai-dev-tools-zoomcamp.html

Remember: the goal is not to blindly accept generated code. Read it, run it, debug it, test it, and document what you did.
