# Course Launch Social Media System

Use this system to plan social content for any live course cohort. It is intentionally abstracted from past Typefully data: the goal is to define a reusable campaign architecture, then adapt it to a specific course, audience, channel, and launch date.

## Operating Principle

A course launch is not one announcement. It is a phased campaign:

1. Build relevance before people are ready to register.
2. Turn attention into trust before asking repeatedly.
3. Make the decision easy during the launch window.
4. Support learners after the course starts.
5. Convert cohort activity into proof for the next cohort.

## Campaign Inputs

Before filling a calendar, collect:

| Input | Why it matters |
| --- | --- |
| Course name and one-sentence promise | Keeps every post anchored. |
| Start date and enrollment deadline | Drives urgency and relative scheduling. |
| Target learner segments | Prevents generic posts. |
| Prerequisites and exclusions | Reduces bad-fit signups and repeated questions. |
| Curriculum outcomes | Supplies educational and launch content. |
| Course format | Explains cohort vs self-paced, homework, peer review, certificates. |
| Proof assets | Testimonials, metrics, rankings, GitHub stars, projects, alumni stories. |
| Events | Workshops, Q&A, launch stream, office hours, guest sessions. |
| Community links | Slack, Telegram, forum, GitHub discussions, hashtags. |
| Primary CTA | Register, join waitlist, attend event, read syllabus, start module, submit project. |

## Platform & distribution guidance

- DTC and Alexey social channels should publish every day when campaign activity supports it.
- For the same account, use the same core message across LinkedIn and X when it makes sense, and customize for format and tone when needed.
- Alexey X is premium and can carry longer-form launch commentary and event storytelling. DTC X should stay concise, punchy, and direct.
- DTC newsletter goes out weekly on Monday with community updates and cohort progress. Alexey newsletter goes out weekly on Friday with launch status, tools, and event invitations.
- Use the canonical course registration URL in cohort launch copy and page updates: https://courses.datatalks.club/register/ai-dev-tools/.
- Use Luma URLs for event-specific RSVP CTAs.
- Telegram messages are auto-reposted into DTC Slack. Treat DTC Slack as the main team channel and also publish separate engagement-first Slack posts such as questions, discussion prompts, or community calls-to-action.
- The campaign calendar should use one row per platform/post. The same date can appear several times when DTC newsletter, Alexey/DTC socials, Telegram, Slack, Website, GitHub, and YouTube each need a separate action.
- Workshops should be promoted regularly. For each workshop week, aim for one announcement plus one reminder or follow-up post when timing allows.
- Website banner and GitHub README updates are part of launch infrastructure: keep the cohort landing page, banner, and course README aligned with the current start date, registration URL, and workshop schedule.

Confirmed AI Dev Tools Zoomcamp 2026 event links:

- Workshop 1: AI-Native Developer Workflow: Using AI Tools Without Losing Control — https://luma.com/lmkti8zj
- Workshop 2: Build and Ship an AI-Assisted Full-Stack App — https://luma.com/50kvfku2
- Workshop 3: Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents — https://luma.com/ap4l3qlj
- Workshop 4: DevOps and Observability for AI-Built Apps — https://luma.com/ycsfxigi
- Pre-Course: AI Dev Tools Zoomcamp 2026 Pre-Course Live Q&A — https://luma.com/a8qa5s2s
- Course Launch: AI Dev Tools Zoomcamp 2026 Course Launch — https://luma.com/tsiusx8s

## Relative Date Notation

`T` means the course start date.

| Notation | Meaning | Example if the course starts on August 31 |
| --- | --- | --- |
| `T+0` | Start day. | August 31 |
| `T-6 weeks` | Six weeks before the course starts. | Around July 20 |
| `T-14 days` | Fourteen days before the course starts. | August 17 |
| `T-1 day` | The day before the course starts. | August 30 |
| `T+1 week` | One week after the course starts. | Around September 7 |
| `T+course_end` | The week the course ends. | Depends on course duration. |
| `T+project_start` | The week the project phase starts. | Depends on curriculum. |
| `T+project_deadline-7 days` | Seven days before the project deadline. | Depends on project deadline. |

Use relative dates because the same system should work for any course. Once a course has an exact start date, convert the relative dates into calendar dates.

Example: if a course starts on Monday, August 31, 2026:

- `T-8 weeks` means the week of July 6, 2026.
- `T-6 weeks` means the week of July 20, 2026.
- `T-2 weeks` means the week of August 17, 2026.
- `T+0` means August 31, 2026.
- `T+1 week` means the week of September 7, 2026.

## Courses In This Repo

These are the courses currently described by local `course.yaml` files:

| Course | Current launch mode from local metadata | Main social implication |
| --- | --- | --- |
| AI Dev Tools Zoomcamp | 2026 cohort starts August 31, 2026; registration open. | Use the full launch system now: awareness, consideration, decision, launch week, active cohort, project, wrap-up. |
| Data Engineering Zoomcamp | Next live cohort starts January 2027; exact date not in local metadata. | Use long-runway awareness and evergreen posts now; convert to launch posts when the exact date is confirmed. |
| LLM Zoomcamp | 2026 cohort started June 8, 2026; self-paced materials available anytime. | Use active-cohort, project, wrap-up, and evergreen posts; avoid pre-launch language for the current cohort. |
| Machine Learning Zoomcamp | Next live cohort starts September 2026; exact date not in local metadata. | Use awareness and consideration now; add exact countdown once the date is confirmed. |
| MLOps Zoomcamp | No live cohort planned in 2026; waitlist/get-updates mode. | Use evergreen and waitlist posts; do not use start-date urgency unless a live cohort is scheduled. |

Note: the proof-library files exist for each course, but they are currently empty in this repo snapshot. That means proof posts are possible as a post type, but they need proof assets added first: testimonials, previous cohort stats, GitHub stars, project examples, rankings, or learner stories.

## Course-Specific Post Opportunities

This section lists posts that can be created from the course information already available in the repo. It is not a final calendar. It is an inventory of strong candidate posts and why each belongs to a phase.

### AI Dev Tools Zoomcamp

Course facts available: free course, 2026 cohort starts August 31, 2026, registration open, beginner-friendly for programmers, focuses on disciplined AI-assisted software development workflows: coding assistants, agents, MCP, OpenAPI, frontend/backend integration, testing, CI/CD, deployment, PR review, and automation.

| Phase | Post opportunity | Why this belongs here |
| --- | --- | --- |
| Foundation | "AI coding tools are useful only if you can review, test, and maintain the code." | This is a belief/problem-framing post. It prepares the audience before asking them to register. |
| Foundation | "Vibe coding vs engineering workflow: where AI helps and where discipline matters." | This defines the market context and attracts the right people early. |
| Awareness | "What is AI Dev Tools Zoomcamp?" | People need the category explained before they evaluate the course. |
| Awareness | "Coding assistant, coding agent, MCP server, OpenAPI: how these pieces fit together." | This is a broad explainer suited to first-touch interest. |
| Awareness | "You do not need prior AI tools experience to join." | This removes a top-of-funnel misconception before the heavier launch push. |
| Awareness | "Tool landscape: ChatGPT, Claude, Cursor, GitHub Copilot, Codex, Gemini CLI, MCP." | Tool lists create interest and make the course feel practical. |
| Consideration | Main registration announcement with August 31, 2026 start date. | This belongs once the cohort date and registration link are confirmed. |
| Consideration | "Who this course is for: developers, ML engineers, MLOps engineers, data scientists, analysts who write code." | This helps people self-select after they are aware of the course. |
| Consideration | "Who this course is not for: not RAG, not training models, not data analytics workflows." | This prevents bad-fit registrations and repeated comments. |
| Consideration | "What you will build: project bootstrapping, MCP workflow, tests, CI/CD, deployment, PR review." | Outcome posts help interested people decide whether the course is worth their time. |
| Consideration | "Prerequisites: basic programming, command line, Git/GitHub." | Prerequisite posts belong in consideration because they answer the practical "can I do this?" question. |
| Decision | Pre-course Q&A announcement. | The final two weeks are when uncertain learners need a low-friction way to ask questions. |
| Decision | Environment/setup checklist: editor, GitHub, command line, tool accounts, free-tier expectations. | Setup content belongs right before launch because learners can act on it immediately. |
| Decision | "What happens in week 1." | First-week previews reduce anxiety right before start. |
| Launch Week | "AI Dev Tools Zoomcamp starts today." | Start-day urgency only belongs on the actual start day. |
| Launch Week | Module 1 announcement: AI tools overview / vibe coding intro. | Learners need the first action after the cohort begins. |
| Active Cohort | Weekly module announcements for MCP, OpenAPI, testing, CI/CD, deployment, low-code/no-code automation. | These map directly to cohort progress after the course has started. |
| Active Cohort | Micro-lessons: "AI-generated code still needs tests", "MCP in plain language", "PR review with AI." | These teach from the active module and keep non-registered followers engaged. |
| Project Phase | Project announcement and examples using the course project docs. | Project posts belong after learners have enough material to build something. |
| Project Phase | "Good AI Dev Tools project scope vs too-large scope." | Scope guidance is most useful once learners are selecting projects. |
| Wrap-Up | Completion/results post. | Belongs after the cohort ends and numbers are verified. |
| Wrap-Up | Student project showcase. | Belongs after submissions are available. |
| Evergreen | "Self-paced materials are available, but live cohort gives deadlines and community." | Between cohorts, this explains value without false urgency. |

### Data Engineering Zoomcamp

Course facts available: free course, next live cohort January 2027, 9 weeks plus final project, beginner-friendly for data engineering, assumes basic Python/SQL/Git/command line, covers end-to-end pipelines, Docker, Terraform, GCP, BigQuery, Kestra, dlt, dbt, Spark, streaming, dashboarding, and final projects.

| Phase | Post opportunity | Why this belongs here |
| --- | --- | --- |
| Foundation | "Modern data engineering is more than moving data from A to B." | Broad problem framing is useful long before the January 2027 start. |
| Foundation | "Data analyst vs data engineer vs analytics engineer." | Role framing attracts people who are still deciding what path fits them. |
| Awareness | "Data Engineering Zoomcamp returns in January 2027." | The exact date is not local, so use month-level awareness, not day-level urgency. |
| Awareness | "What an end-to-end data pipeline includes." | This teaches the domain and shows why the course exists. |
| Awareness | "Batch vs streaming: where each appears in the course." | A concrete explainer creates qualified interest. |
| Awareness | "Tool map: Docker, Terraform, GCP, BigQuery, Kestra, dbt, Spark, streaming." | Tool landscape posts work early because they make the syllabus tangible. |
| Consideration | Main registration announcement once the exact January 2027 date is confirmed. | Registration posts need a confirmed date and link. |
| Consideration | "Prerequisites: Python basics, SQL fundamentals, Git, command line." | This belongs when people are deciding whether they are ready. |
| Consideration | "No prior data engineering or cloud experience required." | This answers a likely blocker for beginner-friendly courses. |
| Consideration | "Time commitment: 10-15 hours/week; Module 1 can take longer because setup is tricky." | Time and setup details belong in the decision process. |
| Consideration | "What you will build: ingestion, warehouse, orchestration, transformations, batch, streaming, dashboard, project." | Outcome posts support registration with concrete value. |
| Decision | Pre-course Q&A announcement. | Good in the final two weeks because doubts are most actionable then. |
| Decision | Environment setup checklist: Docker, GCP/Codespaces/VM, editor, Git. | Setup is known to be a friction point, so it belongs near launch. |
| Decision | "How certificates and final projects work." | Certificate logistics are decision-stage blockers. |
| Launch Week | "Data Engineering Zoomcamp starts today." | Only use when the exact cohort begins. |
| Launch Week | Module 1 announcement and setup guidance. | The first week needs operational clarity. |
| Active Cohort | Weekly module posts: orchestration, warehouse, analytics engineering, batch, streaming. | These follow the cohort rhythm. |
| Active Cohort | Micro-lessons: "orchestration vs scheduling", "data lake vs warehouse", "dbt's role in DE." | Current-module lessons keep the public campaign educational. |
| Project Phase | Final project announcement with rubric, datasets, and gallery links. | Belongs when learners move from modules to independent work. |
| Project Phase | Project idea post using the datasets/project docs. | Helps learners choose a feasible project. |
| Wrap-Up | Graduate/certificate/results post. | Use after final numbers are known. |
| Wrap-Up | Project gallery post. | Belongs after projects are submitted and reviewable. |
| Evergreen | "Learn DE self-paced while waiting for the next cohort." | Useful until the January 2027 date is precise. |

### LLM Zoomcamp

Course facts available: free course, 2026 cohort started June 8, 2026, self-paced materials available anytime, intermediate for programmers, covers LLM apps, RAG, vector search, hybrid search, reranking, agents, function calling, evaluation, monitoring, feedback loops, and a capstone project.

| Phase | Post opportunity | Why this belongs here |
| --- | --- | --- |
| Foundation | "LLM applications are engineering systems, not prompt collections." | This is a durable thesis for future cohorts or evergreen promotion. |
| Foundation | "You probably do not need to train an LLM from scratch." | This corrects a misconception and attracts application builders. |
| Awareness | "What LLM Zoomcamp teaches: RAG, agents, evaluation, monitoring, project." | Useful for evergreen and next-cohort awareness. |
| Awareness | "RAG in plain language." | A broad explainer creates interest without requiring registration urgency. |
| Awareness | "Vector search, hybrid search, reranking: how they differ." | Good awareness/education for the target audience. |
| Consideration | "Who this course is for: software engineers, backend engineers, data engineers, ML practitioners." | Fit posts belong when learners compare options. |
| Consideration | "Prerequisites: Python, command line, Git, Docker, API key or local LLM." | This helps people decide if they can participate. |
| Consideration | "Not about training LLMs from scratch or fine-tuning/deploying open-source LLMs." | This prevents wrong expectations. |
| Consideration | "Hosted API costs and local alternatives." | Cost/API-key concerns are decision-stage blockers. |
| Decision | Setup checklist: Python, uv, Docker, API key/local model, notebooks. | This belongs right before a live cohort or as evergreen onboarding. |
| Decision | Pre-course Q&A for a future cohort. | Use only when a new cohort date is announced. |
| Launch Week | "LLM Zoomcamp starts today." | Not suitable now for the 2026 cohort because the local metadata says it already started on June 8, 2026. Use only for future cohorts. |
| Active Cohort | Module posts for RAG, vector search, agents, orchestration, evaluation, monitoring. | This is the best fit for the current 2026 cohort if still active. |
| Active Cohort | Micro-lessons: hit rate vs MRR, function calling does not run your code, agent loop basics. | These map to current technical modules and are valuable publicly. |
| Project Phase | Capstone project announcement and project guidelines. | Belongs once learners have enough material to build an end-to-end LLM app. |
| Project Phase | "Good LLM project scope: your own knowledge base, evaluation, monitoring, documentation." | Helps learners avoid vague chatbot projects. |
| Wrap-Up | Project gallery and winning/interesting solutions. | Belongs after submissions exist. |
| Wrap-Up | Results/lessons learned from the 2026 cohort. | Belongs after cohort metrics and observations are verified. |
| Evergreen | "LLM Zoomcamp is available self-paced." | Correct message after the live start date has passed. |
| Evergreen | "Awesome LLMs/resources update." | Resource posts can happen anytime because the LLM ecosystem changes quickly. |

### Machine Learning Zoomcamp

Course facts available: free course, next live cohort September 2026, beginner-to-intermediate, 4 months, open registration, teaches ML engineering from ML basics through evaluation, trees, deep learning, deployment, serverless, Kubernetes, and model serving.

| Phase | Post opportunity | Why this belongs here |
| --- | --- | --- |
| Foundation | "Machine learning is not just training a model." | Good early thesis for an engineering-focused ML course. |
| Foundation | "From notebook to deployable ML system." | Frames the course value before registration pressure. |
| Awareness | "ML Zoomcamp starts in September 2026." | Month-level awareness is appropriate until exact date is local. |
| Awareness | "What practical ML engineering means." | Explains the category before asking for commitment. |
| Awareness | "Regression, classification, evaluation, deployment: the course path." | Good syllabus-level awareness. |
| Awareness | "ML role framing for software engineers, data analysts, and data practitioners." | The course has multiple target segments, so role posts belong early. |
| Consideration | Main registration announcement once exact start date is known. | Full CTA needs the exact date. |
| Consideration | "Prerequisites: programming, command line, Git, Docker; no prior ML required." | This helps beginners decide if they can join. |
| Consideration | "Math expectations: intuition over advanced math." | This answers a common ML-course objection. |
| Consideration | "What you will build: regression model, classifier, evaluation workflow, deployment, deep learning, serving." | Concrete outcomes turn interest into signups. |
| Consideration | "Self-paced vs live cohort: deadlines, grading, leaderboard, peer review, certificates." | Explains why live registration matters. |
| Decision | Pre-course Q&A announcement. | Best near the start date when questions are actionable. |
| Decision | Environment setup checklist: Python, notebooks, Docker, Codespaces if needed. | Reduces start-week friction. |
| Launch Week | "ML Zoomcamp starts today." | Use only when the exact September date arrives. |
| Launch Week | Module 1 announcement: ML basics, CRISP-DM, setup, NumPy/Pandas refresher. | Gives learners the first step. |
| Active Cohort | Weekly module posts: regression, classification, evaluation, trees, deployment, deep learning, serverless, Kubernetes. | These track the cohort sequence. |
| Active Cohort | Micro-lessons: leakage, RMSE, precision/recall, ROC AUC, deployment patterns. | These are strong educational posts during the relevant weeks. |
| Project Phase | Midterm/final project announcement. | Project posts belong once learners have enough skills to build. |
| Project Phase | Project scope and portfolio framing. | Helps learners create something useful instead of a toy notebook. |
| Wrap-Up | Completion/certificate post. | Use after the cohort ends and numbers are known. |
| Wrap-Up | Project gallery and learner stories. | Belongs after projects are public. |
| Evergreen | "Study ML Zoomcamp self-paced before the next cohort." | Good when exact launch urgency is not yet available. |

### MLOps Zoomcamp

Course facts available: free course, no live cohort planned in 2026, waitlist/get-updates mode, intermediate level, assumes ML fundamentals, Python, command line, Docker, covers experiment tracking, model registry, orchestration, deployment, monitoring, testing, CI/CD, infrastructure as code, reproducibility, and portfolio project.

| Phase | Post opportunity | Why this belongs here |
| --- | --- | --- |
| Foundation | "Training a model is not the same as operating an ML system." | This is the core problem framing for MLOps. |
| Foundation | "MLOps is for people who already know the basic ML workflow." | This sets expectations early and avoids beginner mismatch. |
| Awareness | "MLOps Zoomcamp is available self-paced." | Since no live 2026 cohort is planned, evergreen awareness is the accurate message. |
| Awareness | "What MLOps covers: tracking, pipelines, deployment, monitoring, testing, CI/CD." | Broad explainer suited to self-paced discovery. |
| Awareness | "Online vs batch vs streaming inference." | Strong educational post from course topics. |
| Consideration | "Who should take MLOps Zoomcamp: data scientists, ML engineers, software engineers working with ML." | Helps readers decide whether the course is right. |
| Consideration | "Prerequisites: ML fundamentals, Python, Docker, command line." | Important because this is not a beginner ML course. |
| Consideration | "What self-paced learners can and cannot get: project for practice, no live-cohort certificate unless scheduled." | This prevents misleading expectations. |
| Consideration | "ML Zoomcamp before MLOps Zoomcamp?" | Natural comparison post because the metadata recommends ML Zoomcamp or equivalent experience. |
| Decision | Waitlist/get-updates post. | Since there is no start date, the decision CTA is waitlist, not register-now urgency. |
| Decision | Self-paced setup checklist: Python, Docker, AWS/local alternatives, MLflow. | Helps motivated learners start immediately. |
| Launch Week | No launch-week post unless a new live cohort is scheduled. | There is no local live cohort date, so start-day urgency would be false. |
| Active Cohort | No active-cohort sequence unless a new live cohort is scheduled. | Current metadata says self-paced only for now. |
| Project Phase | Portfolio project guidance using the project docs. | Self-paced learners can still build a project. |
| Project Phase | "Good MLOps project scope: tracking, pipeline, deployment, monitoring, reproducibility." | Helps learners produce portfolio-quality work. |
| Wrap-Up | Not applicable without a live cohort. | Wrap-up posts need cohort activity and verified results. |
| Evergreen | Micro-lessons: experiment tracking, model registry, monitoring, CI/CD, Terraform, reproducibility. | Evergreen education is the best fit while no cohort is scheduled. |
| Evergreen | "MLOps Zoomcamp waitlist / get updates." | Keeps demand warm without inventing a date. |

## Campaign Phases

### Phase 0: Foundation

Relative period: `T-12 to T-9 weeks`

Use when the course is not ready for heavy promotion yet.

Goal: make the course legible and prepare the market.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Problem framing | Name the painful skill gap the course solves. | Use early, before the first launch announcement. |
| Audience segmentation | Explain who the course is for and not for. | Use when the topic attracts mixed audiences. |
| Market/context post | Explain why this skill matters now. | Use when the course topic is affected by tooling, jobs, regulation, or market change. |
| Founder/instructor thesis | Explain the belief behind the course. | Use when the course has a strong philosophy. |
| Curriculum design note | Show how the course was built and why modules are ordered that way. | Use when learners may not understand the path. |
| Waitlist/interest validation | Ask people to join a waitlist or register interest. | Use when the cohort date, curriculum, or assets are still being finalized. |
| Research question | Ask the audience what they struggle with. | Use to collect objections and language for later posts. |
| Behind-the-scenes build note | Show course preparation, repo updates, new modules, recordings, or tooling. | Use when visible progress builds confidence. |

### Phase 1: Awareness

Relative period: `T-8 to T-6 weeks`

Goal: reach qualified learners and create first-touch interest.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Coming-soon announcement | Tell people the cohort is happening. | Use once the start window is credible. |
| Main topic explainer | Teach the course domain in plain language. | Use for audiences unfamiliar with the course area. |
| Role/pathway post | Connect the course to learner backgrounds and career paths. | Use for courses with multiple learner segments. |
| Educational micro-lesson | Teach one useful concept from the course. | Use throughout the campaign, especially before direct CTAs. |
| Myth/misconception post | Correct a common false belief. | Use when the topic has hype, fear, or confusion. |
| Tool landscape post | Explain tools used in the course and why. | Use for tooling-heavy courses. |
| Resource refresh post | Announce updated docs, syllabus, FAQ, GitHub repo, or article. | Use when assets are ready. |
| Workshop announcement | Promote a pre-course event. | Use if the course has a workshop funnel. |
| Partner/guest teaser | Introduce a sponsor, guest, or collaborator. | Use only when the partnership helps learners. |

### Phase 2: Consideration

Relative period: `T-5 to T-3 weeks`

Goal: help interested people decide whether the course fits them.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Main registration announcement | Open the cohort with start date, promise, outcomes, and CTA. | Use once registration is ready. |
| Course positioning FAQ | Answer who it is for, prerequisites, time commitment, tools, and outcomes. | Use whenever comments reveal friction. |
| Syllabus walkthrough | Show the course path module by module. | Use for longer or more technical courses. |
| Outcome list | List concrete things learners will build, evaluate, deploy, submit, or explain. | Use when the course needs practical credibility. |
| Format explainer | Explain cohort rhythm, homework, deadlines, scoring, peer review, and certificates. | Use for courses with live-cohort mechanics. |
| Self-paced vs cohort post | Explain what changes when learners join live. | Use when materials are also evergreen. |
| Prerequisites post | Make required and not-required skills explicit. | Use when the course risks attracting bad-fit learners. |
| Objection handler | Answer one major objection at a time. | Use for cost, time, math, coding, cloud, API keys, certificates, or job concerns. |
| Proof post | Share learner story, project, ranking, metric, or testimonial. | Use to support, not replace, explanation. |
| Comparison post | Compare roles, tools, approaches, or course paths. | Use when learners are choosing between courses or fields. |
| Instructor credibility post | Explain why the instructor can teach this topic. | Use sparingly; focus on learner value. |

### Phase 3: Decision

Relative period: `T-2 weeks to T-1 day`

Goal: remove blockers and create timely action.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Final registration reminder | Make the start date and CTA unmistakable. | Use in the final week. |
| Pre-course Q&A announcement | Invite people to ask questions live. | Use 1-2 weeks before start. |
| Q&A recap | Summarize answers from the live Q&A. | Use after the event for people who missed it. |
| Launch stream reminder | Promote the kickoff event. | Use in final week and on start day. |
| Setup checklist | Help learners prepare environment, accounts, repo, and community access. | Use 3-7 days before start. |
| First-week preview | Show exactly what happens in week 1. | Use when people are nervous about starting. |
| Last objections post | Answer the final blockers seen in comments. | Use in the final week. |
| Social proof reminder | Share a concrete story or project close to launch. | Use to support late decisions. |
| Community invitation | Point people to Slack, Telegram, forum, or GitHub discussions. | Use right before and after start. |
| Urgency post | Say starts tomorrow, starts today, registration closes, or deadline approaching. | Use only when the date is real. |

### Phase 4: Launch Week

Relative period: `T+0 to T+6 days`

Goal: help learners start, reduce confusion, and convert attention into participation.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Starts today | Announce that the cohort begins now. | Use on launch day. |
| Kickoff/launch stream | Promote or recap the kickoff. | Use on launch day or immediately after. |
| Module 1 announcement | Tell learners what to do first. | Use on day 1 or day 2. |
| Materials link post | Collect repo, platform, docs, FAQ, homework, and community links. | Use once learners need to act. |
| How to ask questions | Teach support norms and where to post issues. | Use when community volume rises. |
| First-week troubleshooting | Address common setup problems. | Use once real questions appear. |
| Welcome/community post | Invite introductions and learning-in-public. | Use early in the cohort. |
| Momentum proof | Share registration, attendance, or community energy if verified. | Use only if metrics are meaningful. |

### Phase 5: Active Cohort

Relative period: `T+1 week to project phase`

Goal: keep learners moving and keep public attention alive without repeating the same CTA.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Weekly module announcement | Say what starts this week and what learners will build. | Use every module. |
| Homework reminder | Remind learners what is due and where to submit. | Use near homework deadlines. |
| Educational micro-lesson | Teach one concept from the current module. | Use weekly. |
| Opinion/principle post | Explain the course philosophy behind a technical choice. | Use when there is a useful teaching stance. |
| Tool deep dive | Explain one tool, its role, and common mistakes. | Use for technical courses. |
| Failure-mode post | Explain what usually goes wrong and how to debug it. | Use when learners are stuck. |
| Office-hours announcement | Promote live support. | Use if office hours exist. |
| Recording/materials update | Share recordings, new docs, fixes, or repo updates. | Use after live sessions or updates. |
| Learner spotlight | Highlight a learner note, project, or useful community answer. | Use with permission and context. |
| Learning-in-public prompt | Encourage learners to share notes or progress. | Use repeatedly but vary the examples. |
| Mid-course motivation | Normalize falling behind and explain how to catch up. | Use after the first difficult module. |

### Phase 6: Project Phase

Relative period: `project start to project deadline`

Goal: move learners from consuming material to producing portfolio-quality work.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Project announcement | Explain project task, rubric, deadlines, examples, and submission link. | Use at project start. |
| Project idea post | Suggest good project scopes and bad project scopes. | Use when learners struggle to choose. |
| Example project breakdown | Walk through a strong previous project. | Use when a project gallery exists. |
| Rubric explainer | Explain how projects are evaluated. | Use before submissions start. |
| Peer-review explainer | Explain review requirements and etiquette. | Use before review phase. |
| Certificate logistics | Explain what counts for certificate eligibility. | Use when certificates are part of the course. |
| Deadline reminder | Remind learners about submission or review deadlines. | Use 7 days, 3 days, and 1 day before deadline. |
| Sponsor/tool challenge | Introduce optional partner prizes or tool-specific project tracks. | Use only if there is a real sponsor or challenge. |
| Project showcase prompt | Encourage learners to post demos and lessons. | Use after submissions open. |
| Extension/update post | Explain deadline changes. | Use only when there is a real change. |

### Phase 7: Wrap-Up

Relative period: `course end to T+4 weeks after`

Goal: close the cohort, celebrate learners, create proof, and prepare the next cycle.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Completion milestone | Share completion numbers, certificates, submissions, reviews, or participation. | Use when numbers are verified. |
| Thank-you post | Thank learners, reviewers, instructors, sponsors, and community helpers. | Use at the end of the cohort. |
| Project gallery post | Share the best projects or the full gallery. | Use after submissions/reviews are public. |
| Winner/results post | Announce competition or challenge results. | Use when there was a contest. |
| Testimonial post | Share learner quotes or transformations. | Use after collecting permission. |
| Lessons learned post | Reflect on what worked, what changed, and what will improve. | Use for transparency and trust. |
| Alumni call | Ask graduates to share outcomes or stories. | Use after certificates/projects. |
| Next cohort teaser | Invite people to waitlist for the next run. | Use after the current cohort closes. |
| Evergreen resource post | Reposition course materials for self-paced learners. | Use after the live cohort ends. |

### Phase 8: Evergreen Between Cohorts

Relative period: `always-on`

Goal: keep the course discoverable without pretending a live cohort is happening.

Possible post types:

| Post type | Purpose | When to use |
| --- | --- | --- |
| Evergreen course reminder | Tell people they can study self-paced. | Use between cohorts. |
| Concept lesson | Teach one durable concept from the course. | Use any time. |
| Resource update | Announce docs, videos, repo updates, FAQ changes, or article refreshes. | Use whenever assets change. |
| Alumni story | Share what a learner built or learned. | Use when proof is available. |
| Project inspiration | Highlight project ideas and examples. | Use to help self-paced learners. |
| FAQ post | Answer recurring questions. | Use whenever comments repeat. |
| Waitlist post | Invite people to get notified about the next cohort. | Use when no date is confirmed. |
| Ecosystem update | Explain changes in tools, libraries, cloud providers, or industry practice. | Use when the course topic changes over time. |

## Minimum Calendar

If time is limited, use this minimal sequence:

| Relative date | Post type |
| --- | --- |
| `T-30 days` | Reddit: cohort starts in a month |
| `T-28 days` | Main registration announcement |
| `T-24 days` | Who it is for / prerequisites |
| `T-21 days` | Educational micro-lesson |
| `T-18 days` | Social proof |
| `T-14 days` | Pre-course Q&A announcement |
| `T-10 days` | Format and certificate logistics |
| `T-7 days` | Final registration reminder |
| `T-3 days` | Setup checklist |
| `T+0 days` | Starts today |
| `T+0 days` | Reddit: starts today |
| `T+1 day` | Module 1 announcement |
| `project start` | Project announcement |
| `course end` | Completion milestone |

## Full Calendar Density

Use this when the campaign has enough runway:

| Period | Recommended density | Notes |
| --- | --- | --- |
| `T-12 to T-9 weeks` | 1-2 posts/week | Mostly market education and light validation. |
| `T-8 to T-6 weeks` | 2-4 posts/week | Mix awareness, education, and first proof. |
| `T-5 to T-3 weeks` | 3-5 posts/week | Registration is open; rotate FAQ, proof, outcomes, and launch posts. |
| `T-2 weeks to T-1 day` | 4-6 posts/week | Decision support, Q&A, setup, reminders. |
| `T+0 to T+6 days` | 3-5 posts/week | Start support, links, troubleshooting, community. |
| Active cohort | 2-4 posts/week | Module announcement, lesson, event/update, community. |
| Project phase | 3-5 posts/week | Project announcement, examples, logistics, deadlines. |
| Wrap-up | 2-4 posts/week | Results, thanks, testimonials, projects, next waitlist. |
| Evergreen | 1-2 posts/week or lower | No false urgency; focus on lessons, resources, proof, waitlist. |

For a single-person LinkedIn account, start at the low end. For a brand account plus newsletter, community, and video channels, use the higher end.

## Post Type Library

Use this library to generate a calendar. Each post should have one primary job.

| Category | Post types |
| --- | --- |
| Demand creation | Problem framing, market/context, role/pathway, future-skill post, misconception correction. |
| Education | Micro-lesson, tool explainer, framework, checklist, mistake/failure-mode, comparison, teardown. |
| Course positioning | Main launch, syllabus walkthrough, prerequisites, self-paced vs cohort, time commitment, format, certificate logistics. |
| Proof | Testimonial, alumni story, project showcase, ranking, GitHub stars, completion metric, learner quote, community answer. |
| Event | Workshop announcement, Q&A announcement, launch stream, office hours, event recap, recording post. |
| Community | Join community, learning-in-public prompt, introductions, how to ask questions, peer review etiquette. |
| Resource | Repo update, docs update, article update, FAQ update, recording, checklist, reading list, templates. |
| Project | Project announcement, idea list, rubric, examples, deadline reminder, peer review, winner/results, gallery. |
| Partner | Sponsor thanks, tool challenge, guest instructor, partner workshop, contributor call. |
| Community post | Reddit cohort announcement, Reddit start-day post. Written for a community that is not our audience. |
| Urgency | Starts soon, starts tomorrow, starts today, deadline approaching, registration closes, last call. |
| Retention | Catch-up guide, troubleshooting, motivation, weekly rhythm, homework reminder. |
| Wrap-up | Results, thank-you, lessons learned, certificate/project sharing, next-cohort teaser. |

## Channel Adaptation

| Channel | Best role |
| --- | --- |
| Personal LinkedIn | Thought leadership, practical lessons, proof, objections, launch announcements. |
| Brand LinkedIn | Official announcements, resources, events, project galleries, community updates. |
| X/Twitter | Short reminders, hooks, threads, live event timing, quick lessons. |
| Newsletter | Bigger narrative, registration pushes, Q&A recap, course logistics. |
| Slack/Telegram | Operational reminders, links, deadlines, troubleshooting, community prompts. |
| YouTube/Live | Workshops, Q&A, launch stream, office hours, recording recaps. |
| GitHub/Docs | Source of truth for curriculum, setup, homework, project, FAQ. |
| Reddit | Two posts per cohort: one a month before the start, one on the start day. Reaches people outside our channels who are actively looking for a course. |

### Reddit

Reddit is the one channel where our own audience is not the audience, so it does not take the same copy as the rest.

Cadence is fixed at two posts per cohort:

| When | Job |
| --- | --- |
| One month before the start | Announce the cohort while readers still have time to plan. Lead with what the course covers. |
| On the start day | Catch anyone who missed the first post. Late joiners can still start in week 1. |

`01-course-assets-map.md` lists the subreddit for each course.

Rules specific to this channel:

- Read the subreddit's self-promotion rules first. Several remove course launches posted as plain ads, and some require a flair or route them to a weekly thread.
- Write for that community. Do not paste the launch tweet or the LinkedIn post.
- Lead with the curriculum and what a learner will build, not the brand.
- Answer comments. On Reddit the comment thread is most of the value, and unanswered questions read as an ad.
- Two posts is the ceiling, not a starting point. More reads as spam and risks the account.

## Quality Rules

- One post, one job.
- Lead with the reader's problem, not the course name, unless it is a launch-day post.
- Use dates only when confirmed.
- Use proof with context; do not turn learners into props.
- Do not promise jobs, salary, promotions, or guaranteed outcomes.
- Prefer concrete outcomes over hype.
- Repeat the CTA, but vary the angle.
- Do not overuse urgency. Save it for real deadlines.
- Treat comments as research for the next FAQ post.
- Keep a post inventory so each phase has a balance of education, proof, logistics, and CTA.

## Measurement

Choose KPIs by phase:

| Phase | Useful signals |
| --- | --- |
| Foundation | Comments, saves, qualitative objections, waitlist signups. |
| Awareness | Reach, profile visits, shares, follower growth, event registrations. |
| Consideration | Link clicks, registration conversion, FAQ comments, direct questions. |
| Decision | Registrations, event attendance, setup checklist clicks, comment resolution. |
| Launch week | Active learners, community joins, setup issues resolved, homework starts. |
| Active cohort | Homework submissions, event attendance, community questions, learner posts. |
| Project phase | Project submissions, peer reviews, project shares, deadline completion. |
| Wrap-up | Certificates, testimonials, project gallery visits, next waitlist signups. |

Use UTM links for registration, event, syllabus, and resource posts when possible.

## Calendar Generation Rules

When turning this system into a CSV:

1. Start with the course start date as `T+0`.
2. Choose the campaign runway: short (`4 weeks`), normal (`8 weeks`), long (`12 weeks`).
3. Pick the active channels.
4. Select post types from each phase.
5. Limit each channel to a sustainable cadence.
6. Prioritize working days for professional audiences.
7. Keep no more than 3 posts per channel per day.
8. Assign every post a primary type, audience, angle, CTA, proof asset, and source link.
9. Mark posts as `Planned`, `Drafted`, `Approved`, `Scheduled`, or `Published`.
10. Review weekly and replace low-value repetition with FAQ/proof/lesson posts based on audience response.

## References

- Hootsuite: social campaigns should be focused, time-bound, goal-driven, scheduled in advance, and measured against campaign-specific KPIs. See `https://blog.hootsuite.com/social-media-campaign-strategy/`.
- Sprout Social: campaign content should map to the funnel, use proof/UGC where relevant, measure against goals, and run in phases long enough to gather useful data. See `https://sproutsocial.com/insights/social-media-campaigns/`.
- LinkedIn Marketing Solutions: LinkedIn recommends consistent posting, rich media, documents, video/live formats, reshares, hashtags, targeting, and analytics for Page growth and engagement. See `https://business.linkedin.com/advertise/linkedin-pages/best-practices`.
