# Course Launch Event Description Template

Use this template for the live launch event that happens on the first day of a course cohort. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

The launch event should help learners start. It is not a sales page. The description should explain what the course is, what learners should do first, how the cohort works, and where to get help.

## Template

Webinar: {{ course_name }} {{ cohort_year }}, Course Launch
Title: {{ course_name }} {{ cohort_year }} Course Launch
Date: {{ launch_date }} - the day the course starts, {{ launch_time }} {{ timezone }} time.

The new cohort of [{{ course_name }} {{ cohort_year }}]({{ registration_url }}) starts today.

In this launch session, {{ speaker_name }} will help you start the cohort with a clear path through the course: what to do first, how the materials are organized, how the cohort works, and how to get help when you get stuck.

This course is not about {{ not_about_short }}. It is about {{ course_core_promise }}.

## What We'll Cover

{{ speaker_first_name }} will walk through:

- The course outcome: {{ course_outcome }}
- The first week: {{ first_week_focus }}
- The cohort rhythm: {{ cohort_rhythm }}
- The course map: {{ course_map }}
- The support system: {{ support_system }}

There will also be time for live questions, so bring anything about {{ question_topics }}.

## Starting {{ course_short_name }}?

{{ course_short_name }} is {{ course_cost_and_format }} for {{ target_learners }} who want to {{ learner_goal }}.

It is about {{ practical_workflow_or_learning_path }}.

You should be comfortable with {{ prerequisite_1 }}, {{ prerequisite_2 }}, and {{ prerequisite_3 }}. You do not need {{ not_required_1 }}, {{ not_required_2 }}, or {{ not_required_3 }}.

The cohort starts on {{ launch_date }}. If you haven't joined yet, you can [register here]({{ registration_url }}).

## About the Speaker

{{ speaker_name }} is {{ speaker_one_line_role }}.

{{ speaker_credibility_paragraph }}

## Short Version

The new cohort of [{{ course_name }} {{ cohort_year }}]({{ registration_url }}) starts today.

Join {{ speaker_name }} for a live course launch session. We will cover what to do first, how the cohort works, what learners will build or practice, how deadlines and peer review work, and where to get help.

There will also be time for live questions about {{ question_topics }}.

If you haven't joined yet, you can [register here]({{ registration_url }}).

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ course_name }}` | Official course name, for example `Machine Learning Zoomcamp`. |
| `{{ course_short_name }}` | Short course name used conversationally, for example `ML Zoomcamp`. |
| `{{ course_cost_and_format }}` | Cost and format phrase built from `course.cost` and `course.format`. |
| `{{ cohort_year }}` | Cohort year, for example `2026`. |
| `{{ launch_date }}` | Human-readable date, for example `Monday, August 31, 2026`. |
| `{{ launch_time }}` | Event time range, for example `17:00-18:00`. |
| `{{ timezone }}` | Timezone label, for example `Europe/Madrid`. |
| `{{ registration_url }}` | Public registration link. |
| `{{ speaker_name }}` | Full speaker name. |
| `{{ speaker_first_name }}` | First name for the coverage bullets. |
| `{{ not_about_short }}` | One short exclusion, for example `collecting tools` or `watching disconnected tutorials`. |
| `{{ course_core_promise }}` | The practical course promise in one sentence. |
| `{{ course_outcome }}` | Main artifact, project, workflow, or skill path learners build toward. |
| `{{ first_week_focus }}` | What learners need to do in week one. |
| `{{ cohort_rhythm }}` | Live cohort mechanics: lectures, homework, deadlines, scoring, leaderboard, peer review, certificates. |
| `{{ course_map }}` | Main topics/modules/tools in the course. |
| `{{ support_system }}` | Support channels and help resources. |
| `{{ question_topics }}` | Comma-separated topics learners may ask about. |
| `{{ target_learners }}` | Intended audience. |
| `{{ learner_goal }}` | What learners want to learn or become able to do. |
| `{{ practical_workflow_or_learning_path }}` | Concrete description of the course path. |
| `{{ prerequisite_1 }}` to `{{ prerequisite_3 }}` | Honest starting requirements. |
| `{{ not_required_1 }}` to `{{ not_required_3 }}` | Things learners do not need before joining. |
| `{{ speaker_one_line_role }}` | Short source-backed role line from the course instructor data. |
| `{{ speaker_credibility_paragraph }}` | Speaker background, kept to one paragraph. |

## Editing Rules

- Keep the event focused on starting the cohort, not re-selling the whole course.
- Put the first-week path and support system in the description.
- Keep 5 bullets in "What We'll Cover".
- Make the bullets parallel enough to scan, but not robotic.
- Keep prerequisites honest and specific.
- Do not promise jobs, promotions, certificates without requirements, or guaranteed outcomes.
- Do not use hype language such as "master", "transform", "unlock", or "10x".
- Replace placeholders before publishing.
