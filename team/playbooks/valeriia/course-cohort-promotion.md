# Playbook: Course cohort promotion machine (Valeriia)

Source: `team/telegram-analysis/reports/valeriia-analysis.md` §3B, §6,
playbook 4. This is the biggest single automation target: per-cohort
campaigns that recur for every course, with copy already living in
`DataTalksClub/playbooks` (this repo).

**Alexey's stated intent** (2026-07-01): "по каждому курсу был плейбук с
контентом. Тогда можно будет заниматься другими делами, а курсы сами будут
продвигаться" — a playbook per course so courses promote themselves.
Validated on ML Zoomcamp (2026-08-03: "вообще отлично все прошло").

## Where copy comes from (in this repo)

- `courses/<course>/copy-bank/email/` — module-start emails (markdown)
- `courses/<course>/copy-bank/telegram/` — weekly course-channel updates
  (Valeriia authored the AI-Dev-Tools versions, 2026-08-31; updated to the
  new schedule when it moved off Mailchimp)
- `courses/ai-engineering-buildcamp/posts/` — Buildcamp post library +
  lightning-lesson libraries (2026-09-08)
- Prior-year copy adapted ("точно так же можно сделать… грейс спросить их
  отправлять в следующем году", 2026-01-13)
- Fresh material: Alexey's voice dumps → Telegram Writing Assistant →
  her edit; Substack module articles (AI DevTools experiment, 2026-07);
  event notes generated from recordings

Since 2026-08-31 module emails/Telegram updates are sent via the
site/agent pipeline on a schedule — not Mailchimp.

## The cohort campaign sequence (observed timing)

1. **T−6…2 weeks — registration opens**: course-platform registration page
   (`courses.datatalks.club/register/<course>/`, with visible registration
   counts — her request, 2026-07-01) + announcement posts + newsletter
   feature + README refresh + pre-course event promo.
2. **T−2 weeks — scholarship window**: fresh form clone; deadline 2 weeks
   before start; the 5-post sequence: announce → how-to-write →
   partial-scholarship → last call (−1 week) → last call (−1 day)
   (2026-08-26); results post + "sorry, partial still open" (2026-09-15).
3. **T−1 week → day 0 — countdown**: countdown posts, promo-code post
   (SUBSTACK 20%, EARLYBIRD 30%, DTCLOVESYOU, CODEAGENT 15% — 2026-09-08),
   launch-stream promo, milestone posts.
4. **Week 1 — buffer**: "deadline extended, second week is buffer" posts
   (2026-04-12, 2026-09-21); module-1 email; pinned navigation message in
   the course Telegram channel (she authored, 2026-07-07).
5. **Weekly — module rhythm**: module-start email + course-Telegram update
   + 1–3 social posts per module (workshop recaps from clips); homework
   and deadline reminders; sponsored-module promo as a 3-post pattern
   (Kestra, dictated 2026-06-17); Q&A stream promos; contest mechanics
   (Bruin Mac-mini giveaway, Kestra blog-post contest).
6. **Mid-course**: capstone pushes ("вторая попытка… не забудьте сделать
   ревью", 2026-02-09); office hours for ASL members.
7. **End**: certificate generation (his script) → certificates post in all
   channels with enrollment-profile link + "(make sure you're logged in)"
   + sponsor-thanks post + demo-day article + stats post.
8. **Between cohorts**: archive the cohort's posts into the course
   library; evergreen reuse.

## Course channel management

She is admin of the per-course Telegram channels (asked to be added
2026-01-19); weekly channel updates come from the copy-bank; registration
moved from Airtable to the course platform (2026-07-01).

## Decisions needing Alexey

Promo codes and their percentages; deadline extensions; slot swaps in the
newsletter; scholarship outcomes; anything money-related.

## Frequency

Continuous across the year: DE Zoomcamp (Jan), Buildcamp cohorts (Apr 13,
Sep 21 + "last call" — none until 2027), LLM Zoomcamp (Jun 8 launch →
modules → project), AI Dev Tools 2026 (reg open Jul, start Sep 1),
ML Zoomcamp certs (Feb), plus evergreen AI Hero.
