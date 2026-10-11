# Playbooks: Daily ops — calendar, Slack, website, Maven LLs (Grace)

Source: `team/telegram-analysis/reports/dtc-chat-grace-analysis.md`
(P8–P11, taxonomy 3.8–3.13). Condensed into one file: these are the daily
grind, each individually simple.

## A. Alexey's calendar management

**Trigger**: blocker requests, new events, or Grace noticing clashes.
**Steps**: create invites/placeholders (1h default, sometimes from raw JSON
datetime lists Alexey pastes); attach the right Zoom link; keep the calendar
as the single source of truth ("I have to plan so many events so I can
accidentally plan something else if I don't remember about this one");
flag clashes ("Oh but you have a call with Alex"); fix wrong dates Alexey
spots from his own calendar.
**Evidence**: calendar screenshot when proposing times.

## B. Slack community ops & moderation

**Trigger**: daily bot item "Invite people to Slack from <Airtable view>";
DM/spam reports.
**Steps**:
1. Process the Airtable queue → Slack invites.
2. Spam: deactivate per the no-spam policy; thank the reporter; draft the
   ban-notice reply for approval.
3. Member DMs: redirect to public/course channels with the standard reply
   ("Posting in the public channels ensures that the mentors and community
   experts can see your question…").
4. Impersonation/security → escalate to Alexey immediately.
**Frequency**: daily invites; moderation ~monthly.

## C. Website content updates (Airtable → GitHub)

**Trigger**: new person/event/podcast/episode or removal request.
**Steps**:
1. Fill the Airtable form, status ToDo, run the workflow.
2. Verify on the site.
3. Known fixes: SHA1 email-hash mismatch → update the hash in the GitHub
   `_people` folder; removals → delete the GitHub file + remove the event +
   prefix the podcast file with `_`.
4. If the GitHub action is green but content is missing → **flag to Alexey**
   (a restart is needed); never leave it silent.
**Evidence**: before/after screenshots; error logs.

## D. Maven Lightning Lesson creation

**Trigger**: Alexey's voice notes describing an event (or an article link),
sometimes with explicit skip-approval ("you don't need to run it by me just
publish and send me the link").
**Steps**:
1. Feed the transcript to the "Maven Prompt" (ChatGPT) — rules: concrete,
   not generic, avoid "strategic", series naming.
2. Post the draft (what-you'll-learn + bullets) for approval.
3. Create the LL on Maven: Canva cover, correct Zoom link, guest edit
   access enabled (fix from 2026-06-30).
4. Publish (or skip approval when granted); send the link to Alexey +
   Valeriia.
5. After the session: run the video pipeline (upload, cut, clips).
**Frequency**: ~2–4/month.

## E. Recurring hygiene (todo bot items)

- Invite people to Slack from Airtable (daily, ×179 in 2026)
- Create/update Trello cards (daily, ×179) — being folded into the unified
  ops system (ops.dtcdev.click, since 2026-08)
- Backup the Mailchimp mailing list to Google Drive (weekly-ish, ×36)
- Create a Slack dump (×10)
- "Make sure the newsletter for the next week is prepared" / "…for the week
  after next" (weekly, ×7 each)
