# Shared Content Templates

These files define reusable structure. They must not contain course-specific names, links, channels, dates, module titles, hashtags, certificate rules, or learning outcomes.

## Source Values

Before filling a template, read the target course's `courses/<course>/course.yaml`.

Use course YAML for durable values:

| Template value | Course YAML source |
| --- | --- |
| Course name, short name, description, format, and cost | `course.*` |
| Repository, registration, platform, playlist, documentation, FAQ, and community links | `urls.*` |
| Lecture, live-session, homework, submission, and certificate behavior | `delivery.*` |
| Audience and prerequisites | `audience`, `prerequisites` |
| Topics, tools, modules, projects, and outcomes | `topics`, `tools`, `modules`, `projects`, `outcomes` |
| Cohort rhythm and timing conventions | `cohort_cadence.*` |
| Community channels and learning-in-public rules | `community.*` |
| Instructor names and profiles | `people.instructors` |

Use the campaign folder for cohort-specific values such as confirmed dates, registration targets, event links, speakers for a particular event, deadlines, and final campaign decisions. Campaign values override durable course values only for that campaign.

Some placeholders are derived summaries rather than direct scalar fields. Build them only from the relevant YAML values; do not invent missing facts. Remove optional blocks when the source value is unavailable.

## Template Rules

- Keep all course-specific values as `{{ placeholders }}`.
- Do not append a real course example to a shared template. Store approved examples in that course's `copy-bank/`.
- Keep placeholder names consistent with this folder and the course schema.
- Preserve conditional blocks such as `{{#if ...}}` only when the publishing workflow supports them; otherwise resolve them while creating the course-specific copy.
- Write finished course and campaign copy outside this folder.
