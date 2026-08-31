# Social Post Taxonomy Analysis

Source taxonomy: `research/typefully/post-type-taxonomy.json`

Referenced export: `research/typefully/typefully-examples.json`

The taxonomy analyzes 216 Typefully posts that mention `zoomcamp` or `free course`. It defines 15 reusable primary post types. It does not store a full per-record classification for all 216 posts, so the "unique social media posts" below are the 42 unique example post IDs listed in the taxonomy.

Note: 4 taxonomy example IDs are not present in the current normalized export: `6825728`, `6918323`, `6919241`, `7314383`.

## Unique Post Types

| ID | Type | Phase | Purpose | Example posts |
|---|---|---|---|---|
| `course_launch` | Course Launch Announcement | pre_launch, launch | Open or promote a cohort with date, promise, outcomes, and registration CTA. | `8960565`, `6918323`, `5695158` |
| `interest_validation` | Interest Validation / Coming Soon | interest_validation, pre_launch | Test demand, announce that a course will happen, or collect early signups. | `5695158`, `6814599`, `7147871` |
| `course_positioning_faq` | Course Positioning / FAQ Answer | pre_launch, launch, evergreen | Answer learner objections about fit, prerequisites, practicality, and logistics. | `7147871`, `7228631`, `7482218` |
| `module_announcement` | Module / Week Announcement | active_cohort | Tell learners what starts this week and what they will build or study. | `9549329`, `8111970`, `8048693` |
| `educational_micro_lesson` | Educational Micro-Lesson | pre_launch, active_cohort, evergreen | Teach one course-relevant concept and softly connect it to course materials. | `9333232`, `9164504`, `9341648`, `9333135` |
| `opinion_principle` | Opinion / Principle | pre_launch, active_cohort, evergreen | State a course philosophy or counterintuitive technical stance. | `9333232`, `9176590`, `8802566` |
| `live_event_workshop` | Live Event / Workshop | pre_launch, launch, active_cohort | Promote a live session, Q&A, office hour, or workshop connected to the course. | `9328336`, `9174752`, `9047907` |
| `resource_update` | Resource / Materials Update | pre_launch, active_cohort, evergreen | Announce or explain a repo, README, article, list, recording, or docs update. | `9709998`, `6814872`, `7482218` |
| `social_proof` | Social Proof / Testimonial | pre_launch, launch, wrap_up, evergreen | Use learner stories, rankings, metrics, or reviews to prove value. | `8802681`, `8518298`, `8986489`, `7314383` |
| `project_challenge` | Project / Challenge / Competition | project_phase, active_cohort | Ask learners to build, submit, compete, share, or complete a project. | `8388879`, `8115013`, `7229150` |
| `partner_sponsor_instructor` | Partner / Sponsor / Instructor Call | pre_launch, active_cohort, wrap_up | Feature a sponsor, partner workshop, guest instructor, or contributor need. | `9159711`, `8388879`, `6825728` |
| `milestone_results` | Milestone / Wrap-Up / Results | active_cohort, wrap_up | Mark cohort progress, completion, certificates, competition results, stars, or growth. | `9159705`, `8913769`, `7482340` |
| `career_audience_framing` | Career / Audience Framing | pre_launch, launch, evergreen | Connect the course to learner backgrounds, role transitions, or job-market context. | `7650176`, `7800561`, `6951674` |
| `community_learning_public` | Community / Learning In Public | active_cohort, project_phase, evergreen | Encourage sharing, asking questions, peer review, Slack participation, or public progress. | `8519005`, `7800221`, `6919241` |
| `companion_offer_support_layer` | Companion Offer / Support Layer | pre_launch, launch, active_cohort | Explain optional paid or high-touch support while preserving the free course promise. | `9531386`, `9482899`, `9435750` |

## Unique Example Posts And Types

| Post ID | Type(s) |
|---|---|
| `5695158` | `course_launch`, `interest_validation` |
| `6814599` | `interest_validation` |
| `6814872` | `resource_update` |
| `6825728` | `partner_sponsor_instructor` |
| `6918323` | `course_launch` |
| `6919241` | `community_learning_public` |
| `6951674` | `career_audience_framing` |
| `7147871` | `interest_validation`, `course_positioning_faq` |
| `7228631` | `course_positioning_faq` |
| `7229150` | `project_challenge` |
| `7314383` | `social_proof` |
| `7482218` | `course_positioning_faq`, `resource_update` |
| `7482340` | `milestone_results` |
| `7650176` | `career_audience_framing` |
| `7800221` | `community_learning_public` |
| `7800561` | `career_audience_framing` |
| `8048693` | `module_announcement` |
| `8111970` | `module_announcement` |
| `8115013` | `project_challenge` |
| `8388879` | `project_challenge`, `partner_sponsor_instructor` |
| `8518298` | `social_proof` |
| `8519005` | `community_learning_public` |
| `8802566` | `opinion_principle` |
| `8802681` | `social_proof` |
| `8913769` | `milestone_results` |
| `8960565` | `course_launch` |
| `8986489` | `social_proof` |
| `9047907` | `live_event_workshop` |
| `9159705` | `milestone_results` |
| `9159711` | `partner_sponsor_instructor` |
| `9164504` | `educational_micro_lesson` |
| `9174752` | `live_event_workshop` |
| `9176590` | `opinion_principle` |
| `9328336` | `live_event_workshop` |
| `9333135` | `educational_micro_lesson` |
| `9333232` | `educational_micro_lesson`, `opinion_principle` |
| `9341648` | `educational_micro_lesson` |
| `9435750` | `companion_offer_support_layer` |
| `9482899` | `companion_offer_support_layer` |
| `9531386` | `companion_offer_support_layer` |
| `9549329` | `module_announcement` |
| `9709998` | `resource_update` |

## Campaign Calendar For Any Zoomcamp

Use the course start date from the cohort brief or `course.yaml`. If the course has no scheduled live cohort, use the evergreen/self-paced variant and remove deadline urgency.

### 8 Weeks Before

- [ ] `interest_validation`: "A new cohort is coming" or waitlist/interest post.
- [ ] `educational_micro_lesson`: one practical concept from the first module.
- [ ] `career_audience_framing`: who the course is for, who it is not for, and what skill gap it solves.
- [ ] `resource_update`: course repo/docs/FAQ refreshed for the cohort.
- [ ] `live_event_workshop`: workshop announcement, if applicable.
- [ ] `partner_sponsor_instructor`: instructor/guest/sponsor call, if needed.

### 6 Weeks Before

- [ ] `live_event_workshop`: workshop reminder.
- [ ] `resource_update`: workshop recording or materials post.
- [ ] `educational_micro_lesson`: concept from a core module.
- [ ] `course_positioning_faq`: prerequisites, time commitment, certificate rules, self-paced vs cohort.
- [ ] `social_proof`: previous learner story, ranking, GitHub stars, project, or completion metric.

### 4 Weeks Before

- [ ] `course_launch`: main registration announcement.
- [ ] `course_positioning_faq`: "Is this course for me?" post.
- [ ] `resource_update`: curriculum, README, FAQ, or course article post.
- [ ] `career_audience_framing`: role-transition or job-market angle without promising jobs.
- [ ] `community_learning_public`: invite learners to Slack/Telegram and learning-in-public.
- [ ] Newsletter, Slack, DTC social, Alexey social, and website/GitHub updates.

### 2 Weeks Before

- [ ] `live_event_workshop`: pre-course Q&A announcement.
- [ ] `social_proof`: alumni/project proof post.
- [ ] `course_positioning_faq`: cohort vs self-paced post.
- [ ] `course_positioning_faq`: logistics post covering homework, leaderboard, peer review, certificates.
- [ ] `educational_micro_lesson`: "first thing you will learn/build" post.
- [ ] Newsletter reminder.

### Final Week

- [ ] `course_launch`: final reminder with exact start date.
- [ ] `live_event_workshop`: launch stream reminder.
- [ ] `resource_update`: environment setup / before-you-start checklist.
- [ ] `course_positioning_faq`: last FAQ post for blockers.
- [ ] `community_learning_public`: join Slack/Telegram and ask questions in the right channel.
- [ ] Final DTC social, Alexey social, newsletter, and Slack reminder.

### Start Week

- [ ] `course_launch`: starts today post.
- [ ] `live_event_workshop`: launch stream live/today post.
- [ ] `module_announcement`: Module 1 / Week 1 announcement.
- [ ] `resource_update`: links to materials, homework, docs, FAQ, and community.
- [ ] `community_learning_public`: introduce-yourself / share-progress prompt.
- [ ] `course_positioning_faq`: first-week troubleshooting and how to ask questions.

### Active Cohort

- [ ] `module_announcement`: weekly module posts.
- [ ] `educational_micro_lesson`: one compact lesson per module.
- [ ] `opinion_principle`: one philosophy/mental-model post per major theme.
- [ ] `live_event_workshop`: office hours, workshops, Q&A, recordings.
- [ ] `resource_update`: repo/docs/recordings/homework updates.
- [ ] `community_learning_public`: ask questions, share notes, publish homework learnings.

### Project Phase

- [ ] `project_challenge`: project announcement with task, rubric, deadline, and examples.
- [ ] `community_learning_public`: share project ideas and progress.
- [ ] `social_proof`: previous project examples or alumni projects.
- [ ] `partner_sponsor_instructor`: sponsor/tool challenge, if applicable.
- [ ] `project_challenge`: deadline reminder and extension post, if applicable.
- [ ] `course_positioning_faq`: peer review/certificate logistics.

### Wrap-Up

- [ ] `milestone_results`: completion/certificate/project numbers.
- [ ] `social_proof`: testimonial or learner transformation.
- [ ] `project_challenge`: winning projects or project gallery.
- [ ] `partner_sponsor_instructor`: sponsor/partner thanks.
- [ ] `community_learning_public`: encourage graduates to share certificates/projects.
- [ ] `interest_validation`: next-cohort waitlist or coming-soon teaser.

## Course-Specific Suggestions

### AI Dev Tools Zoomcamp

Current metadata says the 2026 cohort starts on August 31, 2026, so the immediate campaign should use the 8-week and 6-week buckets.

- Prioritize posts about AI coding assistants, agents, MCP, testing, CI/CD, pull request review, and automation.
- Strong FAQ angles: "Do I need prior AI tools experience?", "Is this about building LLM apps?", "Do I need web/Django experience?", "Which tools do we use?"
- Strong proof assets: first cohort stats, student projects, testimonials.
- Good micro-lessons: responsible AI-generated code review, agent vs assistant, MCP in plain language, tests as guardrails for AI coding.

### LLM Zoomcamp

Current metadata says the 2026 cohort started on June 8, 2026 and was in progress as of July 6, 2026.

- Prioritize active-cohort posts: module announcements, RAG/evaluation/vector-search micro-lessons, office hours, resource updates, and project preparation.
- Strong FAQ angles: API keys/costs, Docker setup, no ML background required, not training LLMs from scratch, certificate/project rules.
- Strong proof assets: previous projects from 2024/2025, project example repo, community posts, course GitHub activity.
- Use companion-offer posts only when AI Shipping Labs is relevant, and preserve the "LLM Zoomcamp is free" message.

### Data Engineering Zoomcamp

Current metadata says the next live cohort starts in January 2027, with exact date not yet in the local metadata.

- Prioritize long-runway posts: waitlist/registration, social proof, career framing, refreshed FAQ, and workshop announcements.
- Strong FAQ angles: Python/SQL/Git prerequisites, GCP/Docker setup, time commitment, certificate and project rules.
- Strong proof assets: GitHub stars, previous cohort stats, testimonials, project gallery.
- Good micro-lessons: batch vs streaming, orchestration vs scheduling, data lake vs warehouse, analytics engineering inside DE.

### Machine Learning Zoomcamp

Current metadata says the next live cohort starts in September 2026, with exact date not yet in the local metadata.

- Prioritize pre-launch posts now: role framing, proof, course positioning, and practical ML engineering lessons.
- Strong FAQ angles: prior ML not required, programming expectations, math level, Docker/cloud basics, self-paced vs cohort.
- Strong proof assets: ranking/reviews, graduate stories, project gallery, previous cohort stats.
- Good micro-lessons: evaluation metrics, leakage, deployment basics, model serving, trees vs linear models.

### MLOps Zoomcamp

Current metadata says no live cohort is planned in 2026; treat it as self-paced/waitlist unless this changes.

- Avoid "starts soon" urgency unless a cohort date is confirmed.
- Prioritize evergreen posts: self-paced availability, portfolio project, MLOps concepts, resource updates, and waitlist/get-updates CTA.
- Strong FAQ angles: not a beginner ML course, expected ML/Python/Docker basics, certificate unavailable without live cohort, project for self-assessment.
- Good micro-lessons: experiment tracking, model registry, batch vs online inference, monitoring, testing ML pipelines.

## Minimum Useful Campaign

If there is not enough time for the full calendar, make at least these 10 posts:

1. `course_launch`: main registration announcement.
2. `course_positioning_faq`: who it is for and prerequisites.
3. `educational_micro_lesson`: one technical concept.
4. `social_proof`: testimonial, metric, project, ranking, or stars.
5. `resource_update`: curriculum/repo/docs/FAQ.
6. `live_event_workshop`: pre-course Q&A or launch stream.
7. `career_audience_framing`: role/skill-gap angle.
8. `community_learning_public`: Slack/Telegram and sharing prompt.
9. `module_announcement`: starts today / Module 1.
10. `project_challenge`: project or certificate path.
