# Course Platform Setup

This process creates the cohort on the course management platform: the course record, the registration campaign that produces the registration link, and the course outline of homework and project deadlines.

Run it early. Almost every other launch task needs the registration link, the start date, and the deadline schedule, so the campaign calendar, website banner, GitHub README, and welcome email all block on this.

Platform: `https://courses.datatalks.club` (dev instance: `https://dev.courses.datatalks.club`).
Authentication: `AUTH_TOKEN` environment variable, used as `Authorization: Token ${AUTH_TOKEN}`.
The generated OpenAPI spec at `/api/openapi.json` is the source of truth for routes and request bodies.

Automation note: the `course-management-agent` workspace has skills (`course-content`, `homework-questions`, `deploy-prod`) that drive these endpoints. Use them instead of hand-writing requests when they are available.

## 1. Decide the Schedule

Before touching the platform, fix these four values:

- Start date. Zoomcamps start on a Monday.
- Deadline weekday. Keep one weekday for every homework and project deadline so learners only remember one rule.
- Deadline time. Reuse the previous cohort's time-of-day so the leaderboard and scoring scripts behave the same way.
- Project blocks. Where the midterm and capstone slots sit between modules, and how many weeks each block gets.

Copy the previous cohort's outline as the starting point and shift it, rather than designing a new schedule. Pull it with:

```bash
curl -s "https://courses.datatalks.club/api/courses/<previous_course_slug>/" \
  -H "Authorization: Token ${AUTH_TOKEN}"
```

Then adjust: change the year, snap every deadline to the chosen weekday, and check the holiday weeks. December and early January gaps usually need widening.

Record the final schedule in the campaign's `00-cohort-brief.md` before creating anything.

## 2. Create the Course

Course slugs use `<course_short>-zoomcamp-<year>`, for example `ml-zoomcamp-2026`. Some courses drop the `zoomcamp` part; match whatever the previous cohort used.

```bash
curl -s -X POST "https://courses.datatalks.club/api/courses/" \
  -H "Authorization: Token ${AUTH_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "slug": "<course_slug>",
    "title": "<Course Title> <Year>",
    "description": "<one-paragraph course description>",
    "start_date": "<YYYY-MM-DD>",
    "end_date": "<YYYY-MM-DD>",
    "registration_url": "https://courses.datatalks.club/register/<campaign_slug>/",
    "github_repo_url": "<course repo URL>",
    "social_media_hashtag": "<#hashtag>",
    "faq_document_url": "<FAQ URL>",
    "min_projects_to_pass": 1,
    "project_passing_score": 7,
    "finished": false,
    "visible": true
  }'
```

Copy `social_media_hashtag`, `faq_document_url`, `min_projects_to_pass`, and `project_passing_score` from the previous cohort unless the certificate rules changed this year. Set `end_date` to the last peer review deadline.

Keep `visible: true` so the course appears in the course list, and `finished: false` so it is treated as an active cohort.

## 3. Create the Registration Campaign

The registration campaign owns the public registration page at `https://courses.datatalks.club/register/<campaign_slug>/`. The campaign slug has no year in it: it stays stable across cohorts, and `current_course` is repointed each year.

```bash
curl -s -X POST "https://courses.datatalks.club/api/registration-campaigns/" \
  -H "Authorization: Token ${AUTH_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "slug": "<campaign_slug>",
    "title": "<Course Title>",
    "edition_label": "<Year> cohort",
    "current_course": "<course_slug>",
    "is_active": true,
    "marketing_markdown": "<short markdown blurb shown on the registration page>",
    "meta_description": "<one-line description for search and social previews>",
    "hero_image_url": "<course cover image URL>",
    "video_url": "<launch or trailer video URL, optional>"
  }'
```

If the campaign already exists from a previous cohort, do not create a second one. Repoint it instead:

```bash
curl -s -X PATCH "https://courses.datatalks.club/api/registration-campaigns/<campaign_slug>/" \
  -H "Authorization: Token ${AUTH_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"current_course": "<course_slug>", "edition_label": "<Year> cohort", "is_active": true}'
```

Check the existing campaigns first:

```bash
curl -s "https://courses.datatalks.club/api/registration-campaigns/" \
  -H "Authorization: Token ${AUTH_TOKEN}"
```

`marketing_markdown` and `meta_description` are learner-facing copy. Draft them from the copy bank rather than leaving a placeholder in place. Verify `hero_image_url` returns HTTP 200 before announcing the page.

## 4. Create the Course Outline

The outline is the set of homeworks and projects with their deadlines. Create it in one bulk request per type.

Homeworks:

```bash
curl -s -X POST "https://courses.datatalks.club/api/courses/<course_slug>/homeworks/" \
  -H "Authorization: Token ${AUTH_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Homework 1: <Module 1 title>", "slug": "hw01", "due_date": "<ISO 8601>"},
    {"name": "Homework 2: <Module 2 title>", "slug": "hw02", "due_date": "<ISO 8601>"}
  ]'
```

Projects:

```bash
curl -s -X POST "https://courses.datatalks.club/api/courses/<course_slug>/projects/" \
  -H "Authorization: Token ${AUTH_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Midterm Project", "slug": "midterm",
     "submission_due_date": "<ISO 8601>", "peer_review_due_date": "<ISO 8601>"}
  ]'
```

Rules for the outline:

- Create homeworks closed and empty. They are created with `state: CL` by default. Do not add questions at outline time; questions come from the module's `homework.md` once the module is ready, and adding them early risks publishing an unfinished homework.
- Keep the previous cohort's slugs. Learners, scripts, and old links depend on them, and gaps such as a missing `hw07` are usually intentional because that slot is a project.
- Keep the previous cohort's deadline time-of-day.
- Every project needs both a submission deadline and a peer review deadline.

Open each homework with `PATCH {"state": "OP"}` when its module goes live, not during setup.

## 5. Verify

Fetch the course detail and read the full outline back:

```bash
curl -s "https://courses.datatalks.club/api/courses/<course_slug>/" \
  -H "Authorization: Token ${AUTH_TOKEN}"
```

Confirm:

- Every deadline falls on the intended weekday.
- Every homework is `CL` with zero questions.
- Every project has both deadlines.
- No holiday week swallows a deadline.
- `registration_url` on the course matches the campaign page, and that page returns HTTP 200.

## 6. Record the Outline

Write the confirmed schedule into the campaign folder:

- Put the deadline table in `campaigns/<course>-<year>/processes/00-cohort-brief.md`.
- Put the course platform URL and registration URL into `campaigns/<course>-<year>/course.yaml`.
- Use those deadlines when filling `02-campaign-calendar.csv`, so module announcements and deadline reminders line up with the real dates.

## Checklist

- [ ] Previous cohort outline pulled and reviewed
- [ ] Start date, deadline weekday, and deadline time confirmed
- [ ] Course created with correct slug, dates, and certificate settings
- [ ] Registration campaign created or repointed to the new course
- [ ] Registration page returns HTTP 200 and shows the right cohort
- [ ] Homeworks created, closed, and empty
- [ ] Projects created with both deadlines
- [ ] Outline verified against the intended weekday and holiday weeks
- [ ] Schedule recorded in the cohort brief and campaign `course.yaml`
