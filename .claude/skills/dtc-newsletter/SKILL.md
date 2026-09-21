---
name: dtc-newsletter
description: Assemble and draft the weekly DataTalks.Club newsletter (DataTalks.Club Weekly) from a fixed slot structure, including only the slots that have content that week. Use when asked to write, draft, plan, or review a DataTalks.Club Weekly issue or one of its slots, such as a promo slot, a Zoomcamp slot, a course registration slot, an event detail slot, the upcoming events list, Book of the Week, the Alexey on Data mention, or the latest recording; also use to export sent issues and click stats from Mailchimp. Do not use for Alexey's own newsletter or for registrant follow-up emails.
---

# DataTalks.Club Weekly

Use this skill to produce one issue of DataTalks.Club Weekly: a fixed sequence of slots, each written in DataTalks.Club's organizational voice. A slot appears only when it has content that week; empty slots are dropped without a placeholder.

## Workflow

1. Refresh the sent issues so calibration and numbering are current:
   ```bash
   python3 .claude/skills/dtc-newsletter/scripts/mailchimp_export.py --last 4
   ```
   It saves each sent issue (with its real links, subject line, and preview text) and its click stats to `newsletter/issues/`, and rewrites `newsletter/performance.md`. It needs `MAILCHIMP_API_KEY` in `.env`; if the key is missing, skip this step and say so.
2. Settle the send date (issues go out on Mondays) and create `newsletter/issues/<YYYY-MM-DD>-weekly-<N>/`.
3. Gather this week's facts from the repository root:
   ```bash
   ruby .claude/skills/dtc-newsletter/scripts/week_sources.rb --date <YYYY-MM-DD> --out newsletter/issues/<folder>/sources.md
   ```
   It reports the issue number, running Zoomcamps from the course platform (this week's module, deadlines, module materials, peer reviews, project submissions), upcoming events with times checked on Luma and speaker names, Book of the Week, recordings published in the last week, and new Alexey on Data posts.
4. Read `references/issue-structure.md` for the slot order and inclusion rules. Decide which slots are present from `sources.md`, `newsletter/sponsors.yaml` if it exists, and anything the user supplied.
5. Ask the user only for what the sources cannot supply, using `references/week-brief-template.md` as the checklist. Save the answers to `brief.md` in the issue folder.
6. Draft each present slot with `references/slots.md`. Read `../datatalks-event-promotion/references/datatalks-style.md` for the voice. For event detail slots, read the event's Luma page; for a recording slot, read the YouTube description or transcript; for Alexey on Data, read the post.
7. Read the two most recent sent issues in `newsletter/issues/` for calibration, and `newsletter/performance.md` when deciding what to feature or cut.
8. Save the draft as `issue.md` in the issue folder, using the output format in `references/issue-structure.md`, and run the final checks there.
9. The user copies the draft into Mailchimp. After the issue is sent, step 1 of the next run replaces `issue.md` with the sent text and keeps the draft as `draft.md`. Compare the two, and when the user's edits show a rule, update `references/slots.md` or `references/issue-structure.md`.

## Rules

- Mailchimp access is read-only. Never create, edit, schedule, test-send, or send a campaign, and never change audiences, without the user's explicit permission for that specific action.
- Draft only from supplied or fetched sources. Keep names, dates, times, promo codes, and links exactly as given. When a fact or link is missing, leave `TODO(...)` in the draft and list it in your reply; do not invent it.
- Take deadlines and event times from `sources.md` verbatim. They carry the correct CET or CEST label. The course platform is the source of truth for deadlines; if `course.yaml` disagrees, mention it.
- Sponsor copy is approved by the sponsor. Tighten it and fix obvious typos, but do not change claims, offers, or the call to action. Flag inconsistent spellings of names, such as a company spelled two ways.
- Never write the email template parts: the "DataTalks.Club Weekly #N" title, the tagline, "View this email in your browser", or the Slack invite and sign-off footer. The Mailchimp template adds them.
- Never commit or print the Mailchimp API key.

## Reference Map

- `references/issue-structure.md`: slot order, when each slot is present, subject line format, output file format, and final checks.
- `references/slots.md`: format, length, and examples for every slot.
- `references/week-brief-template.md`: what to collect from the user each week.
- `scripts/week_sources.rb`: fetches the facts for one send date.
- `scripts/mailchimp_export.py`: read-only export of sent issues and click stats.
