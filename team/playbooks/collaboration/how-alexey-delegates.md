# How Alexey delegates (input playbook)

How work flows from Alexey to Grace (ops) and Valeriia (content), as observed
in the 2026 Telegram exports and email. This is the input interface: if an
agent is to replace or assist them, it must accept work in these shapes.

Sources: `team/telegram-analysis/reports/dtc-chat-grace-analysis.md`,
`team/telegram-analysis/reports/team-email-analysis.md`,
`team/telegram-analysis/reports/valeriia-analysis.md` (for the content side).

## Input forms, in order of frequency

1. **Voice-note brain dumps** (255 notes to Grace in 2026; 1,334 to Valeriia;
   often 2–4 in a row). Alexey narrates context, intent, preferred outcome.
   He expects the receiver to structure it. Numeric facts (dates, amounts) are
   sometimes wrong and corrected later in text.
2. **`/todo` command to the dtc-chat bot** (~64 in 2026). One-liners, often
   minimal: `/todo podcast guest`, `/todo invoice dlthub (workshop 10k)`.
   The bot mirrors them into the daily TODO list.
3. **Recurring bot items** (posted daily ~05:00–06:00 Berlin, still active as
   of 2026-10-09): "Invite people to Slack from <Airtable view>",
   "Create new trello cards if necessary and go through existing ones",
   "Backup the mailing list from mailchimp to google drive",
   "Create a slack dump", "Make sure the newsletter for the next week is prepared".
4. **Link + one-line instruction**: Loom (process docs), Zoom recordings (with
   passcode), YouTube playlists, GitHub files (e.g. copy-bank event briefs).
5. **Contact forwarding**: email address ± LinkedIn URL ± one-line brief and
   context flags ("he was already a guest", "topic: his interview experience").
6. **Files**: invoice PDFs, bank statements, payment screenshots ("Kestra paid").
7. **Dictated content for ChatGPT**: full event descriptions dictated by voice
   for the receiver to promptify ("paste these to your GPT and turn them into
   lightning lesson descriptions").

## What he includes vs omits

- Includes: links, contact emails, sometimes price ("It's 5000 Eur"),
  date constraints, pointers to prior art ("check what we did last two times
  for the demo days").
- Omits: explicit deadlines (implicit), sponsor context (expects receiver to
  pull from Finom/contracts/Airtable: "you have all the details there like
  price, invoice items, etc also who to send"), and whether he already did
  part of the task himself.

## Phrasing conventions (verbatim examples)

- "Hey Grace are you here?" then the ask.
- "Can you please find it? Because I think we don't bill sandbox directly"
- "you don't need to run it by me just publish and send me the link when it's
  ready" — explicit skip-approval grant (rare, remember these).
- "please don't forget to chop the videos after editing so we can post them
  on social media / I think we haven't been doing it lately" — process nudges.
- Follow-ups: "what's the status of this?", "Did we send invoices to Kestra
  and dlt?", "are we ready with trello?"

## Contract for the receiving side

1. Acknowledge briefly ("Got it, thank youu^^" / "on it").
2. Look up missing context in the systems of record (calendar, Finom,
   Airtable, contracts, past threads) — do not ask Alexey for what is
   findable.
3. Draft the artifact, post it for approval with a screenshot
   ("Here is the draft for your checking / Kindly check for any changes
   needed").
4. Execute on approval, then report completion with evidence (link +
   screenshot of the result).
5. If Alexey hasn't replied and it's blocking, one polite follow-up ("Just
   following up on the invoices and statements, thank youu^^").

## Response-time expectations

Median reply Alexey→Grace ~11 min, Grace→Alexey ~14 min during working
hours (Berlin mornings overlap). Grace works ~08:00–17:00 Berlin (APAC
timezone). Weekends are mostly off; both break the rule for live events.
