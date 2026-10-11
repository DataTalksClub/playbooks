# How Grace and Valeriia ask Alexey things (escalation playbook)

What an assistant escalates to Alexey, in what form, and what Alexey's answer
looks like. Use this to decide what an agent must surface vs decide alone.
Sources: the 2026 Telegram + email analyses (`team/telegram-analysis/reports/`).

## Question taxonomy (Grace, by frequency)

1. **Scheduling choice** — "For Ricardo's Workshop Will February 02 at
   12:00–1:30 PM CET works for you?" Always 1–3 pre-filtered options,
   usually with a calendar screenshot attached (explicitly praised by Alexey:
   "I like it when you do that =)").
2. **Draft approval** — "Here is the draft for your checking" / "Kindly check
   the draft for any changes needed". Nearly all outbound communication goes
   through this gate.
3. **Missing information** — "For Exasol, kindly advise on VAT number";
   "Is the description 'AI Bootcamp 2026 Cohort 2, Payout 3'?"
4. **Confirm assumption** ("Should we…?" ×44) — "Should we use your Personal
   bank account for the IBAN…just like what we did to their last invoice?"
5. **Understanding check** — "Please correct me, we will also have a podcast
   with Leonid Kholkine and if yes…"; "I got confused does it mean he wants
   the date to be earlier?"
6. **Policy / judgment** — "They are asking for discount. Kindly advise";
   "Should we follow up, or since she didn't confirm at the end of the month
   they will not take it".
7. **Technical blocker** — GitHub action failures, Finom lockouts,
   YouTube transcript missing, LinkedIn access.

## What gets escalated vs decided alone

**Always escalate (money & commitments):**
- prices, discounts ("typically we don't really give discounts for one of
  new sliders"), payment-link surcharge % (2–3%)
- which legal entity to bill; VAT treatment when ambiguous
- sponsor date/slot commitments when non-standard
- anything using Alexey's identity: signatures, bank statements, his accounts

**Escalate for information only:**
- unlabeled transactions ("What should we put as description for 6 Jan 2026
  Xai LLC invoice?" → "GLM Max coding plan - put this")
- missing invoice PDFs (Alexey hunts them in email/Stripe/PayPal)

**Proceed on assumption, confirm in passing (reversible/formatting):**
- currency choice based on last invoice, address found online
  (confirm with the client, not Alexey: "We found this VAT ID online.
  Please confirm that it's yours")
- formatting fixes, moving drafts into the right folder

## How Alexey answers

- Short, fast, text — "Yes", "Looks good", "March 17 please", "let's do
  tuesday". Median ~11 min during working hours.
- Explains reasoning by voice when teaching (attribution logic, VAT rules,
  why not to count third-party RSVPs).
- Sometimes late with apology ("I'm sorry, I missed that message about
  August report").
- Rarely grants skip-approval; when he does it's explicit: "you don't need
  to run it by me just publish and send me the link".

## Valeriia's escalations (content side)

- Copy that would confuse readers → she proposes concrete edits and a
  hard deadline ("Please respond within 2 hours. Otherwise, we will send it
  as is because we cannot delay the send due to the other sponsor.")
- Reserved newsletter slots at risk → she owns the release warning
  ("we treat it as confirmed… so we need to know whether we should keep
  this slot for you or release it")
- Performance dips → honest reporting + suggested next step, Alexey frames
  the external message ("likely because of the summer break")
- Pricing beyond the menu → Alexey ("We don't do discounts on blasts
  because we want to minimize the volume we send.")

## Handoff phrases in email (verbatim)

- Grace→Alexey: "I have added Alexey to this thread so we can review your
  request together." / "Adding Alexey to this conversation, thank you." /
  "CC'ing Alexey so he is in the loop."
- Alexey→Grace: "Thanks for the ping! Grace please do it" / "Adding Grace.
  Can you please do it?" / "I'll add Grace to help us select the dates, she
  manages my calendar way better than me and otherwise I'll drop the ball
  again" / "please pay"
- Grace→Valeriia: "I am adding Valeriia to this thread. She is our content
  manager… will help review the materials for the event."
- Valeriia→Grace: "Grace, our community manager, will handle this. Grace,
  could you please create the documents…?"
- Valeriia→sponsor about Grace: "I shared your email with our community
  manager, Grace. She will soon connect with you to agree on all the
  details."

## Blocking behavior rules (observed norms)

- One polite follow-up after ~1 day; do not spam.
- Never leave a failure silently — flag it ("I'll appreciate it if next time
  you flag it" — Alexey, after a silent GitHub failure).
- Self-report misses immediately with the fix ("I missed to post Snowflake
  last week… Just posted it now").
- System outages: document attempts, escalate with screenshots, propose a
  workaround.
