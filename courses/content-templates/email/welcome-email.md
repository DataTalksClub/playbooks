# Course Welcome Email Template

Use this email after a learner registers for a course cohort. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

The goal is to welcome the learner, confirm the start date, give them the first setup actions, and point them to the main support channels. Keep it practical. Do not turn the welcome email into a full course landing page.

## Ready-To-Use Template

# Welcome to {{ course_name }}

Hello!

Thank you for signing up for **{{ course_name }}**. The next live cohort starts on **{{ cohort_start_date }}**.

{{ course_name }} is {{ course_cost_and_format }} about {{ course_topic }}.

The focus is {{ course_focus }}. During the course, you will {{ learner_outcome }}.

## Before the course starts

Please do these three things first:

1. Join the {{ community_name }} workspace:
   [Join {{ community_name }}]({{ slack_invite_url }})

2. Join the course channel:
   [{{ slack_channel_name }}]({{ slack_channel_url }})

3. Open the course platform:
   [Course platform]({{ course_platform_url }})

Use {{ slack_channel_name }} for course questions, homework discussions, troubleshooting, and cohort announcements. Please keep course-related questions in the channel, so other learners can find the answers later.

If the Slack invite link does not work, use this form:
[Slack invite request form]({{ slack_invite_request_url }})

If you are new to Slack, start here:
[How to use Slack]({{ slack_guide_url }})

## What to expect

The lectures are pre-recorded, so you can watch them when it works for you.

The live cohort adds {{ live_cohort_mechanic_1 }}, {{ live_cohort_mechanic_2 }}, {{ live_cohort_mechanic_3 }}, {{ live_cohort_mechanic_4 }}, and {{ certificate_or_completion_path }}.

During the course, you will work toward {{ final_project_or_course_output }}.

The course covers:

- {{ topic_1 }}
- {{ topic_2 }}
- {{ topic_3 }}
- {{ topic_4 }}
- {{ topic_5 }}

## Start here

You can already open the main materials:

- [Course platform]({{ course_platform_url }})
- [Environment setup]({{ environment_setup_url }})
- [GitHub repository]({{ github_url }})
- [Course documentation]({{ documentation_url }})

Start with the course platform, then check the environment setup before the first homework.

## Live sessions

{{#if live_sessions_available}}
We will run live sessions around the course start:

- Pre-course Q&A: [{{ pre_course_qna_title }}]({{ pre_course_qna_url }})
- Launch stream: [{{ launch_stream_title }}]({{ launch_stream_url }})

We will use these sessions to explain how the course works, how to start, how homework and peer review work, and how to earn the certificate.
{{/if}}

{{#unless live_sessions_available}}
If we add Q&A sessions, launch streams, or updated recordings, we will announce them in Slack and the course announcement channel.
{{/unless}}

## Prerequisites

You do not need {{ not_required_1 }}, {{ not_required_2 }}, or {{ not_required_3 }}.

You should be comfortable with {{ prerequisite_1 }}, {{ prerequisite_2 }}, and {{ prerequisite_3 }}.

During the course, {{ tool_or_course_support_line }}, but you will still need to {{ learner_responsibility_line }}.

## Announcements

We also have a course announcement channel:

[{{ announcement_channel_label }}]({{ announcement_channel_url }})

If you do not use this channel, no problem. Important updates will also be shared in Slack.

## Spread the word

{{#if sharing_templates_available}}
If you want to share that you joined the course, you can use one of these templates.

LinkedIn:

```text
I have joined {{ course_name }} {{ cohort_year }} by {{ community_social_handle }}.

Over the course, I will learn {{ public_learning_outcome_1 }}, {{ public_learning_outcome_2 }}, and {{ public_learning_outcome_3 }}.

The course is {{ course_cost_and_format }}.

{{ sharing_credit_line }}

You can register here: {{ registration_url }}
```

X:

```text
Joined {{ course_name }} {{ cohort_year }} by {{ community_social_handle }}.

I will learn {{ short_public_learning_outcome_1 }}, {{ short_public_learning_outcome_2 }}, and {{ short_public_learning_outcome_3 }}.

Thanks @Al_Grigor and team.

{{ registration_url }}
```
{{/if}}

## Quick links

- [Course platform]({{ course_platform_url }})
- [Course repository]({{ github_url }})
- [Course playlist]({{ youtube_playlist_url }})
- [Course documentation]({{ documentation_url }})
- [FAQ]({{ faq_url }})
- [Slack]({{ slack_invite_url }})
- [Announcement channel]({{ announcement_channel_url }})

See you in Slack!

{{ sender_name }}

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ browser_view_url }}` | Optional hosted email preview URL. Remove the line if unavailable. |
| `{{ course_name }}` | Official course name. |
| `{{ cohort_year }}` | Cohort year, for example `2026`. |
| `{{ cohort_start_date }}` | Human-readable date, for example `August 31, 2026`. |
| `{{ course_topic }}` | Plain course description. |
| `{{ course_cost_and_format }}` | Cost and format phrase built from `course.cost` and `course.format`. |
| `{{ course_focus }}` | One or two sentences about the main course focus and exclusions. |
| `{{ learner_outcome }}` | What the learner will build, practice, or finish with. |
| `{{ slack_invite_url }}` | Community workspace invite URL from `urls.slack_invite`. |
| `{{ community_name }}` | Community or workspace name. |
| `{{ community_social_handle }}` | Social account learners should tag when sharing. |
| `{{ sharing_credit_line }}` | Optional source-backed credit line for instructors or organizers. |
| `{{ slack_invite_request_url }}` | Backup Slack invite request form. |
| `{{ slack_guide_url }}` | Beginner Slack guide URL. |
| `{{ slack_channel_name }}` | Course Slack channel name. |
| `{{ slack_channel_url }}` | Direct course Slack channel URL. |
| `{{ course_platform_url }}` | Cohort platform URL. |
| `{{ environment_setup_url }}` | Setup guide URL. |
| `{{ github_url }}` | Course GitHub repository. |
| `{{ documentation_url }}` | Course documentation root. |
| `{{ faq_url }}` | Course FAQ URL. |
| `{{ youtube_playlist_url }}` | Course playlist URL. |
| `{{ live_cohort_mechanic_1 }}` to `{{ live_cohort_mechanic_4 }}` | Cohort mechanics such as deadlines, homework, leaderboard, peer review, or support. |
| `{{ certificate_or_completion_path }}` | Certificate eligibility or completion requirement. |
| `{{ final_project_or_course_output }}` | The main project, portfolio artifact, or learner output. |
| `{{ topic_1 }}` to `{{ topic_5 }}` | Main topics covered by the course. |
| `{{ pre_course_qna_title }}` | Optional Q&A session title. |
| `{{ pre_course_qna_url }}` | Optional Q&A session URL. |
| `{{ launch_stream_title }}` | Optional launch stream title. |
| `{{ launch_stream_url }}` | Optional launch stream URL. |
| `{{ not_required_1 }}` to `{{ not_required_3 }}` | Things learners do not need before starting. |
| `{{ prerequisite_1 }}` to `{{ prerequisite_3 }}` | Required learner baseline. |
| `{{ tool_or_course_support_line }}` | Short explanation of how tools, materials, mentors, or the course support learners. |
| `{{ learner_responsibility_line }}` | What learners still need to do themselves. |
| `{{ announcement_channel_label }}` | Telegram or other announcement channel label. |
| `{{ announcement_channel_url }}` | Announcement channel URL. |
| `{{ registration_url }}` | Public registration URL. |
| `{{ public_learning_outcome_1 }}` to `{{ public_learning_outcome_3 }}` | Longer LinkedIn sharing outcomes. |
| `{{ short_public_learning_outcome_1 }}` to `{{ short_public_learning_outcome_3 }}` | Short X sharing outcomes. |
| `{{ sender_name }}` | Email sender or team signature. |

## Editing Rules

- Keep the email focused on onboarding, not selling the course again.
- Put the first three learner actions near the top.
- Keep Slack instructions specific, because private-message support does not scale.
- Keep the prerequisites honest.
- Use optional blocks for live sessions and sharing templates.
- Do not promise jobs, promotions, production expertise, or guaranteed productivity gains.
- Remove placeholder sections that do not apply before publishing.
