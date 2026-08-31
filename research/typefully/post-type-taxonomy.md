# Course Social Post Type Taxonomy

Source: `research/typefully/typefully-examples.json`

Analyzed set: 216 Typefully posts containing `zoomcamp` or `free course`.

Use this taxonomy to generate reusable course-promotion drafts. Each draft should have one primary post type and may add secondary modifiers such as urgency, proof, event, resource, or community.

## Draft Schema

For every generated draft, choose:

- `primary_type`: the main reason this post exists.
- `course_phase`: `interest_validation`, `pre_launch`, `launch`, `active_cohort`, `project_phase`, `wrap_up`, or `evergreen`.
- `audience`: the reader segment, such as beginner, practitioner, career switcher, current learner, alumni, sponsor, or instructor.
- `angle`: the specific promise, objection, lesson, update, or proof point.
- `proof_asset`: testimonial, metric, GitHub stars, student project, ranking, sponsor, competition result, or none.
- `cta`: register, read, watch, join event, submit project, share progress, ask questions, sponsor, or apply.
- `urgency`: none, date-based, deadline, starts-today, last-call, or live-now.

## Primary Post Types

### 1. Course Launch Announcement

Use when a cohort is opening, restarting, or ready for registration.

Common hooks:

- `{Course} starts on {date}.`
- `Our free {Course} starts today.`
- `A new cohort of {Course} starts on {date}.`

Body formula:

1. State the course and date.
2. Define the course in one practical sentence.
3. List 4-7 concrete things learners will build or learn.
4. Mention format, duration, cost, or cohort mechanics only if relevant.
5. End with a direct registration/repo CTA.

Reusable inputs:

- course name, start date, duration, cost, learning outcomes, registration URL.

Examples from export:

- `8960565`: new LLM Zoomcamp cohort starts June 8.
- `6918323`: AI Dev Tools Zoomcamp starts soon.
- `5695158`: AI Dev Tools Zoomcamp is happening after signup threshold.

### 2. Interest Validation / Coming Soon

Use before a course is fully built, when testing demand or announcing that the course will happen.

Common hooks:

- `We're exploring a new free course: {topic}.`
- `We decided to run {Course} if we reach {signup_count} signups.`
- `Great news: {Course} is happening.`

Body formula:

1. State the exploration or threshold.
2. Explain why the course topic matters now.
3. Share what is known and what is still being prepared.
4. Ask readers to register interest or comment with what they want to learn.

Reusable inputs:

- problem, target audience, threshold or signal, planned topics, interest form URL.

Examples from export:

- `5695158`: course confirmed after 2,000 signups.
- `6814599`: audience curiosity after announcement.
- `7147871`: answers “What is the AI Dev Tools Zoomcamp?”

### 3. Course Positioning / FAQ Answer

Use when learners are asking whether the course is for them, whether it is practical, or what prerequisites they need.

Common hooks:

- `People are asking: "What is {Course}?"`
- `You asked us: "Is {Course} practical?"`
- `A common question I receive is: Should I take {Course}?`

Body formula:

1. Start with the exact learner question.
2. Answer plainly.
3. Clarify who the course is for and not for.
4. List prerequisites or outcomes.
5. End with the next step.

Reusable inputs:

- top objections, audience segments, prerequisites, project examples, certificate/logistics details.

Examples from export:

- `7147871`: “What is the AI Dev Tools Zoomcamp?”
- `7228631`: top questions summarized.
- `7482218`: frequent Data Engineering Zoomcamp questions.

### 4. Module / Week Announcement

Use during an active cohort to tell learners what starts this week.

Common hooks:

- `This week in {Course}: {module_topic}.`
- `In {Course}, we begin Module {n}: {module_name}.`
- `Astrologers proclaim the beginning of a new module at {Course}.`

Body formula:

1. Announce the module/week.
2. Explain the module goal in practical terms.
3. List lessons, tools, and deliverables.
4. Remind learners where to ask questions or find materials.
5. Include a course link or module link.

Reusable inputs:

- module number, module title, outcomes, tools, homework/project task, support channel.

Examples from export:

- `9549329`: LLM Zoomcamp week on AI orchestration.
- `8111970`: DE Zoomcamp Module 5.
- `8048693`: DE Zoomcamp Module 4.

### 5. Educational Micro-Lesson

Use to teach one course-relevant concept and softly connect it to the course.

Common hooks:

- `{Concept} is usually more than {oversimplified thing}.`
- `A basic {system} is just {n} steps.`
- `{Metric A} and {Metric B} answer two different questions.`

Body formula:

1. Open with a specific technical claim.
2. Break down the mechanism or misconception.
3. Give a compact mental model, steps, or trade-offs.
4. Connect to workshop/course materials.
5. End with a soft CTA to learn more.

Reusable inputs:

- concept, misconception, 3-5 step explanation, failure modes, course/module link.

Examples from export:

- `9333232`: you do not always need an agent.
- `9164504`: basic RAG in three steps.
- `9341648`: hit rate vs. MRR.
- `9333135`: function calling does not run Python.

### 6. Opinion / Principle

Use for a stronger teaching stance that clarifies how the course approaches a topic.

Common hooks:

- `Hard truth: {counterintuitive claim}.`
- `One principle I strongly believe in: {principle}.`
- `Don't start {project_type} with {default_tool} by default.`

Body formula:

1. State the opinion directly.
2. Explain what people commonly get wrong.
3. Provide a more disciplined approach.
4. Tie it to the course philosophy or workflow.
5. Invite learners to practice it in the course.

Reusable inputs:

- belief, common mistake, alternative method, concrete example, course CTA.

Examples from export:

- `9333232`: hard truth about agents.
- `9176590`: do not start RAG with vector search by default.
- `8802566`: teach concepts, not tools.

### 7. Live Event / Workshop

Use to promote a live session, Q&A, office hour, or workshop connected to the course.

Common hooks:

- `Tomorrow we are doing a live Q&A before {Course} starts.`
- `I'm starting a live workshop in {time}.`
- `Join me for a free hands-on workshop on {topic}.`

Body formula:

1. Lead with date/time or event topic.
2. Explain who should attend.
3. List what will be covered.
4. Add course context if relevant.
5. End with event registration or watch link.

Reusable inputs:

- event title, date/time/timezone, agenda, audience, course connection, registration URL.

Examples from export:

- `9328336`: pre-cohort LLM Zoomcamp Q&A.
- `9174752`: live RAG-to-agent workshop.
- `9047907`: first workshop in LLM Zoomcamp update series.

### 8. Resource / Materials Update

Use when a repo, README, article, list, recording, cheatsheet, or course asset is updated.

Common hooks:

- `I updated the list of {resource} for {Course} students.`
- `The {Course} repo is live.`
- `We've refreshed the {Course} article/README.`

Body formula:

1. State what changed.
2. Explain why it helps learners.
3. Summarize what is inside.
4. Add caveats when information changes over time.
5. Link to the resource.

Reusable inputs:

- resource name, changed sections, audience, reason for update, URL.

Examples from export:

- `9709998`: OpenAI API alternatives list.
- `6814872`: Module 2 project overview.
- `7482218`: refreshed FAQ/article content.

### 9. Social Proof / Testimonial

Use when a learner, review, ranking, metric, or community story proves the course is useful.

Common hooks:

- `Got this message from a {Course} participant.`
- `{Course} ranked #{n} in {review/source}.`
- `{metric} people submitted homework in our free Zoomcamps.`

Body formula:

1. Present the proof.
2. Explain why it matters.
3. Connect it to the course promise.
4. Keep the learner/community as the hero.
5. Invite similar learners to join.

Reusable inputs:

- quote/story, source, metric, learner transformation, course URL.

Examples from export:

- `8802681`: community member overcame fear of coding.
- `8518298`: DE Zoomcamp participant review.
- `8986489`: ML Zoomcamp ranked #1.
- `7314383`: 5,000+ homework submissions in 2025.

### 10. Project / Challenge / Competition

Use when asking learners to build, submit, share, or compete.

Common hooks:

- `Build your {Course} project using {tool} and get a chance to win:`
- `Reminder: {Competition} is live.`
- `We've reached the midterm/final projects at {Course}.`

Body formula:

1. State the task or challenge.
2. Explain the required output.
3. List prizes, criteria, or submission steps.
4. Clarify deadline and channel.
5. End with link to rules or submission page.

Reusable inputs:

- project brief, tool/sponsor, prizes, evaluation method, deadline, submission URL.

Examples from export:

- `8388879`: Bruin project competition.
- `8115013`: DE project with Claude Pro prize.
- `7229150`: ML Zoomcamp midterm projects.

### 11. Partner / Sponsor / Instructor Call

Use when a sponsor, partner, guest instructor, or collaborator is part of the course.

Common hooks:

- `{Partner} is back with a workshop for {Course}.`
- `{Course} would not have been possible without our sponsors.`
- `Join {Course} as an instructor.`

Body formula:

1. Name the partner or role.
2. Explain what they contribute.
3. Make the benefit to learners explicit.
4. Thank or invite the relevant group.
5. Include partner/course links.

Reusable inputs:

- partner name, contribution, learner benefit, sponsor/instructor CTA, URL.

Examples from export:

- `9159711`: sponsor thank-you after DE Zoomcamp.
- `8388879`: Bruin competition.
- `6825728`: instructor call for AI Dev Tools Zoomcamp.

### 12. Milestone / Wrap-Up / Results

Use to mark cohort progress, completion, certificates, competition results, GitHub stars, or community growth.

Common hooks:

- `{Course} has officially wrapped up.`
- `{Course} has gained {metric} stars on GitHub.`
- `Congratulations to {number} participants who completed {Course}.`

Body formula:

1. Announce the milestone.
2. Share concrete numbers or outcomes.
3. Thank participants, reviewers, sponsors, or community.
4. Tell people what happens next.
5. Invite graduates to share or future learners to join the next cohort.

Reusable inputs:

- milestone, metric, completion/certificate info, next cohort note, community CTA.

Examples from export:

- `9159705`: DE Zoomcamp wrapped up with 581 certificates.
- `8913769`: DE Zoomcamp complete.
- `7482340`: DE Zoomcamp GitHub stars.

### 13. Career / Audience Framing

Use to connect the course to a role transition, job-market problem, or learner background.

Common hooks:

- `{Role A} vs. {Role B}: what's the difference?`
- `The job market is tough right now, especially for {segment}.`
- `Many {role} are transitioning into {target_role}.`

Body formula:

1. Name the learner situation.
2. Explain the gap or transition.
3. Show how the course/project builds relevant skills.
4. Avoid promising jobs.
5. End with a course or resource CTA.

Reusable inputs:

- audience segment, pain point, skill gap, relevant modules/projects, CTA URL.

Examples from export:

- `7650176`: entry-level job market context.
- `7800561`: data analyst vs. engineer vs. analytics engineer.
- `6951674`: DevOps to MLOps/AI Engineering transition.

### 14. Community / Learning In Public

Use to encourage learners to share work, ask questions, publish notes, or use the community.

Common hooks:

- `Here's why I recommend learning in public:`
- `Learning in public makes your work visible.`
- `{Course} participants are sharing {homework/project}.`

Body formula:

1. Explain the behavior you want.
2. Show what learners gain from it.
3. Give specific examples of what to post/share.
4. Point to Slack, GitHub, LinkedIn, or a hashtag.
5. Encourage low-pressure participation.

Reusable inputs:

- sharing channel, examples, community norms, course hashtag, support link.

Examples from export:

- `8519005`: why learning in public matters.
- `7800221`: visibility and outcomes.
- `6919241`: AI Dev Tools participants sharing Homework 1.

### 15. Companion Offer / Support Layer

Use when explaining an optional paid or higher-touch support layer around a free course.

Common hooks:

- `{Course} is free and will stay free.`
- `If you're in {Program}, you get your own {Course} cohort.`
- `{Program} starts today.`

Body formula:

1. Reassure that the core course remains free.
2. Explain who the companion offer is for.
3. List support benefits.
4. Clarify what is included and not included.
5. Link to companion program details.

Reusable inputs:

- free course promise, support program name, included benefits, tier rules, URL.

Examples from export:

- `9531386`: LLM Zoomcamp remains free, AI Shipping Labs optional.
- `9482899`: AI Shipping Labs members get their own LLM Zoomcamp cohort.
- `9435750`: AI Shipping Labs Sprint 2.

## Secondary Modifiers

Use modifiers to adapt a primary type without creating too many categories.

- `urgency`: starts today, tomorrow, in one week, last chance, deadline extended, live in 3 hours.
- `proof`: learner quote, ranking, GitHub stars, registration count, certificate count, homework submissions.
- `event`: workshop, live Q&A, office hours, recording, launch session.
- `resource`: GitHub repo, README, article, list, cheatsheet, recording, docs page.
- `community`: Slack channel, DataTalksClub, peer review, learning in public, project sharing.
- `partner`: sponsor, guest instructor, tool partner, competition partner.
- `technical_depth`: beginner explanation, conceptual model, implementation steps, evaluation/failure modes.
- `course_logistics`: prerequisites, homework, deadlines, leaderboard, peer review, certificate, final project.

## Campaign Coverage Model

For any course, build the campaign with these buckets:

1. Pre-launch: `Interest Validation`, `Course Positioning`, `Social Proof`.
2. Launch week: `Course Launch`, `FAQ Answer`, `Live Event`, `Resource Update`.
3. Active cohort: `Module Announcement`, `Educational Micro-Lesson`, `Community`, `Workshop`.
4. Project phase: `Project/Challenge`, `Partner/Sponsor`, `Deadline Reminder`.
5. Wrap-up: `Milestone/Results`, `Testimonial`, `Next Cohort Teaser`.
6. Evergreen: `Educational Micro-Lesson`, `Career Framing`, `Resource Update`, `Learning In Public`.

## Generation Checklist

Before drafting, collect:

- Course name and one-sentence promise.
- Target audience and prerequisite level.
- Cohort date or evergreen availability.
- 3-7 concrete learning outcomes.
- Course URL, repo URL, docs URL, community channel.
- Current campaign phase.
- One proof asset if available.
- One clear CTA.

When drafting:

- Start with the concrete reason to care.
- Keep paragraphs short.
- Prefer mechanisms, examples, and outcomes over hype.
- Use dates, numbers, and links only when verified.
- Do not promise jobs, salary outcomes, or guaranteed results.
- Keep the course adaptable: swap course name, module, audience, proof, CTA, and logistics.
