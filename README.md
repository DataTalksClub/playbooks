# Course and Content Playbooks

This repository stores reusable launch playbooks, course messaging, outreach lists, copy banks, proof libraries, and social post research for DataTalks.Club courses.

Use it when preparing a new live cohort, refreshing course pages, writing newsletter, Slack, Telegram, YouTube, website, or GitHub copy, planning a launch campaign, or mining previous social posts for reusable patterns.

## Start Here

For a new cohort:

1. Create or open a folder under `courses/campaigns/`, for example `courses/campaigns/ai-dev-tools-zoomcamp-2026/`.
2. Copy the process templates from `courses/` into `courses/campaigns/<course>-<year>/processes/` if they are not already there.
3. Fill `courses/00-cohort-brief.md` or the campaign copy with the course, dates, registration target, campaign intensity, channels, events, and owners.
4. Use `courses/01-launch-checklist.md` to track asset updates, events, promotion tasks, and outreach.
5. Use `courses/02-course-launch-social-system.md` to choose campaign phases, post types, cadence, CTAs, and channel adaptations.
6. Fill `courses/02-campaign-calendar.csv` or the campaign copy with the planned announcement schedule. Replace placeholders with course and campaign values.
7. Adapt the relevant course folder's `course.yaml`, `copy-bank/`, and `proof-library/` assets into the campaign folder when the campaign needs cohort-specific versions.
8. Use `research/typefully/` when you need examples of past course-promotion posts or a taxonomy for social post ideas.
9. After the cohort, complete `03-retrospective.md` so next year's launch has numbers, reusable proof, and lessons learned.

## Repository Map

| Path | Purpose |
| --- | --- |
| `courses/00-cohort-brief.md` | Planning template for cohort basics, registration gap, channel decisions, event decisions, owners, and approval. |
| `courses/01-launch-checklist.md` | Execution checklist for asset updates, events, promotion, and outreach. |
| `courses/01-course-assets-map.md` | Cross-repository map of course assets, URLs, and launch destinations. |
| `courses/01-course-platform-setup.md` | Process for opening a cohort on the course management platform. |
| `courses/01-course-repo-cohort-setup.md` | Process for opening and archiving cohort material in the course repository. |
| `courses/02-course-launch-social-system.md` | Main social launch system: campaign phases, post types, cadence, channel adaptation, metrics, and reusable strategy. |
| `courses/02-campaign-calendar.csv` | Campaign calendar skeleton with relative timing, phase, platform, post type, CTA, needed assets, and status. |
| `courses/03-retrospective.md` | Post-cohort retrospective template for final numbers, best channels, best posts, repeated questions, and next-year improvements. |
| `courses/content-templates/` | Shared placeholder-only channel templates populated from course and campaign sources. |
| `research/outreach/` | Outreach lists for practitioners, communities, podcasts, and potential amplifiers. |
| `research/typefully/` | Curated Typefully examples, export tooling, manifest, and social post taxonomy. |
| `courses/campaigns/` | Cohort-specific campaign decisions and finished campaign assets. |
| `skills/` | Canonical Codex workflows and their task-specific reference material, plus supporting scripts and assets. |
| `courses/*-zoomcamp/` | Reusable course reference material, copy banks, proof libraries, and optional course assets. |

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
| `copy-bank/events/` | Event descriptions such as pre-course workshops, launch sessions, and live Q&A sessions. |
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

`courses/campaigns/` stores campaign-specific decisions and assets. Use it for work tied to a particular course cohort, year, registration target, and launch calendar.

Current campaign workspaces:

- `courses/campaigns/ai-dev-tools-zoomcamp-2026/`
- `courses/campaigns/ml-zoomcamp-2026/`

Typical structure:

| Path | Purpose |
| --- | --- |
| `courses/campaigns/<course>-<year>/course.yaml` | Cohort-specific overrides when durable course metadata is insufficient. |
| `courses/campaigns/<course>-<year>/positioning.md` | Campaign-specific positioning, claims, and exclusions. |
| `courses/campaigns/<course>-<year>/audience.md` | Audience segments and messaging angles for this cohort. |
| `courses/campaigns/<course>-<year>/curriculum-and-outcomes.md` | Campaign-specific curriculum and outcome framing. |
| `courses/campaigns/<course>-<year>/faq-and-objections.md` | Cohort-specific FAQ and objection handling. |
| `courses/campaigns/<course>-<year>/processes/` | Cohort brief, checklist, campaign calendar, social system, and retrospective. |
| `courses/campaigns/<course>-<year>/copy-bank/` | Cohort-specific final channel copy. |
| `courses/campaigns/<course>-<year>/proof-library/` | Campaign-specific metrics, testimonials, and project proof. |

Keep reusable references and copy patterns in the course folder. Put cohort-specific edits, dates, URLs, and final campaign decisions in `courses/campaigns/`.

## Main Processes

### Plan a Cohort Launch

Start from `courses/campaigns/<course>-<year>/processes/00-cohort-brief.md`. If the campaign folder does not exist yet, create it from the process templates in `courses/` and the relevant course folder.

The most important decision is whether this is a normal launch or an extra-push launch. Extra-push launches add channels such as alumni outreach, influencer outreach, partner posts, external newsletters, communities, podcasts, short clips, SEO, or paid distribution.

Once the brief is complete, use `01-launch-checklist.md` to track execution. The checklist intentionally separates asset updates, events, promotion, and outreach so owners can work in parallel.

### Set Up the Course Platform

Use `courses/01-course-platform-setup.md`. Use the course management agent project (`~/git/course-management-agent`) to make the actual changes; the playbook covers the decisions.

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

Every course reference file must follow `courses/schema/course.schema.json`. Validate all course files after editing:

```bash
scripts/validate_courses.rb
```

Shared files under `courses/content-templates/` contain placeholders only. Resolve those placeholders from the target course's `course.yaml`; use campaign sources only for cohort-specific dates, deadlines, event links, and final campaign decisions.

If a campaign has its own `courses/campaigns/<course>-<year>/course.yaml`, use it only for cohort-specific overrides. Use `courses/<course>/course.yaml` and the reusable course folder for durable facts and copy patterns.

Use `copy-bank/` for reusable copy:

- Put event descriptions in `copy-bank/events/`, named so they sort by date: `NN-YYYY-MM-DD-slug.md` in a campaign folder, `NN-yyyy-mm-dd-slug.md` in a reusable course folder.
- Keep recurring events in the reusable course folder: the launch session and the pre-course Q&A. Cohort-specific workshops belong in the campaign folder only.
- Index past workshops from `copy-bank/events/README.md` in the course folder, so the drafts stay findable after the campaign folder goes quiet.
- Name the person running an event the **Instructor**, not the host.
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

The `research/typefully/` folder stores Alexey social post research for posts that mention terms such as `zoomcamp` or `free course`.

Important files:

| Path | Purpose |
| --- | --- |
| `research/typefully/README.md` | Detailed export instructions. |
| `research/typefully/manifest.json` | Latest curated export summary and file pointers. |
| `research/typefully/typefully-examples.json` | Curated normalized examples from the export. |
| `research/typefully/typefully-examples.csv` | Spreadsheet-friendly version of the examples. |
| `research/typefully/typefully-examples.md` | Human-readable post digest. |
| `research/typefully/post-type-taxonomy.md` | Human-readable taxonomy for reusable course social post types. |
| `research/typefully/post-type-taxonomy.json` | Machine-readable taxonomy. |
| `research/typefully/post-type-taxonomy-analysis.md` | Notes and analysis behind the taxonomy. |

Run the exporter from the repo root. Use `--output-dir typefully` when refreshing the central research snapshot:

```bash
TYPEFULLY_API_KEY=... python3 research/typefully/scripts/download_posts.py \
  --social-set-name-match alexey \
  --limit 50 \
  --hydrate-details \
  --output-dir research/typefully
```

The script defaults to `research/typefully/`. Raw and timestamped filtered exports are ignored; promote reviewed outputs to the curated example files when they should be shared.

Do not commit or store Typefully API keys in this repository.

## Outreach Lists

Use `research/outreach/influencers.csv` and `research/outreach/podcasts.csv` when the cohort brief selects extra outreach.

Typical workflow:

1. Filter for the course topic and audience fit.
2. Decide the outreach angle from `course.yaml`, `positioning.md`, or the copy bank.
3. Track planned outreach separately or add campaign moments to `02-campaign-calendar.csv`.
4. Record reusable outcomes or proof in the relevant course folder.

## Local Skills

The `skills/` folder is the canonical source for Codex behavior and reusable writing guidance in this repository. Each skill keeps routing and essential constraints in `SKILL.md`; substantial style, audience, channel, format, and domain guidance belongs in that skill's `references/` folder.

- `skills/social-content-studio/`: Alexey's social voice, audience, examples, structured post creation, and export workflows.
- `skills/newsletter-editor/`: AI Shipping Blog voice and editing guidance for Alexey's newsletter.
- `skills/datatalks-event-promotion/`: DataTalks.Club event campaign strategy, audience, channel, owner, and platform guidance.
- `skills/alexey-carousel-generator/`: social carousel and resource-image rendering workflows.
- `skills/transcript-post-miner/`: transcript analysis for post ideas and clip recommendations.
- `skills/video-clip-cutter/`: ffmpeg-based clip cutting from timestamp manifests.
- `skills/.system/`: team-shared system skills intentionally versioned so collaborators receive the same GitHub-distributed skill set.

Do not maintain parallel copies of skill references under a general `documents/` folder. Update the owning skill reference directly. When guidance belongs to more than one skill, keep each skill operationally self-contained and make the ownership boundary explicit in its `SKILL.md`; avoid a second human-document mirror that can drift independently.

Course and campaign material has different ownership:

| Information | Canonical location |
| --- | --- |
| Skill workflow and routing | `skills/<skill>/SKILL.md` |
| Style, audience, channel, format, and domain rules used by a skill | `skills/<skill>/references/` |
| Deterministic automation | `skills/<skill>/scripts/` |
| Durable course facts | `courses/<course>/course.yaml` and adjacent course files |
| Reusable course copy | `courses/<course>/copy-bank/` |
| Cohort-specific decisions and copy | `courses/campaigns/<course>-<year>/` |
| Generated working artifacts | `content-runs/` or the user-requested output folder |

Examples and templates belong with the narrowest owner that uses them. A style example used only to calibrate Alexey's social posts belongs in `skills/social-content-studio/references/`; a reusable course announcement belongs in the relevant course copy bank.

## File Conventions

- Treat `skills/<skill>/references/` as the source of truth for guidance consumed by that skill.
- Do not recreate a top-level `documents/` mirror of skill references.
- Route conditional references from `SKILL.md` and load only the references needed for the current deliverable.
- Keep durable course facts in `course.yaml`.
- Keep reusable launch copy in `copy-bank/`.
- Keep proof points in `proof-library/`.
- Keep reusable planning templates in `courses/` and reusable channel templates in `courses/content-templates/`.
- Keep campaign execution in `courses/campaigns/<course>-<year>/`.
- Use placeholders for cohort-specific values.
- Avoid secrets in the repository, especially API keys.
- Preserve source links for stats, testimonials, and examples whenever possible.
- Prefer concrete learner outcomes, project examples, dates, and logistics over vague promotional language.
