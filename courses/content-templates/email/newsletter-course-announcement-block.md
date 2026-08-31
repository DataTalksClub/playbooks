# Newsletter Course Announcement Block Template

Use this block inside a newsletter when a course needs a compact announcement with one clear registration CTA. Populate course-specific values from `courses/<course>/course.yaml` as described in `../README.md`.

The block should feel useful, not salesy. Lead with the course, date, and practical outcome. Keep the bullets concrete. Remove internal notes before publishing.

## Ready-To-Paste Template

## {{ course_name }} {{ cohort_year }} cohort

The next live cohort of {{ course_name }} starts on {{ cohort_start_date }}.

{{ course_name }} is {{ course_cost_and_format }} about {{ course_topic }}. It is for {{ target_learners }} who want to {{ practical_outcome }}.

In the course, you will practice:

- {{ outcome_1 }}
- {{ outcome_2 }}
- {{ outcome_3 }}
- {{ outcome_4 }}

{{ delivery_summary }} The live cohort adds {{ cohort_mechanic_1 }}, {{ cohort_mechanic_2 }}, {{ cohort_mechanic_3 }}, {{ cohort_mechanic_4 }}, and {{ certificate_or_completion_path }}.

{{ prerequisite_or_fit_line }}

[{{ registration_cta_label }}]({{ registration_url }})

## Short Version

{{ course_name }} {{ cohort_year }} starts on {{ cohort_start_date }}. It is {{ course_cost_and_format }} about {{ course_topic }}. You will practice {{ short_outcome_1 }}, {{ short_outcome_2 }}, and {{ short_outcome_3 }}. {{ short_live_cohort_summary }}

[{{ registration_cta_label }}]({{ registration_url }})

## Button Version

Use this version when the newsletter editor supports a simple Markdown button table.

## {{ course_name }} {{ cohort_year }} cohort

The next live cohort of {{ course_name }} starts on {{ cohort_start_date }}.

{{ course_name }} is {{ course_cost_and_format }} about {{ course_topic }}. It is for {{ target_learners }} who want to {{ practical_outcome }}.

You will practice:

- {{ outcome_1 }}
- {{ outcome_2 }}
- {{ outcome_3 }}
- {{ outcome_4 }}

{{ delivery_summary }} The live cohort includes {{ cohort_mechanic_1 }}, {{ cohort_mechanic_2 }}, {{ cohort_mechanic_3 }}, {{ cohort_mechanic_4 }}, and {{ certificate_or_completion_path }}.

| [{{ registration_cta_label }}]({{ registration_url }}) |
| --- |

## Placeholder Guide

| Placeholder | Use |
| --- | --- |
| `{{ course_name }}` | Official course name. |
| `{{ cohort_year }}` | Cohort year, for example `2026`. |
| `{{ cohort_start_date }}` | Human-readable date, for example `August 31, 2026`. |
| `{{ course_topic }}` | Plain description of what the course teaches. |
| `{{ course_cost_and_format }}` | Cost and format phrase built from `course.cost` and `course.format`. |
| `{{ target_learners }}` | The intended audience. |
| `{{ practical_outcome }}` | What learners should be able to do after the course. |
| `{{ outcome_1 }}` to `{{ outcome_4 }}` | Concrete actions learners will practice. |
| `{{ cohort_mechanic_1 }}` to `{{ cohort_mechanic_4 }}` | Live cohort mechanics such as deadlines, homework, leaderboard, peer review, or community support. |
| `{{ certificate_or_completion_path }}` | Certificate eligibility or completion requirement. |
| `{{ delivery_summary }}` | One sentence built from `delivery.*`. |
| `{{ short_live_cohort_summary }}` | Compact live-cohort summary built from delivery and cohort values. |
| `{{ prerequisite_or_fit_line }}` | Optional fit line. Keep it short. |
| `{{ registration_url }}` | Registration link. |
| `{{ registration_cta_label }}` | CTA label that matches the course cost and campaign stage. |

## Editing Rules

- Remove exported table spacer rows before publishing.
- Keep one CTA.
- Keep 3 to 5 outcome bullets.
- Start each bullet with a concrete verb.
- Do not promise jobs, promotions, guaranteed productivity gains, or production expertise.
- Do not describe the course as beginner-friendly unless the learner still has the required prerequisites.
- Do not use hype language such as "master", "transform", "unlock", or "10x".
