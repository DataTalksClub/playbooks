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
- Certificate and peer review rules.

Use placeholders for cohort-specific values:

- `{{ cohort_year }}`
- `{{ cohort_start_date }}`
- `{{ registration_url }}`
- `{{ course_platform_url }}`
- `{{ launch_stream_url }}`
- `{{ pre_course_qna_url }}`
- `{{ homework_deadline }}`

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
