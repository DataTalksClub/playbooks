# Slots

Every slot is a heading, a short body, and usually one button. Write for a reader skimming an email: the first sentence of each slot should tell them whether it is for them. Word counts are for the body, excluding the heading and button.

## Primary And Secondary Promo

For a sponsor or a DataTalks.Club product such as AI Engineering Buildcamp.

- Heading: the offer, resource, or event title the sponsor uses.
- Body: one or two short paragraphs on the reader's problem and what the offer gives them, then three to five bullets when the source has concrete items, then the promo code or date line if there is one. At most 120 words.
- Button: the sponsor's call to action, such as "Enroll here", "Download for free", or "Save your seat".
- End with `_Sponsored content_` for any paid placement or DataTalks.Club paid product.

Example, from #295:

```markdown
## AI Engineering Buildcamp: From RAG to Agents

AI Engineering Buildcamp starts today. 25 people enrolled last week, and the first week is buffer time, so you can still join.

You'll build 15 AI projects from scratch:

- Documentation Agent that evolves from basic RAG to production system
- AI Coding agent, Deep Research agent, and Code Evaluator
- Multi-agent orchestrator with observability and monitoring

Use the DTCLOVESYOU promo code for a special 15% off discount for DataTalks.Club members.

[Enroll here](https://...)

_Sponsored content_
```

## Zoomcamp Slot

One slot per running cohort. Pick the variant from `sources.md`.

### Module week

- Heading: `[Course name] [Year]: Module [N]`, for example `Machine Learning Zoomcamp 2026: Module 2`.
- Body, at most 80 words:
  1. Why the module matters, in one or two positive sentences. Condense the module's Telegram announcement listed in `sources.md` rather than writing from scratch.
  2. Optionally, what the module covers, as one sentence or up to four bullets.
  3. The deadline, exactly: `The deadline for Homework [N] is [deadline from sources.md].`
  4. Optionally: `Next week, Module [N+1] covers [topic].`
- Button: `Join Module [N]`, linking to the "Module materials" URL in `sources.md` (the module folder in the course repository).

Example, from #295:

```markdown
## AI Dev Tools Zoomcamp 2026: Module 4

Once you deploy your application, you need to know what it is doing. In Module 4, we cover DevOps and observability.

These approaches help you see where the app failed, investigate with the right context, and decide how to respond.

The deadline for Homework 4 is September 29, 2026 at 01:00 CEST (September 28 at 23:00 UTC).

[Join Module 4](https://...)
```

When a homework draft is not final, add: "Homework [N] is currently a draft and the questions will likely change."

### Project or peer-review week

- Heading: `[Course name] [Year]: [Project name]`, for example `LLM Zoomcamp 2026: Final Project`.
- Body: one or two sentences on what learners do now (submit, or review peers) and the deadline from `sources.md`.
- Button: `Submit your project`, linking to the project page, or `Review your peers`, linking to the learner review page (`.../project/<slug>/eval`) from `sources.md`.

Example, from #294, with the review link corrected (the sent issue linked a `/cadmin/` admin page):

```markdown
## LLM Zoomcamp 2026: Final Project

If you've already handed in your project, it's time to review your peers' projects. Reviews are due September 17, 2026 at 11:00 CEST (September 17 at 09:00 UTC).

[Review your peers](https://courses.datatalks.club/llm-zoomcamp-2026/project/project3/eval)
```

## Course Registration Slot

For a course open for registration before its cohort starts. It usually runs for several weeks, so vary the angle from week to week instead of repeating the same text.

- Heading: `[Course name] [Year] Cohort`.
- Body, at most 90 words: the start date, one sentence on what the course is and who it is for, three to four bullets on what learners will do, and one line on how the live cohort works.
- Button: `Register for the free [Year] cohort`, linking to the registration page.

Start from the course's newsletter block in `courses/<course>/copy-bank/email/` when there is one, or fill `courses/content-templates/email/newsletter-course-announcement-block.md` from `course.yaml`.

Example, from #291:

```markdown
## AI Dev Tools Zoomcamp 2026 Cohort

The new live cohort of AI Dev Tools Zoomcamp starts on August 31.

This free, hands-on course teaches you how to use AI coding tools in a structured software engineering workflow. You'll learn how to:

- Turn specifications into working, tested code
- Build and deploy a full-stack application with AI assistance
- Extend coding agents with MCP, skills, plugins, and custom agents
- Use open-source tools for code review, security, audit, and DevOps

Lectures are pre-recorded. The live cohort includes deadlines, graded homework, a leaderboard, peer review, community support, and eligibility for a certificate.

[Register for the free 2026 cohort](https://courses.datatalks.club/register/ai-dev-tools/)
```

### Launch week

Feature the launch stream as an event detail slot (below). Do not add a separate module slot until the first module slot the following week, unless the user asks.

## Event Detail Slot

- Heading: `Live workshop: [Title]`, `Webinar: [Title]`, or the event title alone when the type is obvious.
- Body, at most 110 words:
  1. The problem the event addresses, in one or two sentences.
  2. `On [Month D], [speaker] will [what happens].` Then up to five bullets on what participants will see or build, when the source lists them.
  3. For launch streams and Q&As, one line on what to bring, such as questions about prerequisites or time commitment.
- Button: `Register here`, or a specific label such as `Register for the launch stream`.

Put the date in the body; the exact time lives in the Upcoming events list.

### Course event series

When a course runs several pre-course events, group them in one slot instead of one detail slot each.

- Heading: `[Course name] Live Events`.
- Body: one sentence on what the series is for, then a numbered list with one event per line: `[Month D, H:MM PM CEST: Event title](Luma link)`.
- No button.

### Workshop notes

When an article based on a workshop is published, for example on Alexey on Data.

- Heading: `Workshop notes: [Workshop title]`.
- Body, at most 80 words: which workshop the notes come from, what was built or shown (up to three bullets), and one sentence on where the reader ends up.
- Button: `Read the notes`.

## Upcoming Events

- Heading: `Upcoming events`.
- One line per upcoming event from `sources.md`, in date order, including events on the send date:

```markdown
- [September 15, 4:30 PM CEST | Workshop: Building AI Agent Workflows with Switch](https://luma.com/...)
```

- Use the time and zone label from `sources.md`. Add `with [Speaker name]` only when the name is supplied, and then add it for every event in the list that has one.
- No body text and no button.

## Book of the Week

- Heading: `Book of the Week`.
- Body, at most 70 words:
  1. `From [Month D–D], [author] joins us to discuss [book title].` Take the dates, author, and title from `sources.md`.
  2. One sentence on what the book covers, from the book's description in the website repository.
  3. The participation rules, which are the same for every book: `To take part, join our Slack and ask your questions in #book-of-the-week. [Author first name] will answer questions Monday through Thursday and choose the winners of free book copies on Friday.`
- Button: `Participate here`, linking to the book's page on datatalks.club (the "Participate link" in `sources.md`). That page describes the book and explains how to join Slack.

## From Alexey On Data

- Heading: `From Alexey on Data: [post title, shortened if long]`.
- Body, about three short paragraphs, no bullets:
  1. A question that states the reader's problem the post answers.
  2. `In his new newsletter, Alexey [looks at / tries / compares]...` with one or two sentences of concrete content from the post.
  3. One sentence on why the post is useful to the reader.
- Button: `Read here`, linking to the post URL from `sources.md`.

Read the post itself, not only the feed summary, before writing paragraph 2. Use the product and company names as the post spells them, and flag it if the post spells a name two ways.

Example, from #294:

```markdown
## From Alexey on Data: Free and Affordable AI-Native Development

Where can you use coding agents without spending much?

In his new newsletter, Alexey looks at free models, lower-cost coding plans, and pay-as-you-go APIs, including options from OpenCode and OpenRouter. He also explains trade-offs such as data use on some free models and strict API rate limits.

Prices and quotas change quickly, but the article gives you a useful starting point for choosing what to try.

[Read here](https://aishippingblog.com/p/free-and-affordable-ai-native-development)
```

## Latest Recording

- Heading: `[Podcast / Workshop / Webinar] recording: [Title]`.
- Body, at most 60 words: who spoke, what the session covers, and one concrete thing viewers will take away. Base it on the YouTube description, the transcript, or the event page in `events-archive/`. If only the title is available, write one sentence and tell the user.
- Button: `Watch the recording`.
