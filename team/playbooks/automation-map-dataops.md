# Automation map: observed team work vs dataops/dataops-knowledge

Cross-reference of what Grace and Valeriia actually did in 2026 (Telegram +
email evidence) against the automation inventory in
`~/git/dataops` and `~/git/dataops-knowledge`
(full inventory: `team/telegram-analysis/reports/dataops-inventory.md`).
Purpose: decide what to automate first and where the playbooks land.

## The model dataops already assumes

- Humans own outcomes; agents only **draft or recommend** under a named
  human manager; every mutation is an exact-approval proposal; no automated
  external side effects (no publishing/sending) in MVP.
- The Telegram bot ("dtc-chat") is the operator interface — inbound intake,
  clarifications, proposals, approvals, result notifications.
- Seed users: Grace, Valeriia, Alexey. Workflow templates default-assign to
  Grace; `course.yaml` assigns event descriptions to Valeriia.
- Both conversational plugins (todo, typefully-draft) are built but
  rollout-gated OFF.

## Observed work → existing automation → gap

| Observed workflow (2026 evidence) | Existing in dataops | Gap |
|---|---|---|
| Delegation via `/todo` + daily bot items | `todoPlugin` (proposal→approval→task.create), gated | Turn on; migrate the 5 recurring bot items into cron templates |
| "Draft a social post" → Typefully | `typefullyPlugin` (unscheduled drafts only), gated | Turn on for Valeriia's weekly-post flow |
| Calendar/slot negotiation (92 scheduling msgs; Calendly handoff exists) | calendar module tracks Alexey's schedule/holidays | Auto-proposal of canonical slots from free-busy; Calendly link for edge cases |
| Multi-platform event mirroring (Luma/Meetup/LinkedIn/X/website) | none | Net-new; start with a "times match across platforms" checklist gate (the 2026-05-30 process step) |
| Invoice creation + chasing ladder (weekly; one fixed reminder paragraph) | sponsorCRM, invoices, bookkeeping modules exist for records | Draft-from-sponsor-master + scheduled T10 reminders until bank feed clears |
| Monthly tax report (10/10 cycles; recurring missing-invoice hunt) | bookkeeping doc import; email-document intake API | Auto-draft T14 from bank data; missing-invoice detector |
| YouTube finishing + transcript fallback (14 stall mentions) | none (YouTube skill exists on Alexey's workstation, not in dataops) | Transcript-fallback job; auto timecodes/description draft |
| Newsletter slot sales + stats (T4/T5 fully formulaic) | `newsletterSlots` API (lifecycle) exists; Mailchimp assembly is human SOP | Auto-draft T4/T5 from Mailchimp/social stats |
| Sponsor stats report (~monthly per event) | none | Pull-based stats collector → sheet → draft email |
| Slack invites from Airtable (daily bot item, ×179) | none (SOP only) | Net-new automation, trivial rules |
| Cohort Telegram announcements (Valeriia's core job) | **nothing** — bot is inbound-only; no channel management | Net-new: announcement calendar → draft → approval → post |
| Copy bank / announcement templates | scattered templates + Google Docs; this `playbooks` repo has `courses/<course>/copy-bank/` | Consolidate into dataops-knowledge templates (the copy-bank here is the source) |
| Sponsor reactivation outreach (Valeriia quarterly batches) | sponsorCommunications suggestions module proposes follow-ups | Extend with T15/T16 template drafts |
| AI Shipping Labs onboarding (Valeriia) | none | Stripe webhook → T17 welcome + questionnaire flow |

## Migration conventions (from dataops-knowledge)

When these playbooks graduate from staging:

- Location: `content/<NN-department>/<business-system>/playbooks|sops|templates/`
  (01-audience-growth, 03-programs-and-community, 04-content-production,
  05-education-operations, 07-internal-operations).
- Frontmatter: `id` (`playbook.<dept>.<system>.<slug>`), `doc_type: playbook`,
  `status: proposed`, `owner_role`, `tools` slugs, `source` (this staging
  folder + export dates).
- Person names → roles (Grace → Operations Assistant; Valeriia → Content
  Manager; keep Alexey as Owner).
- Publication goes through the portal (`POST /knowledge/publish`), never a
  raw git push.
- Any agent that executes these needs an entry in the
  `agent-specification-template.md` control spec (approval matrix, kill
  switch, shadow mode).

## Priority recommendation (evidence-weighted)

1. **Cohort campaign machine** (Valeriia's main recurring job; copy already
   lives in this repo's `courses/*/copy-bank`; Alexey already announced
   module emails will go through the agent pipeline — 2026-08-31; the
   sequence is documented in
   `valeriia/course-cohort-promotion.md`). Biggest continuity risk
   (Valeriia's maternity leave).
2. **Close the clip→Typefully loop** — `social-content-studio` +
   `video-clip-cutter` skills exist and work; the remaining step is the
   auto-trigger on new Zoom/YouTube recordings (Zoom transcripts
   preferred — speaker-separated). Alexey's recording→agent forward
   pipeline (2026-10-07) is half of this.
3. **Turn on the todo + typefully plugins** (already built; the observed
   `/todo` and social-draft flows map 1:1).
4. **Formulaic email sends** (T4, T5, T9, T10, T11, T7a, T18 — parameter
   fill + approval; the payment-chasing ladder T10 is pure rules; the
   30-minute silence rule from 2026-08-10 is the approval policy).
5. **Monthly tax report auto-draft** (10/10 cycles, identical shape).
6. **Style gate as code** — Alexey's 17 rules
   (`valeriia/alexey-style-rules.md`) + his `stylint` should become the
   automated check every content draft passes before human review
   (the "voice/tone edit" is the one step Valeriia called herself the
   least efficient link in: "самое неэффективное звено", 2026-07-02).
