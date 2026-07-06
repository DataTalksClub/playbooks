# Course And Content Playbooks

This repository stores reusable launch playbooks, course messaging, outreach lists, and copy research for DataTalks.Club courses.

Use it when preparing a new live cohort, refreshing a course announcement, writing newsletter or Telegram copy, or mining previous social posts for reusable launch patterns.

## Start Here

For a new cohort:

1. Copy `00-cohort-brief.md` and fill in the course, dates, registration target, campaign intensity, channels, events, and owners.
2. Use `01-launch-checklist.md` to track the required asset updates and promotion tasks.
3. Fill `02-campaign-calendar.csv` with the planned announcement schedule.
4. Open the relevant course folder and adapt the templates, proof points, and copy-bank files.
5. Use the Typefully export and taxonomy when you need examples of past course-promotion posts.

## Repository Map

| Path | Purpose |
| --- | --- |
| `00-cohort-brief.md` | Cohort planning template: goals, registration gap, channels, event decisions, owners. |
| `01-launch-checklist.md` | Execution checklist for asset updates, events, promotion, and outreach. |
| `02-campaign-calendar.csv` | Calendar skeleton for planned campaign posts and announcements. |
| `influencer-list.csv` | Outreach list for practitioners, influencers, and potential amplifiers. |
| `podcast-list.csv` | Podcast and guest-appearance outreach list. |
| `scripts/download_typefully_posts.py` | Typefully exporter for collecting and filtering course-related posts. |
| `typefully/` | Exported Typefully data, filtered post digests, and social post taxonomy. |
| `*-zoomcamp/` | Course-specific metadata, templates, proof libraries, and copy assets. |

## Course Folders

Each course folder is designed to keep the core facts and reusable launch assets in one place.

Current course folders:

- `ai-dev-tools-zoomcamp/`
- `de-zoomcamp/`
- `llm-zoomcamp/`
- `ml-zoomcamp/`
- `mlops-zoomcamp/`

Common files:

| Path | Purpose |
| --- | --- |
| `course.yaml` | Structured course metadata: URLs, cadence, prerequisites, audience, modules, tools, certificate rules, and CTAs. |
| `templates/course-launch.md` | Reusable launch announcement structure. |
| `templates/pre-course-live-qa.md` | Reusable pre-course Q&A announcement structure. |
| `proof-library/testimonials.md` | Testimonials and learner quotes. |
| `proof-library/previous-cohorts-stats.md` | Registration, completion, stars, or cohort metrics. |
| `proof-library/student-projects.md` | Student project examples and portfolio proof. |

## AI Dev Tools Zoomcamp Copy Bank

`ai-dev-tools-zoomcamp/` currently has the most complete launch package.

It includes:

- `positioning.md`: positioning, audience fit, differentiation, claims to use, and claims to avoid.
- `audience.md`: learner segments and messaging angles.
- `curriculum-and-outcomes.md`: curriculum framing and learner outcomes.
- `faq-and-objections.md`: common objections and answer angles.
- `copy-bank/faq.md`: course FAQ copy.
- `copy-bank/newsletter/`: welcome email, module emails, final project email, certificate email, and reusable newsletter blocks.
- `copy-bank/telegram/`: pinned post and module announcement drafts.

Use this folder as the reference implementation when adding deeper copy banks for other courses.

## Typefully Export

The `typefully/` folder stores a snapshot of Alexey social posts matching:

- `zoomcamp`
- `free course`

Important files:

| Path | Purpose |
| --- | --- |
| `typefully/README.md` | Detailed export instructions. |
| `typefully/manifest.json` | Latest export summary and file pointers. |
| `typefully/raw/` | Raw Typefully API responses. |
| `typefully/filtered/` | Normalized matching posts as JSON, CSV, and Markdown. |
| `typefully/post-type-taxonomy.md` | Human-readable taxonomy for course social posts. |
| `typefully/post-type-taxonomy.json` | Machine-readable version of the taxonomy. |

Run the exporter from the repo root. Pass `--output-dir typefully` when updating the current export snapshot:

```bash
TYPEFULLY_API_KEY=... python3 scripts/download_typefully_posts.py \
  --social-set-name-match alexey \
  --limit 50 \
  --hydrate-details \
  --output-dir typefully
```

Do not commit or store Typefully API keys in this repository.

## File Conventions

- Keep durable course facts in `course.yaml`.
- Keep reusable launch copy in `templates/` and `copy-bank/`.
- Keep proof points in `proof-library/` so announcements can cite them without hunting through old docs.
- Use placeholders such as `{{ cohort_start_date }}` for values that change every cohort.
- Prefer grounded course claims over hype; many files include explicit claims to use and avoid.
