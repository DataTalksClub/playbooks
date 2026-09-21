# DataTalks.Club Content Playbooks

This repository holds the playbooks, skills, and source facts for writing copy for DataTalks.Club and for Alexey Grigorev: social posts, newsletters, Telegram, Slack, email, and YouTube. `README.md` has the full repository map.

## Who is speaking

Decide the owner of every piece before drafting. The subject does not decide it: a post about a DataTalks.Club event can still be Alexey's post.

| Owner and channel | Skill |
| --- | --- |
| DataTalks.Club account: LinkedIn, X, Telegram, Slack, YouTube, registrant follow-ups | `datatalks-event-promotion` |
| DataTalks.Club Weekly newsletter, whole issue or one slot | `dtc-newsletter` |
| Alexey's LinkedIn and X | `social-content-studio` |
| Alexey's newsletter (AI Shipping Blog) | `newsletter-editor` |
| Carousels and X resource images for Alexey's saved posts | `alexey-carousel-generator` |
| Post ideas and clip picks from a long video or transcript | `transcript-post-miner`, then `social-content-studio` |
| Cutting video clips from timestamps | `video-clip-cutter` |

Never mix voices. DataTalks.Club writes as an organization with no personal narrator. Alexey writes in the first person. Do not invent why Alexey recommends something or how he knows someone.

## Where facts come from

- Course facts: `courses/<course>/course.yaml` and the files next to it.
- Reusable course copy: `courses/<course>/copy-bank/`.
- Proof such as testimonials and cohort stats: `courses/<course>/proof-library/`.
- Cohort-specific decisions: `courses/campaigns/<course>-<year>/`.
- Past posts for calibration: `research/typefully/`.

Draft only from supplied sources and these files. Keep names, dates, times, timezones, claims, and links exactly as given. If a fact you need is missing, ask; do not fill the gap.

## Where output goes

- Social post runs: `content-runs/<YYYY-MM-DD>-<slug>/` with `run.json`, `source/`, and `posts/post_NNN/`. This folder is gitignored.
- DataTalks.Club Weekly issues: `newsletter/issues/<YYYY-MM-DD>-weekly-<N>/` with `sources.md`, `brief.md`, and `issue.md`. This folder is tracked, and sent issues are the calibration set for the next one.
- Course copy that will be reused: the relevant `copy-bank/`.
- Never save generated drafts inside `.claude/skills/`.

## Never publish without permission

Do not publish, send, schedule, or post anything to an external service without the user's explicit permission for that specific action. This covers Mailchimp (campaigns, test sends, audiences), Typefully, social accounts, Slack, Telegram, and the course platform. Reading is fine: Mailchimp access in this repository is read-only, and scripts that talk to external services only make GET requests unless the user asks otherwise. When a draft is ready, hand it to the user; do not push it anywhere.

Secrets such as `MAILCHIMP_API_KEY` live in the gitignored `.env` at the repository root (see `.env.example`). Never commit, print, or copy them into other files.

## Keeping the rules in one place

`.claude/skills/<skill>/references/` is the single source of truth for style, format, and channel rules. When the user corrects a draft or gives a style rule that should apply next time, update the owning reference file (and `SKILL.md` routing if needed) instead of saving it to personal memory. Scheduled and cloud runs, Codex, and other collaborators read only the repository.

Skills are shared with Codex: `skills/<skill>` and `~/.codex/skills/<skill>` are symlinks to `.claude/skills/<skill>`, and `AGENTS.md` is a symlink to this file. Keep skill text agent-neutral: refer to another skill as "the `<skill>` skill" and write script paths relative to the repository root.

After editing any `course.yaml`, run `ruby scripts/validate_courses.rb`.
