# DataTalks.Club — Contractor Email Analysis (Grace Domisiw & Valeriia Kuka)

Source: `data/team-emails-2026.jsonl` — 2,149 messages, 340 threads, 2026-01-04 → 2026-10-09, from two mailboxes (`alexey@datatalks.club`, `alexey.s.grigoriev@gmail.com`). Rendered digests: `data/email-threads-digest.txt`, `data/email-by-grace.txt` (622 msgs), `data/email-by-valeriia.txt` (237 msgs), `data/email-thread-index.txt`, `data/email-stats.txt`. All quotes below are verbatim from the digest files; citations are `threadId + date`.

---

## 1. Overview

### 1.1 Who writes how much

| Author | Messages | Share | Role in email |
|---|---|---|---|
| Grace Lordel Domisiw <grace@datatalks.club> | 622 | 29% | Community/operations manager — runs all scheduling, docs, invoices, reminders, stats reports, accounting |
| Valeriia Kuka <valeriia@datatalks.club> (+valeriia.kuka@gmail.com) | 237 | 11% | Content manager — sponsor copy review, newsletter sends, sponsor reactivation sales, podcast questions, AI Shipping Labs co-founder |
| Alexey Grigorev | 383 | 18% | Founder — pricing negotiation, disputes, technical content, final decisions |
| Counterparties + automation | 907 | 42% | Sponsors, guests, accountants, vendors, calendar/Zoom/Zapier notifications |

Messages per month (from `email-stats.txt`):

| Month | Total | Grace | Valeriia | Alexey | Other |
|---|---|---|---|---|---|
| 2026-01 | 209 | 51 | 39 | 33 | 86 |
| 2026-02 | 168 | 44 | 32 | 29 | 63 |
| 2026-03 | 235 | 66 | 28 | 51 | 90 |
| 2026-04 | 211 | 43 | 35 | 38 | 95 |
| 2026-05 | 256 | 66 | 36 | 54 | 100 |
| 2026-06 | 292 | 102 | 16 | 39 | 135 |
| 2026-07 | 203 | 60 | 9 | 39 | 95 |
| 2026-08 | 288 | 88 | 25 | 51 | 124 |
| 2026-09 | 217 | 77 | 16 | 31 | 93 |
| 2026-10 (through 10-09) | 70 | 25 | 1 | 18 | 26 |

Grace is the stable every-month workload (43–102 msgs, avg ~66); her June peak = LLM Zoomcamp season + AI Camp/Snowplow/Orkes cycles. Valeriia's volume collapses after June (39→16→9) because the AI Shipping Labs onboarding wave (Apr–May, ~20 "AI Shipping Labs Onboarding and Personalized Plan" threads) ended and Sprint 1 started — her remaining output shifts to sponsor copy review.

Grace appears in 215 of 340 threads, Alexey in 157, Valeriia in 98.

### 1.2 Thread taxonomy (340 threads, classified by subject/participants)

| Category | Threads | Typical shape |
|---|---|---|
| Sponsor newsletter slot ("X + DataTalks.Club Newsletter - <date>") | 45 | Grace creates Google Doc → sponsor fills copy → Valeriia reviews → Monday send → stats +1 week → invoice |
| Workshop / webinar logistics ("<Name> at DataTalks.Club Workshop/Webinar", Lightning Lessons, meetups) | 56 | Grace proposes slot → workshop doc → calendar invite → reminder → post-event stats |
| Podcast guest scheduling ("<Name> at DataTalks.Club Podcast") | 50 | Grace intro → date → questions doc (Valeriia) → reminder → thank-you + YouTube link |
| Sponsorship inbound/outbound (mediakit inquiries, "Interested in partnering", reactivation, content plans) | 24 | Alexey/Valeriia negotiate, Grace executes slots |
| Sponsor relationship/quarterly planning ("Astronomer plans for FY27Q4", "Featuring Snowflake's…", "Alexey <> Social Capital", DMF 2026, conference promos) | ~30 (in "other") | Multi-month threads mixing planning, promo and invoicing |
| Invoicing / payments ("Invoice for X", "Invoice F-000x", Maven/Course invoices) | 38 | Grace requests billing info → sends PDF → chases → confirms receipt |
| Accounting (ILZ Steuerberatung: monthly "DataTalks.Club <Month>" reports + requests) | 13 | Grace sends table + zip upload; accountants reply in German/Russian to Alexey |
| AI Shipping Labs member onboarding | 20 | Valeriia welcome template → questions doc → call → plan |
| Auto-notifications (Zoom recordings, Google Play, GoDaddy, Uber, Zapier `dtctodo@zapiermail.com` todo forwarding) | 34 | No human action except filing; receipts auto-forwarded to Grace + Zapier todo |
| Community misc (Book of the Week, guest post offers, session proposals, invites) | ~20 | Grace triages, loops in Alexey or Valeriia |

Top counterparties: Atlan (Pragadeesh, 46 msgs), Astronomer (Natasha/Danielle, 35+), Podcast Engineers (Dave, 25 — podcast editing vendor), omane.media (Beatriz — Cube's agency, 25), SoCap/socialcap.uk (24 — paid social posts), JetBrains (Elizaveta, 18+), Snowplow (Jordan/Adrianna/John/Sydney, 50+), Snowflake (Krista/Jacob/Elsa, 30+), Kisa Research mediakit (18), heyCommand (McKenzie/McKenzie, 18), EEA (Bokul, 18 — Buildcamp cohort purchase), EEA/Maven (Vanmark).

### 1.3 Who talks to whom

- **Grace → everyone operational**: sponsor marketing/ops contacts, podcast/workshop guests (individual Gmail addresses), AP departments (ap@atlan.com, ap@astronomer.io, ap@dlthub.com), accountants (N.Kindt@ilz-steuerberatung.de, t.ilz@…), vendors (Podcast Engineers, Maven), and Valeriia's private Gmail for contractor payment proofs. She is the public "face" of DTC logistics.
- **Valeriia → content-side sponsor contacts + lapsed sponsors + AI Shipping Labs members**: newsletter copy review with Natasha/Sydney/Beatriz; cold/revival outreach to NVIDIA, W&B, MindsDB, CodeRabbit, Galileo, Contextual, Pinecone, Anyscale, Estuary; Russian-language coordination with JetBrains (Elizaveta Zaytseva, thread 1972f9fbff6e435d).
- **Alexey → negotiation & exceptions only**: package pricing (Atlan €20,500 plan, thread 19c9471a5f3a8d67 2026-02-25), discount policy ("We don't do discounts on blasts", same thread 2026-02-27), payment disputes (SoCap, thread 19ce75ee70944131 2026-05-13), technical questions, and the SoCap/social-media paid-post deals where he himself is the product.

---

## 2. Grace's email persona

### 2.1 Signature (verbatim, used on essentially every message)

```
Regards,

*Grace Domisiw*
Community Manager
DataTalks.Club
```

(The asterisks are literal — a Gmail rich-text bold paste that survives as markdown.) Almost never varies across 10 months. Occasional variants: "Thank you and Happy weekends!" (19aa60c78d3e4912, 2026-01-24), "Have a great day ahead!" as a closing line before the signature.

### 2.2 Greeting / opening / closing formulas

- Greeting: `Hi <FirstName>,` (dominant); "Hi there," for shared/anonymous inboxes (teams@socialcap.uk, invoice@kestra.io, factuur@reshift.nl); "Hello," for the accountants; "Hi <Name1> and <Name2>," when two contacts.
- Opening line on follow-ups: "Hope you are doing well!" (extremely frequent, e.g., 19a9bedadccf887c 2026-01-19; 19c9471a5f3a8d67 2026-03-20).
- Self-introduction on first contact (three near-identical variants, all recurring):
  - "I'm Grace, nice to meet you! I'm a community manager at DataTalks.Club and take care of organizing events." (19b99ca1a730b2b7, 2026-01-08)
  - "Nice to meet you! I'm Grace and I'm taking care of organizing events at DataTalks.Club." (19c47889cf210043, 2026-02-10)
  - "I'm Grace, a community manager at DataTalks.Club." (newsletter threads, 19bb138a54dc9040, 2026-01-12)
- Closers before signature: "Looking forward to your response, thank you!" / "Let us know if you have any questions, thank you." / "Thank you!" / "Thanks!" / "We're looking forward to your talk. See you soon!"
- Persistently uses "we/us" for DTC ("We will use this document…", "We hope you're satisfied with the results") even for actions she alone performs — the community voice.

Fingerprints (recurring typos, useful for authenticity in playbooks — keep or fix deliberately): "will that works on you?" (1a0cd7fffd1419b5 2026-10-07; 19c89f85914bbe19 2026-02-23), "The you for providing the information!" (19c47366ad305395 2026-02-24), "Octiber 12" (1a0a97c036c917ce 2026-09-16), "We have recieved the payment" (19e353a0790f5870 2026-05-22), "Happy weekends", "Aattached here" (19d1ac3b84fae785 2026-08-19), "Scondary Slot" in subject lines of Snowplow threads.

### 2.3 Structure habits

- Short emails, one purpose each: greeting → one-line context → the ask (often with date bolded `*February 09*`) → link → closer → signature.
- Bulleted lists for: available slots ("The available dates in February for the newsletter are *February 09* and *February 23.*" 19bdbad3a4e51afe 2026-01-21), required info ("We need some information for the invoice: - the full legal name of the company - the address - VAT ID(If you are based in EU)" 19bdfb4134b81ecb 2026-01-21), talk-details checklist (title / subtitle / outline 3-4 bullets / bio / links — verbatim in §6).
- Every email carries exactly one link (Luma event, Google Doc, Mailchimp archive, YouTube, Zoom).
- Deadlines are always explicit dates, never relative: "please submit your copy and graphics by January 12, 2026."
- Sends in morning batches, overwhelmingly 07:00–09:00 CET (dozens of messages timestamped 07:00/08:00/09:00 sharp — she schedules sends or works through a queue each morning; "Following up" batches land same minutes each week, e.g. every Monday ~09:00 "Your promotion is now live!").

### 2.4 How she proposes dates/slots

Three patterns, always with day-of-week + date + timezone:

1. Single slot: "For the interview, will March 02, Monday at 12:30 - 1:30 PM CET work for you?" (19c478896beb9a07 2026-02-10)
2. Alternatives after a decline: "No worries and thank you for letting us know. Will July 6, Monday at 12:30 PM - 1:30 PM works for you?" (19d055a3600ca686 2026-04-15); "How about on November 9, Monday at 12:30 - 1:30 PM CET, will that works on you?" (1a0cd7fffd1419b5 2026-10-07)
3. Option menu (workshops / reschedules): "Which of these dates works best for you? - *July 6,* Monday at 5:00 PM – 6:30 PM CET or - *July 13,* Monday at 5:00 PM – 6:30 PM CET" (19cac6fb0da6df69 2026-05-05); three-option menu for a schedule shift (19e83e94fe9a434b 2026-06-12).

When Alexey's calendar is the bottleneck she hands off to Calendly: "Yes, please select a slot here for a call with Alexey: https://calendly.com/dtc-alexey/30min" (19cac6fb0da6df69 2026-06-02; also 19ff19a6f1498c2f 2026-08-19). Calendar invites are sent from her account ("Organizer Grace Lordel Domisiw"), titled "<Name> at DataTalks.Club Podcast/Workshop", often prefixed "(Proposed)" until confirmed, with the Zoom link and the Google Doc embedded in the invite description (e.g., 19be4f38f9ddfe14 2026-01-22).

### 2.5 Payment chasing — the escalation ladder (one thread, verbatim)

Atlan, thread 19d1ac3ef88436f6 (plus 19c9471a5f3a8d67):

1. **Send invoice** (2026-03-23): "This is Grace from DataTalks.club. Please see the attached invoice for January and let us know if you have any questions."
2. **Next invoice, reference nothing** (2026-04-10): "Please see attached invoice for the Stand-alone newsletter on March 6."
3. **Reminder 1 (~3–4 weeks later), soft, no blame** (2026-05-06): "Hope you are doing well! Following up on these invoices, please advise. Thank you."
4. **Clarify when sponsor is confused** (2026-05-07): enumerates exactly which placements the invoices cover ("1. Newsletter Sponsorship Secondary Slot (19 January 2026)…").
5. **Confirmation + goodwill close** (2026-05-12): "We have received the payment. Thank you for supporting our community!"

The same ladder repeats on Snowflake (invoice 2026-05-07 → follow-up 2026-05-26: "Following up on the invoice for the workshop, please see the attached invoice here for convenience." 19b2184f54a65677), Exasol (invoice 2026-04-09 → 2026-04-27 "Following up on this invoice, please advise." → paid 2026-05-06, 19c0e43f93e5c279), SoCap (invoice 2026-03-30 → 2026-05-07 "Following up on this invoice, please advise." 19ce75ee70944131), Kestra (invoice 2026-08-10 → 2026-09-07 "Following up on this invoice, please advise." → paid 2026-09-08, 19feb59825ae481c). **There is no step beyond repeating "please advise"** — when a payment is actually disputed or "missing", Alexey takes over (SoCap 2026-05-13: "Following up on the missing payment." — sent by Alexey, not Grace). She also re-attaches the invoice on each follow-up rather than pointing to the old email, and forwards AP threads together "so you have everything in one place" (19c9471a5f3a8d67 2026-04-10: "I have also forwarded the March invoice in the thread with ap@atlan.com so you have everything in one place.").

Payment mechanics she handles herself: Revolut payment links with commission disclosure — "Here is the payment link with 3% on top: https://checkout.revolut.com/… Please let us know if this works out for you and if not we can send you an invoice for bank transfer." (19ce75ee70944131 2026-03-26); "we can generate a payment link, but please note that this method includes a 2% commission fee on top" (19e566fae1cb8e9f 2026-06-15). And she defends billing details when challenged: "We checked the IBAN and this is correct, this is a bank in Lithuania thats why its 20 characters long." (2026-03-31).

### 2.6 Docs & attachments

- Invoices: PDF attached, filename pattern `2026-<MM>-<Legal Entity>-datatalksclub-sponsorship.pdf`.
- Event/content docs: always Google Docs links, never attachments; the same "workshop document" / "podcast document" / "newsletter copy document" is reused across the thread and embedded in the calendar invite.
- Lead sharing: Google Sheets of opted-in emails, mentioned in post-event stats emails.
- Internal: monthly zip `datatalksclub-2026-MM.zip` (2–4 MB) uploaded to the accountant's server; `Finom_payment_<DDMMYYYY>.pdf` proof-of-payment PDFs to Valeriia (19cc2d6b0ef59dcd 2026-03-09 etc.).
- She reads receipts/statements and even corrects them: flags "We cannot find the invoice for Feb 2026 AWS Cloud services: €-0.78" in the Feb report (19cf608e550bbcaf 2026-03-16) and annotates a personal-card mistake: "the transaction on 26 May 2026 Flix -73.47 was a mistake, as Alexey accidentally used the company card instead of his personal card" (19ecb771317d0031 2026-06-15).

### 2.7 How she writes to accountants

Monthly report thread, subject "DataTalks.Club <Month> YYYY", to Natalie Kindt + t.ilz@ilz-steuerberatung.de, CC Alexey. Verbatim skeleton (19b8dc28cb1d6ae8 2026-01-05, identical through 1a11062a7a214f77 2026-10-06):

> Hello,
>
> Here's the report for December 2025.
>
> Date paid Provider What Price, $ Price, EUR Statement
> 2 Dec 2025 2 Dec 2025 Aws Cloud services -246.56 -212.36 Revolut
> …(one line per transaction, occasionally with " - statement-YYYY-MM-<name>.pdf")…
>
> Also, the zip archive file has been uploaded to the server. Let us know if you have any questions. Thank you and Happy New Year!

Ten consecutive monthly reports (Dec-2025 … Sep-2026), sent between the 5th and 12th of the following month. The accountants almost never reply in these threads (all are 1-message threads); their separate German/Russian requests go to Alexey, who routes them back: accountant asks for March documents in Russian (19daa4ad1d58e363 2026-04-20) → Alexey: "I think Grace has already done it. Grace can you please confirm?" On their fee invoices Alexey forwards to Grace + the Zapier todo address with a one-liner: "please pay" (1a0f2780075e52d5 2026-09-30).

### 2.8 What she answers herself vs. routes to Alexey

**Answers herself (recurring):**
- Standard slot availability and the Monday rule: "Please let us know your preferred date and it should fall on Mondays" (198ebc1159a1ff51 2026-06-19; 1a081cd43fb9500b 2026-09-09).
- Standard price quotes: "Confirmed on the secondary slot, and the price is 1,000 EUR." (19c9471a5f3a8d67 2026-03-27); "The standalone newsletter is €2,500." (19fd70244f5b09fd 2026-08-11); "The rate for Alexey's Social Media posts is 1,200 Euro." (19ce75ee70944131 2026-07-21); audience stats "Our newsletter reaches 120K+ subscribers… 700 to 2,000 direct clicks" for standalone, and "if you'd like to book 5 placements… 10% discount" (19fd6845a8bb2456 2026-08-07).
- Event-format mechanics, in surprising detail — the Snowplow workshop-format explainer (how live chat Q&A works, "it's mostly hands-on… The only real way for them to communicate back to us is by using the live chat") is entirely hers (19e8757346a32ec8 2026-07-14).
- Billing-info collection, invoice sending, chasing, receipt confirmation.
- Empathy/deprioritization responses: guest medical appointment → "No worries and thank you for letting us know" + new slot; guest quits job → "Whenever the time is right, feel free to reach out, we'd love to have you. Wishing you all the best!" (19fa79fd01f093b0 2026-08-25); unresponsive partner → "Since we haven't received a response, we're not sure if you're interested… For now, we are going to use that time slot for something else." (19f37d15972fa49a 2026-07-30).

**Routes to Alexey (recurring patterns):**
- Guest-post/content-placement requests: "I have added Alexey to this thread so we can review your request together." (19bb6a6e36e40e3c 2026-01-13)
- Anything priced beyond the menu, packages, discounts, contracts, or "rate card" questions: "Thank you for reaching out! Adding Alexey to this conversation, thank you." (19e0142b42f3fb95 2026-05-07)
- Availability of Alexey himself: redirects to Calendly.
- Relevance judgment calls she soft-routes: for SoCap's freehand.ai she answers with a hedged position herself ("we're not sure how relevant it will be for our audience… If this is fine with you, we are open to moving forward") — but Alexey had already set the 1,200 EUR precedent.

---

## 3. Valeriia's email persona

### 3.1 Signatures (three distinct, context-dependent)

Content-manager role (formal):
```
Best,
Valeriia Kuka
Content Manager at DataTalks.Club
```
(sometimes with hyperlink on DataTalks.Club; variants "Best regards,", "Thank you!" + "Valeriia", "Cheers, Valeriia", "Thank you, Valeriia")

AI Shipping Labs role:
```
Best,
Valeriia Kuka
Co-founder, AI Shipping Labs
```

Russian personal threads with JetBrains: signs "Лера" or "Валерия" (1972f9fbff6e435d 2026-01-12: "Лиза, привет! С Наступившим Новым Годом!…").

### 3.2 What she writes, to whom

1. **Sponsor newsletter copy review** (to Astronomer/Natasha, Snowplow/Sydney&Adrianna, Cube/Beatriz, Atlan/Pragadeesh, Meritmap/Angela, Hackmamba/Henry): "Thank you for the copy and graphic. Everything looks good." (19f45adaf5afe718 2026-07-14) — or concrete editorial feedback: "I'd replace 'on top of Databricks' with another phrase because its already used in the first bullet point… Here's how we could edit it: '…*fits atop* Databricks…' or '…*integrates with* Databricks…'" (19ef370a01fd8b04 2026-06-26). She enforces the house rule: "we ask our sponsors to avoid using 'we' or 'our' because it can confuse our readers" (19bdbad3a4e51afe 2026-02-02). She also sends test emails: "I just sent a test email to … The subject line is '[Test] Build AI Analytics Agents on Trusted Data | DataTalks.Club Weekly.'" (19d3d8b8145e1fb7 2026-04-10) and can hard-deadline a sponsor: "Please respond within 2 hours. Otherwise, we will send it as is because we cannot delay the send due to the other sponsor." (19fead55212a8439 2026-08-17)
2. **Sponsor acquisition/reactivation (outbound sales)** — see templates in §6. A burst on 2026-03-06 hit Contextual, CodeRabbit, Galileo, W&B, MindsDB, NVIDIA in one afternoon; later Pinecone, Anyscale, Estuary, Snowflake-Elsa. Voice: "I'd be happy to share a few ideas if this is still relevant for your team."
3. **Podcast content prep**: drafts event descriptions on Luma and question docs, explains the podcast format to guests ("Alexey sets aside 10-15% of that time for audience questions", 19a9bedadccf887c 2026-01-20; "the podcast usually just goes with the flow… those as guide if the conversation ever gets stuck", 19f83c43758ec2d1 2026-09-14).
4. **Social-media promotion coordination**: Typefully draft links (19b6e84b5f190dd8 2026-01-23), promo-overview reports with every post link + metrics (DMF 2026, 19c0f00867199990 2026-05-18), performance commentary ("the clicks and CTR are definitely on the higher side… My suggestion is that we tweak the copy in our posts", 19d3d8b8145e1fb7 2026-04-20).
5. **AI Shipping Labs member onboarding** (Apr–Aug): welcome template (§6), personalized questionnaire docs, booking links (`calendar.app.google/...`), sprint onboarding, cancellations ("Sorry to see you go! You can cancel or manage your recurring subscription directly through Stripe.", 19f272a036d8eb8f 2026-09-30).
6. **Her own monthly invoices** to Grace+Alexey: "I'm sending over invoice F-0002-2026, dated May 13, 2026, for €1,000. Please find it attached. If you have any questions, just let me know." (19e20c9495ac5d06 2026-05-13; F-0001 €2,760.22 → F-0006 €1,000; Grace then pays and replies "Please see attached proof of payment.").
7. **Occasional sponsor-side diplomacy**: honest performance post-mortems — Snowflake March workshop underperformed and she wrote a long candid analysis + upsell to LLM Zoomcamp integration (19be4f3d7e05311a 2026-04-09: "To be honest, we expected it to perform better in terms of registrations and recording views…"); chased Snowflake's unpaid invoice herself when Grace's chases stalled: "Since the workshop was in March 2026 and it's now June 2026, could you please let us know the status of the invoice?" (2026-06-16).

### 3.3 Tone & structure

- Warmer and more personal than Grace: first-person "I", enthusiasm ("That sounds amazing!", "Excited to have you on board!"), empathy ("I understand that taking care of the baby is like another full-time job!"), owns mistakes plainly ("Oops, sorry for the 'Atlan' part!… I apologize for the mistake, and I promise it won't happen again." 19df1c9f126a136f 2026-05-19; 19d629d46a4fa2a1 2026-04-20).
- Longer, reasoned emails when persuading: numbered recap of a call (Snowflake options 1-2-3 with pricing links, 19bc178d4c12c921 2026-01-23), explanation of edit rationale (Collate rewrite, 19fa600fcaeee009 2026-08-21: "I've tried to make the user value clear from the start and catch their attention with the efficiency improvement (from 22 minutes to 90 seconds)…").
- Occasionally playful asides: "That's quite a bit of content to share today, especially at the end of the week :)"; "I know I've written a lot :)"
- Follow-up style: "Just wanted to follow up… in case it got lost in the shuffle." (19eee211d156bf4c 2026-07-02) — same politeness as Grace but more explanatory ("As soon as you can answer it, we can start working on your personal plan. Sprint 1 has already started…").
- Bilingual: switches to Russian with Elizaveta/JetBrains for scheduling and invoice nudges (1972f9fbff6e435d 2026-02-02: "Хотела спросить, как дела с обработкой нашего инвойса…").

---

## 4. Recurring email workflows

### W1. Podcast guest lifecycle (Grace leads; Valeriia prepares questions)

Trigger: guest confirmed by Alexey/Valeriia, or guest pitches in (1a0a8f81ef4e6ea9 "Guest pitch… evals that lie").

| Step | Timing | Who | Email |
|---|---|---|---|
| 1. Outreach intro | T-4 to -10 weeks | Grace | Intro template (§6 T1) with one proposed slot, e.g. Ruslan 2026-02-10 → event 2026-03-16; Sahil 2026-07-21 → event 2026-09-14 |
| 2. Guest replies w/ materials | — | — | Grace: "Thank you for confirming the date!" |
| 3. Questions doc + bio ask | same/next day | Grace | "I started a document for the podcast event on <date>. Check it out and feel free to add questions that you would like Alexey to ask you. I have added Valeriia, who will be helping to prepare the questions for the interview. Here's the document: <link> Also, please put your Bio in the document." (19c47889cf210043 2026-02-13) |
| 4. Calendar invite | immediately | Grace | Google Calendar, "(Proposed) <Name> at DataTalks.Club Podcast", 12:25–13:30 CET Monday slot, Zoom link in description; guest asked to accept: "also please accept the calendar invite sent to your email" |
| 5. Doc nudge if silent | +1–2 weeks | Grace | "Following up on the document details so we can publish it on our website and event platforms." (19e1b9d2a056e60e 2026-06-08) / "Following up, please fill up the document: <link>" (19c47889cf210043 2026-03-02) |
| 6. Registration link + share ask | ~1–2 weeks before | Grace | "For the event on <date>, we'll appreciate it if you could share the registration link to the event with your networks on social media. Here's the link: <luma>" (19e794950ae8a0d9 2026-06-22) |
| 7. Reminder | ~1 week / day before | Grace | "Just wanted to remind you about our podcast event tomorrow/on <date>… If you haven't shared the link, please help us spread the word… Happy New Year and see you tomorrow!" (19a4f28bd0540afc 2026-01-05) |
| 8. Event (live YouTube) | — | — | Alexey hosts |
| 9. Thank-you + links ask | next day | Grace | "Thanks again for the interview! It was great! Here is the Youtube link: <url> If you have a moment, could you please send us the links we should include to the description?" (19a9bedadccf887c 2026-01-27 — sent verbatim ~15× across the year) |
| 10. Amplification ask (sometimes) | +1–2 days | Grace | "If you have time, can you please share the podcast page with your networks… Also, we're always looking for more guests. Do you know anyone who you think would be interested in taking part in our events? We'll highly appreciate any recommendation." (19c47366ad305395 2026-03-04) |

Typical ending: guest sends links → "The links has been added to the description. Thank you so much." (19c89f9a7655a61b 2026-04-23). Guest ghosts/cancels: 1–2 gentle bumps → event cancelled with calendar note "Cancelled event, thank you." (19ef8a7f7931e2a8 2026-06-24; Brett 1a03d76a4fda83e2 2026-08-26) or postponed with warmth ("We'll reach out to you in November and good luck with your studies!" 1a0c82e26296d507 2026-10-01). Reschedule flow when DTC initiates: apology + options menu ("Please accept our sincere apologies for the late notice… *June 15, Mon at 2:30 PM - 3:30 PM*…" 19e83e94fe9a434b 2026-06-12).

### W2. Sponsor newsletter slot cycle (Grace operates, Valeriia reviews, Alexey prices)

Newsletter facts embedded in the workflow: sends Mondays ~10:00 CET ("Usually, we send the newsletter at 10:00 AM CET, and once it is sent, we can't make further changes." — Valeriia, 19b6e84b5f190dd8 2026-01-19); Primary/Secondary slots are Mondays only; Standalone ("blast") any non-Monday, "Wednesday is the best slot" (19cac6fb0da6df69 2026-03-23). Prices: Primary €1,500 / Secondary €1,000 / Standalone €2,500 (menu verbatim from Valeriia, 19bc178d4c12c921 2026-09-15).

1. **Quarterly booking** (e.g., Astronomer "plans for Q4 and 2026" 198ebc1159a1ff51; "FY27Q4" 1a081cd43fb9500b): Grace: "Would you be interested in booking newsletter slots for the upcoming quarter?" (2026-06-18) → sponsor sends dates → Grace validates Monday rule ("Just noticed these dates are mostly on Tuesdays. Since our slots are for Mondays, I wanted to double-check…" 2026-03-18) → confirms/declines per date ("The August 10 is already taken. Let us know if August 3, 17 or 24 works… Confirmed on: - August 31 …" 2026-06-29).
2. **Doc creation, T-14 days**: new thread "X + DataTalks.Club Newsletter - <date>" with template §6 T3, deadline = send date minus ~7–10 days.
3. **Copy chase**: Grace bumps the deadline; Valeriia bumps with more detail ("The newsletter with your ad will be live next Monday. Could you please fill out the copy and add media?" 2026-07-02); Valerija requests 1200×600 graphics ("It's our preferred format… media like that will make your ad more visible" 19e1c74cd2eb86fd 2026-06-25) and reviews ("Everything looks great, no edits needed." 2026-09-04).
4. **Test email** (standalones, Valeriia): "[Test] 📆 …" subject, feedback loop.
5. **Go-live** (Grace, Monday ~09:00): "Your promotion is now live! You can check how it looks here: <mailchi.mp link> In a week we will share the performance statistics with you."
6. **Stats, T+1 week** (Grace): "We just wanted to share how the newsletter performed last week: - 34,125 views / 3,134 clicks in the newsletter - 5,308 views / 260 clicks in LinkedIn - 423 views / 9 clicks in Twitter So 39,856 views and 3,403 clicks in total We hope you're satisfied with the results. Thanks for supporting us!" (19b2107245949d52 2026-01-19). If numbers disappoint, she contextualizes: "We checked the numbers and they are indeed lower than what we'd expect. That's probably likely because of the summer break." (19f7e53d1b41b715 2026-08-07).
7. **Invoice** (Grace): after slot or after confirmed booking (Astronomer: invoice sent 2026-03-19 right after date confirmation, 198ebc1159a1ff51); payment ladder §2.5; close: "We have received the payment. Thank you for supporting our community!"
8. **Renewal**: next quarter's "Would you be interested in booking…?" — cycle repeats. Thread ends when the sponsor goes quiet or the annual plan completes.

Decision points: slot taken (offer secondary/alternatives); sponsor wants discount → Alexey (volume-only policy); copy late near send-time → Valeriia's 2-hour ultimatum or send as-is; sponsor silent on reserved slot → Valeriia's release warning (§6 T19).

### W3. Sponsored workshop / webinar with external speaker (Grace leads; Valeriia edits copy; Alexey hosts)

Trigger: deal closed by Alexey/Valeriia, or inbound "Sponsorship Inquiry" (1a0f905bd60e88af, Voices.com 2026-10-05).

1. Grace kickoff (template §6 T2) with slot proposal — workshops typically Tue/Thu 16:25–18:00 CET ("Will August 24 at 2:00 PM to 3:30 PM CET work for the workshop?" 19f3678e1437fd44 2026-07-06), webinars Mon/Tue 12:25–13:30.
2. Speaker fills workshop doc (title/subtitle/description/bio/links). Placeholder Luma event if undecided: "we understand that you are busy and still deciding… everything is adjustable. However, we want to start promoting the event early… which is why we created this placeholder event." (19b2c4ebe3bada6d 2026-01-10)
3. Valeriia rewrites/versions the description (V2/V3 for Snowflake, 19be4f3d7e05311a 2026-02-19).
4. Grace: calendar invite, Zoom link, "please accept", share-the-registration-link ask, ~1-week reminder (identical templates as W1 steps 6–7).
5. Event day (Alexey hosts; Grace sometimes reminds the day before: "Let us know if you need anything from us like content feedback or other details." 19ece5fde8de8860 2026-08-17).
6. Post-event stats (Grace, T+1 day, template §6 T7): "We had 1,186 registrations: - 1,067 from Luma - 87 from Meetup - 32 from LinkedIn From them, 189 people came to the workshop to watch it live. Here's the recording: <yt> As of now, it has 1,291 views Also, attached here are the participants who agreed to share their emails with you: <sheet>" (19b2c4ebe3bada6d 2026-02-18). Bigger sponsors get the stats spreadsheet instead ("Here is a spreadsheet link with all the statistics that we pulled from social media and other platforms" 19b2184f54a65677 2026-02-18).
7. Invoice + ladder; occasionally a follow-up upgrade report a month later ("Just a quick update on the statistics we've pulled… Please note that it now include the post-workshop engagement as well." 2026-03-31).
Ending: sponsor thanks (dltHub Aashish 2026-02-18: "It is always a pleasure organizing these events with you, and we are looking forward to the next one!") or underperformance analysis from Valeriia + upsell (Snowflake 2026-04-09).

### W4. Invoicing & payments (Grace owns; verbatim ladder in §2.5)

Trigger: slot/workshop delivered or booking confirmed.
Steps: (1) billing-info request → (2) invoice PDF ("Please see the attached invoice and let us know if you have any questions.") → (3) if VAT unknown, she googles: "We found your VAT ID online. Please confirm that its yours…" (19c0e43f93e5c279 2026-04-09) or "We have found the billing details online." (Pathway 2026-08-18) → (4) wait 2–4 weeks → (5) "Following up on this invoice, please advise." (repeat every ~2–4 weeks) → (6) "We have received the payment. Thank you for supporting our community!" Payment-link alternative with 2–3% surcharge for credit-card payers (SoCap, Maven/Audrey). Installment tracking for Snowplow: "We have received the payment for the 1st installment. Please see attached invoice for the 2nd installment…" (19dfe2684ae57382 2026-06-06); 3rd installment 2026-09-02.

Related internal loop: Valeriia's own monthly invoice (F-000N-2026, €1,000–€7,000, varies with scope) → Grace pays via Finom → "Please see attached proof of payment. Thank you!" (×6 occurrences Feb–Sep).

### W5. Monthly accounting exchange (Grace)

Trigger: month end. Report 5th–12th (§2.7). Inbound from accountants in German/Russian → Alexey forwards/routes to Grace ("I think Grace has already done it", "please pay"). Once a year-style items: VAT-number correction invoice from ILZ (1a0f2780075e52d5). Zapier `dtctodo.2ebx61@zapiermail.com` is CC'd on many vendor receipts (Google Play, GoDaddy, Zoom, Uber) — an automated bookkeeping pipeline feeding the monthly report.

### W6. AI Shipping Labs member onboarding (Valeriia, Apr–Aug)

Trigger: new paid subscriber (Stripe) or access request.
1. Welcome (template §6 T16) — CC Alexey.
2. Reply → questionnaire doc ("I've prepared a list of questions to learn more about your goals and background: <doc>. You can answer them, and I'll share them with Alexey so he can prepare the plan." 2026-05-05) or direct call via `calendar.app.google/…` booking link.
3. Answers → "Alexey prepared the plan for you, and I added it to our document: <link>. Could you please take a look?" (2026-06-01).
4. Sprint context & nudges ("Sprint 1 started two weeks ago and will run for another four weeks, so that you can join it with your plan" 2026-05-18).
5. Endings: active member ("Sounds great!"); churn ("Sorry to see you go! You can cancel or manage your recurring subscription directly through Stripe… you're always welcome to join us again" 2026-09-30).

### W7. Book of the Week (Grace)

Intro template (19f1349daaa4cd01 2026-06-29): "I'm Grace, nice to e-meet you! I'm taking care of organizing events at DataTalks.Club, including the book of the week event. If you don't know much about this event yet, you can read more about it here: https://datatalks.club/docs/activities/book-of-the-week/… In summary, we invite book authors to our Slack and ask them questions about their book. You'll need to show up in our Slack for four days… not more than 15-20 minutes each day." Then: reminder + share link ("Your book is the book of the next week… Please help us spread the word on social media. Here's the link: <datatalks.club/books/…>" 19f17c2d24a7548e 2026-09-09); winners collection; winners sent to author — "Please send them e-book copies. Thank you!" (2026-09-23); chase if winners complain ("Just following up on the e-book copies… as one of them reached out asking for an update." 2026-10-05).

### W8. Sponsor reactivation campaign (Valeriia)

Trigger: quarterly (2026-03-06 batch; 2026-09-14 batch). Template §6 T15. Pattern: reference the previous contact ("DataTalks.Club partnered with X some time ago, and I wanted to reconnect."), update community stats ("We now have 90k+ Slack members and 149k+ newsletter subscribers"), tie to a hook (new LLM Zoomcamp cohort, their recent product launch — "I saw your recent runtime update and thought it would be a great time to reconnect", 197c06168df2a72a 2026-09-14), offer menu. Ends with booking (Estuary → slots quoted 2026-09-15) or polite silence.

---

## 5. Handoffs & escalation

### 5.1 CC patterns

- Grace CCs Alexey on virtually every external thread by default (he is on 157/340 threads mostly as CC). Valeriia CCs Alexey similarly. Guests/sponsors reply-to-all, so Alexey sees everything without acting.
- Grace adds Valeriia when copy review starts: "I am adding Valeriia to this thread. She is our content manager at DataTalks.Club and will help review the materials for the event." (19b2c3470965007e 2026-02-02) / "I have also added Valeriia who will review the document." (every newsletter doc email).
- Valeriia adds Grace for scheduling: "Grace, our community manager, will handle this. Grace, could you please create the documents for these two newsletter promo slots?" (19b6e84b5f190dd8 2026-01-13); "I'm adding Grace, our community manager, who will help us find a date…" (19e1c74cd2eb86fd 2026-05-13).

### 5.2 Explicit handoff phrases (verbatim)

- Grace → Alexey: "I have added Alexey to this thread so we can review your request together." (19bb6a6e36e40e3c 2026-01-13); "Adding Alexey to this conversation, thank you." (19e0142b42f3fb95 2026-05-07); "CC'ing Alexey so he is in the loop." (1a0b6bfadbf2442d 2026-09-30); "Please select a slot here for a call with Alexey: https://calendly.com/dtc-alexey/30min" (19ff19a6f1498c2f 2026-08-19).
- Alexey → Grace: "Thanks for the ping! Grace please do it" (19c0e43f93e5c279 2026-04-09); "Adding Grace. Can you please do it?" (SoCap payment link, 2026-03-25); "Grace, can you please check the availability of our newsletter?" (1a0b6bfadbf2442d 2026-09-24); "I'll add Grace to help us select the dates, she manages my calendar way better than me and otherwise I'll drop the ball again" (19cad4357823a7a9 2026-06-10); "Grace can you please confirm?" (accountants, 2026-04-20); "please pay" (1a0f2780075e52d5 2026-09-30).
- Alexey → Valeriia: "Sure. Adding Valeria and Grace" (Atlan last-minute blast, 2026-03-05).
- Valeriia → sponsor, referencing Grace: "I shared your email with our community manager, Grace. She will soon connect with you to agree on all the details." (19e5f2fd319f8a3f 2026-07-20).

### 5.3 Where Alexey steps in directly

- Package pricing & discounts (Atlan: "For your budget of $10k, it'd recommend going with 6 primary integrations, it'll be 9k EUR"; "We don't do discounts on blasts because we want to minimize the volume we send." 19c9471a5f3a8d67 2026-02-26/27). Quotes combos himself (NEXT QUERY: "standalone newsletter around 21st of October: 2,500 EUR; social media promotion from my personal accounts on October 26: 1,200 EUR… Total: 3,700 EUR" 2026-09-30).
- Payment disputes and missing money (SoCap "We haven't received it", IBAN back-and-forth 2026-05-13).
- Anything about him as a person: his rates ("My rate is 1200 Eur per post on both Twitter and LinkedIn", 2026-03-13), his availability, his content.
- Technical depth and negotiation of course integrations (Mihail cross-promo design, 2026-03-05).
- Vendor craft decisions (Podcast Engineers edit approvals: "The guests confirmed that it's good. Thanks Dave! Grace please schedule it for the next week." 19e78cee6cbdb0a7 2026-06-12).
- Contracts/legal (JetBrains procurement, SandboxAQ influencer contract — handled in threads Grace is not on).

### 5.4 Signature differences as role signals

Grace: full signature block always. Valeriia: short "Best, Valeriia" in quick replies, full block with role title in first-contact/formal; role in the signature changes with the product ("Content Manager at DataTalks.Club" vs "Co-founder, AI Shipping Labs"). Alexey: no signature at all, one-to-three-line messages, lowercase-informal ("Sure let's do it", "Got it. I booked next Friday 18:00") — an instant signal of who is speaking in mixed threads.

---

## 6. Template library candidates (verbatim skeletons, `{placeholders}`)

**T1. Podcast/webinar guest outreach (Grace)**
```
Hi {FirstName},

Nice to meet you! I'm Grace and I'm taking care of organizing events at
DataTalks.Club.

In case you don't know about our podcasts, you can read more about them here
<{podcasts-doc-link}>.

Do you already have ideas on the topics you'd like to talk about? Please
share them with us.

Also, please share anything you published online that you think will help
us prepare for the interview. For example:

   - Blog posts
   - Talks and podcast interviews
   - Social media posts
   - Github repositories

For the interview, will {Month} {Day}, {Weekday} at {12:30 - 1:30 PM CET} work for
you?

Looking forward to your response, thank you.
```
(cite: 19c47889cf210043 2026-02-10; webinar variant swaps in "Here you can read more about our webinars." — 19fd0b9dde84bb5f 2026-08-05; guest-pitch variant thanks for topics first — 1a0a8f81ef4e6ea9 2026-09-16)

**T2. Workshop kickoff with doc (Grace)**
```
Hi {FirstName},

This is Grace, a community manager at DataTalks.Club and take care of
organizing events.

Will {Day} at {4:30 PM to 6:00 PM CET} work for the workshop?

I created a Google document for our workshop:
{doc-link}

We will use this document for planning and announcements.

Please review it and fill in the missing parts: title, subtitle and
description, the speaker's bio and the links to the social media profiles.

I am adding Valeriia to this thread. She is our content manager at
DataTalks.Club and will help review the materials for the event.

Let us know if you have any questions. Thank you.
```
(19e8757346a32ec8 2026-06-02; placeholder-event variant: 19b2c4ebe3bada6d 2026-01-10)

**T3. Newsletter copy-document invite (Grace)**
```
Hi {ContactNames},

I'm Grace, a community manager at DataTalks.Club.

I've created a Google document for you to enter your copy:
{doc-link}

You'll find guidelines at the top of the document and in this visual guide
<{visual-guide-link}>.

For inspiration, here are a few examples of past sponsored content from our
newsletter:
"Model Monitoring Industry Certification":
 {https://mailchi.mp/datatalks.club/weekly-108}
"The Ultimate Guide to Scaling AI: AI at Scale":
{https://mailchi.mp/datatalks.club/weekly-110}
"The Robust & Responsible AI Summit 2023":
{https://mailchi.mp/datatalks.club/weekly-106}

You can find more examples here
<{campaign-archive-link}>.

To ensure we have enough time for any adjustments, please submit your copy
and graphics by {date}.

I have also added Valeriia who will review the document.

Looking forward to receiving your materials!

Thanks!
```
(19bb138a54dc9040 2026-01-12; used ~20× Jan–Oct with only the link/date changing)

**T4. Promotion live (Grace)**
```
Hi {FirstName},

Your promotion is now live! You can check how it looks here:
{mailchimp-link}

In a week we will share the performance statistics with you.

Thank you!
```
(19b2c344aae465bd 2026-01-05)

**T5. Newsletter performance stats (Grace)**
```
Hi {FirstName},

We just wanted to share how the newsletter performed last week:

- {34,125} views / {3,134} clicks in the newsletter
- {5,308} views / {260} clicks in LinkedIn
- {423} views / {9} clicks in Twitter

So {39,856} views and {3,403} clicks in total

We hope you're satisfied with the results. Thanks for supporting us!
```
(19b2107245949d52 2026-01-19)

**T6. Event reminder + share ask (Grace)**
```
Hi {FirstName},

Just wanted to remind you about the event next week on {date}.

Also, we'll appreciate it if you could share the registration link to the
event with your networks on social media.

Here's the link: {luma-link}

We're looking forward to your talk. See you soon!
```
(19a0143c5ea849b3 2026-01-13)

**T7a. Post-event thank-you, podcast (Grace)**
```
Hi {FirstName},

Thanks again for the interview! It was great!

Here is the Youtube link: {youtube-link}

If you have a moment, could you please send us the links we should include
to the description?
```
(19a9bedadccf887c 2026-01-27)

**T7b. Post-event stats, workshop (Grace)**
```
Hi {FirstName},

Thank you for the talk! Here are some statistics about the workshop.

We had {1,186} registrations:
   - {1,067} from Luma
   - {87} from Meetup
   - {32} from LinkedIn

From them, {189} people came to the workshop to watch it live.

Here's the recording: {youtube-link}

As of now, it has {1,291} views

Also, attached here are the participants who agreed to share their emails
with you:
{leads-sheet-link}
```
(19b2c4ebe3bada6d 2026-02-18)

**T8. Billing info request (Grace)**
```
Hi {FirstName},

We need some information for the invoice:

- the full legal name of the company
- the address
- VAT ID(If you are based in EU)

Looking forward to your response, thank you!
```
(19bdfb4134b81ecb 2026-01-21; "VAT ID(If based in EU)" variant 2026-05-05)

**T9. Invoice send (Grace)**
```
Hi {FirstName},

Please see the attached invoice and let us know if you have any questions.

Thank you!
```
(19bdfb4134b81ecb 2026-01-21)

**T10. Payment reminder (Grace — ladder steps 1 and 2 are the same text)**
```
Hi {FirstName},

Hope you are doing well.

Following up on this invoice, please advise.

Thank you.
```
(19ce75ee70944131 2026-05-07; plural "these invoices" when >1)

**T11. Payment received (Grace)**
```
Hi {FirstName},

We have received the payment. Thank you for supporting our community!
```
(19bdfb4134b81ecb 2026-02-23; short form "We have received the payment, thank you." 198ebc1159a1ff51 2026-03-02)

**T12. Payment link with surcharge (Grace)**
```
Hi {FirstName},

Here is the payment link with {3}% on top:
{revolut-checkout-link}

Please let us know if this works out for you and if not we can send you an
invoice for bank transfer.
```
(19ce75ee70944131 2026-03-26; 2% variant: 19e566fae1cb8e9f 2026-06-15)

**T13. Company/billing details block (Grace, for sponsors' procurement)**
```
Here are the details you requested:
*Company Details  *
Organization Name: DataTalks.Club
Registered Office: Schonensche Str. 13 10439 Berlin, Germany
TIN & TAX Number: DE343190995

*Billing Address  *
Country: Germany
Street Address: Schonensche Str. 13
Zip Code: 10439

*Bank Details  *
USD or EUR Account: EUR
Customer Name / Organization Name: DataTalks.Club
Account Number: Same as IBAN
Bank Address: Konstitucijos ave. 21B, 08130, Vilnius, Lithuania
IBAN Number: {LT583250049157217578}
Account Currency: EUR
SWIFT Code (Bank): {REVOLT21XXX}

*Authorized Signatory  *
Full name of the person signing the contract: Alexey Grigorev
Phone number and email address of the person signing the contract: {+49 162 267 9385} , alexey@datatalks.club
```
(19bdbad3a4e51afe 2026-01-21; short VAT form: "Company name: DataTalks.Club / Registered address: SCHONENSCHE STR, 13, BERLIN, 10439, GERMANY / VAT number: DE343190995" 19b30de3f93716bb 2026-01-13)

**T14. Monthly accountant report (Grace)** — see §2.7 verbatim; columns: `Date sent | Date paid | Provider | What | Price, $ | Price, EUR | Statement`.

**T15. Sponsor reactivation (Valeriia)**
```
Hi {FirstName},

DataTalks.Club partnered with {Company} some time ago, and I wanted to reconnect.

Since then, our community has grown significantly. We now have 90k+ Slack
members and 149k+ newsletter subscribers, and we continue running events
and courses for engineers working with data and AI.

It would be great to explore a collaboration again.

Happy to share a few ideas if it sounds interesting.

Best,
Valeriia Kuka
Content Manager at DataTalks.Club
```
(19cc3a3396832e6e 2026-03-06; event-hook variant: "I saw your recent runtime update and thought it would be a great time to reconnect." 197c06168df2a72a 2026-09-14; first-contact pitch variant with stats "135k newsletter subscribers, 80k Slack members" 19bb12b6feb0a911 2026-01-12)

**T16. Newsletter menu quote (Valeriia)**
```
For the newsletter, we have three sponsorship options:

- Primary slot: At the top of the newsletter. A good fit for product
announcements, courses, e-books, and guides. Expected clicks: 700-1,500.
Price: 1,500 euros.
- Secondary slot: In the middle of the newsletter, alongside community
content. Well-suited to events, webinars, and conferences. Expected clicks:
250-300. Price: 1,000 euros.
- Stand-alone email: A dedicated email to the full list, featuring only
your content, on an agreed date and time. A good option for launches and
lead-generation campaigns. Expected clicks: 700-2,000. Price: 2,500 euros.

We work with you on the copy and share a report with opens, clicks, and
click-through rate after the send.

We also have a media kit with all the sponsorship options:
{mediakit-link}
```
(19bc178d4c12c921 2026-09-15)

**T17. AI Shipping Labs welcome (Valeriia)**
```
Hey {FirstName},

Thank you for joining AI Shipping Labs! I'm Valeriia, one of the
co-founders, and I've cc'd Alexey here as well.

I'd love to learn more about what you're hoping to get from the community.
This will help us improve the community experience and give Alexey the
context he needs to prepare a personalized plan based on your background,
goals, and current situation.

You'll be able to use that plan in our upcoming community sprints. Each
sprint will have a clear timeline, deadlines, and regular stand-ups where
members can share progress, discuss challenges, and learn from each other.

Would you be open to a short call to discuss this?

Welcome to the community!

Best,
Valeriia Kuka
Co-founder, AI Shipping Labs
```
(19db4b3153dc930c 2026-04-22; sent ~8× verbatim Apr–Jul)

**T18. Questions-doc nudge (Grace, generic chase)**
```
Hi {FirstName},

Hope you are doing well!

Following up on the document details so we can publish it on our website
and event platforms. Let us know if you have any questions.

Thank you!
```
(19e1b9d2a056e60e 2026-06-08; Valeriia's variant: "Just wanted to follow up … in case it got lost in the shuffle." 19eee211d156bf4c 2026-07-02)

**T19. Reserved-slot release warning (Valeriia — the one escalation she owns)**
```
When we reserve a newsletter slot, we treat it as confirmed, keep it for
your campaign, and don't offer it to other sponsors. So we need to know
whether we should keep this slot for you or release it.

If you'd like to move forward, please complete the promo copy by tomorrow
so we can keep it on the schedule. Otherwise, we need to postpone it to a
later date.
```
(19bc178d4c12c921 2026-04-27)

**T20. Valeriia's monthly invoice (Valeriia)**
```
Hi Grace and Alexey,

I'm sending over invoice F-{000N}-2026, dated {date}, for {amount}€.
Please find it attached.

If you have any questions, just let me know.

Best,
Valeriia Kuka
```
(19e20c9495ac5d06 2026-05-13)

**T21. Calendar-invite body (Grace as organizer)** — includes Zoom link `https://zoom.us/j/94755324762` (later `https://us06web.zoom.us/j/86583618661`) plus "Podcast document: {doc-link}" or "Workshop document: {doc-link}" in the description; guests = speaker + Alexey (both mailboxes).

---

## 7. Automation notes

### Fully formulaic — an agent could draft (and mostly send with approval)

- **T4 promotion-live** (needs only the mailchimp link + Monday trigger), **T5 stats report** (needs the three platform metrics — pull from Mailchimp/LinkedIn/X), **T11 payment received** (bank-feed trigger), **T12 payment link** (Revolut link generation is the manual step).
- **T9 invoice send / T10 reminder** — the reminder is a scheduled re-send of one fixed paragraph every 2–4 weeks until the bank feed shows the amount; fully rule-based. Invoice PDFs are generated outside email (template + billing info from T8 answers).
- **T1/T2/T3 outreach & doc invites** — parameter fill from a "confirmed guest/sponsor + slot" record; doc + Luma event + calendar invite creation are the same pipeline (Grace already produces identical artifacts each time).
- **T6 reminder, T7a thank-you, T18 nudge** — event-date-triggered, content-identical.
- **T7b workshop stats** — formulaic given Luma/Meetup/LinkedIn export + YouTube count + leads sheet; only the "views so far" number is manual.
- **T14 accountant report** — the table is assembled from bank statements; auto-draftable, human check needed for the occasional annotation lines.
- **T17 ASL welcome** — Stripe webhook → verbatim email; the questionnaire doc link is per-member.
- Calendar invites with "(Proposed)" naming, cancellations with "Cancelled event, thank you." note.

### Needs human/agent judgment (not template-fillable)

- Date negotiation when guests counter-propose (Grace adapts slots, timezone slips — she even caught her own EST/CET mixup with Louis, 1a043288b730714a 2026-09-01).
- Performance objections (Astronomer's low-click summer — Grace decided to explain rather than compensate, 19f7e53d1b41b715 2026-08-07/10).
- Relevance calls on sketchy sponsors (SoCap/freehand — "we don't immediately see how it's relevant to our audience", 2026-07-20).
- Any discount, package, or nonstandard price → Alexey (volume-discount policy is verbal, not written down anywhere in these threads).
- Copy editing and sponsor-brand diplomacy (Valeriia's rewrites — Collate 2026-08-21, Meritmap banner redesign 2026-08-17/20).
- Conflict/lateness edge cases: Atlan's hour-before-publication edit (Valeriia's process-correction reply, 19b6e84b5f190dd8 2026-01-19), Pathway 2-hour ultimatum (2026-08-17), missing-payment dispute (Alexey), guest personal crises (medical appointment, family emergency — empathy replies + reschedule).
- Deciding when to cancel vs keep chasing (Irina webinar cancelled after two chases: "We're cancelling the event for now, let us know when you're ready", 19f1d24ecf2eca69 2026-10-02).

### Data dependencies an automation would need

Mailchimp campaign archive URL + open/click stats; LinkedIn/X impressions; Luma/Meetup registration breakdowns; YouTube view counts; opted-in leads sheet; invoice PDF generator + billing-info store; bank feed (Revolut/Finom) for received-payment detection; calendar (Google) with the fixed Zoom rooms; the two Google Doc templates (podcast questions, workshop details, newsletter copy) and the visual guide asset.

---

## Limitations

- ~10 messages have HTML-only or missing bodies (rendered from snippets; e.g., 19b2c3470965007e 2026-01-16). Quote-stripping cuts anything below the first quoted line, so rare bottom-posted replies may be truncated. Attachments are metadata-only — invoice PDFs, zips, and images referenced above could not be opened.
- The corpus is Alexey's two mailboxes: messages Grace/Valeriia sent to each other or to third parties without Alexey on CC are absent; Mailchimp test-sends to sponsors exist here only when Alexey was CC'd; Valeriia's LinkedIn outreach and Telegram are separate channels (a companion Telegram dataset exists in the same folder).
- Newsletter platform actions (test emails, the actual Monday sends) and stats-gathering steps happen outside email; the report infers timing from surrounding messages.
- Sponsor-side internal approvals (procurement, AP queues) are visible only through their replies.
