# Course and Content Playbooks

This repository stores reusable launch playbooks, course messaging, outreach lists, copy banks, proof libraries, and social post research for DataTalks.Club courses.

Use it when preparing a new live cohort, refreshing course pages, writing newsletter, Slack, Telegram, YouTube, website, or GitHub copy, planning a launch campaign, or mining previous social posts for reusable patterns.

## Start Here

For a new cohort:

1. Create or open a folder under `campaigns/`, for example `campaigns/ai-dev-tools-zoomcamp-2026/`.
2. Copy the root process templates into `campaigns/<course>-<year>/processes/` if they are not already there.
3. Fill `00-cohort-brief.md` with the course, dates, registration target, campaign intensity, channels, events, and owners.
4. Use `01-course-platform-setup.md` to create the cohort on `courses.datatalks.club` through the course management agent project. Do this early: the registration link and the deadline schedule block most other launch tasks.
5. Use `01-launch-checklist.md` to track asset updates, events, promotion tasks, and outreach.
6. Use `02-course-launch-social-system.md` to choose campaign phases, post types, cadence, CTAs, and channel adaptations.
7. Fill `02-campaign-calendar.csv` with the planned announcement schedule. Replace placeholders such as `{{ course_name }}`, `{{ course_topic }}`, and registration links with cohort-specific values.
8. Adapt the relevant course folder's `course.yaml`, `copy-bank/`, and `proof-library/` assets into the campaign folder when the campaign needs cohort-specific versions.
9. Use `typefully/` when you need examples of past course-promotion posts or a taxonomy for social post ideas.
10. After the cohort, complete `03-retrospective.md` so next year's launch has numbers, reusable proof, and lessons learned.

## Repository Map

| Path | Purpose |
| --- | --- |
| `00-cohort-brief.md` | Planning template for cohort basics, registration gap, channel decisions, event decisions, owners, and approval. |
| `01-course-platform-setup.md` | Process for creating the cohort on the course platform: the course record, the registration campaign, and the course outline of homework and project deadlines. Changes are made through the course management agent project. |
| `01-launch-checklist.md` | Execution checklist for course platform setup, asset updates, events, promotion, and outreach. |
| `02-course-launch-social-system.md` | Main social launch system: campaign phases, post types, cadence, channel adaptation, metrics, and reusable strategy. |
| `02-campaign-calendar.csv` | Campaign calendar skeleton with relative timing, phase, platform, post type, CTA, needed assets, and status. |
| `03-retrospective.md` | Post-cohort retrospective template for final numbers, best channels, best posts, repeated questions, and next-year improvements. |
| `influencer-list.csv` | Outreach list for practitioners, influencers, communities, and potential amplifiers. |
| `podcast-list.csv` | Podcast and guest-appearance outreach list. |
| `scripts/download_typefully_posts.py` | Typefully exporter for collecting and filtering course-related social posts. |
| `typefully/` | Curated Typefully examples, export manifest, and social post taxonomy. |
| `campaigns/` | Cohort-specific campaign workspaces copied from reusable playbooks and course assets. |
| `skills/` | Local Codex skills and scripts used for social content, carousels, transcript mining, and video clipping workflows. |
| `*-zoomcamp/` | Course-specific metadata, copy banks, proof libraries, and optional course assets. |

## Course Folders

Each course folder keeps durable course facts and reusable launch assets close together.

Current course folders:

- `ai-dev-tools-zoomcamp/`
- `de-zoomcamp/`
- `llm-zoomcamp/`
- `ml-zoomcamp/`
- `mlops-zoomcamp/`

Common structure:

| Path | Purpose |
| --- | --- |
| `course.yaml` | Structured source of truth for course metadata: URLs, cadence, delivery, prerequisites, audience, topics, tools, certificate rules, CTAs, and logistics. |
| `copy-bank/faq.md` | Reusable FAQ copy and objection-handling snippets. |
| `copy-bank/email/` | Email copy and reusable newsletter/module-email templates. |
| `copy-bank/events/` | Event descriptions such as course launch sessions and pre-course live Q&A sessions. |
| `copy-bank/website/` | Website banner, landing page, and page-copy blocks where available. |
| `copy-bank/github/` | GitHub README update blocks where available. |
| `copy-bank/youtube/` | YouTube descriptions and pinned comment blocks where available. |
| `copy-bank/telegram/` | Telegram pinned posts and module announcement templates. |
| `copy-bank/slack/` | Slack-specific support nudges, discussion prompts, and moderator replies where available. |
| `copy-bank/social-media/` | Reserved for course-specific social examples, exports, or drafts. |
| `course-assets/` | Reserved for course-specific assets that support copy, pages, or campaigns. |
| `proof-library/testimonials.md` | Learner quotes and testimonials. |
| `proof-library/previous-cohorts-stats.md` | Registration, completion, certificate, GitHub, or cohort metrics. |
| `proof-library/student-projects.md` | Student project examples and portfolio proof. |

`ai-dev-tools-zoomcamp/` is currently the most complete folder. In addition to the shared structure, it has:

- `positioning.md`: positioning, audience fit, differentiation, claims to use, and claims to avoid.
- `audience.md`: learner segments and messaging angles.
- `curriculum-and-outcomes.md`: curriculum framing and learner outcomes.
- `faq-and-objections.md`: common objections and answer angles.
- `copy-bank/README.md`: channel map and positioning guardrails.
- Fully drafted email, Telegram, and Slack support sequences.
- Owned-channel blocks for website banners, landing pages, GitHub README updates, and YouTube descriptions or pinned comments.

Use `ai-dev-tools-zoomcamp/` as the reference implementation when deepening the copy banks for the other courses.

## Campaign Folders

`campaigns/` stores campaign-specific copies of reusable assets. Use it for work tied to a particular course cohort, year, registration target, and launch calendar.

Current campaign workspaces:

- `campaigns/ai-dev-tools-zoomcamp-2026/`
- `campaigns/ml-zoomcamp-2026/`

Typical structure:

| Path | Purpose |
| --- | --- |
| `campaigns/<course>-<year>/course.yaml` | Cohort-specific course metadata and links. |
| `campaigns/<course>-<year>/positioning.md` | Campaign-specific positioning, claims, and exclusions. |
| `campaigns/<course>-<year>/audience.md` | Audience segments and messaging angles for this cohort. |
| `campaigns/<course>-<year>/curriculum-and-outcomes.md` | Curriculum and outcome framing for campaign copy. |
| `campaigns/<course>-<year>/faq-and-objections.md` | Cohort-specific FAQ and objection handling. |
| `campaigns/<course>-<year>/processes/` | Cohort brief, checklist, campaign calendar, social system, and retrospective. |
| `campaigns/<course>-<year>/copy-bank/` | Cohort-specific channel copy. |
| `campaigns/<course>-<year>/proof-library/` | Metrics, testimonials, and project proof used by this campaign. |

Keep reusable assets in the course folder. Put cohort-specific edits, dates, URLs, and final campaign decisions in `campaigns/`.

## Main Processes

### Plan a Cohort Launch

Start from `campaigns/<course>-<year>/processes/00-cohort-brief.md`. If the campaign folder does not exist yet, create it from the root process templates and the relevant course folder.

The most important decision is whether this is a normal launch or an extra-push launch. Extra-push launches add channels such as alumni outreach, influencer outreach, partner posts, external newsletters, communities, podcasts, short clips, SEO, or paid distribution.

Once the brief is complete, use `01-launch-checklist.md` to track execution. The checklist intentionally separates asset updates, events, promotion, and outreach so owners can work in parallel.

### Set Up the Course Platform

Use `01-course-platform-setup.md`. Use the course management agent project (`~/git/course-management-agent`) to make the actual changes; the playbook covers the decisions.

Three things must exist before the campaign can promote anything:

- The course record on `courses.datatalks.club`, with the cohort slug, start date, and certificate settings.
- The registration campaign, which owns the public registration page and produces the registration link used in every piece of launch copy.
- The course outline: homeworks and projects with their deadlines. Homeworks are created closed and empty; questions are added later, per module.

Copy the previous cohort's outline and shift it rather than designing a new schedule. Keep the previous homework and project slugs. Deadlines are always Monday at 23:00 UTC. Record the confirmed schedule in the cohort brief, then use those dates when filling the campaign calendar.

### Build the Campaign Calendar

Use `02-course-launch-social-system.md` first to pick the launch shape. Then fill `02-campaign-calendar.csv` in the campaign's `processes/` folder.

The calendar columns are:

- `Date`, `Relative week`, `Relative date`: timing.
- `Phase`: campaign phase such as foundation, awareness, consideration, launch, or urgency.
- `Platform`: channel or channel group.
- `Post type`: reusable social pattern.
- `Typefully examples`: example IDs from the Typefully research.
- `Working title / angle`: draft idea.
- `Audience`, `Primary CTA`, `Assets needed`: targeting and inputs.
- `Why this belongs in this phase`: strategy note.
- `Status`: planning state.

Keep the calendar as the coordination artifact. Drafts can live elsewhere, but every planned campaign item should have a row.

### Update Course Copy

Use `course.yaml` as the structured source of truth before editing prose. Pull durable facts from it: URLs, start dates, duration, prerequisites, tools, module names, certificate rules, submission platform, Slack/Telegram links, and CTAs.

If a campaign has its own `campaigns/<course>-<year>/course.yaml`, use that for cohort-specific dates and URLs. Use the reusable course folder for durable copy patterns.

Use `copy-bank/` for reusable copy:

- Put event descriptions in `copy-bank/events/`.
- Put newsletter and module email copy in `copy-bank/email/`.
- Put Telegram announcements in `copy-bank/telegram/`.
- Put Slack support prompts in `copy-bank/slack/`.
- Put website and landing page blocks in `copy-bank/website/`.
- Put GitHub README snippets in `copy-bank/github/`.
- Put YouTube descriptions and pinned comments in `copy-bank/youtube/`.
- Put course FAQ and objection-handling copy in `copy-bank/faq.md`.

Use placeholders such as `{{ cohort_year }}`, `{{ registration_url }}`, `{{ module_number }}`, and `{{ module_title }}` for values that change by cohort.

### Use Proof Responsibly

Use `proof-library/` before making performance claims. Proof should come from:

- `previous-cohorts-stats.md` for numbers.
- `testimonials.md` for learner quotes.
- `student-projects.md` for concrete learner output.

Prefer grounded claims over hype. If a claim needs a number or example, put the source in the proof library first.

### Close the Loop

After the cohort, fill in the campaign's `03-retrospective.md` with final numbers, best-performing channels, best posts, best proof assets, repeated learner questions, and changes for next year. This is the input for the next launch brief.

## Typefully Research

The `typefully/` folder stores Alexey social post research for posts that mention terms such as `zoomcamp` or `free course`.

Important files:

| Path | Purpose |
| --- | --- |
| `typefully/README.md` | Detailed export instructions. |
| `typefully/manifest.json` | Latest export summary and file pointers. |
| `typefully/typefully-examples.json` | Curated normalized examples from the export. |
| `typefully/typefully-examples.csv` | Spreadsheet-friendly version of the examples. |
| `typefully/typefully-examples.md` | Human-readable post digest. |
| `typefully/post-type-taxonomy.md` | Human-readable taxonomy for reusable course social post types. |
| `typefully/post-type-taxonomy.json` | Machine-readable taxonomy. |
| `typefully/post-type-taxonomy-analysis.md` | Notes and analysis behind the taxonomy. |

Run the exporter from the repo root. Use `--output-dir typefully` when refreshing the central research snapshot:

```bash
TYPEFULLY_API_KEY=... python3 scripts/download_typefully_posts.py \
  --social-set-name-match alexey \
  --limit 50 \
  --hydrate-details \
  --output-dir typefully
```

The script can also write to its default course-specific path under `ai-dev-tools-zoomcamp/copy-bank/social-media/typefully/`. It writes raw API responses, filtered JSON, filtered CSV, filtered Markdown, and an updated manifest.

Do not commit or store Typefully API keys in this repository.

## Outreach Lists

Use `influencer-list.csv` and `podcast-list.csv` when the cohort brief selects extra outreach.

Typical workflow:

1. Filter for the course topic and audience fit.
2. Decide the outreach angle from `course.yaml`, `positioning.md`, or the copy bank.
3. Track planned outreach separately or add campaign moments to `02-campaign-calendar.csv`.
4. Record reusable outcomes or proof in the relevant course folder.

## Local Skills

The `skills/` folder contains local Codex skills and helper scripts used by this workspace:

- `skills/social-content-studio/`: structured social post creation and export workflows.
- `skills/alexey-carousel-generator/`: social carousel and resource-image rendering workflows.
- `skills/transcript-post-miner/`: transcript analysis for post ideas and clip recommendations.
- `skills/video-clip-cutter/`: ffmpeg-based clip cutting from timestamp manifests.
- `skills/.system/`: system skills copied into this workspace.

These are supporting automation assets, not course copy. Edit them only when updating the automation workflow itself.

## File Conventions

- Keep durable course facts in `course.yaml`.
- Keep reusable launch copy in `copy-bank/`.
- Keep proof points in `proof-library/`.
- Keep reusable planning templates in the root playbook files.
- Keep campaign execution in `campaigns/<course>-<year>/`.
- Use placeholders for cohort-specific values.
- Avoid secrets in the repository, especially API keys.
- Preserve source links for stats, testimonials, and examples whenever possible.
- Prefer concrete learner outcomes, project examples, dates, and logistics over vague promotional language.
