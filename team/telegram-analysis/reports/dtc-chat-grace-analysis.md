# How Alexey Grigorev Works with Grace (DTC Ops Chat, 2026)

Analysis of the Telegram chat "dtc-chat", 2026-01-01 → 2026-10-09 (~5,830 rendered lines / 2,615 JSONL messages).
All quotes verbatim from the export (original spelling/typos kept). Counts computed from `data/dtc-chat-2026.jsonl`.
August–October 2026 is treated as the current way of working; earlier months are history/context and changes are noted.

---

## 1. Overview

### Volume

| Metric | Value |
|---|---|
| Total messages | 2,615 |
| Alexey | 1,364 (52%) |
| Grace | 775 (30%) |
| todo bot | 475 (18%) |
| (Marina Zavgorodnyaya) | 1 (Alexey pasted her reply into the chat on 2026-03-18) |
| Period | 2026-01-01 06:00 → 2026-10-09 19:19 |
| Days with any message | 227 of 282 |
| Alexey active days | 196; Grace active days | 171 |

**Media mix** (from JSONL `media` fields):
- Alexey: **255 voice notes** (transcribed inline in this render), 85 photos, 45 files (invoices/PDFs), 3 link-media. ~4 of his messages are empty with no usable transcript; several voice transcripts are garbled (Polish/Romanian-looking text) — see Limitations.
- Grace: **531 photos (screenshots) + 4 files**, **0 voice messages**. Screenshots are her default evidence artifact; their *content* is not available in this export.
- todo bot: 475 structured texts.

**Monthly message volume (Alexey / Grace / bot)**: Jan 172/86/68, Feb 179/87/51, Mar 154/85/12, Apr 127/90/55, May 177/74/56, Jun 225/114/57, Jul 89/58/55, Aug 137/92/55, Sep 65/64/49, Oct(1-9) 39/25/17. March's bot drop is a bot outage, not a process change (Alexey 2026-02-20 "I'm just testing the bot - I moved it to a different server"; 2026-03-26 "I fixed the bot").

### The cast

- **Alexey Grigorev** — founder of DataTalks.Club; host/instructor of podcasts, webinars, workshops, Maven courses (AI Engineering Buildcamp, LLM Zoomcamp, DE Zoomcamp, AI Dev Tools Zoomcamp, AI Shipping Labs). Delegates all operations.
- **Grace** — operations assistant / "community manager" (her own email signature in drafts: "I'm Grace and I'm taking care of organizing events at DataTalks.Club"). Executes events, invoices, bookkeeping, YouTube, sponsor comms, scheduling, website/Airtable, Slack moderation. Based in an Asia-Pacific timezone (2026-01-23 10:36 Berlin Alexey: "it's not good morning for you, it's a good day, right?"; Grace: "yes its afternoon in here already☺️").
- **todo bot** — posts recurring intake items at 05:00/06:00 Berlin time and confirms Alexey's `/todo` commands ("Done! Message saved to the todo list!"). Recurring items over the period: "Invite people to Slack from https://airtable.com/appbZvzANm1074oQx/..." ×179, "Create new trello cards if necessary and go through existing ones" ×179, "Backup the mailing list from mailchimp to google drive" ×36, "Create a slack dump" ×10, "Make sure the newsletter for the next week is prepared" / "Prepare a newsletter for the week after next" ×7 each. These recur **daily through Oct 9, 2026** — still the backbone intake.
- Referenced third parties (not in chat): **Valeriia** (content/social, has her own "content chat" channel with Alexey+Grace), **Dave** (podcast audio editor), **Alena/dltHub** (organizer contact), sponsors' contacts.

### What the chat is for

Grace ↔ Alexey's single operational channel: delegation intake (todo bot + `/todo`), draft approvals, scheduling confirmations, invoice/bookkeeping assembly, YouTube/video pipeline reporting, sponsor and platform issues, process documentation. It is the system of record for "Grace asks → Alexey approves → Grace executes → Grace reports back with screenshot + link".

### Working rhythm

- **Reply latency** (gap < 4h between counterpart messages): Alexey answers Grace with **median ~11 min** (p90 ~2.2h); Grace answers Alexey with **median ~14 min** (p90 ~1.9h). Same-hour turnaround is the norm during overlapping hours.
- **Active hours** (chat timestamps = Berlin): Alexey spreads 07:00–24:00, peak 09:00–11:00 (209+205 msgs). Grace works ~08:00–17:00 Berlin with peak 09:00–11:00 (203+174) — i.e., her late afternoon/evening — plus occasional 00:00–05:00 Berlin slots (her daytime; e.g., 2026-02-23 02:37, 2026-06-28 00:03 when she fixed a calendar clash on a Sunday evening her time).
- **Weeks run Mon–Fri**: Mon 491 / Tue 430 / Wed 398 / Thu 396 / Fri 292 human messages; weekends 132 total (Alexey 100, Grace 32 — she does reply on weekends when events break, e.g. 2026-06-28).
- **Daily cadence**: bot posts 05:00; Grace's morning bundle lands 09:00–11:00 Berlin ("Hi Alexey," + numbered asks + screenshots); Alexey batch-approves; execution and reporting flow through the day.
- Grace's staples: "Thank you" variants ×306, "Kindly advise" ×89, "works for you" ×81, "Kindly check" ×47, "for your checking" ×43, "for any changes needed" ×41, "Here is the draft(ed)…" ×56. Alexey's staples: "Yes" ×90, thanks in 175 messages, "Looks good/great/okay" ×22.

---

## 2. How Alexey delegates

### Input forms (in rough order of frequency)

1. **Voice-note brain dumps** (255 total; often 2–4 in a row). He narrates context, intent, and preferred outcome; expects Grace (or ChatGPT) to structure it. Example 2026-01-07 08:19 (53s): "So I'll be sending you some links Also, please find the YouTube video … and Combine these all the statistics … So let's then show them this per resource, per link and then show the aggregated statistics."
2. **`/todo` command** (57 confirmed, ~64 textual occurrences). Text one-liners, often minimal: "podcast guest" (2026-02-09); "invoice dlthub (workshop 10k)" (2026-03-04); "webinar" (2026-02-27); "invoices: Kestra 20k sponsoring LLM Zoomcamp module; dlthub 5k for LLM Zoomcamp workshop" (2026-08-10); "during todays workshop I had two breaks - at 14:54 and at 16:05 (I started aroud 13:55). Please find them and remove them" (2026-08-10). Occasionally typo'd "/please" (2026-02-09).
3. **Link + one-line instruction**. Loom links for process docs ("https://www.loom.com/share/… please create process doc - uploading videos from maven LL to YouTube" 2026-01-06), Zoom recording links with passcode (2026-05-04, 2026-06-25, 2026-08-08), YouTube playlist links ("please add videos from this playlist to DE Zoomcamp playlist" 2026-01-22), GitHub copy-bank files (2026-08-04: "/todo please create an event: https://github.com/DataTalksClub/playbooks/…/03-2026-08-10-test-containerize-deploy.md").
4. **Email + contact forwarding**: pastes an email address and a LinkedIn URL, sometimes with a one-line brief and context flags: "ruslan.shchuchkin@gmail.com (he was already a guest - also Mariano)" (2026-02-10); "gustaf.gyllensporre@gmail.com … for Gustaf - he has an interesting story about him transitioning from a real estate agent to AI engineer" (2026-06-04); "w.brett.coleman@gmail.com / invite for podcast … Topic: his interview experience for the forward deployed engineer role" (2026-07-27).
5. **Files**: PDFs/statements for bookkeeping (e.g., 2026-02-10 five files in a row: "openai invoices… booking… airbnb… uber"; 2026-10-05 six receipts in one burst). Photos (screenshots of payments — "Astronomer paid" 2026-03-18, "They paid" 2026-05-22, "Both paid" 2026-06-24, "Kestra paid" 2026-09-07).
6. **Dictated content for ChatGPT**: 2026-02-04 he dictates three full event descriptions by voice for Grace to "paste these things to your GPT and turn them into light[n]ing less[on] descriptions"; 2026-07-31 he pastes an AI-formatted event brief plus instructions.

### Typical phrasing (verbatim)

- "Hey Grace are you here?" then the ask (2026-01-28, 2026-01-14, 2026-06-25).
- "/todo check all planned events taht there's no mismatch between calendar and luma, meetup and linkedin" (2026-01-06).
- "/todo start the workshop process for March 10 (I already create a time blocker - check my calendar) josh.reini@snowflake.com krista.rockson@snowflake.com" (2026-01-21).
- "For Monday 5 p.m. can you please create a lightning lesson with title forward deployed engineer I will send you an article use the beginning of this article to fill it in you don't need to run it by me just publish and send me the link when it's ready" (2026-07-31) — note explicit *skip-approval* grant.
- "24 Feb 17 / 3 March 17 / 9 March 18:00" + voice: "I want to organize some lighting lessons … Can you please make a blocker in my calendar for this?" (2026-02-04).
- "Can you please remind snowflake about the payments? Also have we sent an invoice to jetbrains?" (2026-05-25).
- "please don't forget to chop the videos after editing so we can post them on social media / I think we haven't been doing it lately" (2026-08-18).
- "I just realized that with Ruslan I didn't save the audio … so can you please create the podcast episode from video?" (2026-03-19) — self-caught gaps.
- "Are we having it? I think she didn't prepare anything" (2026-09-14) — spot-checks via his calendar.

### What context he includes / omits

- **Includes**: links (Loom/Zoom/YouTube/GitHub), contact emails, occasionally prices ("It's 5000 Eur" 2026-01-21), date constraints ("he wants a date in June" 2026-04-07), and pointers to prior art ("check what we did last two times for the demo days" 2026-06-04).
- **Omits**: deadlines (rarely stated; implicit), full company/sponsor context (expects Grace to pull from Finom/contracts/Airtable: "you have all the details there like price, invoice items, etc also who to send" 2026-05-26), precise amounts sometimes wrong or corrected later ("Correction: 700 USD" then "Cancel it. Don't send anything" 2026-09-28), and sometimes the fact that he already did part of the task himself ("I'll take care of uploading the zoom video I forwarded yesterday but please take care of the rest" 2026-01-14; "I just banned Adam" 2026-02-17; "I edited the begining now - it's processing" 2026-05-11).
- He compensates for memory load explicitly: "I'm very busy today and tomorrow / Can you please remind me about it on Wednesday?" (2026-03-09); "sometimes now I have too much work, so I tend to forget about these things" (2026-02-11 voice).

### Follow-up style

- Presence checks: "are you here?" ×3; "are we ready with trello?" (2026-08-11).
- Status nudges: "what's the status of this?" (2026-01-09); "Did we send invoices to Kestra and dlt for LLM Zoomcamp? They haven't paid yet" (2026-09-04); "did you have a chance to take care of the office hours video?" (2026-02-10); "Did she reply?" (2026-10-01).
- Appreciation is frequent and warm: "You're the best" (2026-02-03); "You're amazing, thank you!" (2026-02-17); "you did a lot of stuff today - thanks a lot. I appreciate your help!" (2026-06-15); "Thanks a lot Grace - really appreciate your help!" (2026-10-06); "I'm going a bit crazy with my calendar so thanks for keeping me sane" (2026-06-28).

### Corrections / redirects

- Small, immediate, blame-light: "can you please use DD.MM.YYYY format? I'll edit this one" (2026-02-10); "Alexey's My substack Account Post -> Alexey's Substack … so remove 'Account Post', it feels repetetive" (2026-01-07); "Let's do June 16" overriding own suggestion (2026-04-25); "Ignore my comment about Tuesday" (2026-05-05).
- Iterating on ChatGPT output via Grace: "can you make ask it to make it less abstract and based on the one what I said so … it cannot come up with new things" (2026-02-05); "Can you please adjust the prompt that we use? Ask it to make it more concrete and less generic and avoid using words like strategic … when you update the prompt please show it to me" (2026-02-05).
- Post-incident process patches: after a Luma/calendar mismatch "Please make sure it doesn't happen again … please try to make sure that the time is always aligned" (2026-01-06); after a midnight-timezone Meetup error "Maybe we can have a step in the process to double check the time zone" (2026-05-30); after a Zoom-link leak "I'll create a new link … update all the future events that use the the old link to the new one" (2026-06-08).
- Meta-feedback on communication format: "Usually when you ask if something works for me or not you also send calendar screenshots … I like it when you do that =)" (2026-04-25); "can you please next time write instead of one message like each separate topic in separate messages this way is more convenient for me to reply" (2026-08-10).
- Process-discipline push (one-off, early in year): "our processes are very important - they make sure we can continue running our business … please take this seriously, okay?" + "please send me the steps for the LL process in this format - step description - docment link - docment link" (2026-02-03).

### Anatomy of a typical delegation (end-to-end)

1. Alexey drops minimal input (voice/link/email + `/todo` or plain text).
2. Grace acknowledges ("Got it, thank youu^^" ×41; "on it" ×7).
3. Grace does lookups (calendar, Finom, Airtable, contracts, LinkedIn), drafts the artifact (email/invoice/event/description).
4. Grace posts **draft + screenshot(s) + "Kindly check … for any changes needed"**.
5. Alexey replies short ("Looks good" / "Yes" / 1–3 line corrections), often < 30 min.
6. Grace executes, then reports completion with evidence ("Adjusted and sent, thank youuu" 2026-01-05; "It has been moved from DE Zoomcamp to DE Zoomcamp 2025" + screenshots 2026-01-13; "email has been sent to Atlan" 2026-03-20).
7. Occasionally a follow-up loop (payment chasing, transcript waits) re-opens the thread days later.

---

## 3. Task taxonomy

Ordered by observed frequency × business weight. "Grace mentions" = messages containing the keyword (undercounts actual work, since much is visible only in screenshots).

### 3.1 Scheduling & date negotiation (podcasts / webinars / workshops / LLs / book-of-the-week)
- **Trigger**: guest or sponsor replies; Alexey `/todo podcast <email>`; speaker requests change.
- **Frequency**: the single most common interaction — 92 messages proposing dates ("Will X at … works for you"), spread over 65 distinct days; constant all year (e.g., 2026-01-08 Ricardo, 2026-02-19 Slawomir, 2026-06-08 three guests at once, 2026-09-21 Suhas/Dewang two-part podcast).
- **Procedure**: Grace checks Alexey's calendar (often attaches calendar screenshots — explicitly requested 2026-04-25), picks 1–2 candidate slots in the canonical windows (podcasts Mon/Tue 12:30–13:30 CET; workshops 16:30–18:00 CET; LLs 17:00–19:00 CET), asks Alexey "will that work for you?", then emails the guest; on guest counter-offers loops again. Handles timezone conversion (PST/Brazil/Australia/East-coast; uses converters, occasionally misreads — 2026-09-01 "Oh I misread his time request he said 9 AM EST thats 3:00 PM CET").
- **Tools**: Google Calendar, email, Luma, Airtable.
- **Output**: confirmed slot, calendar invite sent to guest (with podcast questions-doc link attached — Alexey's rule from 2026-03-17: "can you please double-check that all the future calendar invites with podcasts they have the link to the Google document with the questions").
- **Reporting**: "Got it, email has been sent to Revathy. Thank youuu" (2026-02-06).

### 3.2 Invoicing & payment chasing (Grace 90 invoice-mention msgs; Alexey 42)
- **Trigger**: completed newsletter slot/workshop/social promo; Alexey "/todo invoice …"; sponsor asks for invoice; monthly "who hasn't paid" sweep.
- **Frequency**: near-weekly; dozens of invoices (Temporal, Atlan, Nebius, Snowflake, Snowplow, dlthub, Bruin, Exasol, JetBrains, Astronomer, Cube, PlayerZero, TestMu, NS Groep, European Environment Agency, Kestra, Pathway, Ripply/Springest, Maven, X Corp, Stripe, Fancy Media, McKenzie/Command, Phoenix, Anaconda, Hackmamba…).
- **Procedure**: pull sponsor details from Finom contacts (or find VAT/address online via AI — 2026-04-09 "since they are in Germany i look for their VAT ID online"), draft invoice in **Finom**, screenshot + "Here is the drafted invoice for your checking"; send after approval; log in bookkeeping sheet; chase unpaid ("Done following up with Exasol" 2026-04-27); annotate currency-conversion differences on the PDF (2026-05-12 Alexey explains the process); split contracts into 4 installments (Snowplow 20k → 4×5k "community sponsorship … first installment", 2026-05-07).
- **Decision points for Alexey**: price, description wording, VAT/reverse-charge, currency, which entity to bill ("I think we don't bill sandbox directly … it's this agency who we should bill I believe" 2026-10-09), payment-link fee (2–3% on top; "let's add 3% in the document" 2026-03-26).
- **Output**: sent invoice, updated Finom/bookkeeping, payment confirmations relayed by Alexey ("Astronomer paid" 2026-07-10).

### 3.3 Monthly tax report / bookkeeping assembly (10 cycles: Dec→Sep reports)
- **Trigger**: Grace, first days of each month (2026-01-05 for December, 2026-02-05 Jan, 2026-03-09 Feb, 2026-04-06 Mar, 2026-05-05 Apr, 2026-06-05 May, 2026-07-07 Jun, 2026-08-10 Jul, 2026-09-02 Aug, 2026-10-05 Sep).
- **Procedure**: Grace reconciles bank statements (Finom/Revolut/PayPal) and lists missing items ("For February Tax Report we need the following: Invoices: … Statements: …"), asks description questions ("What should we put as description for 6 Jan 2026 Xai LLC invoice (its not indicated)?" 2026-02-05; answer: "GLM Max coding plan - put this"), Alexey hunts and drops invoice PDFs/Stripe links over hours/days, Grace compiles the report draft + screenshot, Alexey approves ("Looks okay. Thanks!" 2026-09-08), Grace emails accountants.
- **Friction**: recurring missing-invoice hunt (AWS 2026-02-11 and 2026-07-15, Google Cloud 2026-03-13, Loom, GoDaddy 2026-02-10, OpenAI 2026-09-07); statement-vs-invoice ambiguity; Alexey occasionally supplies late ("sorry for the delay … thanks for reminding me!" 2026-04-17).
- **Revenue-side invoices**: Grace also creates invoices for money *received* (X revenue sharing, Stripe/AI Shipping Labs payouts, Maven payouts, reimbursements) — process docs created 2026-04-07.

### 3.4 YouTube video pipeline (upload → edit → transcript/timecodes → announce → chop for socials)
- **Trigger**: Alexey forwards Zoom/Loom links or says "I'm already uploading … please take it from here" (2026-02-23); todo bot/`/todo`.
- **Frequency**: ~2–4 videos/week across DTC channel + Alexey's personal channel (22 Grace link-share messages; many more in screenshots). Includes weekly "Inference Engineering Book Club" series (Weeks 1–6, Aug–Sep), office hours, workshops, podcasts, AI Shipping Labs.
- **Procedure** (as observed): download Zoom/Loom → upload to YouTube (public/unlisted per instruction) → cut the beginning/breaks per Alexey's timestamps ("in the stream at 12:17 … let's remove this part" 2026-01-27; "I had two breaks - at 14:54 and at 16:05" 2026-08-10) → wait for auto-transcript → generate timecodes + description (copy from Luma page for Luma events, 2026-03-13) → make announcement in Maven/Slack → send link to Alexey + Valeriia in content channel → cut "interesting things" chunks for Valeriia's social posts (generalized to ALL content types 2026-08-19: "We are cutting the sponsored workshop and Maven. Should we cut all workshops and webinar moving forward" / Alexey: "Yes please … Let's also do it for podcasts").
- **Known failure mode**: YouTube transcripts not appearing (14 mentions; 2026-03-11 workaround: split audio, transcribe via Groq (rendered "GROC"), re-merge with AI; 2026-09-21 same fallback plan again).
- **Reporting**: "Here is the link for … https://www.youtube.com/watch?v=…" + "(will wait for transcript to show in order to add description and timecodes)" (2026-03-13).

### 3.5 Newsletter slot management & sponsor newsletter ops
- **Trigger**: sponsor inquiry (Grace triages inbox/Spam), Astronomer quarterly rebooking, slot collisions.
- **Frequency**: ~weekly (43 Grace messages mention newsletters). Product: Primary slot (Mon), Secondary slot, Standalone (usually Wed; "usually we found out that this is the best day … it can be any day except Monday" 2026-03-23). Observed pricing: primary €1,500 (Pathway, 2026-08-18), secondary ~$1,000–1,200 (Cube), standalone €2,500 (Atlan, 2026-08-11), social-media promo €1,200 (Pathway/PlayerZero), bundle: "If they order 5 we can give them a 10% discount" (2026-08-07).
- **Procedure**: check the newsletter calendar sheet for free slots, propose 2–3 options, draft the sponsor email for approval, coordinate copy deadlines ("we will need a few iterations and we don't want to do anything in Harry" — i.e., hurried — 2026-01-28), track stats (views/clicks from Mailchimp) and answer performance questions, send stats ~1 week after campaign ("we typically send this after one week of the campaign" 2026-04-27).
- **Reporting**: draft + stats screenshots; "email has been sent to Atlan" (2026-03-20).

### 3.6 Podcast guest pipeline (Grace 54 / Alexey 31 podcast mentions)
- **Trigger**: Alexey `/todo podcast <email>` (≥15 times: 2026-02-09, 02-10, 02-18, 02-21, 03-18, 03-20, 04-07, 05-07, 05-12, 05-14, 06-04, 06-06, 06-27, 07-27, 08-05), guest recommendations, or inbound (2026-07-03 Aishwarya).
- **Procedure**: reach out with template intro, propose date, collect bio (generate from LinkedIn when missing — rule from 2026-03-19: "we just copy whatever they have in LinkedIn"), create questions doc (ChatGPT-generated from LinkedIn profile, 2026-08-21), calendar invite with doc link, post-recording: audio → Dropbox → Dave (editor), video → YouTube, transcript → description, schedule Spotify release on Fridays (2026-04-06 "Please prepare the transcripts for all the backlog and schedule the audios for every coming Friday and send me a list with podcast names and dates"), episode numbering s23e01…, website entry via Airtable.
- **Reporting**: list messages like the Season 23 schedule (2026-04-06 18:15, 8 episodes with dates and titles).

### 3.7 Event operations (workshops/webinars/LLs end-to-end)
- **Trigger**: sponsor contract, Alexey voice brief, speaker inbound.
- **Procedure** ("the usual process"): create Luma event (+ Canva cover from template; sponsor logos), send workshop requirements Google doc to speaker, calendar invite, mirror event to Meetup/LinkedIn/X (+ global meetup group since 2026-01-14), add to website (Airtable → GitHub workflow; SHA1 email hash for people records), Maven LL creation for lightning lessons (via "Maven Prompt" with ChatGPT), reminders to speakers who don't fill docs, reminder emails to attendees, live-day support, post-event: upload video, stats to sponsor, detailed statistics report ~1 month later (process added 2026-02-18: "after one month or so we want to send this report to the sponsors"), sponsors' email-opt-in list sharing.
- **Change over year**: Zoom link for all events replaced 2026-06-08 after leak; LL-specific Zoom link noted 2026-06-30; "Company Name" added to sponsor registration forms 2026-03-27; invoice-before + paid-after checklist added to Trello templates 2026-02-11; Grace's Luma account deactivated 2026-08-31 (cost) — she now uses public links or Alexey's account ("there's a process document that describes how you you can connect to my account").

### 3.8 Calendar management for Alexey
- **Trigger**: Alexey asks for blockers/placeholders ("can you also please create a blocker on my calendars for the LL maven events?" 2026-06-04; raw JSON list of 6 office-hours datetimes 2026-06-08), or Grace notices clashes.
- **Procedure**: create invites, keep events aligned across platforms, fix wrong dates Alexey spots ("Wrong month here … It was in my calendar that's how I noticed it" 2026-06-25), dedupe ("Oh but you have a call with Alex" 2026-06-28).
- **Quality bar**: calendar hygiene is Alexey's memory — "I have to plan so many events so I can accidentally plan something else if I don't remember about this one" (2026-06-08).

### 3.9 Community/Slack moderation & member ops
- **Trigger**: todo bot daily "Invite people to Slack from Airtable…"; Slack DMs/spam reports.
- **Frequency**: daily invites (bot), ~monthly spam handling (Douglas/Adam 2026-01-07 & 02-17, "Samu Baby" 2026-04-08, Javier 2026-03-23, Maria 2026-04-08), redirect DM questions to public channels (2026-06-09 Prem, 2026-06-22, course-channel rule).
- **Reporting**: "Yes i have thanked him for letting us know^^" / "he's been deactivated" + drafted reply screenshot.
- Also: impersonation incident handling (2026-02-26, Alexey deactivated Grace's fake account), profile removal from website (Airtable → GitHub people folder + rename podcast file with underscore, 2026-03-09).

### 3.10 Process documentation & Trello upkeep
- **Trigger**: every new repeated task gets a doc; Loom → process doc conversions; Alexey audits.
- **Frequency**: steady Jan–Jun (docs for: Maven LL creation, Canva banners, Maven video upload/edit, office hours summaries, Maven announcements, meetup signups, X/Stripe payout invoices, conference-podcast prep, Slack announcements). Grace links docs in Trello templates and screenshots them for review (2026-02-03 rule).
- **Current state (Aug–Oct)**: 2026-08-09 Alexey announced consolidation: "I want to have a new unified system that combines both Trello and the to-do list … plus all their process documents in one place … eventually I also want to make it easier to use it from telegram"; Grace cleaned Trello + todo list same week; 2026-08-11 new tool at `https://ops.dtcdev.click/` (SSO with datatalks.club email). The daily todo-bot items still run alongside as of Oct 9.

### 3.11 Sponsor statistics & performance reports
- **Trigger**: sponsor asks, or ~1 month post-event (Trello template step).
- **Procedure**: compile registrations (Luma/Meetup/LinkedIn split), live attendees, YouTube views/impressions, per-post impressions/likes/reposts across X/LinkedIn/Substack, newsletter views/clicks; format in Google Spreadsheet; draft email; send. Origin: Temporal report 2026-01-07 (Grace's 495-registrations breakdown), generalized 2026-02-18; reused as sales collateral ("we can use this report also to send it to other sponsors" 2026-02-18).
- Examples: Snowflake ad stats (2026-01-08 "The ad has reached 38,978 views with 1,308 clicks"), Astronomer metrics dip (2026-08-07 "43,659 views and 443 clicks in total" + summer-break framing).

### 3.12 Website/Airtable data maintenance
- **Trigger**: new people/events/podcasts; broken GitHub Actions.
- **Procedure**: Airtable form → workflow → GitHub repo deploy; fix SHA1 hash mismatches (2026-04-17), missing authors (2026-08-12), episodes not showing (2026-06-02, 2026-07-06 — escalate to Alexey to restart). Rule: "if next time you flag it so I can check it and see if I need to restart something" (2026-06-01).

### 3.13 Misc recurring
- **Book of the week** scheduling (Maria Vechtomova Sep 14–18; Suhas/Dewang/Divya Oct 5–9 or 12–16, 2026-09-17).
- **Vendor/compliance forms** (Legent "gigantic form", 2026-04-28–30, incl. whitened bank statement and signature).
- **Reimbursement invoicing** (Python Software Verband, Carmen/Springest flight).
- **Socials cross-posting** and missed-post self-corrections (2026-05-07 Snowflake LinkedIn/X).
- **Trello playlist hygiene** on YouTube (sorting/moving course videos; 2026-01-13, 01-22, 02-13, 02-20, 03-15).

---

## 4. How Grace works

### Reporting results
- Default artifact: **screenshot(s) + short caption** (531 photos; typically 2–4 screenshots per report).
- Completion formulas: "It has been sent/moved/added/updated…" + thanks. Examples: "Adjusted and sent, thank youuu" (2026-01-05); "Luma has been created and informed Valeriia and Alena" (2026-01-10); "videos are added on both playlists, thank youu" (2026-02-18); "They have been added, thank youu^^" (2026-06-15).
- Link delivery with status caveats: "Here is the youtube link … (will wait for transcript to show in order to add description and timecodes)" (2026-03-13); "Just sending here coz I might forget😅" (2026-07-03).
- Proactive status digests on stuck items: "Letting you know that up until now the videos in youtube are still processing to do some edits" (2026-08-26); "we haven't sent the concurrent views and registration details, as the YouTube transcript still isn't available" (2026-09-17).

### Drafting-for-approval loops
- Nearly everything outbound goes through Alexey first: emails to sponsors/guests, invoices, event descriptions, Luma/Maven pages, stats replies — "Here is the draft for your checking" (36) / "Kindly check the draft for any changes needed" (41). 98 Grace messages mention "draft".
- She structures asks one-topic-per-message when possible and numbers them ("1. … 2. …"), bundles the morning batch ("Hi Alexey, Good day!"), and follows up politely ("Following up on the invoices and statements, thank youu^^" — recurring).

### Question taxonomy (verbatim examples)
1. **Scheduling choice** (81 "works for you"): "For Ricardo's Workshop Will February 02 at 12:00 -1:30 PM CET works for you?" (2026-01-08); multi-option: "How about 2:00 PM - 4:30 PM CET (10 AM- 12:30 PM Brazil time) Or 4:30 - 6:00 PM CET" (2026-01-08).
2. **Draft approval**: "For Snowflake newsletter, Kindly check the draft for any changes needed" (2026-01-08).
3. **Missing information / how-to**: "For Exasol, kindly advise on VAT number" (2026-01-13); "For Bruin the description do we have a date?" (2026-03-05); "What description should we put in the Datamakers Fest podcast?" (2026-05-20).
4. **Confirm assumption** ("Should we…" ×44): "Should we use your Personal bank account for the Iban the DE801, just like what we did to their last invoice?" (2026-02-09); "Is it now 3% should we update the document from 2%" (2026-03-26); "should we put the link into the Luma post?" (2026-01-19).
5. **Understanding check / confusion**: "Please correct me, we will also have a podcast with Leonid Kholkine and if yes…" (2026-02-23); "I got confused does it mean he wants the date to be earlier than March 15?" (2026-02-24); "do I understand it correctly😅" (2026-06-05).
6. **Policy/judgment escalation**: "For Claire (Nao) Newsletter Should we follow up, or since she didn't confirm at the end of the month they will not take it" (2026-08-06); discount request: "They are asking for discount. Kindly advise" (2026-09-30).
7. **Technical blockers**: "the GitHub failed saying it doesn't recognize her email … Kindly advise, I'm not sure on what to update" (2026-04-17); "I'm trying to Log into your Linkedin to view the results … I cant seem to view them just by the link using my profile" (2026-05-19); Finom lockout (2026-04-25, 04-27).

### Assumptions vs blocking
- Proceeds on assumption for reversible/formatting choices, then confirms in the same message ("I deleted the record in the airtable and run a workflow but his profile is still in the website. Do we 'Delete file' in github people and run it again, will that works?" 2026-03-09; "Atlan didnt asked to be invoiced in $ as of now(just assumed based on their previous invoice)so maybe we will send it via Euro and make changes once they request?" 2026-02-09).
- Blocks on: money (prices, discounts, VAT), commitments to sponsors (dates, slots), anything touching Alexey's accounts/identity (signatures, bank statements — she always asks before sending sensitive docs: "I have actually whiten the amounts and transaction details. Should we send this, or the statement itself with the details?" 2026-04-30), and system errors she can't resolve.

### Proactive behaviors
- Suggests process/system improvements: "should i move here all the spreadsheets made for our sponsors … or do we have a specific folder?" → Alexey: "Yes let's create a folder there workshops … Good idea" (2026-01-07); "for Sponsored event should we add a question in the form asking for the registrants company?" (2026-03-27); "I included dates for the first three months for him to choose from to avoid back-and-forth" (2026-05-04); created the VAT-info document herself (2026-01-21 "also I have saved your number in the VAT Information"); added the invoice checklist step to Trello after Alexey's voice note (2026-02-11 "A step was added for the Sponsored workshop in Trello and for the newsletter").
- Spots anomalies: currency discrepancies ("the discrepancies of their payment due to conversion" 2026-06-05), wrong invoices ("Im seeing two different address, maybe well ask Mckenzie for the details?" 2026-10-09), double-bookings ("we have Tatiana at 12:30 PM on April 14" 2026-03-02), calendar conflicts ("Oh but you have a call with Alex" 2026-06-28).
- Self-reports misses immediately with fixes: "Oh no😱, Ive missed the Atlan's newsletter plan in the document" (2026-03-20); "Oh no😱 I missed to post Snowflake last week on Linkedin and in X … Just posted it now" (2026-05-07); "I missed the workshop with Paul Iustin, he confirmed on Aug 17. and we proposed that date to Nicholas (Orkes) is it fine to change…" (2026-06-17); "I missed this one, should I add you to the conversation as well?" (2026-05-14); "Missed these 3 messages they are in the Spam can we send this to them" (2026-09-28).
- Uses AI assistants openly for lookup/drafting: "checked with AI that its still the same" (2026-06-01), "here are the details provided by AI. Should we proceed with this?" (2026-08-18), "I put NA as per AI" (2026-04-28), bio generation "generated this based on his Linkedin profile" (2026-03-19).

### Error handling & rework
- Rework loops are short and good-natured; she applies the correction and re-posts evidence ("Got it, here is the draft for your checking" after VAT fix 2026-03-17).
- Root-cause fixes get added to process docs after incidents (timezone double-check step 2026-05-30: "Will add that to the process, thank you").
- When systems break (Finom login, GitHub actions, YouTube transcripts, Meetup reschedule limits), she documents attempts, escalates with screenshots, and proposes workarounds (upload to Google Drive for Snowplow's video 2026-07-23; Groq audio-split for transcripts 2026-03-11).

---

## 5. How Grace asks Alexey things (escalation patterns)

- **Approval requests (most common)** — draft + "Kindly advise/check": handled same morning; Alexey's modal replies are one-liners: "Looks good" / "Looks great" / "Yes" / "Both look good, thank you!" (2026-03-16). Median Alexey reply ~11 min.
- **Choice questions** — she pre-filters to 2–3 options with trade-offs ("Or based on Arize invoice Goal plan, 1st installment (May 2026 - January 2027)"; "Part 1 (Suhas) on Sept 29 … Or Part 1 Oct 6" 2026-09-21). Alexey picks one ("March 17 please" 2026-02-19; "let's do tuesday" 2026-03-02; "Let's do 17" 2026-06-16).
- **Missing-info requests** — precise, scoped ("What's 265 RSVPs? Where is it from?" is Alexey's; hers: "For Maven Learning 20000 - Is the description 'AI Bootcamp 2026 Cohort 2, Payout 3'?" 2026-09-02). Alexey answers from memory or digs up files, sometimes hours later, sometimes next day with apology ("I'm sorry, I missed that message about August report" 2026-09-07).
- **Blocking situations** — systems/access: Finom ("I was able to log in for like few seconds just enough to click 'create invoice' then im logged back out.😔" 2026-04-27 — Alexey took over the invoice), LinkedIn stats access, GitHub action failures, Luma account (post-deactivation).
- **Judgment escalations** — pricing/discounts/relevance (Socap relevance question 2026-07-20; "They are asking for discount" 2026-09-30 → Alexey: "typically we don't really give discounts for one of new sliders, so if you include me, I can just answer"), sponsor-relations wording (Astronomer low metrics 2026-08-07 → Alexey crafted the framing: "we checked the numbers and they are indeed lower than what we'd expect. That's probably likely because of the summer break").
- **How Alexey responds**: fast, short, in text even to voice questions; explains reasoning in voice notes when teaching (e.g., the RSVP attribution lesson 2026-01-08: "We don't know which RSVPs are coming from where so we cannot really attribute it to us"); occasionally delegates back with Calendly ("Can you send him my calendly? calendly.com/dtc-alexey/30min" 2026-08-19). He also self-corrects and apologizes ("Sorry I didn't see your message" 2026-10-09; "sorry I wasnt following the email thread" 2026-07-23).

---

## 6. Friction & automation candidates

### Repeated back-and-forth (candidates for elimination)
1. **Monthly invoice/statement hunt** — every tax cycle: Grace lists missing items → Alexey searches email/Stripe/PayPal → files dribble in (2026-02-10, 02-11, 03-13, 05-11, 07-15, 09-07, 10-05). Mechanical: a consolidated receipts inbox/auto-forward rule or a standing "statements folder" would remove most of it.
2. **YouTube transcript waits** — 14 mentions of "waiting for transcript"; blocks description/timecodes/announcements for days (2026-01-14 → 2026-09-21). Mechanical: auto-run the Groq/split-audio fallback (already proven 2026-03-11) when transcript absent > 24h.
3. **Date ping-pong** — 92 scheduling messages; each round needs Alexey's yes. Mechanical for first pass: Alexey's free-busy is checkable; Grace already attaches calendar screenshots. An auto-proposal from calendar availability + canonical slots would cut 1–2 rounds; final confirm still needs judgment.
4. **Multi-platform event mirroring** — Luma + Meetup + LinkedIn + X + website + calendar must stay in sync; recurring mismatches (2026-01-06 Luma vs calendar; 2026-05-29 midnight timezone; 2026-06-25 wrong month; 2026-08-06 stale Meetup after Luma deletion; 2026-08-29 hidden event not announced). Mechanical sync + a pre-event "times match" checklist (already added to process 2026-05-30).
5. **Invoice detail lookup** — VAT IDs, addresses, "who do we bill" (2026-10-09 agency vs sandbox; 2026-08-18 Pathway not in contacts). Semi-mechanical: a maintained sponsor master table (Finom + contract refs) with AI-assisted lookup + confirm-with-client step (Grace already does this pattern).
6. **Unpaid-invoice sweeps** — "check which invoices still aren't paid" (2026-04-27), "Did we send invoices to Kestra and dlt" (2026-09-04), "check for all the emails that we sent in the last couple of months if we sent the invoice" (2026-09-07). Mechanical: Finom payment-status report + reminder cadence (the 2026-02-11 Trello checklist step exists — could be automated).
7. **Screenshot-heavy verification** — 531 screenshots; much of it is proof-of-state of SaaS UIs (Finom invoice preview, Luma event, calendar). If an agent executes, it should attach links/state dumps instead; screenshots only needed for human review.
8. **Voice-note comprehension** — 255 voice notes, several garbled in transcription (Polish/Romanian noise, e.g., 2026-01-23, 2026-02-09, 2026-03-13, 2026-08-04); one message Alexey had to re-transcribe himself ("Here I used voice recognition" 2026-07-14). Automation needs robust ASR + a norm that numeric facts (dates, amounts) be confirmed in text.
9. **Stats collection for sponsors** — manual pull from X/LinkedIn/Substack/Mailchimp/YouTube per report (Temporal 2026-01-07 took a full day of iterations). Alexey already flagged: "I know it's some manual work but we'll see how to automate it" (2026-02-18). Judgment: the summary email; mechanical: the pulls.

### Mechanical vs judgment
- **Automatable now (rules/scripts)**: Slack invites from Airtable; Mailchimp backup; Slack dumps; invoice generation from a sponsor master + price table (Finom templates exist); payment-link creation with fee; tax-report reconciliation draft (match bank lines to receipts); transcript fallback; playlist sorting tasks; cross-posting announcements; unpaid-invoice reminders; calendar placeholder creation.
- **Needs judgment (keep human/Alexey)**: pricing and discounts; which entity to bill; sponsor-relevance calls; tone of sponsor-facing emails; content of event descriptions (Alexey iterates on these); timezone edge cases with guest constraints; process exceptions (refunds, reimbursements, vendor forms); anything requiring Alexey's signature/accounts.

### Systems each side touches
- **Alexey**: YouTube (both channels), Zoom, Luma (owner), Maven, banks (Revolut personal+business, Finom), Stripe/PayPal/X payouts, Substack, his calendar, Telegram todo bot, GitHub (website repo), ops.dtcdev.click (new, Aug).
- **Grace**: Gmail (sponsor threads), Finom (invoices), Google Calendar/Docs/Sheets/Drive, Airtable (+ website workflow via GitHub), Luma (via links/Alexey's account since Aug 31), Meetup, LinkedIn/X (posting; stats via Alexey's account), Mailchimp, Canva, Trello (being folded into unified system), Spotify (podcast scheduling), Dropbox (podcast audio to Dave), ChatGPT/Groq (drafting/transcription), Calendly (handoff link).

---

## 7. Candidate playbooks (top 11, written for an executing agent)

### P1. Podcast guest scheduling & episode pipeline
- **Trigger**: Alexey `/todo podcast <email>` (± LinkedIn URL, notes) or inbound guest.
- **Inputs**: guest email (+LinkedIn); Alexey's calendar; canonical slot (Mon/Tue 12:30–13:30 CET).
- **Steps**: (1) check calendar for 1–2 free canonical slots; (2) ask Alexey "Will <date> at 12:30–13:30 PM CET works for you?" with calendar screenshot; (3) email guest intro ("Nice to meet you! I'm Grace and I'm taking care of organizing events at DataTalks.Club…"); (4) on confirmation: send calendar invite **including the Google-doc link with questions** (mandatory since 2026-03-17); create questions doc via ChatGPT from LinkedIn profile if guest slow (2026-08-21); (5) bio from LinkedIn if not supplied (2026-03-19 rule); (6) post-recording: Alexey uploads video/audio or forwards Zoom link → upload video to YouTube, cut beginning/breaks per timestamps, wait for transcript → timecodes+description; audio → Dropbox → Dave; (7) schedule Spotify release for a Friday; (8) add episode to Airtable (website); (9) report links to Alexey + content channel.
- **Alexey decisions**: slot choice; cutting sensitive parts (e.g., remove Meta affiliation on request, 2026-06-08).
- **Evidence**: links (YouTube, Spotify, doc); episode list with dates.
- **Frequency**: ~2–4 guests/month (15 `/todo podcast` in 9 months plus inbound).

### P2. Sponsor invoice creation & sending (Finom)
- **Trigger**: completed deliverable, or `/todo invoice <company> <amount>`, or sponsor request.
- **Inputs**: company + deliverable + amount + currency (Alexey); invoice details (Grace: Finom contacts, contracts, online VAT lookup).
- **Steps**: (1) find details in Finom/contacts; if absent, look up online and **confirm with the client** ("we found this VAT ID online. Please confirm that it's yours" pattern, 2026-04-09); (2) draft invoice in Finom — description conventions: `<Deliverable> (<date or period>)`, e.g. "AI Engineering Buildcamp: From RAG to Agents Cohort 3 (13 April 2026)", "X Revenue Sharing (Apr 11, 2026 - May 23, 2026)"; reverse-charge VAT for EU B2B; (3) screenshot + "Here is the drafted invoice for your checking"; (4) send on approval; (5) log in bookkeeping sheet; (6) for contracts, split into installments (e.g., 4×5,000 for 20k, "2026 Community Sponsorship, 1st Installment"); (7) chase unpaid per sweep; (8) on payment, annotate conversion differences on the PDF.
- **Alexey decisions**: price, description, currency, entity to bill, fee % on payment links (2–3%).
- **Evidence**: Finom invoice screenshot/PDF; payment status.
- **Frequency**: weekly (dozens across the period).

### P3. Monthly tax report assembly
- **Trigger**: calendar — first week of month.
- **Inputs**: bank statements (Grace: Finom/Revolut/PayPal); invoices (Alexey supplies; Grace lists gaps).
- **Steps**: (1) reconcile statements → produce "For <Month> Tax Report we need the following: Invoices: … Statements: …"; (2) ask description questions for unlabeled items; (3) collect Alexey's files/Stripe links; (4) build report; (5) draft email to accountants + screenshot for approval; (6) send; (7) create revenue-side invoices (X/Stripe/Maven payouts) using the process docs from 2026-04-07.
- **Alexey decisions**: descriptions, whether a statement may substitute an invoice, treatment of refunds/conversions.
- **Evidence**: report screenshot; sent-email confirmation.
- **Frequency**: monthly ×10 cycles observed.

### P4. Event creation & multi-platform publishing (workshops/webinars)
- **Trigger**: sponsor contract, speaker confirmed, or `/todo start a workshop process`.
- **Inputs**: title/description (Alexey, often via voice→ChatGPT), speaker contacts, date (after P1-style negotiation; workshops usually 16:30–18:00 CET Tue), sponsor logo.
- **Steps**: (1) send workshop-requirements Google doc + calendar invite to speaker; (2) create Luma event (cover via Canva template, sponsor logos; registration form incl. "Company Name" + email-opt-in checkbox for sponsors); (3) mirror to Meetup (Berlin + global groups), LinkedIn, X; (4) add to website via Airtable; (5) **verify time/timezone across all platforms + calendar** (mandatory check added 2026-05-30); (6) chase speakers who haven't filled the doc with deadline framing (fill by Friday → Monday newsletter); (7) announce ≥1 month before date (2026-03-26 rule); (8) reminders; (9) post-event: run P5 (video), stats to sponsor, invoice via P2, detailed stats report after ~1 month.
- **Alexey decisions**: date/time, title, description final, cover choice (often delegated to Valeriia in content chat).
- **Evidence**: Luma link + screenshots of each platform; sign-up counts.
- **Frequency**: ~3–5 events/month.

### P5. Video upload & YouTube finishing
- **Trigger**: Zoom/Loom link from Alexey (often with passcode), or "take it from here".
- **Inputs**: recording link; target channel (DTC vs personal) and visibility (public/unlisted); cut instructions (beginning timestamps, breaks); playlist.
- **Steps**: (1) download; (2) upload with title; (3) cut per timestamps (terminal-based cutting — Grace confirmed current process fine, 2026-03-11); (4) wait for transcript → generate timecodes + description (for Luma events copy description+timecodes from the Luma recording page, 2026-03-13); if transcript missing >24h → Groq fallback: extract audio, split, transcribe, merge (2026-03-11); (5) send link to Alexey (+ content channel with Valeriia); (6) **chop highlight clips for socials — applies to all workshops, webinars, Maven LLs and podcasts** (since 2026-08-19); (7) make announcement (Maven/Slack) for office-hours content.
- **Alexey decisions**: visibility, what to cut (he supplies timestamps), cover (via Valeriia).
- **Evidence**: YouTube link + note on transcript status.
- **Frequency**: ~2–4/week.

### P6. Newsletter slot sales & coordination
- **Trigger**: sponsor inquiry (incl. Spam-folder rescues) or quarterly rebooking (Astronomer).
- **Inputs**: newsletter calendar sheet; pricing table (primary €1,500 / secondary ~$1,000–1,200 / standalone €2,500 / socials €1,200; 5+ bundle −10%).
- **Steps**: (1) check availability; (2) propose options in one email to avoid back-and-forth; (3) draft reply for approval; (4) coordinate copy deadline + template doc with sponsor (iterate early — "we don't want to do anything in Harry"); (5) invoice via P2 (before event) + confirm paid (checklist step); (6) ~1 week after send: stats to sponsor (views/clicks; note summer dips proactively); (7) update calendar sheet.
- **Alexey decisions**: pricing exceptions, discounts ("typically we don't really give discounts"), slot conflicts (primary vs secondary vs standalone).
- **Evidence**: draft email + stats screenshot.
- **Frequency**: ~weekly.

### P7. Sponsor performance/statistics report
- **Trigger**: ~1 month post-event (Trello step) or sponsor asks.
- **Inputs**: event links, registration sources, posts list (Alexey/Valeriia share links), YouTube/Mailchimp/socials stats.
- **Steps**: (1) registrations by platform; (2) live attendees + screenshot; (3) per-post impressions/likes/reposts (before vs after event); (4) newsletter views/clicks; (5) structure: before → after → aggregate in a Google Sheet ("first before, then after - it will be amazing" 2026-01-07); (6) draft email; send after approval. Report only metrics attributable to DTC (no third-party RSVPs; "just report the views and clicks" 2026-01-08).
- **Evidence**: sheet link + draft.
- **Frequency**: per sponsored event (Temporal, DLT, Monte Carlo, Cube, Astronomer, Snowflake…).

### P8. Alexey calendar management
- **Trigger**: blocker requests, new events, clutters.
- **Inputs**: datetimes (sometimes raw JSON: `{"start_datetime":"2026-06-15T18:00:00+02:00"},…` 2026-06-08), event names ("LLM Zoomcamp 2026 office hours").
- **Steps**: create invites/placeholders (1h default), attach meeting/Zoom links (LL uses its own link, 2026-06-30), keep calendar as single source of truth, flag clashes, remove cancelled items, fix wrong dates Alexey spots from his calendar.
- **Evidence**: calendar screenshot when proposing times.
- **Frequency**: several times/month; explicitly "I have to plan so many events" (2026-06-08).

### P9. Slack community ops & moderation
- **Trigger**: daily bot item "Invite people to Slack from <Airtable view>"; DM/spam reports.
- **Steps**: (1) process Airtable queue → Slack invites; (2) spam: deactivate profile per no-spam policy (process doc exists; 2026-03-23), thank reporter, draft the ban-notice reply for approval; (3) member questions: redirect to public/course channels with the standard reply ("Posting in the public channels ensures that the mentors and community experts can see your question…"); (4) escalate impersonation/security to Alexey immediately.
- **Evidence**: screenshot of action + drafted reply.
- **Frequency**: daily invites; moderation ~monthly.

### P10. Website content updates (Airtable → GitHub)
- **Trigger**: new person/event/podcast/episode or removal request.
- **Steps**: (1) fill Airtable form, set status ToDo, run workflow; (2) verify on site; (3) known fixes: SHA1 email-hash mismatch → update hash in GitHub `_people` folder; removals → delete GitHub file + remove event + prefix podcast file with `_`; (4) if GitHub action green but content missing → **flag to Alexey** (restart needed); (5) never leave silently — "I'll appreciate it if next time you flag it" (2026-06-01).
- **Evidence**: before/after screenshots; error logs.
- **Frequency**: per event/episode (~weekly).

### P11. Maven Lightning Lesson creation (voice → published event)
- **Trigger**: Alexey voice notes describing an event (or an article/substack link), sometimes "don't need to run it by me".
- **Inputs**: voice transcripts (or article URL), speaker info (or their site, e.g. mihaileric.com), date/time (LLs 17:00–19:00 CET).
- **Steps**: (1) feed transcript to the "Maven Prompt" (ChatGPT) with rules: concrete, not generic, no "strategic", series naming; (2) draft what-you'll-learn/bullets; post for approval; (3) create LL on Maven (cover from Canva template, correct Zoom link, guest edit access enabled — 2026-06-30 fix); (4) publish (or per instruction skip approval); (5) send link to Alexey + Valeriia; (6) after session: run P5 (upload, cut, clips).
- **Alexey decisions**: title/description final pass (iterative), host vs guest roles.
- **Evidence**: Maven link + generated-details doc.
- **Frequency**: ~2–4/month.

---

## Data limitations

- **No image content.** Grace's 531 screenshots (drafts, invoices, calendars, stats, errors) and Alexey's 85 photos are rendered as `[photo]` only. Procedures that live mostly in screenshots (exact Finom invoice fields, bookkeeping sheet layout, calendar sheet) are inferred from captions and surrounding text; counts of screenshot *messages* are exact, their contents are not.
- **Voice transcription noise.** Several of Alexey's 255 voice notes have garbled transcripts (apparent Polish/Romanian text, e.g., 2026-01-23, 2026-02-09, 2026-02-24, 2026-03-13, 2026-08-04) and a few are `(empty)`; quotes from voice were chosen from clean transcripts.
- **One-sided visibility.** Work done entirely inside SaaS tools (Luma setup, Finom, Mailchimp, Canva) or in other channels (content chat with Valeriia, email threads) appears here only via summaries and screenshots; frequency estimates for those tasks are lower bounds.
- **Reply-latency figures are approximations** (computed as next-message gaps under 4h within the chat, not true threading).
- Speaker-name spelling varies in transcripts (e.g., "Exasol/Exazole", "Snowplow/Snowblow", "Maven/Maiden"); counts use the JSONL text as-is.
