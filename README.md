# DataTalks.Club Content Playbooks

Playbooks, agent skills, and source facts for writing DataTalks.Club and Alexey Grigorev content: social posts (LinkedIn, X, Substack Notes, Threads), the DataTalks.Club Weekly newsletter, Alexey's newsletter, Telegram, Slack, email, YouTube, and course launch campaigns.

Most work here is done by an AI agent (Claude Code, or Codex) following the skills in `.claude/skills/`, with a person reviewing every draft. Nothing is published, sent, or scheduled without explicit permission. The rules every agent follows are in [`CLAUDE.md`](CLAUDE.md) (`AGENTS.md` is a symlink to it).

## Quick Start

Ask the agent in this repository. Decide the owner first: DataTalks.Club writes as an organization; Alexey writes in the first person.

| You want | Ask, for example | Skill | Output |
| --- | --- | --- | --- |
| DataTalks.Club Weekly | "Draft the DataTalks.Club Weekly for October 12" | `dtc-newsletter` | `newsletter/issues/<date>-weekly-<N>/` |
| DataTalks.Club social posts, Telegram, Slack, YouTube | "Create DataTalks.Club posts for this week's newsletter" | `datatalks-event-promotion` | `content-runs/<date>-<slug>/` |
| Alexey's LinkedIn, X, Substack Notes, and Threads posts | "Plan Alexey's posts for this week", "Turn this newsletter into posts" | `social-content-studio` | `content-runs/<date>-<slug>/` |
| Carousels and X images for Alexey's posts | Done with his posts by default | `alexey-carousel-generator` | Inside each post folder |
| Post ideas and clips from a recording | "Find post ideas in this workshop transcript" | `transcript-post-miner`, then `video-clip-cutter` | `content-runs/<date>-<slug>/` |
| Edit Alexey's newsletter (AI Shipping Blog) | "Edit this draft" | `newsletter-editor` | Where you ask |
| A course cohort launch | "Set up the ML Zoomcamp 2027 campaign" | Process templates, no skill | `courses/campaigns/<course>-<year>/` |

## Repository Map

```text
.claude/
  skills/<skill>/          Agent skills: SKILL.md (workflow), references/ (rules), scripts/
  agents/post-reviewer.md  Subagent for the independent fact and voice review of posts
courses/
  <course>/                Durable course facts (course.yaml), copy-bank/, proof-library/
  ai-engineering-buildcamp/ Alexey's paid course: lightning lessons, testimonials, post library
  campaigns/<course>-<year>/ Cohort-specific decisions, processes, and final copy
  process-templates/       Cohort launch templates: brief, checklists, social system, calendar, retrospective
  content-templates/       Placeholder-only channel templates (email, events, Slack, Telegram)
  schema/                  course.schema.json, checked by scripts/validate_courses.rb
newsletter/
  issues/<date>-weekly-<N>/ One folder per DataTalks.Club Weekly issue (from #284)
  performance.md           Opens, clicks, and best slots per issue
events-archive/            Published Luma descriptions of past workshops and launches, by course
research/
  typefully/               Alexey's Typefully posts: curated course examples, full export, taxonomy
  outreach/                Influencer and podcast lists for launch outreach
content-runs/              Generated post runs (gitignored)
scripts/validate_courses.rb Validates every course.yaml against the schema
skills/                    Symlinks to .claude/skills/ for Codex, plus Codex system skills in .system/
CLAUDE.md, AGENTS.md       Rules for every agent (AGENTS.md is a symlink)
IMPROVEMENTS.md            Open and done improvements to the content pipeline
.env.example               The environment variables the scripts need
```

## Social Posts: Content Runs

Every batch of posts lives in a content run: `content-runs/<YYYY-MM-DD>-<slug>/`, one per source (a recording, a newsletter, a week's issue), holding posts for both owners. The full pipeline is in [`.claude/skills/social-content-studio/SKILL.md`](.claude/skills/social-content-studio/SKILL.md).

1. **Create the run and save the sources.** `create_content_run.py` makes the folder; the sources go in `source/` (transcript, newsletter text, Luma pages), with every required link and caveat in `source/source.json`.
2. **Scaffold a folder per post.** `scaffold_post.py` creates `posts/alexey_NNN/` or `posts/dtc_NNN/` with `post.json`, empty copy files, and a review stub.
3. **Write.** Alexey: one `linkedin.md`, shared by every platform. DataTalks.Club: `linkedin.md` plus an `x.md` thread under 280 characters per post.
4. **Media.** Carousels and X images for Alexey (`alexey-carousel-generator`); captioned clips from recordings (`video-clip-cutter`).
5. **Check.** `check_posts.py` runs the mechanical checks: X limits, banned phrases, required links, media files.
6. **Review.** The `post-reviewer` subagent checks every claim against the sources and writes findings to `review.json`. Fix errors before handing posts over.
7. **Upload drafts, only with permission.** `typefully_drafts.py` creates Typefully drafts (dry-run first). It never schedules or publishes.
8. **Learn from edits.** After publishing, `pull_typefully_edits.py` writes `edits.md` with a diff per platform. Patterns go into the style references.

Platforms per owner, from [`profiles.json`](.claude/skills/social-content-studio/references/profiles.json):

| Owner | Platforms | Copy | Media |
| --- | --- | --- | --- |
| Alexey | LinkedIn, X, Substack Notes, Threads | One `linkedin.md`; Threads gets it as a chain of posts under 500 characters | Carousel PDF on LinkedIn, resource image elsewhere; or a clip (no video on Substack) |
| DataTalks.Club | LinkedIn, X | `linkedin.md` and an `x.md` thread | Clip, when the post has one |

Where the guidance lives:

| Question | File |
| --- | --- |
| How Alexey writes | `social-content-studio/references/alexey-style.md`, examples in `alexey-good-posts.md` |
| What Alexey posts about, and how one source becomes several posts | `social-content-studio/references/alexey-content-sources.md` |
| How DataTalks.Club writes | `datatalks-event-promotion/references/datatalks-style.md` and `datatalks-social-media.md` |
| Channel rules (Telegram, Slack, YouTube, X, LinkedIn) | `datatalks-event-promotion/references/` |
| Before and after events | `datatalks-event-promotion/references/stage-1-pre-event.md`, `stage-2-post-event.md` |

## DataTalks.Club Weekly

The weekly newsletter is drafted with the `dtc-newsletter` skill; [its `SKILL.md`](.claude/skills/dtc-newsletter/SKILL.md) has the full workflow and rules.

1. **Refresh the archive.** `mailchimp_export.py --last 4` saves recently sent issues and click stats to `newsletter/issues/` and rewrites `newsletter/performance.md`. A draft that was sent is kept as `draft.md` next to the sent `issue.md`, so the edits before sending stay visible.
2. **Collect the facts.** `week_sources.rb --date <send date>` writes `sources.md`: the issue number, running Zoomcamps (module, deadlines, peer reviews), upcoming events with Luma times, Book of the Week, new recordings, and new Alexey on Data posts. The agent also checks the Luma calendar and YouTube, which are often ahead of the website.
3. **Fill the gaps.** The agent asks only for what no source has, mainly the sponsor copy, and saves the answers as `brief.md`.
4. **Draft.** `issue.md` with subject line options, preview text, the campaign name, and every slot that has content.
5. **Review and send.** A person edits the draft, builds it in Mailchimp, and sends it.
6. **Learn from the edits.** The next export compares the sent issue with the draft, and rules that changed go into the skill's references.

Slots, in order, each only when it has content: sponsored promo, one Zoomcamp slot per running course, course registration, a second promo, event details, upcoming events, recordings (workshop, podcast, and webinar, one slot each), Book of the Week, and From Alexey on Data. Slot rules are in `dtc-newsletter/references/slots.md`, the order and output format in `issue-structure.md`, and the Mailchimp template setup in `design-brief.md`.

Limits worth knowing:

- Mailchimp access is read-only.
- The course platform wins over `course.yaml` for deadlines, and the agent flags a mismatch.
- Luma times come from the public page, not an API.
- Gmail clips emails over 102 KB, so check a test send for "[Message clipped]".

## Course Launches

1. Create `courses/campaigns/<course>-<year>/` and copy what you need from `courses/process-templates/` into its `processes/` folder.
2. Fill `00-cohort-brief.md`: dates, registration target, campaign intensity (normal or extra push), channels, events, and owners.
3. Set up the course platform with `01-course-platform-setup.md` and the course repository with `01-course-repo-cohort-setup.md`. Deadlines are Monday at 23:00 UTC; copy and shift the previous cohort's outline.
4. Track execution in `01-launch-checklist.md`, and find every asset and URL in `01-course-assets-map.md`.
5. Choose the campaign shape in `02-course-launch-social-system.md`, then fill `02-campaign-calendar.csv`. Every planned item gets a row.
6. Write copy from `courses/<course>/course.yaml` and `copy-bank/`. Put cohort-specific versions in the campaign folder, not over the reusable ones.
7. After the cohort, fill `03-retrospective.md`. It is the input for next year's brief.

Course folder contents:

| Path | What it holds |
| --- | --- |
| `course.yaml` | Durable facts: URLs, cadence, prerequisites, audience, modules, tools, certificate rules. Validate after editing: `ruby scripts/validate_courses.rb` |
| `copy-bank/` | Reusable copy by channel: `email/`, `events/`, `telegram/`, `slack/`, `website/`, `github/`, `youtube/`, and `faq.md` |
| `proof-library/` | `testimonials.md`, `previous-cohorts-stats.md`, `student-projects.md`. Make claims only from here |

`ai-dev-tools-zoomcamp/` is the most complete course folder and the model for the others. Shared templates in `courses/content-templates/` hold placeholders only, filled from the course's `course.yaml`. Event copy is named `NN-YYYY-MM-DD-slug.md`, and the person running an event is the Instructor, not the host.

## Research And Archives

| Path | What it is |
| --- | --- |
| `research/typefully/` | Curated examples of Alexey's course-promotion posts (`typefully-examples.*`, August 2026) and the post-type taxonomy. Export tooling and instructions in its `README.md` |
| `research/typefully/all-posts/` | Full export of Alexey's posts (603 published, August 2024 to October 2026); the analysis is in `alexey-content-sources.md`. Raw and filtered files are gitignored |
| `research/outreach/` | `influencers.csv` and `podcasts.csv` for launches with extra outreach |
| `events-archive/` | Luma descriptions of past events, kept verbatim, indexed in its `README.md` |
| `courses/ai-engineering-buildcamp/` | Buildcamp lightning lessons (`lightning-lessons/`), testimonials, the Typefully export of its posts, and its past content runs (`posts/runs/`) |
| `newsletter/issues/` | Every DataTalks.Club Weekly from #284: sources, brief, draft, sent issue, and click stats |

## Where Things Belong

| Information | Location |
| --- | --- |
| Skill workflow and routing | `.claude/skills/<skill>/SKILL.md` |
| Style, audience, channel, and format rules | `.claude/skills/<skill>/references/` |
| Automation | `.claude/skills/<skill>/scripts/`; `scripts/` for repository-wide checks |
| Durable course facts | `courses/<course>/course.yaml` |
| Reusable course copy and proof | `courses/<course>/copy-bank/`, `courses/<course>/proof-library/` |
| Cohort-specific decisions and copy | `courses/campaigns/<course>-<year>/` |
| Generated drafts | `content-runs/` (social) or `newsletter/issues/` (DataTalks.Club Weekly), never inside `.claude/skills/` |
| Pipeline gaps found but not fixed | `IMPROVEMENTS.md` |

Conventions:

- When a draft is corrected, update the owning reference file, not a personal memory, so every agent and later run uses the correction.
- Keep one copy of each rule. Do not mirror skill references into another folder.
- Use placeholders such as `{{ registration_url }}` for values that change by cohort.
- Keep source links for stats, testimonials, and examples.
- Never commit secrets.

## Setup

- **Secrets:** copy `.env.example` to `.env` (gitignored) and fill in `MAILCHIMP_API_KEY` (read-only newsletter export) and `TYPEFULLY_API_KEY` (post export and draft upload). Load them with `set -a && . ./.env && set +a`.
- **Tools:**
  - Python 3 and Ruby for the scripts.
  - `uv` with `mlx-whisper` for transcription.
  - Homebrew `ffmpeg-full` (with libass) for captioned clips.
  - The carousel renderer in `~/carousel-automation` (Node).
- **Run scripts from the repository root.**
- **Codex:** `skills/<skill>` and `~/.codex/skills/<skill>` are symlinks to `.claude/skills/<skill>`. Link new skills the same way (`ln -s "$PWD/.claude/skills/<skill>" ~/.codex/skills/<skill>`), keep skill text agent-neutral, and write script paths relative to the repository root. `agents/openai.yaml` in a skill is Codex UI metadata.
