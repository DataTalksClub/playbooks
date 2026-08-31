# Pre-Course Live Q&A Event Description Template

Use this template for the live Q&A event that happens before a course cohort starts. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

The pre-course Q&A should help people decide whether to join and help registered learners prepare. It should answer fit, prerequisites, workload, course structure, project expectations, certificate path, and support questions.

## Template

Title: {{ course_name }} {{ cohort_year }} Pre-Course Live Q&A
Date: TBD - schedule around {{ recommended_timing }} before the confirmed {{ cohort_start_date }} course start date. Suggested time: {{ event_time }} {{ timezone }} time.

Thinking about joining [{{ course_name }} {{ cohort_year }}]({{ registration_url }})?

Come to this live Q&A with {{ speaker_name }} and get a clear picture of what the course is like before the cohort starts on {{ cohort_start_date }}.

Bring your questions about {{ question_topics }}, or whether the course is a good fit for you.

## What We'll Cover

{{ speaker_first_name }} will walk through:

- What you'll build or practice: {{ course_outcome }}
- How the course works: {{ course_mechanics }}
- The course map: {{ course_map }}
- How to approach the course: {{ learner_success_advice }}
- Where to get help: {{ support_system }}

You'll also hear practical advice on {{ practical_advice_topics }} during the cohort.

## Is This Course for You?

{{ course_short_name }} is {{ course_cost_and_format }} for {{ target_learners }} who want to {{ learner_goal }}.

It is about {{ practical_workflow_or_learning_path }}.

You should be comfortable with {{ prerequisite_1 }}, {{ prerequisite_2 }}, and {{ prerequisite_3 }}. You do not need {{ not_required_1 }}, {{ not_required_2 }}, or {{ not_required_3 }}.

The next live cohort starts on {{ cohort_start_date }}. You can join it by [registering here]({{ registration_url }}).

## About the Speaker

{{ speaker_name }} is {{ speaker_one_line_role }}.

{{ speaker_credibility_paragraph }}

## Short Version

Thinking about joining [{{ course_name }} {{ cohort_year }}]({{ registration_url }})?

Join {{ speaker_name }} for a live pre-course Q&A before the cohort starts on {{ cohort_start_date }}. We will cover who the course is for, what you will build or practice, how the cohort works, what prerequisites you need, and where to get help.

Bring your questions about {{ question_topics }}, or whether the course is a good fit for you.

You can join the cohort by [registering here]({{ registration_url }}).

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ course_name }}` | Official course name, for example `Machine Learning Zoomcamp`. |
| `{{ course_short_name }}` | Short course name used conversationally, for example `ML Zoomcamp`. |
| `{{ course_cost_and_format }}` | Cost and format phrase built from `course.cost` and `course.format`. |
| `{{ cohort_year }}` | Cohort year, for example `2026`. |
| `{{ recommended_timing }}` | Scheduling guidance, for example `two weeks` or `10 days`. |
| `{{ cohort_start_date }}` | Human-readable course start date, for example `Monday, August 31, 2026`. |
| `{{ event_time }}` | Event time range, for example `17:00-18:00`. |
| `{{ timezone }}` | Timezone label, for example `Europe/Madrid`. |
| `{{ registration_url }}` | Public registration link. |
| `{{ speaker_name }}` | Full speaker name. |
| `{{ speaker_first_name }}` | First name for the coverage bullets. |
| `{{ question_topics }}` | Comma-separated topics attendees may ask about. |
| `{{ course_outcome }}` | Main artifact, project, skill path, or practice outcome. |
| `{{ course_mechanics }}` | Videos, homework, deadlines, scoring, leaderboard, peer review, certificate path, or equivalent mechanics. |
| `{{ course_map }}` | Main modules, concepts, tools, or learning stages. |
| `{{ learner_success_advice }}` | How learners should approach the course, choose tools, manage time, avoid common traps, or prepare. |
| `{{ support_system }}` | Support channels and help resources. |
| `{{ practical_advice_topics }}` | Topics for practical advice, for example setup, project scope, tool choice, or catching up. |
| `{{ target_learners }}` | Intended audience. |
| `{{ learner_goal }}` | What learners want to learn or become able to do. |
| `{{ practical_workflow_or_learning_path }}` | Concrete description of the course path. |
| `{{ prerequisite_1 }}` to `{{ prerequisite_3 }}` | Honest starting requirements. |
| `{{ not_required_1 }}` to `{{ not_required_3 }}` | Things learners do not need before joining. |
| `{{ speaker_one_line_role }}` | Short source-backed role line from the course instructor data. |
| `{{ speaker_credibility_paragraph }}` | Speaker background, kept to one paragraph. |

## Editing Rules

- Keep the event focused on fit, expectations, and preparation.
- Answer "Should I join?" and "What should I do before the course starts?"
- Keep 5 bullets in "What We'll Cover".
- Include prerequisites and things not required.
- Mention live cohort mechanics only if they apply to the course.
- Do not overfill the description with every module detail.
- Do not promise jobs, promotions, certificates without requirements, or guaranteed outcomes.
- Do not use hype language such as "master", "transform", "unlock", or "10x".
- Replace placeholders before publishing.
