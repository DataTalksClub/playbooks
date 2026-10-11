# DataOps / DataOps-Knowledge — Automation Inventory and Gap Report

How DataTalks.Club automates (or plans to automate) the work of two human contractors:

- **Grace** — Operations Assistant / Program Operations Coordinator (the "dtc-chat" AI assistant team's human counterpart): course ops, community management, TODO tracking, Trello, Slack invites, newsletter support.
- **Valeriia** — Content & Social Media Manager: Telegram channel management for course cohorts, announcement copy, content calendars, course promotional posts.

Repos analyzed (clones current as of 2026-10-10):

- `C:\Users\User\git\dataops` (public, `DataTalksClub/dataops`)
- `C:\Users\User\git\dataops-knowledge` (private, `DataTalksClub/dataops-knowledge`)

---

## (a) Repo purposes

### dataops (public) — the operations portal and agent runtime

DataOps is the combined DataTalks.Club **operations portal** deployed at `ops.dtcdev.click`: a single TypeScript Lambda backend + vanilla-JS frontend (source: `README.md`, `AGENTS.md`). It merged three earlier systems: `dtc-operations` (process docs app), `datatasks` (task execution engine), and `podcast-assistant`. GitHub is the source of truth for markdown content; DynamoDB holds execution state; infra is SAM/CloudFormation deployed via GitHub Actions OIDC.

Key contents:

- `backend/src/conversation/` — the **conversational agent runtime**: one shared Telegram bot (single webhook `POST /api/webhook/telegram`), plugin registry, proposal/approval engine, TODO plugin, Typefully plugin. This is the code behind "dtc-chat".
- `backend/src/{cards,tasks,templates,cron,recurring,notifications}/` — the work engine (templates → cards → tasks, cron-triggered creation, reminders).
- `backend/src/{sponsorCrm,sponsorCommunications,sponsorFinance,invoices,bookkeeping}/` — sponsor and finance automation.
- `backend/src/calendar/`, `routes/newsletterSlots.ts`, `routes/emailDocuments.ts` — calendar, newsletter sponsor-slot booking, machine-to-machine email intake.
- `assistants/podcast/` — Python podcast assistant module (guest-intake → guest docs).
- `.agents/skills/loom-to-sop/` — agent skill turning Loom recordings into SOPs in dataops-knowledge.
- `docs/` — architecture specs, notably `conversational-agent-plugin-architecture/` (3 parts) and `operations-manager-platform-jtbd/` (3 parts).
- `backend/scripts/import-trello-csv.ts` — one-off migration that imported the Trello board + TODO spreadsheets into the work engine (Trello is legacy/replaced).

Important boundary (from `AGENTS.md`): the public repo holds product/runtime code only. All operational documents, SOPs, prompts, and private links belong in the private `dataops-knowledge` repo. The old `content/` dir in dataops has already been moved out.

### dataops-knowledge (private) — the Git-backed operating knowledge base

The private home for operating knowledge across DataTalks.Club, AI Shipping Labs, Maven/AI Engineering Buildcamp, and Founder Media & R&D. Operating model (from `README.md`):

```
business units + shared functions → business systems → workflows → SOPs/templates → evidence
```

- `content/<NN-department>/<business-system>/` — 11 numbered departments (`00-start-here` … `10-engineering-and-automation`, `90-archive`); each business system has `system-overview.md` plus `sops/`, `templates/`, `playbooks/`, `reference/` subfolders. Screenshots in `content/assets/<business-system>/<doc-slug>/`.
- `workflow-templates/*.yaml` — 24 authored workflow definitions (schema v2, validated), with generated read-only views in `content/00-start-here/workflow-catalog/reference/`.
- `document-templates/`, `schemas/` — authoring templates and JSON schemas.
- `scripts/` — ~25 Python validators/index builders (run via `uv` before commit).
- `_docs/` — operating-model registers (`role-registry.yaml`, `automation-opportunity-register.csv`, `system-gap-register.csv`, `weekly-roadmap.csv`), audits, plans.

---

## (b) Automation inventory

Maturity legend: **production** (deployed/used), **built-gated** (complete code, disabled/rollout-gated), **documented** (SOP/playbook for humans, no code), **stub** (placeholder page).

### dataops repo

| Path | Capability | What it does / trigger → output | Maturity |
|---|---|---|---|
| `backend/src/conversation/telegramWebhook.ts`, `telegramProtocol.ts`, `telegramMedia.ts`, `telegramOutbound.ts`, `telegramRecords.ts` | Shared Telegram bot ("dtc-chat") | One bot, one webhook, chat allowlist, verified-user identity binding; accepts text/voice/photos in private chats. Inbound intake for `/podcast`, `/social`, and general operations requests | Production (webhook live per `backend/README.md`); mutation plugins gated |
| `backend/src/conversation/todoPlugin.ts`, `todoCore.ts`, `todoWriter.ts` | TODO bot ("create a todo" via chat) | Natural-language todo in a private message → exact preview proposal → **human approval** → `task.create` effect (one actor-owned, date-only todo, Europe/Berlin TZ). Heavy input hardening (rejects multiple-item and time/reminder requests) | Built-gated: complete 850+ line implementation with crash recovery, but `plugins.ts` defaults `todoEnabled: false` behind rollout eligibility |
| `backend/src/conversation/typefullyPlugin.ts`, `typefullyExecutor.ts`, `typefullyGate.ts` | Social draft creation (Typefully) | "Draft a social post" → proposal with exact non-lossy preview → approval → creates an **unscheduled, unpublished saved draft** in Typefully (accounts: `alexey`, `datatalksclub`; platforms: X, LinkedIn). Delivery mode `operator_reconciliation_only` — publishing/scheduling explicitly forbidden | Built-gated (`typefullyEnabled: false` by default) |
| `backend/src/conversation/proposalCoordinator.ts`, `proposalTransactions.ts` | Human-in-the-loop approval engine | Every agent-requested mutation becomes an immutable proposal; executors receive only server-stored execution envelopes; exact approval required for all MVP mutations | Production architecture; powers both plugins above |
| `backend/src/result-notification-handler.ts` | Telegram result delivery | Sends assistant job results back to the Telegram chat that originated the request (bot token from AWS Secrets Manager) | Production |
| `backend/src/conversation/executionWorker.ts`, `zaiClient.ts` | Agent execution + LLM client | Executes conversational jobs against GLM (`glm-5.2` via z.ai Anthropic-compatible API); skill_load → skill_invoke two-turn pattern | Production |
| `backend/src/assistant/socialDraftAssistant.ts` | Legacy social-draft assistant | Retired — route returns `410` with pointer to the conversational Typefully flow | Retired (prior art) |
| `assistants/podcast/` (incl. `process/podcast.md`, `main.py`, `dry_run.py`) | Podcast prep assistant | Telegram `/podcast <notes>` routed as assistant job → Python module (Heru boundary, `HERU_ENGINE=codex|claude`) reads `inbox/raw/`, searches the podcast knowledge base, writes guest prep docs with house-style questions; explicit TODOs for missing facts | Production module with unit + opt-in integration tests; document format still flagged "temporary until final template provided" |
| `backend/src/cron/runner.ts` | Scheduled workflow instantiation | Scans templates with `triggerType: automatic`, evaluates cron schedules, creates cards with duplicate prevention | Production |
| `backend/src/sponsorCommunications/suggestions.ts` (+ `worker.ts`, `sesEvents.ts`) | Sponsor follow-up suggestions | Cron evaluator proposes booking confirmations, materials reminders (14/10/3 days before publication + overdue), publication-live and performance follow-up messages — suggestions only, human sends | Production (draft-or-recommend pattern) |
| `backend/src/routes/newsletterSlots.ts` | Newsletter sponsor-slot booking | Slot lifecycle `open → reserved → drafting → scheduled → sent → cancelled`, linked to sponsor CRM and cards | Production |
| `backend/src/routes/emailDocuments.ts` (`docs/email-document-intake.md`) | Email document intake API | Machine-to-machine metadata-only intake (e.g. invoice emails) from an upstream mail automation; secret-based auth, rate limiting, audit | Production |
| `backend/src/calendar/` (`docs/calendar.md`) | Operations calendar | Non-newsletter activities table, Berlin holiday layers with last-known-good generations, private workbook import (dry-run default) | Production |
| `backend/src/{sponsorCrm,sponsorFinance,invoices,bookkeeping}*` | Sponsor CRM / finance | CRM records, booking/finance alerts (cron), invoice prep, bookkeeping document import | Production (guarded manual migration for indexes noted in README) |
| `.agents/skills/loom-to-sop/SKILL.md` | Loom recording → SOPs | Agent skill: fetch Loom transcript+video, segment processes, extract frames, privacy-curate, draft one SOP per process into dataops-knowledge, validate, publish via portal | Production agent skill (recently used: bookkeeping SOPs from a September recording, per git history) |
| `backend/scripts/import-trello-csv.ts` | Trello/spreadsheet → work engine | One-off import of Trello board templates/cards + TODO CSVs | Completed migration (Trello replaced) |
| `docs/conversational-agent-plugin-architecture/` | Agent architecture spec | Goals, MVP decisions, approval model, plugin/skill framework, post-MVP roadmap (SOP editing, workflow execution, recurring work, web adapter) | Accepted spec, implementation tracked via issues |
| `docs/operations-manager-platform-jtbd/` | Operator product spec | Defines the daily loop for the operations manager — explicitly the Grace persona | Design doc |

### dataops-knowledge repo

| Path | Capability | What it does | Maturity |
|---|---|---|---|
| `workflow-templates/*.yaml` (24 files: newsletter, course, social-media, podcast, webinar, workshop, book-of-the-week, oss, tax-report, maven-ll, office-hours, operating-model w01–w13) | Workflow definitions | Schema-v2 YAML: outcome, owner role, tools, trigger (manual or automatic cron + lead days), phases with entry/exit criteria, tasks with day offsets, linked SOPs, required proof, closure conditions. `newsletter.yaml` triggers automatically (Mon 09:00, 14-day lead); `course.yaml` is manual | Production schema + validators; most templates `status: proposed` |
| `content/01-audience-growth/publish-weekly-newsletter/` (sops, templates) | Newsletter SOPs | Mailchimp draft assembly, sponsored block, scheduling, stats — all human procedures | Documented (Valeriia's execution domain) |
| `content/05-education-operations/launch-and-promote-course-cohorts/playbooks/` | Course promotion playbooks | `playbook-for-promoting-courses-at-dtc.md` (activities with timing offsets: pre-course Q&A −2wk, social posts −1mo, feedback posts −1wk; **names Valeriia as copy writer**; templates live in Google Docs) and `ml-zoomcamp-2025-promotion-playbook.md` (concrete instance) | Documented; `status: proposed`, not yet run-validated |
| `content/01-audience-growth/plan-and-publish-social-content/playbooks/` | Social promotion playbooks | 5 playbooks: new-live-event-announcement, book-of-the-week social promotion, OSS spotlight, post-podcast overview, upcoming-events promotion | Documented |
| Announcement templates across `01-audience-growth` / `03-programs-and-community` (Slack, LinkedIn, X, communities) | Copy templates | ~20 markdown templates for event/article/book announcements (Slack announcements channel, LinkedIn/X posts, cross-community posts) | Documented (static copy, not a queryable bank) |
| `content/01-audience-growth/publish-x-content/sops/saving-voice-notes-from-telegram.md` | Telegram voice-note → post workflow | Human SOP: open "DTC Chat" in Telegram → Groq Whisper transcription → ChatGPT summary → paste into Google Doc | Documented (manual, tool-assisted) |
| `content/05-education-operations/manage-course-data-and-registrations/sops/` | Course cohort ops SOPs | Airtable registration bases, Mailchimp tags + welcome automation, Airtable↔Mailchimp sync — human click-through procedures | Documented |
| `content/03-programs-and-community/operate-slack-community/` | Community SOPs | Slack bans for promo spam, account reactivation, data export, speaker images, event announcements | Documented |
| `content/00-start-here/operating-model/reference/current-role-coverage.md` | Division-of-labor doc | See section (c) | Draft (owner review pending) |
| `_docs/operating-model/automation-opportunity-register.csv` | Automation backlog | 45 candidate automations across 9 functions, all `draft-or-recommend`, each with human owner and prerequisite | Register (planning artifact) |
| `document-templates/agent-specification-template.md` | Agent governance template | Approval matrix (draft-only / approval-required / automatic-allowed), forbidden actions, kill switch, shadow-mode test plan | Template (control spec) |
| `scripts/generate_workflow_views.py` + `content/00-start-here/workflow-catalog/reference/` | Generated workflow views | Read-only markdown views of each workflow YAML | Production tooling |
| `_docs/plans/dataops-operating-model-integration/` | Memory-wiki plan | Seed/guideline/log/wiki for integrating the operating model with the dataops portal | Planning artifact |

Note on **Trello**: fully replaced. The work engine (templates/cards/tasks in DynamoDB + portal UI) is the Trello successor, seeded from a Trello export; `workflow-templates/*.yaml` are the canonical task templates, and the seeded users are literally Grace, Valeriia, and Alexey (`backend/src/deploymentSeeds.ts`).

Note on **Mailchimp / YouTube / Slack / Luma**: no API automation exists in either repo — all are human SOPs with screenshots. (A `youtube-manager` skill exists on this workstation but is not part of these repos.)

Note on **"todo bot"**: the intended product is the conversational TODO plugin above, plus the work-engine intake; the pre-dataops TODO workflow was a spreadsheet (`TODO list - todo.csv` / `done.csv`) imported by the Trello migration script.

---

## (c) Human / automation division of labor

The repos are unusually explicit about this. Canonical sources:

1. **`dataops-knowledge/content/00-start-here/operating-model/reference/current-role-coverage.md`** (draft, restricted-internal):

   | Person | Role | Scope |
   |---|---|---|
   | Alexey | Owner / individual entrepreneur | Founder/CEO + interim manager of most functions; **final decision authority across all functions**; goal is documentation + automation so he can *add* work, not just stop work |
   | Valeria | Freelancer; **maternity-leave continuity risk** | Content & Social Media Manager — owns DTC newsletter execution and social publishing (Alexey's personal + DTC channels) |
   | Grace | Part-time freelancer | Operations Assistant / Program Operations Coordinator — **executes most SOP-based work**: speaker outreach, calendars, event/program routines, delegated operational tasks |
   | External accountant | Specialist | Bookkeeping, close, tax |
   | AI agents | Digital execution capacity | **"Executor roles inside functions, never final accountable manager. Each agent needs a human owner, permitted actions, approval mode, evidence, exception path and kill switch."** |

2. **`_docs/operating-model/automation-opportunity-register.csv`** — 45 rows, every one `default_mode: draft-or-recommend`, with the uniform risk note: *"Do not automate external side effects or promises until approval policy is validated."* Owners: F05 Marketing & Content → "Alexey + Valeria; continuity risk"; F06 Community → "Vacant; Alexey covers ASL ad hoc; **Grace executes routines**"; F08 Operations → "Alexey accountable; **Grace executes most SOP-based work**".

3. **Q4 2026 roadmap** (`content/00-start-here/operating-model/reference/q4-operating-system-roadmap.md` + weekly files):
   - **W02 (2026-09-17) "Document and hand over content operations"** — content-operations inventory, newsletter decision guide, social publishing guide, handover checklist, automation candidates. This is the Valeriia-continuity work; systems G027–G031 (editorial calendar, content-ops transfer, SEO, founder pipeline, attribution) exist as draft stubs.
   - **W06 (2026-10-15, i.e. next week) "Organize Operations and agent queues"** — output includes *operations queue, waiting-on-Alexey view, exception taxonomy, **Grace role card**, agent work-queue standard*. The human-decisions slot asks: *"Approval thresholds; escalation SLAs; **which routines Grace owns end-to-end; what agents may do automatically**."*

4. **`dataops/docs/operations-manager-platform-jtbd/part-1-user-context-and-daily-loop.md`** — the portal's primary user is the operations manager; *"The imported work-engine specification names this person as Grace, but the product should not be built around one hard-coded person."* Describes the four daily questions (what's due, what's late/blocked, who needs a follow-up, which workflows are at risk) and the tool sprawl (Trello-like cards, Sheets, Calendar, Slack, Mailchimp, Luma, Meetup, YouTube, Airtable, Telegram…).

5. **`dataops/docs/conversational-agent-plugin-architecture/part-1-goals-decisions-and-approval-model.md`** — the operating contract for agent automation: every mutation is an immutable proposal requiring exact human approval; channel-neutral runtime; agents cannot self-grant permissions; external side effects (publishing, scheduling) excluded from MVP.

6. **`dataops-knowledge/document-templates/agent-specification-template.md`** — per-agent control spec: approval matrix, forbidden actions, evidence, exceptions/timeout/escalation, kill switch, shadow → approval → production rollout.

7. **Seed data** (`dataops/backend/src/deploymentSeeds.ts`): users Grace, Valeriia, Alexey (all admin). All workflow templates default-assign to Grace's user ID; `course.yaml` assigns "Prepare the description for the event" specifically to Valeriia's ID — matching the playbook text that Valeriia writes event descriptions.

**Summary of the model:** humans own outcomes (Alexey final authority; Valeriia content outcomes; Grace routine execution); agents may only *draft or recommend* under a named human manager, with exact-approval gates for every mutation and no automated external side effects. The Telegram bot is the operator's interface, not an autonomous actor.

---

## (d) Playbook / runbook authoring conventions (for staging new playbooks to migrate later)

These two repos do **not** use "runbook"; the house term is **SOP / playbook / template / workflow**, governed by frontmatter schemas. New playbooks authored elsewhere should follow these rules to migrate cleanly into `dataops-knowledge`.

### Location and naming

- Path: `content/<NN-department>/<business-system>/{system-overview.md, sops/, templates/, playbooks/, reference/}`. Relevant departments: `01-audience-growth` (newsletters, social, website), `03-programs-and-community` (Slack, events, campaigns), `04-content-production` (podcasts, video, YouTube), `05-education-operations` (course cohorts, Maven), `07-internal-operations` (systems library, communications).
- Filename = kebab-case of the title (enforced by `scripts/align_document_filenames.py`).
- ID convention: dotted stable IDs `<doctype>.<department-token>.<system-token>.<slug>`, e.g. `playbook.courses.playbook-for-promoting-courses-at-dtc`, `sop.finance.bookkeeping.get-invoices-from-mailchimp`, `sop.social-media.twitter.saving-voice-notes-from-telegram`. Legacy paths go in `aliases:`.

### Frontmatter (validated by `schemas/document-metadata.schema.json`)

Required in practice: `id`, `title`, `summary`, `doc_type`, `schema_version: 1`, `department`, `business_system`, `owner_role`, `status`, `criticality`, `confidentiality`, `review_cycle_days`, `last_reviewed_at`, `next_reviewed_at`, `tags`, `tools`, `related_docs`, `source`.

- `doc_type` enum: `sop | template | reference | task-template | playbook | checklist | prompt | system-overview | archive | process | doc`.
- `status` lifecycle: `draft → proposed → active` (after a validated real run), then `review-due` when `next_review_at` passes; also `blocked / deprecated / archived`.
- `criticality`: `core | supporting | historical`. `confidentiality`: `public | internal | restricted | restricted-internal`.
- `tools` = lowercase platform slugs (`mailchimp`, `typefully`, `slack`, `telegram`, `luma`…) — metadata, never the taxonomy.
- `source` = provenance (often the original Google Doc path or recording URL); recordings also under `training_assets` (a `loom:` key is rejected as deprecated).

### Body shape

- **SOPs**: `Summary` (Purpose / Outcome / Trigger / Frequency), `Prerequisites` (Access / Tools / Inputs / Safety), `Procedure` (numbered steps wrapped in HTML-comment markers `<!-- sop-section-start: … -->`, `<!-- sop-step-start id=N -->`, `<!-- sop-screenshot-start -->` + caption), `Validation`, `Troubleshooting`, `References`. Spec: `dataops/docs/sop-format.md`; lint via `make sop-lint` in dataops. One outcome per document; steps must stand without the video; person names replaced by roles.
- **Playbooks** (`doc_type: playbook`): lighter — `Summary` + `Content` organized as timed activities (e.g. "1 Pre-course Q&A (2 weeks before the course start)"), with per-person subsections (the course playbook has "Ceth part" / "Valeriia" headings), inline links to copy templates (currently Google Docs), and a `References` block listing owning system IDs. See `content/05-education-operations/launch-and-promote-course-cohorts/playbooks/playbook-for-promoting-courses-at-dtc.md`.
- **Templates** (`doc_type: template`): ready-to-copy copy skeletons (announcement emails/posts) with the same frontmatter.
- **Workflows**: authored YAML in `workflow-templates/<type>.yaml` (schema `schemas/workflow-template.schema.json`, v2): `outcome`, `owner_role`, `tools`, `trigger` (`mode: manual|automatic`, cron `schedule`, `lead_days`), `phases` (entry/exit criteria, `allowed_next_phase_ids`), `tasks` (`id`, `name`, `schedule.offset_days`, `task_kind: procedure|checklist|milestone|milestone-plus-publication`, `owner_role`, `instruction_doc_id` → SOP, `tools`, required `proof`, `closure`, `validation`). Read-only views are generated — never hand-edit `workflow-catalog/reference/`.

### Validation and publication

- Before commit: `uv run --with pyyaml --with jsonschema python -m unittest discover -s tests -v` plus the four validators (`validate_workflow_templates.py`, `validate_document_metadata.py`, `build_system_catalog.py --check`, `validate_operating_model.py`).
- Publishing goes **through the portal** (`POST /knowledge/publish` or editor save): the portal reads its own S3 store; a git push alone never goes live, and the daily store-to-GitHub mirror deletes managed `content/` files never published to the store (per loom-to-sop skill).
- New content ships as `status: proposed` (SOPs from the loom-to-sop pipeline ship `active` with real review dates); enrichment happens after an owner validates a real run.

---

## (e) Gaps — Grace/Valeriia work with NO automation yet

1. **Telegram *outbound* / cohort channel management — the biggest gap.** The DataOps bot is inbound-only (intake, clarifications, proposals, approvals, result notifications to allowed private chats). Nothing posts, schedules, or manages **Telegram channels** (course cohort announcement channels). No SOP, no template, and no playbook exists for cohort-channel management either — Telegram appears only as (a) the "DTC Chat" internal chat humans already use, (b) a place where humans *receive* reminders, (c) a handoff target ("send YouTube link to DTC Content team in Telegram"), and (d) the voice-note source SOP. Any new Telegram-announcement playbook would be net-new.
2. **Copy bank.** No structured, queryable copy bank. Announcement copy lives in ~20 scattered `templates/*.md` and, worse, in linked Google Docs (course playbook description templates are GDocs). The closest prior art is `content/07-internal-operations/manage-operating-communications/templates/datatalks-club-email-template-index.md` (an index of email templates).
3. **Content / editorial calendar.** The system pages (`manage-marketing-strategy-and-editorial-calendar` G027, `manage-founder-content-pipeline` G030) are draft stubs; no calendar automation. The dataops `calendar/` module tracks Alexey's schedule/holidays only, not a content calendar.
4. **Social publishing end-to-end.** Typefully plugin creates unscheduled drafts only, and it is rollout-gated off. Scheduling/publishing on X/LinkedIn remains human (Valeriia), via the `social-media.yaml` weekly workflow tasks.
5. **Newsletter assembly in Mailchimp.** Slot booking (newsletterSlots API) is automated; Mailchimp draft assembly, sponsored blocks, scheduling, and stats are human SOPs (`sop.newsletter.mailchimp.*`).
6. **Community management (Grace's F06 domain).** Slack invites/reactivation/moderation, member health, check-ins, onboarding concierge — all documented as future automation opportunities only (register rows A-F06-01…05); no code.
7. **Task/workflow *execution*.** Cron auto-creates cards from templates (good), but executing a task — following the SOP and attaching proof — is fully human. The plugin architecture lists "workflow execution, recurring work" as post-MVP.
8. **Escalation/exception queues.** Architecture supports exceptions conceptually (agent spec template has an escalation section; W06 plans an exception taxonomy and waiting-on-Alexey view), but nothing is implemented.
9. **Agent-to-agent communication.** No multi-agent orchestration in either repo; one mutation plugin may be active at a time, by design.
10. **YouTube, Luma, Meetup, Airtable, Canva.** Human SOPs with screenshots only.

Also note: both conversational plugins are **built but disabled in production** (`backend/src/conversation/plugins.ts` defaults both to `false`), so even the existing todo/social-draft automation is not yet live.

---

## (f) Prior art for replacing/documenting Grace's and Valeriia's workflows

- **The JTBD spec literally models Grace**: `dataops/docs/operations-manager-platform-jtbd/` — daily loop, reminders, follow-ups, proof-gated completion, screens and roadmap for the operator role.
- **The automation backlog**: `_docs/operating-model/automation-opportunity-register.csv` (45 draft-or-recommend candidates incl. all of Valeriia's F05 and Grace's F06/F08 routines) and `_docs/operating-model/system-gap-register.csv` (missing systems).
- **Valeriia handover is an explicit planned deliverable**: Q4 roadmap W02 "Document and hand over content operations" + system `G028 document-and-transfer-content-operations` (draft stub) — driven by her maternity-leave continuity risk.
- **Grace role formalization is scheduled**: W06 (2026-10-15) "Grace role card" + agent work-queue standard + "which routines Grace owns end-to-end".
- **The dtc-chat replacement skeleton exists and is hardened**: `conversational-agent-plugin-architecture/` (approval model, plugin/skill framework, post-MVP roadmap) plus the working todo/typefully plugins, the podcast skill pipeline, and `result-notification-handler` — the pattern to extend for new capabilities.
- **The documentation factory**: `.agents/skills/loom-to-sop/SKILL.md` + `content/07-internal-operations/manage-systems-library/sops/draft-an-sop-from-a-recorded-task.md` — the established way a human's recorded workflow becomes governed, screenshot-backed SOPs (already applied to bookkeeping).
- **Workflow templates as executable job descriptions**: the 24 YAML workflows encode exactly who does what, when (offset days), with which SOP and proof — e.g. `course.yaml` assigns Valeriia the event description; all templates default to Grace.
- **Trello precedent**: `backend/scripts/import-trello-csv.ts` shows the migration pattern (export → seed → replace) used when a contractor tool (Trello) was absorbed into DataOps.
- **Agent governance template**: `dataops-knowledge/document-templates/agent-specification-template.md` — the required control spec (approval matrix, kill switch, shadow mode) for any new agent taking over human work.

### Quick SWAG of where new Telegram/cohort playbooks would land

Per conventions in (d): `content/05-education-operations/launch-and-promote-course-cohorts/playbooks/` or a cohort-comms system for announcement playbooks; `templates/` for copy; `doc_type: playbook`, `tools: [telegram, …]`, `status: proposed`, IDs like `playbook.education.course.<slug>`; workflow changes via `workflow-templates/course.yaml` tasks; publication through the portal, not raw git push.
