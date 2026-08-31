# Telegram Pinned Message Template

Use this template for the pinned "start here" message in a course Telegram announcement channel. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

The pinned message should orient learners quickly. It should make clear that Telegram is for announcements, move support questions to Slack, and collect the most important course links in one place.

## Template

START HERE

Welcome to the {{ course_name }} Telegram channel.

The next live cohort starts on {{ cohort_start_date }}.

Register here:
{{ registration_url }}

{{ course_name }} is {{ course_cost_and_format }} about {{ course_topic }}.

The focus is {{ course_focus }}:

- {{ focus_point_1 }}
- {{ focus_point_2 }}
- {{ focus_point_3 }}
- {{ focus_point_4 }}
- {{ focus_point_5 }}

1. This channel is for announcements only.

We do not regularly check it for questions.

2. For questions, homework discussions, and troubleshooting, use Slack.

Join the {{ community_name }} workspace:
{{ slack_invite_url }}

After joining Slack, join the course channel:
{{ slack_channel_name }}
{{ slack_channel_url }}

If the Slack invite does not work, use this form:
{{ slack_invite_request_url }}

3. Start here:

Course platform:
{{ course_platform_url }}

Environment setup:
{{ environment_setup_url }}

GitHub repository:
{{ github_url }}

Course documentation:
{{ documentation_url }}

Course playlist:
{{ youtube_playlist_url }}

FAQ:
{{ faq_url }}

4. How the live cohort works:

Lectures are pre-recorded, so you can watch them when it works for you.

The live cohort adds {{ live_cohort_mechanic_1 }}, {{ live_cohort_mechanic_2 }}, {{ live_cohort_mechanic_3 }}, {{ live_cohort_mechanic_4 }}, and {{ certificate_or_completion_path }}.

The final goal is {{ final_project_or_course_output }}.

5. Homework:

Homework submissions are available only during the live cohort. Each homework has a fixed deadline.

In self-paced mode, you can still complete the homework for practice, but it does not count toward live-cohort scoring.

6. Certificate:

To get a certificate, you need to {{ certificate_requirement_1 }} and {{ certificate_requirement_2 }}.

{{ certificate_homework_note }}

Certificate information:
{{ certificate_url }}

Final project:
{{ final_project_url }}

7. Rules:

How to ask questions:
{{ question_guidelines_url }}

Community guidelines:
{{ community_guidelines_url }}

## Compact Version

START HERE

Welcome to the {{ course_name }} Telegram channel.

The next live cohort starts on {{ cohort_start_date }}.

Register here:
{{ registration_url }}

{{ course_name }} is {{ course_cost_and_format }} about {{ course_topic }}.

This channel is for announcements only. For questions, homework discussions, and troubleshooting, use Slack:
{{ slack_invite_url }}

After joining Slack, join the course channel:
{{ slack_channel_name }}
{{ slack_channel_url }}

Start here:

- Course platform: {{ course_platform_url }}
- Environment setup: {{ environment_setup_url }}
- GitHub repository: {{ github_url }}
- Course documentation: {{ documentation_url }}
- Course playlist: {{ youtube_playlist_url }}
- FAQ: {{ faq_url }}

Live cohort:

- Lectures are pre-recorded.
- The cohort adds deadlines, homework, peer review, community support, and certificate eligibility.
- Homework submissions are available only during the live cohort.
- Certificate requirements: {{ certificate_summary }}

Rules:

- How to ask questions: {{ question_guidelines_url }}
- Community guidelines: {{ community_guidelines_url }}

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ course_name }}` | Official course name. |
| `{{ cohort_start_date }}` | Human-readable start date, for example `August 31, 2026`. |
| `{{ registration_url }}` | Public registration link. |
| `{{ course_topic }}` | Plain description of what the course teaches. |
| `{{ course_cost_and_format }}` | Cost and format phrase built from `course.cost` and `course.format`. |
| `{{ course_focus }}` | Main practical focus of the course. |
| `{{ focus_point_1 }}` to `{{ focus_point_5 }}` | Short concrete focus bullets. Add or remove bullets as needed. |
| `{{ slack_invite_url }}` | Community workspace invite URL from `urls.slack_invite`. |
| `{{ community_name }}` | Community or workspace name. |
| `{{ slack_channel_name }}` | Course Slack channel name. |
| `{{ slack_channel_url }}` | Direct course Slack channel URL. |
| `{{ slack_invite_request_url }}` | Backup Slack invite request form. |
| `{{ course_platform_url }}` | Cohort platform URL. |
| `{{ environment_setup_url }}` | Setup guide URL. |
| `{{ github_url }}` | Course GitHub repository. |
| `{{ documentation_url }}` | Course documentation root. |
| `{{ youtube_playlist_url }}` | Course playlist URL. |
| `{{ faq_url }}` | Course FAQ URL. |
| `{{ live_cohort_mechanic_1 }}` to `{{ live_cohort_mechanic_4 }}` | Cohort mechanics such as deadlines, homework, leaderboard, peer review, or support. |
| `{{ certificate_or_completion_path }}` | Certificate eligibility or completion requirement. |
| `{{ final_project_or_course_output }}` | Main project, portfolio artifact, or learner output. |
| `{{ certificate_requirement_1 }}` | First certificate requirement. |
| `{{ certificate_requirement_2 }}` | Second certificate requirement. |
| `{{ certificate_homework_note }}` | Note about whether homework affects certificate eligibility. |
| `{{ certificate_url }}` | Certificate information URL. |
| `{{ final_project_url }}` | Final project information URL. |
| `{{ certificate_summary }}` | One-line certificate requirement summary for the compact version. |
| `{{ question_guidelines_url }}` | How to ask questions guide. |
| `{{ community_guidelines_url }}` | Community guidelines URL. |

## Editing Rules

- Keep the pinned message practical and link-heavy.
- Make it clear that Telegram is for announcements only.
- Send all questions to Slack.
- Put the registration link and start date near the top.
- Keep setup links visible and easy to copy.
- Keep certificate rules specific.
- Do not promise certificates without requirements.
- Do not use hype language.
- Replace placeholders before publishing.
