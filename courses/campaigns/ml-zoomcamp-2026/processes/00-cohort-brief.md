# Cohort Brief

This file defines the campaign decisions for this cohort.

It does not contain the execution checklist, campaign calendar, copy drafts, or weekly tracking.

Create a copy of this file for each new course cohort.

## 1. Cohort Basics

Course: Machine Learning Zoomcamp
Cohort year: 2026
Start date: Monday, September 14, 2026
End date: Monday, January 25, 2027
Schedule verified: October 10, 2026 via production API; see `../sources/platform-2026-10-10.json`.
Registration link: https://courses.datatalks.club/register/ml-zoomcamp/

Course platform URL: https://courses.datatalks.club/ml-zoomcamp-2026/

Current registrations: 0 (as of August 2, 2026)
Target registrations:
Stretch goal:
Days until start: 43 (about 6 weeks, as of August 2, 2026)

Campaign intensity:
Normal / Extra push

## 2. Course Outline

The confirmed deadline schedule from `01-course-platform-setup.md`. Fill this in after the outline exists on the platform, and use it when filling the campaign calendar.

Deadlines are Monday at 23:00 UTC. The creation-time plan below has been updated from the production API. Homework 1 is scored; the other homeworks are open as of October 10. All projects are closed. Recheck states before announcing availability.

| Item | Slug | Deadline | Notes |
| --- | --- | --- | --- |
| Homework 1: Introduction to Machine Learning | `hw01` | Mon 2026-09-28 | |
| Homework 2: Machine Learning for Regression | `hw02` | Mon 2026-10-05 | |
| Homework 3: Machine Learning for Classification | `hw03` | Mon 2026-10-12 | |
| Homework 4: Evaluation Metrics for Classification | `hw04` | Mon 2026-10-19 | |
| Homework 5: Deploying Machine Learning Models | `hw05` | Mon 2026-10-26 | Use the FastAPI + uv workshop, not the older module |
| Homework 6: Decision Trees and Ensemble Learning | `hw06` | Mon 2026-11-02 | |
| Homework 8: Neural Networks and Deep Learning | `hw08` | Mon 2026-11-30 | No `hw07`: that slot is the midterm project |
| Homework 9: Serverless Deep Learning | `hw09` | Mon 2026-12-07 | |
| Homework 10: Kubernetes | `hw10` | Mon 2026-12-14 | |

Project blocks and their submission and peer review deadlines:

| Project | Slug | Submission | Peer review |
| --- | --- | --- | --- |
| Midterm Project | `midterm` | Mon 2026-11-16 | Mon 2026-11-23 |
| Capstone 1 | `capstone1` | Mon 2027-01-04 | Mon 2027-01-11 |
| Capstone 2 | `capstone2` | Mon 2027-01-18 | Mon 2027-01-25 |

Schedule notes:

- The 2025 cohort ran three capstone slots. 2026 runs two, matching the certificate rule of two required projects.
- The gap between `hw10` (December 14) and Capstone 1 submission (January 4) covers the holiday weeks.
- Platform certificate settings: one project minimum to pass, project passing score 7. Published ML certification docs require two projects. This conflict needs reconciliation; the drafts link to the requirements without repeating a numeric promise. No platform settings were changed.
- Telegram drafts and their recommended posting dates are indexed in `../copy-bank/telegram/README.md` and `telegram-announcement-calendar.csv`.
- `02-campaign-calendar.csv` has real dates through module 6 week (T+39 days). Rows past that are marked `Needs manual mapping`: the generic template assumes eight consecutive module weeks and one final project, while ML Zoomcamp interrupts the modules with the midterm block and finishes with two capstones. Map those rows against the outline above by hand.

## 3. Registration Gap

Registrations needed for target:
Weeks until start: 6
Needed per week:

Decision:

- [ ] Run standard launch
- [ ] Add extra push

Extra push means we add one or more of these:

- [ ] Alumni outreach
- [ ] Influencer / practitioner outreach
- [ ] Partner and sponsor posts
- [ ] External newsletters
- [ ] External communities
- [ ] Course directories and learning platforms
- [ ] Guest posts / contributed tutorials
- [ ] Podcasts and guest appearances
- [ ] Short-form video clips
- [ ] SEO articles
- [ ] Downloadable lead magnet
- [ ] Referral experiment
- [ ] Paid or boosted distribution
- [ ] University / student club outreach
- [ ] Company / team learning outreach
- [ ] Product Hunt or launch platforms

Note: the standard campaign calendar opens at T-12 weeks. This cohort is at T-6 weeks, so the Foundation phase and the first half of Awareness are already past. Decide whether to compress those posts into the remaining weeks or drop them.

## 4. What Changed This Year?

- Curriculum changed: No — the 2025 materials are reused
- Tools changed: No
- Homework changed: Yes — new homeworks this year
- GitHub README needs major rewrite: No
- FAQ needs update: Done — year-stamped questions rewritten
- Welcome email needs update: Not yet checked

Notes:

- **Materials are reused from 2025, and homeworks are new.** 2025 was the big content refresh: FastAPI for deployment, PyTorch for neural networks, ONNX Runtime on AWS Lambda. Those materials stay. What changes for 2026 is the homework.
- Copy angle: the content is current and proven, not stale, and returning learners get fresh homework. Do not promise a refreshed curriculum, because there is not one this year.
- Because there is no big "what's new" curriculum story, the campaign leans on proof and outcomes. The 2025 numbers and project proof are now in `ml-zoomcamp/proof-library/`; testimonials are still empty and need a human pass.
- New homeworks mean the questions cannot be copied from 2025. Each homework's questions are written from that module's `homework.md` when the module opens.
- What else changed is logistics, not content:
  - Registration moved from Airtable to the platform registration page at `https://courses.datatalks.club/register/ml-zoomcamp/`.
  - Deadlines are now all on Mondays. The 2025 cohort used mixed weekdays.
  - Three capstone slots in 2025 became two in 2026.

## 5. Channel Decisions

Default channels:

- [ ] DTC newsletter
- [ ] DTC LinkedIn
- [ ] Alexey LinkedIn
- [ ] DTC Twitter/X
- [ ] Alexey Twitter/X
- [ ] DTC Slack
- [ ] Reddit (two posts: one month before, and start day)
- [ ] Website banner
- [ ] Course article
- [ ] Course landing page
- [ ] GitHub README
- [ ] YouTube descriptions / pinned comments
- [ ] Launch stream

Extra channels for this cohort:

- [ ] Alumni outreach
- [ ] Influencer / practitioner outreach
- [ ] Partner and sponsor posts
- [ ] External newsletters
- [ ] External communities
- [ ] Course directories and learning platforms
- [ ] Guest posts / contributed tutorials
- [ ] Podcasts and guest appearances
- [ ] Short-form video clips
- [ ] SEO articles
- [ ] Downloadable lead magnet
- [ ] Referral experiment
- [ ] Paid or boosted distribution
- [ ] University / student club outreach
- [ ] Company / team learning outreach
- [ ] Product Hunt or launch platforms

Decision notes:

## 6. Event Decisions

Events start at 17:00 Europe/Berlin, on a Monday or sometimes a Tuesday.

- Pre-course workshops: No — none this year
- Graduate podcast or interview stories: [Yes / No]
- Pre-course Q&A: Yes — Tuesday 1 September 2026, 17:00 Europe/Berlin
- Launch stream: Yes — Monday 14 September 2026, 17:00 Europe/Berlin (course start date)

Decision notes:

- The 2025 cohort ran a pre-course Q&A and a launch stream with course overview. Both are repeated this year.
- The Q&A is 13 days before the start, which puts it in the Decision phase of the campaign calendar with time left to register.
- No pre-course workshops this year. The workshop announcement row in `02-campaign-calendar.csv` is marked dropped.

## 7. Owners and Approval

- Website/GitHub owner:
- Newsletter owner:
- DTC social owner:
- Alexey social drafts owner:
- Events owner:
- Tracking owner:

## Final checklist

This brief is complete when:

- [x] Start date is confirmed
- [x] Course exists on the platform
- [x] Registration campaign points to this cohort
- [x] Course outline is created and verified
- [x] Registration link is confirmed
- [ ] Registration target is set
- [ ] Registration gap is calculated
- [ ] Campaign intensity is selected
- [x] Changes from last year are listed
- [ ] Channels are selected
- [x] Events are selected — no workshops; Q&A 1 Sep, launch stream 14 Sep. Graduate podcast still open
- [ ] Owners are assigned
