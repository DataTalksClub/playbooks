# AI Dev Tools Zoomcamp Copy Bank

This copy bank stores reusable non-social copy for AI Dev Tools Zoomcamp.

Social media posts for LinkedIn and X are handled separately. Use this folder for owned channels, course operations, announcements, support, and page copy.

## Channel Map

| Channel | Files |
| --- | --- |
| DTC newsletter | `email/`, especially `email/newsletter-announcement-block.md` |
| DTC Slack | `slack/` |
| Website banner | `website/website-banner.md` |
| Course landing page | `website/landing-page-blocks.md` |
| GitHub README | `github/readme-update-blocks.md` |
| YouTube descriptions / pinned comments | `youtube/descriptions-and-pinned-comments.md` |
| Launch stream | `events/course-launch.md`, `events/pre-course-live-qa.md`, `youtube/descriptions-and-pinned-comments.md` |
| Telegram | `telegram/` |

## Source of Truth

Use `../course.yaml` for facts before adapting copy:

- Course name, dates, links, and registration URL.
- Course platform and GitHub URL.
- Slack, Telegram, documentation, FAQ, and environment setup links.
- Module names, tools, outcomes, and project requirements.
- Homework repository paths and folder names from `delivery.homework.source`.
- Homework and project deadlines from `cohort_schedule`.
- Cohort module materials, companion articles, and recordings from `urls.cohort_2026_module_resources`.
- Certificate and peer review rules.

Resolve homework placeholders from `course.yaml`. For the 2026 cohort, use the explicit
`homework_url` entries under `delivery.homework.source.locations`. Do not derive homework folders
from the current module materials folder names because the two structures are different.

Resolve deadline placeholders from `cohort_schedule`. Use `deadline_utc` for scheduling and
`deadline_local` when publishing the supplied Europe/Madrid cohort time. Do not save or reuse
countdowns and open/closed statuses because they change over time.

Resolve homework and project submission placeholders from the matching `submission_url` in
`cohort_schedule`; use the logistics links under `urls` for homework, leaderboard, peer-review,
and mid-cohort guidance.

Use placeholders for cohort-specific values:

- `{{ cohort_year }}`
- `{{ cohort_start_date }}`
- `{{ registration_url }}`
- `{{ course_platform_url }}`
- `{{ launch_stream_url }}`
- `{{ pre_course_qna_url }}`
- `{{ homework_deadline }}`

Exception: files under `email/` are currently resolved for the 2026 cohort and should not contain
unfilled placeholders. For a future cohort, regenerate or update them from `course.yaml` and use
`email/module-email-template.md` as an assembly guide.

## Positioning Reminder

AI Dev Tools Zoomcamp is about disciplined AI-assisted software development.

Use this framing:

- AI assistants, coding agents, MCP, tests, CI/CD, deployment, and automation.
- Learners read, run, debug, test, and document AI-generated code.
- The project outcome is a complete application with frontend, backend, API contract, database, tests, deployment, and reproducible documentation.

Avoid positioning it as:

- A course about RAG, LangChain, vector databases, model training, or fine-tuning.
- A non-technical AI introduction.
- A tour of every tool in the market.
- A promise that AI writes production code without engineering review.
