## Current setup: what it covers

| Area            | Current files                | What they help with                                                 |
| --------------- | ---------------------------- | ------------------------------------------------------------------- |
| Course identity | `course.yaml`                | Keeps course name, dates, links, modules, and metadata consistent.  |
| Audience        | `audience.md`                | Defines who we are speaking to and what they need.                  |
| Positioning     | `positioning.md`             | Defines the main course message and value proposition.              |
| Curriculum      | `curriculum-and-outcomes.md` | Explains what learners will study, build, and achieve.              |
| Objections      | `faq-and-objections.md`      | Helps answer doubts and conversion blockers.                        |
| Copy reuse      | `copy-bank/`                 | Stores reusable copy for announcements, posts, emails, CTAs.        |
| Visuals         | `course-assets/`             | Stores images, banners, screenshots, thumbnails, diagrams.          |
| Proof           | `proof-library/`             | Stores credibility: testimonials, past projects, numbers, examples. |

# What your setup is missing

## 1. Launch plan

You need one document that explains the full campaign structure.

Suggested file:

```text
launch-plan.md
```

It should define the main phases:

1. Foundation
2. Announcement
3. Education and trust-building
4. Registration push
5. Onboarding and activation
6. Launch week
7. In-course momentum
8. Post-course proof and evergreen promotion

For each phase, define:

* purpose
* start and end dates
* main message
* channels used
* main deliverables
* success metric

This file connects the strategy to the actual launch.

Without it, you have good content pieces, but no clear campaign flow.

## 2. Goals and metrics

You need a separate place for launch goals.

Suggested file:

```text
goals-and-metrics.md
```

It should include:

| Goal type         | Example                                                          |
| ----------------- | ---------------------------------------------------------------- |
| Registration goal | Number of sign-ups before course start                           |
| Activation goal   | Number or percentage of registrants joining Slack                |
| Attendance goal   | Launch session attendance                                        |
| Engagement goal   | Module 1 homework starts or submissions                          |
| Retention goal    | Module-to-module participation                                   |
| Channel goal      | Registrations by newsletter, LinkedIn, Slack, Telegram, partners |
| Content goal      | Which posts/emails drive meaningful clicks and registrations     |

For a free course, I would avoid treating registrations as the only success metric.

Better core metrics:

```text
registrations → Slack joins → launch attendance → Module 1 homework submissions
```

That gives you a more realistic picture of whether promotion brought actual learners.

## 3. Channel plan

You need a doc that defines what each channel is responsible for.

Suggested file:

```text
channel-plan.md
```

It should not just list channels. It should define their role.

Example:

| Channel                  | Role in launch                     | Main CTA                                     | Content type                                        |
| ------------------------ | ---------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| DataTalksClub newsletter | Conversion from existing audience  | Register                                     | Main announcements, reminders, module updates       |
| Alexey newsletter        | Personal/instructor trust          | Register                                     | Founder-style explanations, why this course exists  |
| LinkedIn                 | Awareness and credibility          | Register                                     | Problem posts, curriculum posts, course value posts |
| X/Twitter                | Fast awareness and repetition      | Register                                     | Short announcements, threads, reminders             |
| Slack                    | Community activation               | Join course channel, attend, submit homework | Operational posts, reminders, discussion prompts    |
| Telegram                 | Broadcast reminders                | Register, attend, submit                     | Short reminders                                     |
| YouTube                  | Live learning and replay discovery | Watch, join, continue                        | Launch stream, module sessions, recaps              |
| Website                  | Conversion                         | Register                                     | Course page, FAQ, schedule                          |
| Partner channels         | Audience expansion                 | Register                                     | Partner blurbs and event mentions                   |

This file prevents the problem where every channel repeats the same message without a clear job.

## 4. Launch calendar

You need a schedule of what gets published when.

Suggested file:

```text
launch-calendar.md
```

Or, if you want it more operational:

```text
campaign-calendar.csv
```

It should include:

| Date      | Phase        | Channel              | Asset                   | Status  | Owner    | Link |
| --------- | ------------ | -------------------- | ----------------------- | ------- | -------- | ---- |
| T-7 weeks | Announcement | Newsletter           | Main launch email       | Drafted | Valeriia |      |
| T-6 weeks | Education    | LinkedIn             | Why this course exists  | Planned | Alexey   |      |
| T-4 weeks | Event promo  | Slack                | Workshop 1 announcement | Ready   | Valeriia |      |
| T-1 week  | Final push   | Email                | Starts next week        | Drafted | Valeriia |      |
| T-0       | Launch       | Slack/Telegram/Email | We start today          | Planned | Valeriia |      |

This is one of the most important missing pieces.

Your current repo can explain the course, but the calendar makes the launch happen.

## 5. Tracking and UTM plan

You need a place for source tracking.

Suggested file:

```text
tracking.md
```

It should define:

* UTM naming rules
* campaign name
* source names
* medium names
* links for each channel
* where registration source is checked
* which metrics are reviewed weekly

Example:

```text
utm_campaign=ai_dev_tools_zoomcamp_2026
utm_source=newsletter
utm_medium=email

utm_source=linkedin
utm_medium=social

utm_source=slack
utm_medium=community

utm_source=telegram
utm_medium=broadcast
```

This matters because otherwise you get sign-ups, but you cannot tell what caused them.

For a course launch, tracking should answer:

* Which channels brought registrations?
* Which channels brought active learners?
* Which workshop converted best?
* Which email drove Slack joins?
* Which reminder increased attendance?

## 6. Landing page copy and page checklist

You may already have course content, but I would keep landing page copy as a separate deliverable.

Suggested file:

```text
landing-page.md
```

It should include final approved copy for:

* hero section
* short course description
* who it is for
* what learners will build
* curriculum
* live cohort benefits
* prerequisites
* schedule
* certificate explanation
* FAQ
* CTA blocks

The landing page is the main conversion asset. It should not be assembled ad hoc from `positioning.md`, `audience.md`, and `curriculum-and-outcomes.md`.

Those are inputs. `landing-page.md` is the final output.

## 7. Registration and onboarding flow

This is probably the most important missing area.

Suggested files:

```text
registration-flow.md
onboarding.md
```

These should define what happens after someone registers.

For example:

```text
Landing page → Registration form → Confirmation page → Welcome email → Slack → Course channel → Calendar/live session → Module 1
```

For a free course, this is critical because many people register and disappear.

The onboarding doc should include:

* confirmation page copy
* welcome email
* Slack instructions
* course channel instructions
* calendar/live session links
* “how the cohort works”
* homework/certificate rules
* first-week checklist

The campaign should not stop at registration. It should move people into participation.

## 8. Email sequence

You need a separate email plan, not just individual newsletter copy.

Suggested file or folder:

```text
emails/
  01-announcement.md
  02-why-join-live.md
  03-workshop-reminder.md
  04-starts-next-week.md
  05-welcome.md
  06-starts-tomorrow.md
  07-launch-day.md
  08-module-1-follow-up.md
```

Or:

```text
email-sequence.md
```

The email sequence should cover two groups:

### Public promotion emails

These go to the general audience.

Purpose:

* announce course
* explain value
* promote workshops
* remind about start date
* drive registration

### Registrant onboarding emails

These go to people who already registered.

Purpose:

* join Slack
* save the date
* attend the launch
* open materials
* start Module 1
* submit homework

These should be treated differently. A person who already registered should not keep getting only “register now” messages.

## 9. Social/content plan

Your `copy-bank/` may contain copy, but you probably need a structured content plan.

Suggested file:

```text
content-plan.md
```

It should define the main angles.

For example:

| Content angle            | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| Course announcement      | Make people aware                         |
| Why this topic matters   | Build motivation                          |
| Common mistakes          | Show practical relevance                  |
| What you will build      | Make outcomes concrete                    |
| Module previews          | Explain curriculum                        |
| Live cohort benefits     | Push registration                         |
| Workshops                | Create learning moments before the course |
| FAQ/objections           | Remove friction                           |
| Launch reminders         | Convert interested people                 |
| Learner/project examples | Build proof                               |

This helps you avoid repeating the same announcement for seven weeks.

## 10. Events and workshop promotion plan

Since this course has pre-course events, I would separate them clearly.

Suggested file:

```text
events-plan.md
```

For each event:

* title
* date
* target audience
* connection to the course
* registration link
* main promise
* newsletter copy
* Slack copy
* LinkedIn copy
* reminder schedule
* post-event follow-up
* CTA to register for the course

The key is that each event should serve the course launch.

For example:

```text
Workshop → useful standalone learning experience → course CTA → follow-up email → course registration
```

Without this, events become separate promotions instead of a launch engine.

## 11. Partner or sponsor kit

For sponsored or collaborative events, you need a simple sharing kit.

Suggested file:

```text
partner-kit.md
```

It should include:

* short course description
* short event description
* speaker names
* approved sponsor/collaboration wording
* social post options
* newsletter blurb
* banner image
* registration links
* tracking links
* do/don’t messaging

This makes it easier for partners, speakers, and sponsors to promote the course without rewriting everything.

## 12. Community activation plan

For DataTalksClub courses, Slack is not just another channel. It is part of the course experience.

Suggested file:

```text
community-plan.md
```

It should define:

* which Slack channel to use
* when to open it
* pinned welcome message
* first discussion prompt
* how learners ask questions
* office hours or Q&A rhythm
* homework reminders
* peer review reminders
* moderation plan
* weekly Slack posts

This is important because community activity helps convert passive registrants into active learners.

## 13. Reporting dashboard

You need a way to review performance during launch.

Suggested file:

```text
reporting.md
```

Or a dashboard linked from:

```text
metrics.md
```

It should define:

* where registration numbers come from
* where traffic numbers come from
* where email metrics come from
* where Slack joins are tracked
* where YouTube attendance is tracked
* who checks metrics
* how often you review them
* what decisions metrics should trigger

Example:

| Signal                               | Possible action                             |
| ------------------------------------ | ------------------------------------------- |
| High page visits, low registrations  | Improve landing page copy or CTA            |
| High registrations, low Slack joins  | Improve welcome email and confirmation page |
| Good email opens, low clicks         | Improve CTA and email structure             |
| Good sign-ups, low launch attendance | Add reminders and calendar flow             |
| Good attendance, low homework        | Improve Module 1 instructions               |

## 14. Owner and status system

You need a simple operational layer.

Suggested file:

```text
ops.md
```

Or use GitHub issues/projects.

It should track:

* owner
* status
* deadline
* dependencies
* approval needed
* final link
* published link

Example statuses:

```text
idea → draft → reviewed → approved → scheduled → published → measured
```

This prevents launch work from staying in “almost ready” mode.

## 15. Retrospective and reusable learnings

Every course launch should improve the next one.

Suggested file:

```text
retrospective.md
```

It should capture:

* what worked
* what did not work
* best-performing channels
* best-performing messages
* registration curve
* activation rate
* learner drop-off
* assets worth reusing
* changes for the next course

This is especially useful for DataTalksClub because courses repeat annually.

# The complete repo could look like this

A more complete setup could be:

```text
ai-dev-tools-zoomcamp/
  course.yaml

  01-foundation/
    audience.md
    positioning.md
    curriculum-and-outcomes.md
    faq-and-objections.md
    proof-library.md

  02-strategy/
    launch-plan.md
    goals-and-metrics.md
    channel-plan.md
    messaging-framework.md

  03-campaign/
    launch-calendar.md
    content-plan.md
    events-plan.md
    partner-kit.md
    tracking.md

  04-copy/
    landing-page.md
    announcement-pack.md
    email-sequence.md
    slack-posts.md
    telegram-posts.md
    linkedin-posts.md
    x-posts.md
    youtube-descriptions.md

  05-onboarding/
    registration-flow.md
    welcome-email.md
    community-plan.md
    launch-week-checklist.md
    module-update-template.md

  06-assets/
    course-assets/
    social-banners/
    thumbnails/
    speaker-photos/
    screenshots/

  07-reporting/
    dashboard-links.md
    weekly-report-template.md
    retrospective.md
```

You do not need to reorganize everything exactly like this. But conceptually, these are the missing layers.

# The main gap

Your current setup likely answers:

> What are we promoting?

But a full course launch setup should also answer:

> How are we promoting it?
> When are we promoting it?
> Where are we promoting it?
> Who is responsible?
> What happens after registration?
> How do we know whether it worked?

So the biggest missing pieces are:

1. **Launch plan**
2. **Goals and metrics**
3. **Channel plan**
4. **Launch calendar**
5. **Tracking/UTM plan**
6. **Email and onboarding sequence**
7. **Community activation plan**
8. **Events/workshop promotion plan**
9. **Reporting and retrospective**

The current setup is good for messaging. To make it campaign-ready, you need the operational layer around it.
