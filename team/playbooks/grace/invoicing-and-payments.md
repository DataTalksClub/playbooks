# Playbook: Sponsor invoicing & payment chasing (Grace)

Source: `team/telegram-analysis/reports/dtc-chat-grace-analysis.md` (P2,
taxonomy 3.2) and `team-email-analysis.md` (W4, T8–T13).

**Trigger**: completed deliverable (newsletter slot, workshop, social promo),
`/todo invoice <company> <amount>`, sponsor request, or the monthly
"who hasn't paid" sweep.

## Invoice creation

1. Find billing details in Finom contacts / prior invoices / contracts.
   Missing VAT or address → look it up online, then confirm with the client:
   "We found this VAT ID online. Please confirm that it's yours."
2. Draft in Finom:
   - description convention: `<Deliverable> (<date or period>)`,
     e.g. "AI Engineering Buildcamp: From RAG to Agents Cohort 3 (13 April
     2026)", "X Revenue Sharing (Apr 11, 2026 - May 23, 2026)"
   - reverse-charge VAT for EU B2B
   - contracts split into installments (e.g. Snowplow 20k → 4×5,000
     "2026 Community Sponsorship, Nth Installment")
   - PDF filename: `2026-<MM>-<Legal Entity>-datatalksclub-sponsorship.pdf`
3. Screenshot + "Here is the drafted invoice for your checking" → Alexey.
4. Send on approval (T9), log in the bookkeeping sheet.
5. Alternative: Revolut payment link with 2–3% surcharge on top (T12) —
   surcharge % is Alexey's call.

**Alexey decisions**: price, description, currency, which entity to bill
(there are agencies behind some products — "I think we don't bill sandbox
directly… it's this agency who we should bill"), surcharge %.

## Payment chasing ladder

1. Send invoice (T9).
2. Mention the unpaid invoice when sending the next one; consolidate AP
   threads ("I have also forwarded the March invoice in the thread with
   ap@atlan.com so you have everything in one place.").
3. Reminder every 2–4 weeks, same paragraph verbatim (T10), re-attaching
   the PDF each time. Defend billing data when challenged ("We checked the
   IBAN and this is correct, this is a bank in Lithuania thats why its 20
   characters long.").
4. Payment received → T11 + notify Alexey; annotate currency-conversion
   differences on the PDF.
5. Disputes or non-payment beyond ~2 months → Alexey steps in.

**There is no step beyond repeating T10** — that is the whole ladder.

## Related

- Revenue-side invoices (X revenue sharing, Stripe/ASL payouts, Maven
  payouts, reimbursements): same flow, process docs from 2026-04-07.
- Valeriia's own monthly invoice F-000N: Grace pays via Finom and returns
  the proof-of-payment PDF.
- The unpaid sweep: "check which invoices still aren't paid" runs roughly
  monthly; a Trello checklist step for invoice-before/paid-after exists
  since 2026-02-11.

**Frequency**: weekly; dozens of sponsors in 2026 (Temporal, Atlan, Nebius,
Snowflake, Snowplow, dlthub, Bruin, Exasol, JetBrains, Astronomer, Cube,
Kestra, Pathway, Maven, X Corp, McKenzie/Command, Anaconda, Hackmamba…).
