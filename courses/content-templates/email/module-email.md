# Module Email Template

Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`. Use campaign sources for cohort dates and deadlines.

## Template

[View this email in your browser]({{ browser_view_url }})

# {{ module_email_headline }}

Hey there,

This week, we {{ module_action }} [Module {{ module_number }}: {{ module_title }}]({{ module_url }}).

{{ module_intro_paragraph }}

## Module {{ module_number }}

In this module, you will:

- {{ module_highlight_1 }}
- {{ module_highlight_2 }}
- {{ module_highlight_3 }}
- {{ module_highlight_4 }}
- {{ module_highlight_5 }}

Important links:

- [Module {{ module_number }} materials]({{ module_url }})
- [Course playlist]({{ youtube_playlist_url }})
- [Course platform]({{ course_platform_url }})
{{ optional_homework_link }}
{{ optional_submission_link }}

{{ optional_deadline_line }}
{{ optional_submission_closes_line }}

[Start Module {{ module_number }}]({{ module_url }})

## Where to Find Materials

All course materials live in the [GitHub repository]({{ github_url }}).

{{ module_materials_structure }}

{{ delivery_and_updates_summary }}

## Self-Paced vs. Live Cohort

{{ self_paced_summary }}

{{ live_cohort_summary }}

{{ live_cohort_participation_requirement }}

## Homework {{ module_number }}

{{#if homework_available}}
For [Homework {{ homework_number }}]({{ homework_url }}), you will {{ homework_summary }}.

{{ homework_working_principle }}

Due date: {{ homework_deadline }}.

[Submit Homework {{ homework_number }}]({{ homework_submission_url }})

### How Homework Works

For homework, you are expected to:

- {{ homework_expectation_1 }}
- {{ homework_expectation_2 }}
- {{ homework_expectation_3 }}
- {{ homework_expectation_4 }}

{{ homework_deadline_policy }}

{{ self_paced_homework_note }}

Submissions also appear on the [leaderboard]({{ leaderboard_url }}).

{{ learning_in_public_line }}
{{/if}}

{{#unless homework_available}}
There is no graded homework for this module.

Use this week to go through the materials, run the examples, and keep moving on your final project. If you are following the live cohort, check the [course platform]({{ course_platform_url }}) for the next open submission.
{{/unless}}

{{#if homework_available}}
## Homework Grade

{{ homework_grading_summary }}

{{ learning_in_public_scoring_line }}

{{ faq_contribution_line }}

{{ optional_question_scoring_line }}

{{ certificate_homework_note }}
{{/if}}

## Got Stuck?

Having questions is a normal part of the learning process.

Here is what to do:

- Check the [course FAQ]({{ faq_url }}).
- Check the [course documentation]({{ documentation_url }}).
- Check the [how to ask questions guide]({{ question_guidelines_url }}).
- Ask your question in [{{ slack_channel_name }}]({{ slack_channel_url }}).

Please ask course-related questions in the course Slack channel, not in private messages. This helps other learners find the answer later.

[Join the community workspace]({{ slack_invite_url }})

## Pace and Deadlines

{{ pace_and_deadlines_summary }}

The full schedule, deadlines, homework forms, and leaderboard are available on the [course platform]({{ course_platform_url }}).

## Quick Links

- [Course repository]({{ github_url }})
- [Course playlist]({{ youtube_playlist_url }})
- [Course platform]({{ course_platform_url }})
- [Course documentation]({{ documentation_url }})
- [FAQ]({{ faq_url }})
- [Community workspace]({{ slack_invite_url }})
- [Announcements]({{ announcement_channel_url }})

## Keep Going

This is Module {{ module_number }} of {{ total_modules }}. Completing the module brings you one step closer to the final project.

It is okay if you do not get everything right away. Most students do not.

{{ closing_encouragement }}

Good luck!

{{ sender_name }}

## Required Source Groups

Resolve the placeholders from these source groups before publishing:

- `course.*`: course name and positioning.
- `urls.*`: every destination link.
- `delivery.*`: homework, submissions, live sessions, and certificate behavior.
- `cohort_cadence.*`: pace and cohort timing.
- `community.*`: support channels and learning-in-public rules.
- `modules`, `projects`, and `outcomes`: module-specific learning content.
- Campaign sources: confirmed module dates, deadlines, and submission links.
