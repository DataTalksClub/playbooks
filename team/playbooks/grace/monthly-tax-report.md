# Playbook: Monthly tax report / bookkeeping assembly (Grace)

Source: `team/telegram-analysis/reports/dtc-chat-grace-analysis.md` (P3,
taxonomy 3.3) and `team-email-analysis.md` (§2.7, W5, T14).

**Trigger**: calendar — first week of each month (observed 2026: sent on the
5th, 5th, 9th, 6th, 5th, 5th, 7th, 10th, 2nd, 6th for months Dec-2025 →
Sep-2026). Ten consecutive monthly cycles.

## Steps

1. Reconcile bank statements (Finom / Revolut / PayPal) against known
   invoices; produce the gap list:
   "For {Month} Tax Report we need the following: Invoices: … Statements: …"
2. Ask Alexey description questions for unlabeled items
   ("What should we put as description for 6 Jan 2026 Xai LLC invoice?" →
   "GLM Max coding plan - put this").
3. Alexey hunts and drops missing invoice PDFs / Stripe links (this is the
   recurring friction: AWS, Google Cloud, Loom, GoDaddy, OpenAI go missing
   regularly).
4. Build the report: monthly email thread "DataTalks.Club {Month} {YYYY}"
   to the accountants (ILZ Steuerberatung), CC Alexey, table with columns
   `Date sent | Date paid | Provider | What | Price, $ | Price, EUR |
   Statement`, one line per transaction, + "Also, the zip archive file has
   been uploaded to the server. Let us know if you have any questions."
5. Upload the monthly zip to the accountant's server.
6. Draft + screenshot → Alexey approves ("Looks okay. Thanks!") → send.
7. Route accountant replies (German/Russian, addressed to Alexey) back to
   actions: confirm what's done, pay their fee invoices ("please pay").

## Known annotations Grace adds

- "We cannot find the invoice for Feb 2026 AWS Cloud services: €-0.78"
- "the transaction on 26 May 2026 Flix -73.47 was a mistake, as Alexey
  accidentally used the company card instead of his personal card"

## Automation notes

- Mechanical: matching bank lines to receipts, the report draft, the zip
  upload, detecting the missing-invoice list.
- Human: descriptions, statement-vs-invoice substitutions, refunds/conversion
  treatment.
- An automated receipts pipeline already partially exists: vendor receipts
  (Google Play, GoDaddy, Zoom, Uber) auto-CC to `dtctodo@zapiermail.com`
  via Zapier.
