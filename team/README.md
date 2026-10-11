# Team workflow staging (Grace & Valeriia)

How Alexey works with his two contractors — documented from the October 2026
Telegram export + mailbox review, so the work can be turned into playbooks
now and automated in `dataops` later (staging area for the next 3–6 months).

- **Grace Domisiw** — community/operations assistant ("dtc-chat"): events,
  podcast pipeline, invoicing, bookkeeping, YouTube, Slack, calendar,
  newsletter slot ops. 2,615 messages + 255 voice notes in 2026.
- **Valeriia Kuka** — content manager ("valeriia"): Alexey's social accounts
  (X/LinkedIn/Substack/Threads), course cohort announcements and Telegram
  channels, sponsor copy review, reactivation outreach, AI Shipping Labs.
  11,432 messages + 1,757 voice notes in 2026 (mostly Russian).
- **Email** (both): 2,149 messages across 340 threads from the two DTC
  mailboxes (2026).

## Playbooks (`playbooks/`)

| File | What it covers |
|---|---|
| `collaboration/how-alexey-delegates.md` | Input interface: how work arrives (voice dumps, /todo, links, contacts), what's included/omitted, the receiving contract |
| `collaboration/how-grace-and-valeriia-escalate.md` | Escalation playbook: question taxonomy, what gets escalated vs decided, handoff phrases |
| `templates/email-templates-2026.md` | 21 verbatim email templates (T1–T21) with placeholders |
| `grace/podcast-guest-pipeline.md` | Guest outreach → questions doc → recording → Spotify/YouTube release |
| `grace/invoicing-and-payments.md` | Finom invoice creation + the payment-chasing ladder |
| `grace/monthly-tax-report.md` | Monthly bookkeeping assembly for the accountants |
| `grace/video-youtube-pipeline.md` | Upload, cutting, transcript fallback, timecodes, social clips |
| `grace/event-creation-and-publishing.md` | Luma/Meetup/LinkedIn/X/website event lifecycle |
| `grace/newsletter-slots-and-sponsor-stats.md` | Slot products & pricing, copy cycle, stats reports |
| `grace/daily-ops-calendar-slack-website.md` | Calendar, Slack, website (Airtable→GitHub), Maven LLs, recurring hygiene |
| `valeriia/alexey-style-rules.md` | The 17 style rules Alexey stated while correcting drafts — the gate every content draft must pass |
| `valeriia/newsletters-alexey-on-data-and-dtc-weekly.md` | The two newsletters: personal Substack (Fri) + DTC Weekly (Mon), incl. the silent-sponsor ladder and the 30-min silence rule |
| `valeriia/social-posts-typefully.md` | Typefully queue discipline, event posts, clip→post pipeline (social-content-studio), milestones, evergreen reposts, stats |
| `valeriia/course-cohort-promotion.md` | The cohort campaign machine: copy-bank, scholarship 5-post sequence, module rhythm, certificates — the biggest automation target |
| `valeriia/sponsor-copy-and-outreach.md` | Sponsor copy rule-check + rewrites, escalation ladder, outbound outreach with 50% commission |
| `valeriia/content-ops-routine.md` | Weekly planning, calendar artifacts, SEO/blog, ASL onboarding (dormant), rework patterns to design against |
| `automation-map-dataops.md` | Observed work ↔ dataops automation inventory ↔ gaps; migration conventions; priorities |

## Raw material (`telegram-analysis/`)

- `reports/` — the four analysis reports the playbooks are built from:
  `dtc-chat-grace-analysis.md`, `team-email-analysis.md`,
  `valeriia-analysis.md`, `dataops-inventory.md`
- `scripts/` — export parser, batch whisper transcriber, transcript
  collector, dialogue renderer (all re-runnable)
- `data/` — parsed messages, transcripts, dialogues, email digests.
  **Gitignored (private conversations, repo is public).** Regenerate from
  the original exports with the scripts below; the reports and playbooks
  carry the derived patterns only.

## How the data was produced

1. `parse_export.py` — Telegram Desktop HTML exports → JSONL (2026+).
2. Voice messages batch-transcribed with faster-whisper (small + base, int8)
   on two machines (hetzner `~/tgvoice`, this Windows box) —
   `scripts/batch_whisper.py`; collected via `collect_transcripts.py`.
3. `make_dialogue.py` — merged transcripts into the message stream.
4. Team email threads extracted from `~/prod/emails/` on hetzner
   (both mailboxes, 2026, threads touching grace@/valeriia@datatalks.club).
5. Analysis subagents read the dialogues/digests (recent months weighted
   most) and wrote the reports in `reports/`.
