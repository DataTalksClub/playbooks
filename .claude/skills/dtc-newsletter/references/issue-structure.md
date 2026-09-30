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
| 7 | Recordings, one slot per type: workshop, podcast, webinar | A recording of that type is published and no sent issue has featured it | `sources.md`, YouTube channel, YouTube description or transcript |
| 8 | Book of the Week | A Book of the Week runs this week | `sources.md` (website) |
| 9 | From Alexey on Data | Alexey published a post since the last issue | `sources.md` |

Past issues sometimes placed an event detail slot after the list or Book of the Week before it. Use the order above unless the user asks otherwise.

## Sections

Slots are grouped into sections, each marked in the email by a section label (see `design-brief.md`, B3):

| Section | Label | Slots |
| --- | --- | --- |
| Sponsor | `SPONSORED` | Primary promo; secondary promo gets its own `SPONSORED` label where it sits |
| Courses | none: each course slot starts with its course banner | Zoomcamp slots, course registration slots |
| Events | `EVENTS` | Event detail slots, Upcoming events |
| Recordings | `RECORDINGS` | Workshop, podcast, and webinar recordings |
| Read | `READ` | Book of the Week, From Alexey on Data |

A divider goes above every section label except the first one in the email. Skip a section's label when the section has no slots.

Order Zoomcamp slots by cohort start date, oldest cohort first. Every running course in `sources.md` gets a slot unless the brief leaves it out; mention in your reply any course you left out.

Give an event a detail slot when it is:

- a Zoomcamp launch stream or pre-course Q&A,
- a hands-on workshop in the next 10 days,
- a new multi-part series (group all parts in one slot, like a course event series), or
- an event the user asks to feature.

A sponsored event normally takes a promo slot instead of a detail slot. Every event with a detail slot still appears in the Upcoming events list.

If there is only one Alexey post, use it. If there are several, prefer the one that is not already promoted elsewhere in the issue, and ask when unsure.

For recordings, pick the newest one of each type (workshop, podcast, webinar) that no sent issue has featured yet, even if it was uploaded before the last issue. Check the YouTube channel as well as `sources.md`, because the website's events list often lags behind. Each type gets its own slot, in that order.

## Length

Include every slot that has content. A complete issue matters more than a short one, and there is no slot limit. The order above keeps the most important slots near the top.

The real limit is size. Gmail clips emails whose HTML is over 102 KB and shows "[Message clipped] View entire message", which hides the lower slots, the unsubscribe footer, and the open-tracking pixel. Past archive pages measured 111–128 KB (6 to 8 slots), and each extra Mailchimp block adds about 8 KB. To keep content without adding size, put related slots in one Mailchimp text block (for example, all recordings in one block, one heading each) instead of a separate block per slot. Remind the user to check a test send in Gmail for clipping; do not send the test yourself.

## Output Format

Save `issue.md` with this shape. The user builds the email by hand in Mailchimp from it, so the draft marks each template piece:

- `[Divider]`: a Divider block (settings in `design-brief.md`, B3).
- A line in capitals such as `SPONSORED` or `EVENTS`: a section label, pasted with the label snippet from `design-brief.md`, B3.
- `[Banner: Course name]`: the course banner image, with the course name as its alt text. When a course has no banner yet (see the status in `design-brief.md`, A2), write `[Banner: Course name (not made yet; fallback heading: [Course name] [Year]: Module N)]` so the user can switch to the fallback heading.
- `##` heading: a slot heading.
- A link alone on its own line: the slot's button. In the Recordings and Read sections it becomes a text link instead (see `design-brief.md`, B7).

```markdown
---
issue: 296
send_date: 2026-09-28
status: draft
---

Mailchimp campaign name: Weekly email #296 (Sep 28, 2026) - sponsored

Subject line options:
1. ...
2. ...
3. ...

Preview text: ...

Masthead line: #296 · September 28, 2026

---

**This week:** [summary]

SPONSORED

## [Sponsor heading]

[Body]

[Button label](https://...)

[Banner: Machine Learning Zoomcamp]

## Module 2: Machine Learning for Regression

[Body]

[Join Module 2](https://...)

[Divider]

EVENTS

## [Slot heading]

...
```

The masthead line goes into the live text under the masthead logo. The **This week** summary is the first text block of the email: one or two sentences, at most 40 words, naming the main items in slot order, for example "This week: an Airflow webinar on ETL/ELT pipelines, Module 5 of AI Dev Tools Zoomcamp, a two-part series on building AI platforms, and three new recordings." Name what is there; do not add urgency or promises.

With a course banner, the course slot heading drops the course name: `Module [N]: [module title]`, using the module title from the course's Telegram announcement or `course.yaml`.

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
- Every button and event title has a real URL or a visible `TODO(...)`.
- Every deadline and event time matches `sources.md` exactly, including CET or CEST.
- Every sponsored slot starts with the `SPONSORED` label, and no other slot has it.
- Every section label has a `[Divider]` above it, except the first section in the email, and no divider sits between slots inside a section.
- The **This week** summary names only items that are in the issue.
- Names of people, companies, and products are spelled the same way in every slot and match the source.
- No pronoun is used for a person unless the source uses it; otherwise use the name or restructure.
- Course headings follow `Module N: [module title]` under a banner, or `[Course name] [Year]: Module N` when the course has no banner yet.
- Buttons point to pages readers can open: module materials on GitHub, learner-facing platform pages (`/project/<slug>/eval` for peer review), never `/cadmin/` admin pages.
- Dates in the body use one format: "October 8", "September 14–18".
