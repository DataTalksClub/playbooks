# Playbooks: The two newsletters (Valeriia)

Source: `team/telegram-analysis/reports/valeriia-analysis.md` §3C, §3A,
playbooks 1–2. Evidence dates cited there.

## A. Alexey on Data / AI Shipping Blog (personal Substack, Fridays)

**Cadence**: weekly, published Friday ~09:00–13:00 CET (a second weekly
"по средам" post existed mid-year). Renamed to aishippingblog.com on
2026-08-20.

**The loop**:
1. Alexey brain-dumps voice notes into the Telegram Writing Assistant bot;
   article drafts land in `telegram-writing-assistant/articles/ready-for-newsletter/`
   (the bot is his logging mechanism; drafts are lossy — see friction).
   Better source when available: workshop/event notes on aishippinglabs.com
   generated from recordings ("гораздо проще с этим работать").
2. Valeriia makes the **first edit in a Google Doc** — this draft is an
   idea/fact check, not a polish pass (agreed 2026-04-24): "первый черновик
   был для проверки идей, всё ли там правильно по смыслу и фактам".
3. Alexey comments inline or by voice (1–3 rounds); she applies.
4. Assemble the issue: main article + "What I've been working on recently"
   (bot weekly-log) + "My experiments" + Tools & Resources. She writes the
   non-main sections herself when the bot log is empty.
5. Paste into a Substack draft; publish Friday (or he presses send).
6. X repost of the article ~1 week later (2026-04-06 rule).
7. Keep 1–2 newsletters prepared ahead (for his travels — 2026-07-25).

**Decisions needing Alexey**: topic choice when ambiguous ("мне сложно одной
выбирать" — she asks), structure rewrites.

**Style gate**: `alexey-style-rules.md`; AI-detector 0%.

## B. DataTalks.Club Weekly (Mondays ~10:00, Mailchimp → migrating off)

**Cadence**: weekly; test email to Alexey first, he reviews, she schedules.

**Current preparation sequence (owner update, October 15, 2026)**: Valeriia prepares editorial content at the end of the week or on Monday, after fresh event listings and Alexey's latest article are available. Collect sponsor inputs earlier when needed, but refresh editorial facts near sending. Fetch the full course inventory, then apply newsletter scope (ML and AI Dev Tools; SMA is excluded). Review recent sent issues, write the complete text in `newsletter/issues/<YYYY-MM-DD>-weekly-<N>/issue.md`, save sources and decisions alongside it, and commit the files. Review and correct Markdown first; transfer that exact version to Mailchimp only when separately requested. Check every saved block against the committed text. Test sends, scheduling and sending remain separate actions.

**Slot structure**: Primary (sponsor) + Secondary (sponsor) + editorial
content; standalone sends separate (Wednesday is the best standalone day).
Monday-only rule for regular slots.

**Sponsor slot rules**: copy must have no "we/us" (house rule), ≤6 lines,
clear CTA, working links; weak copy → proactively send our rewrite
(Nebius pattern, 2026-02-09). Test email ("[Test] …") before the send.

**The silent-sponsor escalation ladder** (codified 2026-04-24/27 after the
Snowflake incident): reminder → CC the boss as last resort → replace the
slot (possibly with a free goodwill promo) + inform the sponsor.

**Empty slot?** Default to course promo — "Может быть твой курс"
(2026-09-07); pull matching posts/images from the course library
(2026-06-08, 2026-09-21).

**Historical send rule, superseded for agent execution** (Alexey, 2026-08-10): "если я не отвечаю то в принципе можно
отправлять не дожидаясь… например после получаса молчания" — 30 minutes of
silence was treated as approval in that historical exchange. Current agent execution requires explicit permission for the specific send; silence is not approval.

**Post-send**: stats to the sponsor after ~1 week (Grace's T5 template);
sponsor-slot performance numbers flow into her reporting.

**Migration note** (2026-08-31): Alexey is moving off Mailchimp — module
emails and eventually the newsletter go through the site/agent pipeline
("агент… поставит их в расписание").
