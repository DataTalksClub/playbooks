# Issue Structure

## Slot Order

Slots always appear in this order. Skip any slot with no content that week.

| # | Slot | Present when | Source |
| --- | --- | --- | --- |
| 1 | Primary promo | A sponsor or DataTalks.Club product has the top slot this week | `newsletter/sponsors.yaml`, user |
| 2 | Zoomcamp slots, one per running cohort | A cohort has a module, project submission, or peer review this week | `sources.md` (course platform) |
| 3 | Course registration slots | A course is open for registration before its cohort starts | Course copy bank, user |
| 4 | Secondary promo | A second sponsor or product slot is booked | `newsletter/sponsors.yaml`, user |
| 5 | Event detail slots, including a course's event series and workshop notes | An event deserves more than a list line (see below) | `sources.md`, Luma page, user |
| 6 | Upcoming events | At least one upcoming event | `sources.md` |
| 7 | Book of the Week | A Book of the Week runs this week | `sources.md` (website) |
| 8 | Latest recording | A podcast, workshop, or webinar recording was published since the last issue | `sources.md`, YouTube description or transcript |
| 9 | From Alexey on Data | Alexey published a post since the last issue | `sources.md` |

Past issues sometimes placed an event detail slot after the list or Book of the Week before it. Use the order above unless the user asks otherwise.

Order Zoomcamp slots by cohort start date, oldest cohort first. Every running course in `sources.md` gets a slot unless the brief leaves it out; mention in your reply any course you left out.

Give an event a detail slot when it is:

- a Zoomcamp launch stream or pre-course Q&A,
- a hands-on workshop in the next 10 days, or
- an event the user asks to feature.

A sponsored event normally takes a promo slot instead of a detail slot. Every event with a detail slot still appears in the Upcoming events list.

If there is only one Alexey post, use it. If there are several, prefer the one that is not already promoted elsewhere in the issue, and ask when unsure.

If several recordings came out, feature the one with the most practical content (workshops before podcasts), and ask when unsure.

## Length

A typical issue has five to seven slots. When an issue runs past seven, suggest to the user which detail slots to cut back to a list line rather than dropping content on your own.

## Output Format

Save `issue.md` with this shape. The email tool renders each `##` heading as a block title, a link alone on its own line as the block's button, and `_Sponsored content_` as the sponsor label.

```markdown
---
issue: 296
send_date: 2026-09-28
status: draft
---

Subject line options:
1. ...
2. ...
3. ...

Preview text: ...

---

## [Slot heading]

[Body]

[Button label](https://...)

_Sponsored content_
```

Subject lines and preview text sit above the `---` divider and are not part of the email body. Past subjects follow one pattern:

```text
🛠️ Build predictive audiences from live data | DataTalks.Club Weekly
📗 Data engineering guide to AI context | DataTalks.Club Weekly
```

- Start with one emoji: 🛠️ for workshops, courses, and hands-on events; 📗 for guides, ebooks, and books.
- Then a short headline for the paid sponsor's slot when the issue has one, even if a DataTalks.Club product holds the primary slot. Without a sponsor, feature the most useful item.
- End with ` | DataTalks.Club Weekly`.
- Offer three options, each under 70 characters including the suffix.
- Preview text: one sentence about the featured item, under 150 characters. Use the sponsor's preview text when they supply one.

Also give the Mailchimp campaign name: `Weekly email #[N] ([Mon D, YYYY]) - sponsored` or `- not sponsored`.

## Final Checks

Before saving, confirm:

- Every slot with no content is gone, with no "nothing this week" filler.
- Every button and event line has a real URL or a visible `TODO(...)`.
- Every deadline and event time matches `sources.md` exactly, including CET or CEST.
- Every sponsored slot ends with `_Sponsored content_`, and no other slot does.
- Names of people, companies, and products are spelled the same way in every slot and match the source.
- No pronoun is used for a person unless the source uses it; otherwise use the name or restructure.
- Course headings follow the `[Course name] [Year]: Module N` pattern.
- Buttons point to pages readers can open: module materials on GitHub, learner-facing platform pages (`/project/<slug>/eval` for peer review), never `/cadmin/` admin pages.
- Dates in the body use one format: "October 8", "September 14–18".
