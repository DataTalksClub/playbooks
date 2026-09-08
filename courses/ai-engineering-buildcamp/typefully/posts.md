# Typefully posts tagged `ai-engineering-buildcamp`

- Exported: 2026-09-08T14:30:51.945781+00:00
- Social set: `188312`
- Tag: `ai-engineering-buildcamp`
- Typefully records: 106

## Typefully draft 10677718

- Typefully ID: `10677718`
- Status: scheduled
- Tags: `ai-engineering-buildcamp`
- Created: 2026-09-08T11:09:18.771Z
- Updated: 2026-09-08T13:05:36.047Z
- Scheduled: 2026-09-19T07:00:00Z
- Typefully URL: https://typefully.com/?d=10677718&a=188312

### x

#### Post 1

I built a Django to-do app in one prompt.

Cost: less than $1.

Here's what the coding agent did:

1. Created the project structure
- Generated Django project and app
- Set up settings and URLs
- Configured Tailwind CSS for styling

2. Built the data model
- Created a Todo model
- Wrote and ran migrations

3. Implemented views and URLs
- List all tasks
- Add new tasks
- Delete tasks

4. Generated styled templates
- Responsive design with Tailwind CSS
- Form for adding tasks
- Interactive task list

5. Verified everything works
- Checked for errors
- Confirmed the app runs

Total time: under 5 minutes.

I documented the complete implementation in my guide.

It covers:
- How function calling works
- Tool schemas and descriptions
- System prompt engineering
- Full Python code with toyaikit

Read it here: https://maven.com/alexey-grigorev/o/0a9e5c

Media IDs: `cfb8f481-44f8-4e80-8938-b0b524dd9f4e`

#### Post 2

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

I built a Django to-do app in one prompt.

Cost: less than $1.

Here's what the coding agent did:

1. Created the project structure
- Generated Django project and app
- Set up settings and URLs
- Configured Tailwind CSS for styling

2. Built the data model
- Created a Todo model
- Wrote and ran migrations

3. Implemented views and URLs
- List all tasks
- Add new tasks
- Delete tasks

4. Generated styled templates
- Responsive design with Tailwind CSS
- Form for adding tasks
- Interactive task list

5. Verified everything works
- Checked for errors
- Confirmed the app runs

Total time: under 5 minutes.

I documented the complete implementation in my guide.

It covers:
- How function calling works
- Tool schemas and descriptions
- System prompt engineering
- Full Python code with toyaikit

Read it here: https://maven.com/alexey-grigorev/o/0a9e5c

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cfb8f481-44f8-4e80-8938-b0b524dd9f4e`

### substack

I built a Django to-do app in one prompt.

Cost: less than $1.

Here's what the coding agent did:

1. Created the project structure
- Generated Django project and app
- Set up settings and URLs
- Configured Tailwind CSS for styling

2. Built the data model
- Created a Todo model
- Wrote and ran migrations

3. Implemented views and URLs
- List all tasks
- Add new tasks
- Delete tasks

4. Generated styled templates
- Responsive design with Tailwind CSS
- Form for adding tasks
- Interactive task list

5. Verified everything works
- Checked for errors
- Confirmed the app runs

Total time: under 5 minutes.

I documented the complete implementation in my guide.

It covers:
- How function calling works
- Tool schemas and descriptions
- System prompt engineering
- Full Python code with toyaikit

Read it here: https://maven.com/alexey-grigorev/o/0a9e5c

Learn to build AI agents and apply new knowledge to create 15 projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cfb8f481-44f8-4e80-8938-b0b524dd9f4e`

## Function Calling in Action

- Typefully ID: `8050596`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T11:57:24.570Z
- Updated: 2026-07-28T07:34:11.958Z
- Scheduled: 2026-07-31T07:00:00Z
- Published: 2026-07-31T07:00:35.998Z
- Typefully URL: https://typefully.com/?d=8050596&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2083085257776238805

#### Post 1

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.

Media IDs: `2cc0ba9e-1d61-462b-bc42-22e3e1195b09`

#### Post 2

Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).

- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.

#### Post 3

1. Calendar & meetings

- Prompt: "Book 30 min with Alice tomorrow at 15:00."
- Tools: create_calendar_event(title, start, attendees)
- Effect: Event created; invite sent.

#### Post 4

2. Docs & notes

- Prompt: "Summarize this PDF and save the notes to Notion."
- Tools: extract_text(file), create_notion_page(title, content)
- Effect: Summary page appears in your workspace.

#### Post 5

3. CRM & sales ops

- Prompt: “Add this lead and enrich with company data.”
- Tools: create_crm_contact(data), enrich_with_clearbit(email)
- Effect: New contact with firmographics; owner assigned.

#### Post 6

4. Support triage

- Prompt: “Route this ticket and draft a first reply.”
- Tools: classify_ticket(text), create_ticket(queue), draft_reply(context)
- Effect: Ticket filed to the right queue with a suggested response.

#### Post 7

5. Data & reporting

- Prompt: “Revenue by region for the last 7 days—export to Sheets.”
- Tools: query_db(sql), create_google_sheet(name, rows)
- Effect: Fresh report in Google Sheets; link returned.

#### Post 8

6. Files & automation

- Prompt: “Rename these images, compress, and upload to S3.”
- Tools: transform_images(params), upload_s3(bucket, paths)
- Effect: Optimized assets live in your bucket.

#### Post 9

7. DevOps

- Prompt: “Is service X healthy? If not, roll back to the last stable.”
- Tools: get_status(service), rollback_deploy(service, version)
- Effect: Status reported; rollback executed if needed.

#### Post 10

8. HR & recruiting

- Prompt: “Schedule a loop with three interviewers next week.”
- Tools: find_slots(attendees), create_calendar_event(series)
- Effect: Calendar holds with invites and meeting links.

#### Post 11

9. Internal search + answer

- Prompt: “What’s our PTO policy?”
- Tools: semantic_search(kb, query), retrieve(doc_ids)
- Effect: Answer grounded in your knowledge base with citations.

#### Post 12

10. Email & comms

- Prompt: “Send the weekly update to the team and attach the report.”
- Tools: generate_summary(data), send_email(to, subject, body, attachments)
- Effect: Email sent with the latest metrics and file.

#### Post 13

Want to learn how to use function calling? I made a free guide on building your own AI coding agent with function calling and the OpenAI API. You can get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7488850959033438208

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.

➡️ Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).
- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.

Want to learn how to use function calling? I made a free guide on building your own AI coding agent with function calling and OpenAI API. You can get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `f4a7f29f-de15-43b4-9a14-0ebab74f1919`

## A Day of AI Engineer

- Typefully ID: `8802560`
- Status: published
- Tags: `ai-engineer`, `ai-engineering-buildcamp`
- Created: 2026-04-21T07:04:33.332Z
- Updated: 2026-04-21T07:21:55.763Z
- Scheduled: 2026-04-24T07:00:00Z
- Published: 2026-04-24T07:00:28.368Z
- Typefully URL: https://typefully.com/?d=8802560&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2047571344666333330

#### Post 1

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

Media IDs: `04c3b8f2-0aea-4d0c-80a5-c235de35a4a8`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7453336991619801088

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `ba86fd9a-ebb2-45c8-92bc-1de32735444b`

## Improving Project Definition

- Typefully ID: `8708838`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T08:56:27.131Z
- Updated: 2026-04-15T17:49:35.088Z
- Scheduled: 2026-04-16T14:00:00Z
- Published: 2026-04-16T14:00:37.705Z
- Typefully URL: https://typefully.com/?d=8708838&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2044777988986990977

One thing I'm changing for the next cohort of the AI Engineer Buildcamp: how I help people with their capstone projects.

The problem:

In the first two cohorts, I noticed a pattern: some participants spent too much time deciding what to build. Not everyone made as much progress as they could have.

What I'm doing differently:

I built a new framework for the project-definition stage, based on design thinking. It gives more structure at the point where people usually get stuck.

If you already have an idea:

- The framework helps you shape it
- Narrow the scope
- Turn it into something you can realistically build during the course

If you don't have an idea yet:

- I'll give you prompts and templates
- You can start right away
- Keep moving forward each week

The goal:

Start working on your capstone from day 1, with less uncertainty and more momentum.

If you follow the process, you should have a working capstone by the end of week 6. Then you can use the remaining time to improve it, test it, polish it, and prepare your presentation.

Apart from the capstone, you'll build 14 other projects during the course.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `f254f43d-a112-492c-aa16-7101deb5bfb5`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7450543678315565056

One thing I'm changing for the next cohort of the AI Engineer Buildcamp: how I help people with their capstone projects.

The problem:

In the first two cohorts, I noticed a pattern: some participants spent too much time deciding what to build. Not everyone made as much progress as they could have.

What I'm doing differently:

I built a new framework for the project-definition stage, based on design thinking. It gives more structure at the point where people usually get stuck.

If you already have an idea:

- The framework helps you shape it
- Narrow the scope
- Turn it into something you can realistically build during the course

If you don't have an idea yet:

- I'll give you prompts and templates
- You can start right away
- Keep moving forward each week

The goal:

Start working on your capstone from day 1, with less uncertainty and more momentum.

If you follow the process, you should have a working capstone by the end of week 6. Then you can use the remaining time to improve it, test it, polish it, and prepare your presentation.

Apart from the capstone, you'll build 14 other projects during the course.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `f254f43d-a112-492c-aa16-7101deb5bfb5`

## AI Engineering Scholarship Update

- Typefully ID: `8708801`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T08:51:38.185Z
- Updated: 2026-04-13T08:55:24.159Z
- Scheduled: 2026-04-14T17:00:00Z
- Published: 2026-04-14T17:00:41.867Z
- Typefully URL: https://typefully.com/?d=8708801&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2044098528822366613

I saw a few questions in the comments about the scholarship results for the new cohort of the AI Engineering Buildcamp.

Yes, I've already selected the recipients and emailed them directly.

The scholarship form is now closed, so if you didn't receive an email from me, that means you weren't selected this time.

Thank you to everyone who applied!

Even if you weren't selected, I really encourage you to keep learning and building. I've shared many free resources online, and you can find them here: https://alexeyondata.substack.com/p/how-i-reviewed-2500-ai-bootcamp-scholarship?open=false#%C2%A7thank-you-for-your-strong-submissions

If you need a student discount and PPP pricing, please contact me at alexey@datatalks.club, and I'll help you.

Media IDs: `2e799797-9dc6-4348-9adf-1573dce95ff8`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7449864215051259904

I saw a few questions in the comments about the scholarship results for the new cohort of the AI Engineering Buildcamp.

Yes, I've already selected the recipients and emailed them directly.

The scholarship form is now closed, so if you didn't receive an email from me, that means you weren't selected this time.

Thank you to everyone who applied!

Even if you weren't selected, I really encourage you to keep learning and building. I've shared many free resources online, and you can find them here: https://alexeyondata.substack.com/p/how-i-reviewed-2500-ai-bootcamp-scholarship?open=false#%C2%A7thank-you-for-your-strong-submissions

If you need a student discount and PPP pricing, please contact me at alexey@datatalks.club, and I'll help you.

Media IDs: `2e799797-9dc6-4348-9adf-1573dce95ff8`

## AI Bootcamp Review

- Typefully ID: `8708718`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T08:41:31.977Z
- Updated: 2026-04-13T08:44:11.810Z
- Scheduled: 2026-04-18T07:00:00Z
- Published: 2026-04-18T07:00:14.025Z
- Typefully URL: https://typefully.com/?d=8708718&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2045396969162670294

Got a new review from cohort 2 of the AI Engineering Buildcamp.

Vishnu, a data scientist at Humana:

"One of the best parts of the AI Agents Bootcamp is that you start building projects from week one. Even if you do not begin with a clear project idea, Alexey does a great job helping you iterate, improve, and shape your ideas along the way. The course is also filled with high-value content in every module, making it a very worthwhile learning experience."

You don't need a fully formed idea to start. You build it as you go.

Cohort 3 registration closes in 2 days.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `0c92681d-9e80-473a-963d-884ed5517be4`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7451162659628097536

Got a new review from cohort 2 of the AI Engineering Buildcamp.

Vishnu, a data scientist at Humana:

"One of the best parts of the AI Agents Bootcamp is that you start building projects from week one. Even if you do not begin with a clear project idea, Alexey does a great job helping you iterate, improve, and shape your ideas along the way. The course is also filled with high-value content in every module, making it a very worthwhile learning experience."

You don't need a fully formed idea to start. You build it as you go.

Cohort 3 registration closes in 2 days.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `0c92681d-9e80-473a-963d-884ed5517be4`

## AI Engineering Buildcamp Insights

- Typefully ID: `8708527`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T08:18:48.376Z
- Updated: 2026-04-13T08:43:26.143Z
- Scheduled: 2026-04-15T14:00:00Z
- Published: 2026-04-15T14:00:31.691Z
- Typefully URL: https://typefully.com/?d=8708527&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2044415575880019984

Another AI Engineering Buildcamp review from the course graduate, Sperydon, a data scientist at Loblaw Companies.

Here's what he shared:

"It pushed me to actually build, experiment, and step outside my comfort zone. The course was especially effective in helping me explore agents in a hands-on way. It gave me the confidence to try new ideas, work through implementation challenges, and think more deeply about how these systems are designed in practice."

Cohort 3 registration closes in 5 days.

If you've been thinking about joining, this is the cohort to do it.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cc275706-7b65-426a-be98-ff6154415c9d`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7450181249706520576

Another AI Engineering Buildcamp review from the course graduate, Sperydon, a data scientist at Loblaw Companies.

Here's what he shared:

"It pushed me to actually build, experiment, and step outside my comfort zone. The course was especially effective in helping me explore agents in a hands-on way. It gave me the confidence to try new ideas, work through implementation challenges, and think more deeply about how these systems are designed in practice."

Cohort 3 registration closes in 5 days.

If you've been thinking about joining, this is the cohort to do it.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cc275706-7b65-426a-be98-ff6154415c9d`

## Course Review Highlights

- Typefully ID: `8708652`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T08:33:04.482Z
- Updated: 2026-04-13T08:42:43.282Z
- Scheduled: 2026-04-14T07:00:00Z
- Published: 2026-04-14T07:00:16.156Z
- Typefully URL: https://typefully.com/?d=8708652&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2043947425501720753

I just got a new course review from Leo, a machine learning researcher at TNO:

"Its learning-by-doing approach is centered on a capstone project, which students can choose based on their personal and professional interests. The individual attention and support for students during weekly Q&A sessions made the learning experience especially valuable. I learned a lot about agentic AI, including how to properly evaluate and test them."

What I like about this feedback: it mentions the specifics.

- Capstone projects
- Hands-on work
- Evaluation
- Testing

That's what the course is built around.

Cohort 3 registration closes in 6 days.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cc930242-8a9b-4676-b379-f8e4fbcca5ba`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7449713113551060992

I just got a new course review from Leo, a machine learning researcher at TNO:

"Its learning-by-doing approach is centered on a capstone project, which students can choose based on their personal and professional interests. The individual attention and support for students during weekly Q&A sessions made the learning experience especially valuable. I learned a lot about agentic AI, including how to properly evaluate and test them."

What I like about this feedback: it mentions the specifics.

- Capstone projects
- Hands-on work
- Evaluation
- Testing

That's what the course is built around.

Cohort 3 registration closes in 6 days.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cc930242-8a9b-4676-b379-f8e4fbcca5ba`

## Last Chance for AI Buildcamp

- Typefully ID: `8708187`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-13T07:34:09.570Z
- Updated: 2026-04-13T08:08:23.091Z
- Published: 2026-04-13T08:08:26.277Z
- Typefully URL: https://typefully.com/?d=8708187&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2043602193975222749

22 people enrolled into AI Engineering Buildcamp last week.

If you saw the deadline too late, I extended enrollment by one week.

This is likely the last cohort I'll run in the near future. The course starts April 13, and week 1 is a buffer week so you can catch up if you join late.

7 days left ton enroll: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `e6133ada-5fd7-4af5-9465-72a921477264`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7449367884226600960

22 people enrolled into AI Engineering Buildcamp last week.

If you saw the deadline too late, I extended enrollment by one week.

This is likely the last cohort I'll run in the near future. The course starts April 13, and week 1 is a buffer week so you can catch up if you join late.

7 days left ton enroll: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `e6133ada-5fd7-4af5-9465-72a921477264`

## AI Engineering Buildcamp Overview

- Typefully ID: `8654809`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-08T10:03:31.175Z
- Updated: 2026-04-08T11:23:49.261Z
- Scheduled: 2026-04-09T07:00:00Z
- Published: 2026-04-09T07:00:33.725Z
- Typefully URL: https://typefully.com/?d=8654809&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2042135483401302068

#### Post 1

AI Engineering Buildcamp is project-driven.

You learn AI engineering by building.

15 projects you can build during the course 👇🏼

(You get lifetime access to the course if you sign up)

Media IDs: `4696a45c-7cda-4737-a07a-7b99c5f6d476`, `b534f9cf-c884-4015-a183-9c1bf597fe17`, `c7fba102-789a-4536-946d-dca6ccb9a75c`, `5b07c7ea-a777-4080-a563-1f74cdea0320`

#### Post 2

1. A running example project

A Documentation Agent that evolves throughout the course. It starts as a RAG system and gradually becomes an agent that is tested, monitored, and evaluated.

Media IDs: `eb0fdde6-55e5-4ca1-b83d-52adb11cd953`

#### Post 3

2. Capstone project

Your own AI application, built step by step during the course, from first RAG version to a more complete system with tools, testing, monitoring, evaluation, and deployment.

Media IDs: `57c3a5b3-70c3-45dc-875c-32f6a8b04b8e`

#### Post 4

Homework projects:

3. Document processing with AI. You download books, extract PDF text, chunk documents, and build a full RAG pipeline.

4. Wikipedia Agent. You implement search and page-fetching tools and build an agent using a framework of your choice.

5. Testing and evaluation through the DuckDB SQL Agent. You build an agent that queries NYC taxi data, write pytest tests, add LLM judges, and track costs.

6. Trivia Quizmaster Agent. You build an interactive trivia system and instrument it with Logfire.

7. Systematic evaluation through the Recipe Assistant Evaluation: You design 20+ evaluation scenarios, run batch tests, and detect hallucinations.

Media IDs: `71be8098-d089-4787-a34a-630684e9ca27`

#### Post 5

Optional projects:

8. FAQ Assistant: Add search integrations and turn it into a support chatbot.

9. YouTube Transcript Summarizer: A system that extracts summaries and chapter structure from YouTube videos using structured output.

10. PDF Book Processor: Similar tasks often appear in take-home assignments and interviews.

11. Web Search Agent: An agent that uses web search tools to find, filter, and synthesize information from the internet.

12. YouTube Researcher: An agent that searches YouTube, fetches transcripts, and produces structured research summaries.

13. Coding Agent: A fully functional coding agent that scaffolds Django applications.

14. Code Analysis Agent: An agent for analyzing and understanding codebases.

15. Deep Research Agent: A multi-stage research system that starts with broad search, expands into follow-up queries, goes deeper into promising directions, fact-checks findings, and generates a final article.

Media IDs: `00552bbc-b84d-4f5f-86a6-de226546ab13`

#### Post 6

So you follow one evolving system, practice on separate mini-projects, explore other examples, and build something of your own in parallel.

That is the core of Buildcamp.

The course starts in less than 5 days. You can sign up for the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `2ba2b04c-c5c7-4ad0-9500-8be11d600763`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7447901178874769408

AI Engineering Buildcamp is project-driven. You learn AI engineering by building.

15 projects you can build during the course 👇🏼

(You get lifetime access to the course if you sign up)

1. A running example project

A Documentation Agent that evolves throughout the course. It starts as a RAG system and gradually becomes an agent that is tested, monitored, and evaluated.

2. Capstone project

Your own AI application, built step by step during the course, from first RAG version to a more complete system with tools, testing, monitoring, evaluation, and deployment.

Homework projects:

3. Document processing with AI. You download books, extract PDF text, chunk documents, and build a full RAG pipeline.

4. Wikipedia Agent. You implement search and page-fetching tools and build an agent using a framework of your choice.

5. Testing and evaluation through the DuckDB SQL Agent. You build an agent that queries NYC taxi data, write pytest tests, add LLM judges, and track costs.

6. Trivia Quizmaster Agent. You build an interactive trivia system and instrument it with Logfire.

7. Systematic evaluation through the Recipe Assistant Evaluation: You design 20+ evaluation scenarios, run batch tests, and detect hallucinations.

Optional projects:

8. FAQ Assistant: Add search integrations and turn it into a support chatbot.

9. YouTube Transcript Summarizer: A system that extracts summaries and chapter structure from YouTube videos using structured output.

10. PDF Book Processor: Similar tasks often appear in take-home assignments and interviews.

11. Web Search Agent: An agent that uses web search tools to find, filter, and synthesize information from the internet.

12. YouTube Researcher: An agent that searches YouTube, fetches transcripts, and produces structured research summaries.

13. Coding Agent: A fully functional coding agent that scaffolds Django applications.

14. Code Analysis Agent: An agent for analyzing and understanding codebases.

15. Deep Research Agent: A multi-stage research system that starts with broad search, expands into follow-up queries, goes deeper into promising directions, fact-checks findings, and generates a final article.

So you follow one evolving system, practice on separate mini-projects, explore other examples, and build something of your own in parallel.

That is the core of Buildcamp.

The course starts in less than 5 days. You can sign up for the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `eb0fdde6-55e5-4ca1-b83d-52adb11cd953`, `57c3a5b3-70c3-45dc-875c-32f6a8b04b8e`, `71be8098-d089-4787-a34a-630684e9ca27`, `00552bbc-b84d-4f5f-86a6-de226546ab13`, `2ba2b04c-c5c7-4ad0-9500-8be11d600763`

## AI Engineering Buildcamp Schedule

- Typefully ID: `8627082`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:56:16.766Z
- Updated: 2026-04-08T10:27:36.993Z
- Scheduled: 2026-04-08T17:00:00Z
- Published: 2026-04-08T17:00:16.081Z
- Typefully URL: https://typefully.com/?d=8627082&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2041924093906448752

People ask about the weekly schedule for AI Engineering Buildcamp.

It's designed for people with full-time jobs: structured, but flexible enough to fit around work.

Here's how much time you'll spend:

The course lasts 9 weeks.

1. Live session - 1 hour per week

We meet for office hours where you can ask technical questions, discuss architecture decisions, and get feedback on your projects.

All sessions are recorded. A written summary is shared a few days later.

2. Async content and homework - 3 to 10 hours per week

Each week includes pre-recorded lessons, practical exercises, and homework. The time depends on your background and pace.

3. Capstone project - ongoing throughout the course

You work on your own AI application from week 1. Each module adds a new layer: RAG, then agentic tools, then testing, monitoring, and evaluation.

By week 6, you'll have a working system. Weeks 7-9 are for polishing, extending, and presenting.

This is not a passive course. It's for people who want to spend real time building and debugging, not just watching and taking notes.

The next cohort starts in less than a week: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `8e7ee732-7aaa-4019-977f-0f2452c8ddb6`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7447689785038548992

People ask about the weekly schedule for AI Engineering Buildcamp.

It's designed for people with full-time jobs: structured, but flexible enough to fit around work.

Here's how much time you'll spend:

The course lasts 9 weeks.

1. Live session - 1 hour per week

We meet for office hours where you can ask technical questions, discuss architecture decisions, and get feedback on your projects.

All sessions are recorded. A written summary is shared a few days later.

2. Async content and homework - 3 to 10 hours per week

Each week includes pre-recorded lessons, practical exercises, and homework. The time depends on your background and pace.

3. Capstone project - ongoing throughout the course

You work on your own AI application from week 1. Each module adds a new layer: RAG, then agentic tools, then testing, monitoring, and evaluation.

By week 6, you'll have a working system. Weeks 7-9 are for polishing, extending, and presenting.

This is not a passive course. It's for people who want to spend real time building and debugging, not just watching and taking notes.

The next cohort starts in less than a week: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `2faa0dcc-996b-4e71-b6a7-270ed6f6597a`

## AI Engineering Buildcamp Update

- Typefully ID: `8587026`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-02T14:11:28.503Z
- Updated: 2026-04-07T09:50:14.525Z
- Scheduled: 2026-04-12T07:00:00Z
- Published: 2026-04-12T07:00:17.046Z
- Typefully URL: https://typefully.com/?d=8587026&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2043222654132621595

The next cohort of the AI Engineering Buildcamp starts tomorrow.

After it concludes, I do not plan to run another cohort in the nearest future. 

So, if you've been thinking about joining, this cohort might be the right time.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents/

Media IDs: `5a91756d-2f62-4ea6-b968-ea97211fe030`, `fec3abf4-aea9-40ad-8cdc-d7c40f72d948`, `a45d51e0-2cea-4529-8a51-a09d0cb588e0`, `d46d3d25-aeb4-4f73-b9c0-c4100d9cbf02`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7448988346338508801

The next cohort of the AI Engineering Buildcamp starts tomorrow.

After it concludes, I do not plan to run another cohort in the nearest future. 

So, if you've been thinking about joining, this cohort might be the right time.

Enroll here: https://maven.com/alexey-grigorev/from-rag-to-agents/

Media IDs: `5a91756d-2f62-4ea6-b968-ea97211fe030`, `fec3abf4-aea9-40ad-8cdc-d7c40f72d948`, `a45d51e0-2cea-4529-8a51-a09d0cb588e0`, `d46d3d25-aeb4-4f73-b9c0-c4100d9cbf02`

## AI Engineering Buildcamp Update

- Typefully ID: `8575880`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-01T16:02:44.480Z
- Updated: 2026-04-07T09:48:01.388Z
- Scheduled: 2026-04-07T14:00:00Z
- Published: 2026-04-07T14:00:21.262Z
- Typefully URL: https://typefully.com/?d=8575880&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2041516428931817780

A few people have been asking about the next cohort of the AI Engineering Buildcamp.

I'm not planning another one right now.

After this April cohort wraps up, I'm taking a break from the course to focus on AI Shipping Labs.

If you've been thinking about joining, don't wait. I'm not sure when the next cohort will happen.

You can still register here: https://maven.com/alexey-grigorev/from-rag-to-agents/

The registration closes on April 13.

Media IDs: `45a40f2a-bf80-4c09-a9c1-2463ad9647b6`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7447282115655704578

A few people have been asking about the next cohort of the AI Engineering Buildcamp.

I'm not planning another one right now.

After this April cohort wraps up, I'm taking a break from the course to focus on AI Shipping Labs.

If you've been thinking about joining, don't wait. I'm not sure when the next cohort will happen.

You can still register here: https://maven.com/alexey-grigorev/from-rag-to-agents/

The registration closes on April 13.

Media IDs: `45a40f2a-bf80-4c09-a9c1-2463ad9647b6`

## AI Engineering Buildcamp Demo Day, Cohort 2

- Typefully ID: `8627079`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:55:30.037Z
- Updated: 2026-04-07T09:43:37.436Z
- Scheduled: 2026-04-11T07:00:00Z
- Published: 2026-04-11T07:00:12.290Z
- Typefully URL: https://typefully.com/?d=8627079&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2042860246889304304

Want to see what people actually build in the AI Engineering Buildcamp?

On April 14 (Tue) at 5:00 PM CET, participants will present their projects.

Over the past weeks, they've been building real AI systems:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Many projects combine RAG pipelines with agentic workflows. Students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

This is a good way to understand what the course covers and what you can build after completing it.

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `44f3909f-da06-46b5-8410-99ebc9e7f3e6`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7448625940060045312

Want to see what people actually build in the AI Engineering Buildcamp?

On April 14 (Tue) at 5:00 PM CET, participants will present their projects.

Over the past weeks, they've been building real AI systems:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Many projects combine RAG pipelines with agentic workflows. Students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

This is a good way to understand what the course covers and what you can build after completing it.

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `44f3909f-da06-46b5-8410-99ebc9e7f3e6`

## Get Sponsored for Buildcamp

- Typefully ID: `8627120`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:59:45.319Z
- Updated: 2026-04-06T08:29:53.520Z
- Scheduled: 2026-04-06T14:00:00Z
- Published: 2026-04-06T14:00:33.989Z
- Typefully URL: https://typefully.com/?d=8627120&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2041154082757640517

#### Post 1

Want to join the AI Engineering Buildcamp but worried about the cost?

Ask your employer to pay for it.

Many companies have learning budgets that cover exactly this kind of training.

Several participants in previous cohorts had their company sponsor them.

Maven works with companies directly. After you enroll, you get a receipt you can submit for reimbursement. You also get a certificate of completion at the end.

If your company needs an invoice or has questions, reach out and I'll help sort it out.

1/2

Media IDs: `03282df0-31d0-40e4-813e-3660b7d481c4`, `73ccec43-2fb0-418d-bb6c-4cce3e295518`

#### Post 2

Not sure how to ask?

- I wrote a short guide with an email template you can use: https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp
- Maven also has their own guide here: https://maven.com/expense

The course starts April 13. Details and syllabus: https://maven.com/alexey-grigorev/from-rag-to-agents

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7446919760446902272

Want to join the AI Engineering Buildcamp but worried about the cost?

Ask your employer to pay for it.

Many companies have learning budgets that cover exactly this kind of training.

Several participants in previous cohorts had their company sponsor them.

Maven works with companies directly. After you enroll, you get a receipt you can submit for reimbursement. You also get a certificate of completion at the end.

If your company needs an invoice or has questions, reach out and I'll help sort it out.

Not sure how to ask?

- I wrote a short guide with an email template you can use: https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp
- Maven also has their own guide here: https://maven.com/expense

The course starts April 13. Details and syllabus: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `03282df0-31d0-40e4-813e-3660b7d481c4`, `73ccec43-2fb0-418d-bb6c-4cce3e295518`

## AI Agents' Skills: GitHub Fetch

- Typefully ID: `8627108`
- Status: draft
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-04-06T07:58:44.466Z
- Updated: 2026-04-06T07:58:44.416Z
- Typefully URL: https://typefully.com/?d=8627108&a=188312

### x

#### Post 1

What are skills in AI agents?

In one of the workshops, I demo a GitHub Fetch skill.

The task seems simple: retrieve files from a GitHub repository. But without this skill, the agent must guess how to:

- Interact with GitHub
- Choose the right commands
- Navigate the repository structure

A skill provides a reusable set of instructions that guides the agent through tasks step by step.

Specifically, the GitHub Fetch skill instructs the agent on:

- Using the gh CLI
- Listing repository contents
- Navigating directories
- Downloading specific files

With these validated instructions, skills minimize reasoning errors by encoding operational knowledge.

In the demo, we used this skill to fetch two commands from a GitHub repo:

- /kid generates a wild project idea
- /parent implements it as code

These commands are stored in GitHub, and the agent uses the GitHub Fetch skill to automatically retrieve them.

Skills offer benefits like:

- Making behavior predictable
- Avoiding repeated prompts
- Reusing hard-won instructions
- Scaling beyond one-off demos

Media IDs: `1d1ce0eb-a069-48c1-bc90-913195a1d71d`

#### Post 2

I teach how to build production-ready AI agents in my AI Bootcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

The next cohort starts tomorrow: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

What are skills in AI agents?

In one of the workshops, I demo a GitHub Fetch skill.

The task seems simple: retrieve files from a GitHub repository. But without this skill, the agent must guess how to:

- Interact with GitHub
- Choose the right commands
- Navigate the repository structure

A skill provides a reusable set of instructions that guides the agent through tasks step by step.

Specifically, the GitHub Fetch skill instructs the agent on:

- Using the gh CLI
- Listing repository contents
- Navigating directories
- Downloading specific files

With these validated instructions, skills minimize reasoning errors by encoding operational knowledge.

In the demo, we used this skill to fetch two commands from a GitHub repo:

- /kid generates a wild project idea
- /parent implements it as code

These commands are stored in GitHub, and the agent uses the GitHub Fetch skill to automatically retrieve them.

Skills offer benefits like:

- Making behavior predictable
- Avoiding repeated prompts
- Reusing hard-won instructions
- Scaling beyond one-off demos

I teach how to build production-ready AI agents in my AI Bootcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

The next cohort starts tomorrow: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `b76d947d-a84c-4cd2-b7af-a1fb4c5c6d1e`

## Agents: Skills vs Commands

- Typefully ID: `8627103`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:58:12.366Z
- Updated: 2026-04-06T07:58:12.315Z
- Typefully URL: https://typefully.com/?d=8627103&a=188312

### x

#### Post 1

When building agents, what is the difference between skills and commands?
They look similar, but they serve different roles.

1. Commands are explicit. You can think of them as user-driven shortcuts

🔸 The user knows exactly what should happen
🔸 The user triggers it directly, for example /kit
🔸 The agent simply executes the instruction

2. Skills are implicit

🔸 The user describes a task in natural language
🔸 The agent decides whether a skill applies
🔸 The agent loads and uses the skill autonomously

The user never says, "Use this skill"

Skills encode operational knowledge. They tell the agent how to do something, so it doesn't have to guess.

3. The key distinction is who makes the decision:

🔸 Commands: the user decides
🔸 Skills: the agent decides

Commands are best when the intent is precise.

Skills are better when you want reusable, predictable agent behavior across tasks and projects.

If you want to go deeper, I've shared a free workshop on implementing skills from scratch:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

Media IDs: `a3c0bd25-d83d-42b0-af68-46e685465d75`

#### Post 2

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

When building agents, what is the difference between skills and commands?
They look similar, but they serve different roles.

1. Commands are explicit. You can think of them as user-driven shortcuts

🔸 The user knows exactly what should happen
🔸 The user triggers it directly, for example /kit
🔸 The agent simply executes the instruction

2. Skills are implicit

🔸 The user describes a task in natural language
🔸 The agent decides whether a skill applies
🔸 The agent loads and uses the skill autonomously

The user never says, "Use this skill"

Skills encode operational knowledge. They tell the agent how to do something, so it doesn't have to guess.

3. The key distinction is who makes the decision:

🔸 Commands: the user decides
🔸 Skills: the agent decides

Commands are best when the intent is precise.

Skills are better when you want reusable, predictable agent behavior across tasks and projects.

If you want to go deeper, I've shared a free workshop on implementing skills from scratch:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up. Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `6dad6722-fdd2-43e1-a459-0ed17befd889`

## Guardrails for AI

- Typefully ID: `8627100`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:58:01.140Z
- Updated: 2026-04-06T07:58:01.100Z
- Typefully URL: https://typefully.com/?d=8627100&a=188312

### x

What are guardrails for AI agents?
Here's a simple way to think about them:

1. What are guardrails?

Guardrails are mechanisms that control how the model reacts to user input and what the user ultimately sees.

2. Why are guardrails important?

An agent will try to be helpful, even when it shouldn't.

For example, imagine an agent built to answer questions about a course.

Without guardrails:
🔸 A student can ask for pizza recipes
🔸 The agent will try to answer
🔸 You spend tokens and money on completely off-topic requests

Guardrails prevent this.

They let you define what is allowed and what is not, before or after the model responds.

3. In practice, guardrails help you:

🔸 Block off-topic questions early
🔸 Refuse requests you don't want to support
🔸 Avoid unsafe or inappropriate outputs
🔸 Save money by stopping useless calls

You decide what the agent is for. Guardrails enforce that decision.

Once agents are exposed to real users, guardrails stop being optional. They become part of the system design.

I walk through this step by step in a free workshop:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `869c0f4b-98b9-4997-8280-bfb3c999efd1`

### linkedin

What are guardrails for AI agents?
Here's a simple way to think about them:

1. What are guardrails?

Guardrails are mechanisms that control how the model reacts to user input and what the user ultimately sees.

2. Why are guardrails important?

An agent will try to be helpful, even when it shouldn't.

For example, imagine an agent built to answer questions about a course.

Without guardrails:
🔸 A student can ask for pizza recipes
🔸 The agent will try to answer
🔸 You spend tokens and money on completely off-topic requests

Guardrails prevent this.

They let you define what is allowed and what is not, before or after the model responds.

3. In practice, guardrails help you:

🔸 Block off-topic questions early
🔸 Refuse requests you don't want to support
🔸 Avoid unsafe or inappropriate outputs
🔸 Save money by stopping useless calls

You decide what the agent is for. Guardrails enforce that decision.

Once agents are exposed to real users, guardrails stop being optional. They become part of the system design.

I walk through this step by step in a free workshop:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `850d9a8b-019a-4b21-8536-55535531399e`

## AI Agent Architecture Essentials (from workshop)

- Typefully ID: `8627096`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:57:40.667Z
- Updated: 2026-04-06T07:57:40.616Z
- Typefully URL: https://typefully.com/?d=8627096&a=188312

### x

#### Post 1

4 key components of AI agent architecture in its simplest form:

1. Brain: The LLM. It reasons, plans, and decides what to do next.

2. Instructions: The system prompt. It defines the agent's role, boundaries, and behavior.

3. Tools: Functions the agent can call to interact with the world:
reading files, writing code, running commands, searching data.

4. Memory: The conversation history and tool results that provide context across steps.

How this works together is what people call the agentic loop:

🔸 The user gives a task
🔸 The agent reasons based on instructions and memory
🔸 It decides to respond or call a tool
🔸 Tool results are added to memory
🔸 The loop continues until the task is complete

The agent decides when to stop.

Once you see this loop clearly, agent frameworks become much easier to reason about. They're mostly different ways of wiring these same components together.

If you want a hands-on walkthrough of this architecture, I've shared free workshop materials.

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

Media IDs: `34f8af52-df6d-4ff1-8058-921ec526a601`

#### Post 2

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

4 key components of AI agent architecture in its simplest form:

1. Brain: The LLM. It reasons, plans, and decides what to do next.

2. Instructions: The system prompt. It defines the agent's role, boundaries, and behavior.

3. Tools: Functions the agent can call to interact with the world:
reading files, writing code, running commands, searching data.

4. Memory: The conversation history and tool results that provide context across steps.

How this works together is what people call the agentic loop:

🔸 The user gives a task
🔸 The agent reasons based on instructions and memory
🔸 It decides to respond or call a tool
🔸 Tool results are added to memory
🔸 The loop continues until the task is complete

The agent decides when to stop.

Once you see this loop clearly, agent frameworks become much easier to reason about. They're mostly different ways of wiring these same components together.

If you want a hands-on walkthrough of this architecture, I've shared free workshop materials.

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `5a35276a-e0c8-4eb1-9641-e5f7d6a9c9e0`

## Building Safe AI Agents

- Typefully ID: `8627095`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:57:34.563Z
- Updated: 2026-04-06T07:57:34.520Z
- Typefully URL: https://typefully.com/?d=8627095&a=188312

### x

#### Post 1

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large FAQ for a Data Engineering course hosted on GitHub: 300+ questions, written by students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

Media IDs: `9a83b90d-6b29-4668-be25-f68580928f18`

#### Post 2

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large FAQ for a Data Engineering course hosted on GitHub: 300+ questions, written by students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `c2864c0b-d8ae-4c72-983c-8bb4512a4805`

## Coding Agent Guide

- Typefully ID: `8627088`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:57:03.601Z
- Updated: 2026-04-06T07:57:03.511Z
- Typefully URL: https://typefully.com/?d=8627088&a=188312

### x

#### Post 1

Developer cheatsheet to turn a chatbot into a coding agent:

1) Chatbot vs agent decision

Decide upfront whether you actually need an agent. Agents are only worth it when you need actions like file I/O, code execution, or search.

2) Tool schema definition

Define concrete tools with strict schemas describing names, parameters, and constraints, and expose only what the agent should be allowed to do.

3) Tool execution loop

Implement a loop where the model proposes tool calls, your system executes them, and the results are fed back into the conversation state.

4) Project-scoped editing tools

Provide file and shell access scoped to a project root, with guardrails to prevent unsafe commands and accidental damage.

5) Project template scaffolding

Start each run from a clean template copied into a fresh directory so all agent edits remain isolated and reproducible.

6) System prompt as documentation

Use the system prompt to document the tech stack, file structure, and rules, and require the model to plan before acting.

Use this as a checklist when building a tool-using coding agent on top of your preferred stack and LLM API.

Want a detailed step-by-step tutorial? Download my guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `1c5f8ad8-0c66-4d55-85c4-f8ef540c07ad`

#### Post 2

Learn to build AI agents and apply new knowledge to create 8+ projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Developer cheatsheet to turn a chatbot into a coding agent:

1) Chatbot vs agent decision

Decide upfront whether you actually need an agent. Agents are only worth it when you need actions like file I/O, code execution, or search.

2) Tool schema definition

Define concrete tools with strict schemas describing names, parameters, and constraints, and expose only what the agent should be allowed to do.

3) Tool execution loop

Implement a loop where the model proposes tool calls, your system executes them, and the results are fed back into the conversation state.

4) Project-scoped editing tools

Provide file and shell access scoped to a project root, with guardrails to prevent unsafe commands and accidental damage.

5) Project template scaffolding

Start each run from a clean template copied into a fresh directory so all agent edits remain isolated and reproducible.

6) System prompt as documentation

Use the system prompt to document the tech stack, file structure, and rules, and require the model to plan before acting.

Use this as a checklist when building a tool-using coding agent on top of your preferred stack and LLM API.

Want a detailed step-by-step tutorial? Download my guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Learn to build AI agents and apply new knowledge to create 8+ projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `4f7e7861-ad06-41d9-87d2-8afc146fac02`

## Connecting AI Agents to Tools

- Typefully ID: `8627087`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:56:49.075Z
- Updated: 2026-04-06T07:56:49.021Z
- Typefully URL: https://typefully.com/?d=8627087&a=188312

### x

#### Post 1

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

Media IDs: `673b6195-8cbb-4517-9da5-9268699d19c5`

#### Post 2

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `796d0c09-2db0-4063-be81-7a0560721b5e`

## AI Engineering Buildcamp Promo Code

- Typefully ID: `8627085`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:56:37.306Z
- Updated: 2026-04-06T07:56:37.257Z
- Typefully URL: https://typefully.com/?d=8627085&a=188312

### x

#### Post 1

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

If you want to join early, use EARLYBIRD for 30% off.

The code is valid for the next 3 days, then I close the promo.

Details + enrollment: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `8184a2b4-ac03-47b3-98f9-2f52ee7867c7`

#### Post 2

You can read more about what the course will teach you here:

### linkedin

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

3 people joined just last week.

If you want to join early, use EARLYBIRD for 30% off.

The code is valid for the next 3 days, then I close the promo.

Details + enrollment: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `52614992-be0c-4465-9d4c-3c0208cabf29`

## AI Engineering Buildcamp Overview

- Typefully ID: `8627083`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-04-06T07:56:24.656Z
- Updated: 2026-04-06T07:56:24.604Z
- Typefully URL: https://typefully.com/?d=8627083&a=188312

### x

What does AI Engineering Buildcamp cover?

It'll teach you to build and ship your own agentic AI assistant, from first prompt to production-ready system:

1. Foundations: LLMs and RAG

We start with core concepts and move quickly into implementation.

You learn how to:

🔸 Work with LLM APIs
🔸 Build retrieval-augmented generation pipelines
🔸 Process and structure real data

Outcome: a working RAG system built on your own dataset.

2. Agentic Flows and Tool Use

Next, we move beyond chat.

You implement:

🔸 Function calling
🔸 Tool integration with structured schemas
🔸 Agent orchestration with libraries like PydanticAI and Agents SDK
🔸 Tool exposure via MCP

Outcome: a capable, tool-using agent that can take actions, not just generate text.

3. Testing and Evaluation

Most AI demos stop at “it works.”

We focus on making it measurable.

You learn how to:

🔸 Build structured evaluation datasets
🔸 Compare approaches using LLMs as judges
🔸 Run offline evaluation
🔸 Use tools like Evidently and LangWatch

Outcome: a tested and benchmarked assistant.

4. Monitoring and Guardrails

Production systems require observability and safety.

You implement:

🔸 Real-time monitoring with Grafana
🔸 Structured logging with Pydantic Logfire
🔸 OpenTelemetry instrumentation
🔸 Guardrails and safety mechanisms

Outcome: a monitored system you can operate with confidence.

5. Applied Use Cases

You build concrete agents, including:

🔸 A website generator
🔸 A code reviewer

You also explore additional real-world scenarios to understand architectural trade-offs.

6. Capstone and Hackathon

Everything comes together.

You build a complete end-to-end AI application using your own data.

Then you apply the stack in a hackathon setting, solving real problems collaboratively.

Outcome: a portfolio-ready project that demonstrates real AI engineering skills.

By the end of the Buildcamp, you will:

🔸 Build, evaluate, and monitor an AI assistant
🔸 Create research and coding agents
🔸 Understand the full lifecycle from prototype to production
🔸 Have a concrete project to show in interviews

Join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `6638ec7d-8fd8-46bd-8774-b2bc010e921e`

### linkedin

What does AI Engineering Buildcamp cover?

It'll teach you to build and ship your own agentic AI assistant, from first prompt to production-ready system:

1. Foundations: LLMs and RAG

We start with core concepts and move quickly into implementation.

You learn how to:

🔸 Work with LLM APIs
🔸 Build retrieval-augmented generation pipelines
🔸 Process and structure real data

Outcome: a working RAG system built on your own dataset.

2. Agentic Flows and Tool Use

Next, we move beyond chat.

You implement:

🔸 Function calling
🔸 Tool integration with structured schemas
🔸 Agent orchestration with libraries like PydanticAI and Agents SDK
🔸 Tool exposure via MCP

Outcome: a capable, tool-using agent that can take actions, not just generate text.

3. Testing and Evaluation

Most AI demos stop at “it works.”

We focus on making it measurable.

You learn how to:

🔸 Build structured evaluation datasets
🔸 Compare approaches using LLMs as judges
🔸 Run offline evaluation
🔸 Use tools like Evidently and LangWatch

Outcome: a tested and benchmarked assistant.

4. Monitoring and Guardrails

Production systems require observability and safety.

You implement:

🔸 Real-time monitoring with Grafana
🔸 Structured logging with Pydantic Logfire
🔸 OpenTelemetry instrumentation
🔸 Guardrails and safety mechanisms

Outcome: a monitored system you can operate with confidence.

5. Applied Use Cases

You build concrete agents, including:

🔸 A website generator
🔸 A code reviewer

You also explore additional real-world scenarios to understand architectural trade-offs.

6. Capstone and Hackathon

Everything comes together.

You build a complete end-to-end AI application using your own data.

Then you apply the stack in a hackathon setting, solving real problems collaboratively.

Outcome: a portfolio-ready project that demonstrates real AI engineering skills.

By the end of the Buildcamp, you will:

🔸 Build, evaluate, and monitor an AI assistant
🔸 Create research and coding agents
🔸 Understand the full lifecycle from prototype to production
🔸 Have a concrete project to show in interviews

Join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `02d00a7f-252c-4405-9ffd-7f71e5abee2c`

## AI Engineering Buildcamp Demo Day, Cohort 2

- Typefully ID: `8402687`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-17T13:31:32.508Z
- Updated: 2026-04-02T13:12:13.534Z
- Scheduled: 2026-04-03T07:00:00Z
- Published: 2026-04-03T07:00:11.966Z
- Typefully URL: https://typefully.com/?d=8402687&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2039961142534316295

On April 14, I'll be hosting the AI Engineering Buildcamp Demo Day Cohort 2.

AI Engineering Buildcamp course participants will present the AI systems they built during the program.

Date: April 14
Time: 5:00 PM CET
Format: Virtual (Zoom)

Over the past weeks, participants have been building real AI applications.

Many of the projects combine RAG pipelines with agentic workflows, and students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

You'll see projects like:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `a85ef71e-cb35-45b5-b58e-54cee8021ab0`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7445726830700965888

On April 14, I'll be hosting the AI Engineering Buildcamp Demo Day Cohort 2.

AI Engineering Buildcamp course participants will present the AI systems they built during the program.

Date: April 14
Time: 5:00 PM CET
Format: Virtual (Zoom)

Over the past weeks, participants have been building real AI applications.

Many of the projects combine RAG pipelines with agentic workflows, and students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

You'll see projects like:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `a85ef71e-cb35-45b5-b58e-54cee8021ab0`

## AI Engineering Buildcamp - Use Your Company Learning Budget

- Typefully ID: `8401902`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-17T12:37:54.576Z
- Updated: 2026-03-17T15:01:20.785Z
- Scheduled: 2026-03-26T08:00:00Z
- Published: 2026-03-26T08:00:10.077Z
- Typefully URL: https://typefully.com/?d=8401902&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2037077131239580099

If you're thinking about joining the AI Engineering Buildcamp, don't hesitate to ask your employer to cover the cost.

Many companies are willing to pay for training, especially when it directly helps employees improve skills they use at work.

For example, I recently received this message from a person whose company sponsor their participation:

"I managed to get it covered by my company. They are asking for an invoice so they can proceed with the payment."

If your company needs an invoice, just let me know, I'm happy to prepare one.

If you're not sure how to ask your employer for a learning budget, I put together a short guide: https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp

Media IDs: `f085bc91-6496-4eb4-9e37-29c3946f4fd1`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7442842821662920704

If you're thinking about joining the AI Engineering Buildcamp, don't hesitate to ask your employer to cover the cost.

Many companies are willing to pay for training, especially when it directly helps employees improve skills they use at work.

For example, I recently received this message from a person whose company sponsor their participation:

"I managed to get it covered by my company. They are asking for an invoice so they can proceed with the payment."

If your company needs an invoice, just let me know, I'm happy to prepare one.

If you're not sure how to ask your employer for a learning budget, I put together a short guide: https://aishippinglabs.com/blog/how-to-join-ai-engineering-buildcamp

Media IDs: `f085bc91-6496-4eb4-9e37-29c3946f4fd1`

## AI Engineering Buildcamp Scholarships

- Typefully ID: `8247567`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-02T15:49:02.504Z
- Updated: 2026-03-17T14:54:39.195Z
- Scheduled: 2026-03-30T07:00:00Z
- Published: 2026-03-30T07:00:15.710Z
- Typefully URL: https://typefully.com/?d=8247567&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2038511606418850138

Last chance to apply for an AI Engineering Buildcamp scholarship.

The course is $1,799, and I'm offering both full and partial scholarships.

Applications close tomorrow. I'll reach out to selected participants by Monday.

Haven't applied yet? https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

Learn more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents/

Media IDs: `a4861335-a782-4ad4-a53f-897ce0e3f901`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7444277297643298816

Last chance to apply for an AI Engineering Buildcamp scholarship.

The course is $1,799, and I'm offering both full and partial scholarships.

Applications close tomorrow. I'll reach out to selected participants by Monday.

Haven't applied yet? https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

Learn more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents/

Media IDs: `a4861335-a782-4ad4-a53f-897ce0e3f901`

## AI Engineering Buildcamp Demo Day, Cohort 2

- Typefully ID: `8402607`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-17T13:26:17.912Z
- Updated: 2026-03-17T13:32:28.632Z
- Scheduled: 2026-03-24T15:00:00Z
- Published: 2026-03-24T15:00:23.205Z
- Typefully URL: https://typefully.com/?d=8402607&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2036458106528604273

On April 14, I'll be hosting the AI Engineering Buildcamp Demo Day Cohort 2.

AI Engineering Buildcamp course participants will present the AI systems they built during the program.

Date: April 14
Time: 5:00 PM CET
Format: Virtual (Zoom)

Over the past weeks, participants have been building real AI applications.

Many of the projects combine RAG pipelines with agentic workflows, and students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

You'll see projects like:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `116af6b4-f89e-41f0-8a38-4e4b7324a67b`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7442223813842460673

On April 14, I'll be hosting the AI Engineering Buildcamp Demo Day Cohort 2.

AI Engineering Buildcamp course participants will present the AI systems they built during the program.

Date: April 14
Time: 5:00 PM CET
Format: Virtual (Zoom)

Over the past weeks, participants have been building real AI applications.

Many of the projects combine RAG pipelines with agentic workflows, and students had to think about the full engineering lifecycle: evaluation, monitoring, and reliability.

You'll see projects like:

- Coding assistants and developer tools
- Research and knowledge agents
- AI applications built on real datasets and workflows

Register here: https://maven.com/p/e76751/ai-engineering-buildcamp-demo-day-cohort-2

Media IDs: `b967eac1-b883-48a4-ba22-ae1fc93f357e`

## AI Engineering Buildcamp Scholarships

- Typefully ID: `8285258`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-06T09:41:23.410Z
- Updated: 2026-03-17T12:49:45.193Z
- Scheduled: 2026-03-25T08:00:00Z
- Published: 2026-03-25T08:00:11.291Z
- Typefully URL: https://typefully.com/?d=8285258&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2036714736369430547

#### Post 1

5 days left to apply for the AI Engineering Buildcamp scholarship.

I offer several full- and partial-scholarship spots.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

If you know someone who'd benefit, please share and tag them.

Media IDs: `d7a4d87f-ec2e-4f35-bd26-2083c43639be`

#### Post 2

The next cohort of the course starts on April 13.

It's live, hands-on, and focused on building production-ready AI agents step by step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7442480426805272576

5 days left to apply for the AI Engineering Buildcamp scholarship.

I offer several full- and partial-scholarship spots.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

If you know someone who'd benefit, please share and tag them.

The next cohort of the course starts on April 13.

It's live, hands-on, and focused on building production-ready AI agents step by step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `d7a4d87f-ec2e-4f35-bd26-2083c43639be`

## A Day of AI Engineer

- Typefully ID: `8202372`
- Status: published
- Tags: `ai-engineer`, `ai-engineering-buildcamp`
- Created: 2026-02-25T12:41:21.454Z
- Updated: 2026-03-17T12:31:46.410Z
- Scheduled: 2026-03-25T15:00:00Z
- Published: 2026-03-25T15:00:18.211Z
- Typefully URL: https://typefully.com/?d=8202372&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2036820461741637635

#### Post 1

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

Media IDs: `749fe96d-5fba-4e99-a8ed-cc1b926f2ac5`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7442586162340306944

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `59a83a3f-2725-4d2f-8764-d7f86086df83`

## A Day of AI Engineer

- Typefully ID: `8202340`
- Status: published
- Tags: `ai-engineering-buildcamp`, `ai-engineer`
- Created: 2026-02-25T12:36:46.385Z
- Updated: 2026-03-09T13:14:24.586Z
- Scheduled: 2026-03-11T15:00:00Z
- Published: 2026-03-11T15:00:45.930Z
- Typefully URL: https://typefully.com/?d=8202340&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2031747147876716601

#### Post 1

Can a data engineer transition into AI engineering?

Short answer: yes. And in many cases, faster than they think.

AI engineering is primarily an engineering role.

There is far less research and model training than people assume. In modern AI systems, the foundation model is usually an API call. The hard part is everything around it.

If you are a data engineer, you already have the core.

You know how to:

- Write tests
- Set up CI/CD
- Monitor pipelines
- Collect logs
- Follow solid engineering practices

The "flavor" changes, but the fundamentals stay the same.

Instead of data quality monitoring, you monitor AI behavior.
Instead of batch pipelines, you may manage RAG pipelines.
Instead of validating transformations, you evaluate model outputs.

But these are extensions of what you already do.

Media IDs: `fcdfb818-2308-461c-9719-1cc77ec341a5`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7437512746558025728

Can a data engineer transition into AI engineering?

Short answer: yes. And in many cases, faster than they think.

AI engineering is primarily an engineering role.

There is far less research and model training than people assume. In modern AI systems, the foundation model is usually an API call. The hard part is everything around it.

If you are a data engineer, you already have the core.

You know how to:

- Write tests
- Set up CI/CD
- Monitor pipelines
- Collect logs
- Follow solid engineering practices

The "flavor" changes, but the fundamentals stay the same.

Instead of data quality monitoring, you monitor AI behavior.
Instead of batch pipelines, you may manage RAG pipelines.
Instead of validating transformations, you evaluate model outputs.

But these are extensions of what you already do.

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `fcdfb818-2308-461c-9719-1cc77ec341a5`

## AI Engineering Buildcamp Schedule

- Typefully ID: `8202301`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-25T12:33:44.467Z
- Updated: 2026-03-09T13:14:14.791Z
- Scheduled: 2026-03-10T18:00:00Z
- Published: 2026-03-10T18:00:15.746Z
- Typefully URL: https://typefully.com/?d=8202301&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2031429943129981421

What does the weekly schedule of AI Engineering Buildcamp look like?

It is designed for working professionals. Structured, but flexible.

Here is how the time is distributed.

1. Live session
⏱ 1 hour per week

We meet once a week for office hours.

You can:

🔸 Ask technical questions
🔸 Clarify architectural decisions
🔸 Discuss your project
🔸 Dive deeper into tricky topics

All sessions are recorded.
A written summary is shared a few days later.

If you cannot attend live, you do not miss anything.

2. Async content and homework
⏱ 3 to 10 hours per week

Each week includes:

🔸 Pre-recorded lectures
🔸 Hands-on exercises
🔸 Structured homework

The time depends on your pace and background.

The focus is practical. You implement, test, iterate.

3. Final project
⏱ 10 to 20 hours per week

The capstone project runs throughout the course.

You progressively build an end-to-end AI application using what you learn each week.

By the end, you are not starting from scratch.
You are polishing and integrating components you have already built.

The effort increases toward the final weeks, but it is distributed across the entire duration.

In total, expect a meaningful time commitment.

This is not a passive course.

It is designed to simulate real AI engineering work:

🔸 Build
🔸 Evaluate
🔸 Monitor
🔸 Improve

You can join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `42f5aabf-9c4f-459c-a457-ed1be3bd7bfe`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7437195645901414400

What does the weekly schedule of AI Engineering Buildcamp look like?

It is designed for working professionals. Structured, but flexible.

Here is how the time is distributed.

1. Live session
⏱ 1 hour per week

We meet once a week for office hours.

You can:

🔸 Ask technical questions
🔸 Clarify architectural decisions
🔸 Discuss your project
🔸 Dive deeper into tricky topics

All sessions are recorded.
A written summary is shared a few days later.

If you cannot attend live, you do not miss anything.

2. Async content and homework
⏱ 3 to 10 hours per week

Each week includes:

🔸 Pre-recorded lectures
🔸 Hands-on exercises
🔸 Structured homework

The time depends on your pace and background.

The focus is practical. You implement, test, iterate.

3. Final project
⏱ 10 to 20 hours per week

The capstone project runs throughout the course.

You progressively build an end-to-end AI application using what you learn each week.

By the end, you are not starting from scratch.
You are polishing and integrating components you have already built.

The effort increases toward the final weeks, but it is distributed across the entire duration.

In total, expect a meaningful time commitment.

This is not a passive course.

It is designed to simulate real AI engineering work:

🔸 Build
🔸 Evaluate
🔸 Monitor
🔸 Improve

You can join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `2c4f4260-c811-4d3e-ad9d-e70af96186b3`

## AI Engineering Buildcamp Overview

- Typefully ID: `8202211`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-25T12:23:50.524Z
- Updated: 2026-03-06T09:54:29.479Z
- Scheduled: 2026-03-06T18:00:00Z
- Published: 2026-03-06T18:00:13.547Z
- Typefully URL: https://typefully.com/?d=8202211&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2029980382842753126

What does AI Engineering Buildcamp cover?

It'll teach you to build and ship your own agentic AI assistant, from first prompt to production-ready system:

1. Foundations: LLMs and RAG

We start with core concepts and move quickly into implementation.

You learn how to:

🔸 Work with LLM APIs
🔸 Build retrieval-augmented generation pipelines
🔸 Process and structure real data

Outcome: a working RAG system built on your own dataset.

2. Agentic Flows and Tool Use

Next, we move beyond chat.

You implement:

🔸 Function calling
🔸 Tool integration with structured schemas
🔸 Agent orchestration with libraries like PydanticAI and Agents SDK
🔸 Tool exposure via MCP

Outcome: a capable, tool-using agent that can take actions, not just generate text.

3. Testing and Evaluation

Most AI demos stop at “it works.”

We focus on making it measurable.

You learn how to:

🔸 Build structured evaluation datasets
🔸 Compare approaches using LLMs as judges
🔸 Run offline evaluation
🔸 Use tools like Evidently and LangWatch

Outcome: a tested and benchmarked assistant.

4. Monitoring and Guardrails

Production systems require observability and safety.

You implement:

🔸 Real-time monitoring with Grafana
🔸 Structured logging with Pydantic Logfire
🔸 OpenTelemetry instrumentation
🔸 Guardrails and safety mechanisms

Outcome: a monitored system you can operate with confidence.

5. Applied Use Cases

You build concrete agents, including:

🔸 A website generator
🔸 A code reviewer

You also explore additional real-world scenarios to understand architectural trade-offs.

6. Capstone and Hackathon

Everything comes together.

You build a complete end-to-end AI application using your own data.

Then you apply the stack in a hackathon setting, solving real problems collaboratively.

Outcome: a portfolio-ready project that demonstrates real AI engineering skills.

By the end of the Buildcamp, you will:

🔸 Build, evaluate, and monitor an AI assistant
🔸 Create research and coding agents
🔸 Understand the full lifecycle from prototype to production
🔸 Have a concrete project to show in interviews

Join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `278bfda5-48b6-47bc-bac1-59367faa3793`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7435746106350927874

What does AI Engineering Buildcamp cover?

It'll teach you to build and ship your own agentic AI assistant, from first prompt to production-ready system:

1. Foundations: LLMs and RAG

We start with core concepts and move quickly into implementation.

You learn how to:

🔸 Work with LLM APIs
🔸 Build retrieval-augmented generation pipelines
🔸 Process and structure real data

Outcome: a working RAG system built on your own dataset.

2. Agentic Flows and Tool Use

Next, we move beyond chat.

You implement:

🔸 Function calling
🔸 Tool integration with structured schemas
🔸 Agent orchestration with libraries like PydanticAI and Agents SDK
🔸 Tool exposure via MCP

Outcome: a capable, tool-using agent that can take actions, not just generate text.

3. Testing and Evaluation

Most AI demos stop at “it works.”

We focus on making it measurable.

You learn how to:

🔸 Build structured evaluation datasets
🔸 Compare approaches using LLMs as judges
🔸 Run offline evaluation
🔸 Use tools like Evidently and LangWatch

Outcome: a tested and benchmarked assistant.

4. Monitoring and Guardrails

Production systems require observability and safety.

You implement:

🔸 Real-time monitoring with Grafana
🔸 Structured logging with Pydantic Logfire
🔸 OpenTelemetry instrumentation
🔸 Guardrails and safety mechanisms

Outcome: a monitored system you can operate with confidence.

5. Applied Use Cases

You build concrete agents, including:

🔸 A website generator
🔸 A code reviewer

You also explore additional real-world scenarios to understand architectural trade-offs.

6. Capstone and Hackathon

Everything comes together.

You build a complete end-to-end AI application using your own data.

Then you apply the stack in a hackathon setting, solving real problems collaboratively.

Outcome: a portfolio-ready project that demonstrates real AI engineering skills.

By the end of the Buildcamp, you will:

🔸 Build, evaluate, and monitor an AI assistant
🔸 Create research and coding agents
🔸 Understand the full lifecycle from prototype to production
🔸 Have a concrete project to show in interviews

Join the next cohort here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `367e31dd-1467-4987-94f4-425a814b5aea`

## AI Engineering Buildcamp Scholarships Reminder

- Typefully ID: `8247553`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-02T15:46:37.781Z
- Updated: 2026-03-03T08:15:08.627Z
- Scheduled: 2026-03-11T08:00:00Z
- Published: 2026-03-11T08:00:09.907Z
- Typefully URL: https://typefully.com/?d=8247553&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2031641311783346211

Quick reminder: If you're interested in my next AI Engineering Buildcamp and haven't applied for a scholarship spot yet, now is your chance.

I understand that not everyone can afford a paid program, but many are highly motivated to learn and build.

This iteration includes several scholarship spots.

You can apply for a scholarship here: https://forms.gle/qAex9yTkZqypJMk67

Last time I shared this form, it spread widely, and I received thousands of applications, so don't wait too long.

🔸 Course starts: April 13, 2026
🔸 Format: Live, hands-on
🔸 Focus: Building production-ready AI agents, step by step

Application deadline: March 30, 2026

If you know someone who could benefit from a scholarship, please share this with them.

Media IDs: `3cb4974d-c6ca-49dc-a068-413cd08aba28`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7437407011371249665

Quick reminder: If you're interested in my next AI Engineering Buildcamp and haven't applied for a scholarship spot yet, now is your chance.

I understand that not everyone can afford a paid program, but many are highly motivated to learn and build.

This iteration includes several scholarship spots.

You can apply for a scholarship here: https://forms.gle/qAex9yTkZqypJMk67

Last time I shared this form, it spread widely, and I received thousands of applications, so don't wait too long.

🔸 Course starts: April 13, 2026
🔸 Format: Live, hands-on
🔸 Focus: Building production-ready AI agents, step by step

Application deadline: March 30, 2026

If you know someone who could benefit from a scholarship, please share this with them.

Media IDs: `3cb4974d-c6ca-49dc-a068-413cd08aba28`

## AI Engineering Buildcamp Scholarships

- Typefully ID: `8247440`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-02T15:33:57.828Z
- Updated: 2026-03-03T08:11:07.251Z
- Scheduled: 2026-03-04T08:00:00Z
- Published: 2026-03-04T08:00:12.246Z
- Typefully URL: https://typefully.com/?d=8247440&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2029104595310657923

#### Post 1

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

It's live, hands-on, and focused on building production-ready AI agents step by step.

As always, I offer several scholarship spots.

I understand that ot everyone has the budget for a paid program, but many are eager to learn, practice, and develop their skills.

I hope this makes the program more accessible to those who need it most.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

If you know someone who'd benefit, please share and tag them.

Media IDs: `dd111b6e-d60e-41dc-93a7-4f361ddee180`

#### Post 2

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7434870287529140224

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

It's live, hands-on, and focused on building production-ready AI agents step by step.

As always, I offer several scholarship spots.

I understand that ot everyone has the budget for a paid program, but many are eager to learn, practice, and develop their skills.

I hope this makes the program more accessible to those who need it most.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/qAex9yTkZqypJMk67

Application deadline: March 30, 2026

If you know someone who'd benefit, please share and tag them.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `dd111b6e-d60e-41dc-93a7-4f361ddee180`

## A Day of AI Engineer

- Typefully ID: `8202431`
- Status: published
- Tags: `ai-engineer`, `ai-engineering-buildcamp`
- Created: 2026-02-25T12:49:12.087Z
- Updated: 2026-03-02T15:32:26.394Z
- Scheduled: 2026-03-05T08:00:00Z
- Published: 2026-03-05T08:00:35.754Z
- Typefully URL: https://typefully.com/?d=8202431&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2029467081742467150

#### Post 1

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

Media IDs: `96ec46df-df63-45e8-82aa-49dc2a11ef6a`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7435232740121378816

How do I transition from Data engineer to AI engineer?
Here's a structured 6-step transition path:

You already have the hardest part: engineering fundamentals + production mindset.

The goal is to add the AI layer on top.

Step 1: Work inside an AI-flavored data pipeline

- Ingestion + cleaning for RAG / analytics
- Chunking, metadata, indexing
- Observability and data quality checks

Step 2: Learn how model providers work

- APIs, limits, retries, rate limits
- Latency and cost trade-offs
- Privacy and data handling constraints

Step 3: Prompting as an engineering discipline

- Prompt templates
- Versioning + change logs
- Structured outputs (JSON schemas)

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks (format, factuality signals, regressions)
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails (allowed tools, timeouts, fallbacks)
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

Examples:
- RAG assistant over internal docs
- Ticket triage bot with tool calls + evals

For an experienced data engineer, this is usually not a multi-year shift.

With focused effort + hands-on work, ~3-4 months can be enough to become interview-ready.

If you're making this transition, what part feels most unclear: evals, prompting, or agents?

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `d8971f29-eab1-44a2-869e-4410ac064699`

## AI Engineering Buildcamp Promo Code

- Typefully ID: `8247271`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-03-02T15:20:28.582Z
- Updated: 2026-03-02T15:32:01.420Z
- Scheduled: 2026-03-03T08:00:00Z
- Published: 2026-03-03T08:00:11.042Z
- Typefully URL: https://typefully.com/?d=8247271&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2028742202038575354

#### Post 1

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

If you want to join early, use EARLYBIRD for 30% off.

The code is valid for the next 3 days, then I close the promo.

Details + enrollment: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `69345e44-b961-4740-9411-6b54206baf55`

#### Post 2

You can read more about what the course will teach you here:

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7434507893368000512

The next cohort of my AI Engineering Buildcamp starts on Apr 13.

3 people joined just last week.

If you want to join early, use EARLYBIRD for 30% off.

The code is valid for the next 3 days, then I close the promo.

Details + enrollment: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `69345e44-b961-4740-9411-6b54206baf55`

## A Day of AI Engineer

- Typefully ID: `8202663`
- Status: published
- Tags: `ai-engineer`, `ai-engineering-buildcamp`
- Created: 2026-02-25T13:10:32.882Z
- Updated: 2026-02-25T13:27:43.432Z
- Scheduled: 2026-03-27T08:00:00Z
- Published: 2026-03-27T08:00:22.132Z
- Typefully URL: https://typefully.com/?d=8202663&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2037439539216892371

#### Post 1

How do you tell an AI hobbyist from an AI engineer?

The difference is about standards. An AI engineer follows engineering discipline.

That means:

- Writing proper tests
- Defining measurable evaluation criteria
- Monitoring performance and cost
- Collecting feedback
- Making data-driven decisions
- Designing for maintainability

A hobbyist can make something work.

An engineer makes it reliable.

For personal use, when you take on the AI hobbist role, you do not need:

- A comprehensive test suite
- Monitoring dashboards
- Structured evaluation pipelines
- Versioning and rollback strategies

You just run it. If it works, great. If not, you tweak it.

In a company setting, that is not enough.

When AI is integrated into a product, you need:

- Reproducibility
- Observability
- Clear evaluation
- Controlled iteration

Media IDs: `a6802755-7569-4b29-8786-077f7b68c190`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7443205227660435456

How do you tell an AI hobbyist from an AI engineer?

The difference is about standards. An AI engineer follows engineering discipline.

That means:

- Writing proper tests
- Defining measurable evaluation criteria
- Monitoring performance and cost
- Collecting feedback
- Making data-driven decisions
- Designing for maintainability

A hobbyist can make something work.

An engineer makes it reliable.

For personal use, when you take on the AI hobbist role, you do not need:

- A comprehensive test suite
- Monitoring dashboards
- Structured evaluation pipelines
- Versioning and rollback strategies

You just run it. If it works, great. If not, you tweak it.

In a company setting, that is not enough.

When AI is integrated into a product, you need:

- Reproducibility
- Observability
- Clear evaluation
- Controlled iteration

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `7653eda7-c1f8-4f1e-a158-e49433d52f0e`

## A Day of AI Engineer

- Typefully ID: `8202436`
- Status: published
- Tags: `ai-engineering-buildcamp`, `ai-engineer`
- Created: 2026-02-25T12:49:45.724Z
- Updated: 2026-02-25T13:09:27.644Z
- Scheduled: 2026-03-24T08:00:00Z
- Published: 2026-03-24T08:00:08.442Z
- Typefully URL: https://typefully.com/?d=8202436&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2036352336675922131

#### Post 1

Can a data engineer transition into AI engineering?

Short answer: yes. And in many cases, faster than they think.

AI engineering is primarily an engineering role.

There is far less research and model training than people assume. In modern AI systems, the foundation model is usually an API call. The hard part is everything around it.

If you are a data engineer, you already have the core.

You know how to:

- Write tests
- Set up CI/CD
- Monitor pipelines
- Collect logs
- Follow solid engineering practices

The "flavor" changes, but the fundamentals stay the same.

Instead of data quality monitoring, you monitor AI behavior.
Instead of batch pipelines, you may manage RAG pipelines.
Instead of validating transformations, you evaluate model outputs.

But these are extensions of what you already do.

Media IDs: `b075e0f2-eb5e-42de-85c7-49e88d8dd8c7`

#### Post 2

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7442118041967988736

Can a data engineer transition into AI engineering?

Short answer: yes. And in many cases, faster than they think.

AI engineering is primarily an engineering role.

There is far less research and model training than people assume. In modern AI systems, the foundation model is usually an API call. The hard part is everything around it.

If you are a data engineer, you already have the core.

You know how to:

- Write tests
- Set up CI/CD
- Monitor pipelines
- Collect logs
- Follow solid engineering practices

The "flavor" changes, but the fundamentals stay the same.

Instead of data quality monitoring, you monitor AI behavior.
Instead of batch pipelines, you may manage RAG pipelines.
Instead of validating transformations, you evaluate model outputs.

But these are extensions of what you already do.

I'm running the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

This course is a great resource for anyone who considers transitioning into AI Engineer role.

Read more here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `f02b204f-61b9-43f1-bd8a-294e77f72947`

## Connecting AI Agents to Tools

- Typefully ID: `8050650`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T12:00:19.652Z
- Updated: 2026-02-25T12:46:27.803Z
- Scheduled: 2026-03-02T18:00:00Z
- Published: 2026-03-02T18:00:15.100Z
- Typefully URL: https://typefully.com/?d=8050650&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2028530825499984181

#### Post 1

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

Media IDs: `ce048eb1-d731-4751-bf68-26e54d2b9667`

#### Post 2

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7434296529076555777

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `7babfb15-270f-4f6f-a176-4d8165193ff2`

## Coding Agent Guide

- Typefully ID: `8061703`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-10T13:51:48.407Z
- Updated: 2026-02-24T11:49:47.959Z
- Published: 2026-02-24T11:50:02.713Z
- Typefully URL: https://typefully.com/?d=8061703&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2026263333452865956

#### Post 1

Developer cheatsheet to turn a chatbot into a coding agent:

1) Chatbot vs agent decision

Decide upfront whether you actually need an agent. Agents are only worth it when you need actions like file I/O, code execution, or search.

2) Tool schema definition

Define concrete tools with strict schemas describing names, parameters, and constraints, and expose only what the agent should be allowed to do.

3) Tool execution loop

Implement a loop where the model proposes tool calls, your system executes them, and the results are fed back into the conversation state.

4) Project-scoped editing tools

Provide file and shell access scoped to a project root, with guardrails to prevent unsafe commands and accidental damage.

5) Project template scaffolding

Start each run from a clean template copied into a fresh directory so all agent edits remain isolated and reproducible.

6) System prompt as documentation

Use the system prompt to document the tech stack, file structure, and rules, and require the model to plan before acting.

Use this as a checklist when building a tool-using coding agent on top of your preferred stack and LLM API.

Want a detailed step-by-step tutorial? Download my guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `cec3d2f4-a17e-4408-8c40-92231b3ac7f3`

#### Post 2

Learn to build AI agents and apply new knowledge to create 8+ projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7432029024245141504

Developer cheatsheet to turn a chatbot into a coding agent:

1) Chatbot vs agent decision

Decide upfront whether you actually need an agent. Agents are only worth it when you need actions like file I/O, code execution, or search.

2) Tool schema definition

Define concrete tools with strict schemas describing names, parameters, and constraints, and expose only what the agent should be allowed to do.

3) Tool execution loop

Implement a loop where the model proposes tool calls, your system executes them, and the results are fed back into the conversation state.

4) Project-scoped editing tools

Provide file and shell access scoped to a project root, with guardrails to prevent unsafe commands and accidental damage.

5) Project template scaffolding

Start each run from a clean template copied into a fresh directory so all agent edits remain isolated and reproducible.

6) System prompt as documentation

Use the system prompt to document the tech stack, file structure, and rules, and require the model to plan before acting.

Use this as a checklist when building a tool-using coding agent on top of your preferred stack and LLM API.

Want a detailed step-by-step tutorial? Download my guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Learn to build AI agents and apply new knowledge to create 8+ projects from scratch on the AI Engineering Buildcamp.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `cec3d2f4-a17e-4408-8c40-92231b3ac7f3`

## AI Coding Agent Workshop

- Typefully ID: `8050578`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T11:55:39.836Z
- Updated: 2026-02-20T09:17:34.038Z
- Scheduled: 2026-02-20T18:00:00Z
- Published: 2026-02-20T18:00:09.519Z
- Typefully URL: https://typefully.com/?d=8050578&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2024906935116726426

Build an autonomous coding agent from scratch using my free workshop materials.

In the workshop, we start with a basic Django template and build an agent that can plan changes, write code, modify files, and iterate on the application using Python.

We progressively move through different levels of abstraction:

- Basic tool-based agents
- OpenAI Agents SDK
- A production-grade setup with PydanticAI and Claude 3.5 Sonnet

Links:

- Watch the video: https://www.youtube.com/watch?v=Sue_mn0JCsY
- Access materials: https://github.com/alexeygrigorev/workshops/tree/main/coding-agent

--
This workshop is a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `a7e6c1dd-0217-4746-8241-7cabe0f75008`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7430672633618370560

Build an autonomous coding agent from scratch using my free workshop materials.

In the workshop, we start with a basic Django template and build an agent that can plan changes, write code, modify files, and iterate on the application using Python.

We progressively move through different levels of abstraction:

- Basic tool-based agents
- OpenAI Agents SDK
- A production-grade setup with PydanticAI and Claude 3.5 Sonnet

Links:

- Watch the video: https://www.youtube.com/watch?v=Sue_mn0JCsY
- Access materials: https://github.com/alexeygrigorev/workshops/tree/main/coding-agent

--
This workshop is a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `1708939d-e5ce-4084-b89c-cb4cd1422f02`

## Coding Agent Guide

- Typefully ID: `8090314`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-13T06:36:55.075Z
- Updated: 2026-02-13T06:37:25.760Z
- Scheduled: 2026-02-18T08:00:00Z
- Published: 2026-02-18T08:00:11.837Z
- Typefully URL: https://typefully.com/?d=8090314&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2024031163095130324

#### Post 1

Free 25+ pages guide on building your own coding agent with Python, Jupyter, and Django

What it covers:

1. Decide: chatbot or agent

- Chatbot: text in -> text out
- Agent: loops with tool calls + stateful history

2. Define tool schemas

- Start with concrete functions: read_file, write_file, see_file_tree, execute_bash_command.
- Describe them using JSON schema (name, description, parameters).

3. Implement the tool loop

- Send messages + tools -> model.
- If it returns function_call, dispatch to Python.
- Append function_call + function_call_output back into the history.

4. Add project-editing tools

- Bind tools to a project_dir (sandbox).
- Block dangerous commands (e.g., runserver).
- Skip .venv, __pycache__, node_modules.

5. Scaffold a template repo

- Clone a minimal Django template.
- Copy it per project, then let the agent refactor and extend it.

6. Write a real system prompt

- Explain the stack, file tree, and constraints.
- Tell the model to plan first, then call tools to execute.

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `2e79c2eb-b9c8-4083-b9d6-3dbb3455ef80`

#### Post 2

This guide is a preview of what we do during the AI Engineering Buildcamp.

During the course, you'll learn to build AI agents and apply new knowledge to create 8+ projects from scratch.

Read the details here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7429796850469330945

Free 25+ pages guide on building your own coding agent with Python, Jupyter, and Django

What it covers:

1. Decide: chatbot or agent

- Chatbot: text in -> text out
- Agent: loops with tool calls + stateful history

2. Define tool schemas

- Start with concrete functions: read_file, write_file, see_file_tree, execute_bash_command.
- Describe them using JSON schema (name, description, parameters).

3. Implement the tool loop

- Send messages + tools -> model.
- If it returns function_call, dispatch to Python.
- Append function_call + function_call_output back into the history.

4. Add project-editing tools

- Bind tools to a project_dir (sandbox).
- Block dangerous commands (e.g., runserver).
- Skip .venv, __pycache__, node_modules.

5. Scaffold a template repo

- Clone a minimal Django template.
- Copy it per project, then let the agent refactor and extend it.

6. Write a real system prompt

- Explain the stack, file tree, and constraints.
- Tell the model to plan first, then call tools to execute.

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide
–
This guide is a preview of what we do during the AI Engineering Buildcamp.

During the course, you'll learn to build AI agents and apply new knowledge to create 8+ projects from scratch.

Read the details here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `e77b792f-ad4d-43b3-82fe-0ccb06c95c5c`

## Coding Agent Guide

- Typefully ID: `8050581`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T11:55:59.486Z
- Updated: 2026-02-12T08:47:07.036Z
- Scheduled: 2026-02-12T15:00:00Z
- Published: 2026-02-12T15:00:16.226Z
- Typefully URL: https://typefully.com/?d=8050581&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2021962549584167070

#### Post 1

Free 25+ pages guide on building your own coding agent with Python, Jupyter, and Django

What it covers:

1. Decide: chatbot or agent

- Chatbot: text in -> text out
- Agent: loops with tool calls + stateful history

2. Define tool schemas

- Start with concrete functions: read_file, write_file, see_file_tree, execute_bash_command.
- Describe them using JSON schema (name, description, parameters).

3. Implement the tool loop

- Send messages + tools -> model.
- If it returns function_call, dispatch to Python.
- Append function_call + function_call_output back into the history.

4. Add project-editing tools

- Bind tools to a project_dir (sandbox).
- Block dangerous commands (e.g., runserver).
- Skip .venv, __pycache__, node_modules.

5. Scaffold a template repo

- Clone a minimal Django template.
- Copy it per project, then let the agent refactor and extend it.

6. Write a real system prompt

- Explain the stack, file tree, and constraints.
- Tell the model to plan first, then call tools to execute.

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `af1d2858-a5b8-4601-af2a-936d8d08bf86`

#### Post 2

This guide is a preview of what we do during the AI Engineering Buildcamp.

During the course, you'll learn to build AI agents and apply new knowledge to create 8+ projects from scratch.

Read the details here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7427728234030505984

Free 25+ pages guide on building your own coding agent with Python, Jupyter, and Django

What it covers:

1. Decide: chatbot or agent

- Chatbot: text in -> text out
- Agent: loops with tool calls + stateful history

2. Define tool schemas

- Start with concrete functions: read_file, write_file, see_file_tree, execute_bash_command.
- Describe them using JSON schema (name, description, parameters).

3. Implement the tool loop

- Send messages + tools -> model.
- If it returns function_call, dispatch to Python.
- Append function_call + function_call_output back into the history.

4. Add project-editing tools

- Bind tools to a project_dir (sandbox).
- Block dangerous commands (e.g., runserver).
- Skip .venv, __pycache__, node_modules.

5. Scaffold a template repo

- Clone a minimal Django template.
- Copy it per project, then let the agent refactor and extend it.

6. Write a real system prompt

- Explain the stack, file tree, and constraints.
- Tell the model to plan first, then call tools to execute.

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide
–
This guide is a preview of what we do during the AI Engineering Buildcamp.

During the course, you'll learn to build AI agents and apply new knowledge to create 8+ projects from scratch.

Read the details here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `af1d2858-a5b8-4601-af2a-936d8d08bf86`

## AI Engineering Buildcamp Projects

- Typefully ID: `8071226`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-11T11:02:31.441Z
- Updated: 2026-02-11T11:31:36.866Z
- Scheduled: 2026-02-17T08:00:00Z
- Published: 2026-02-17T08:00:09.521Z
- Typefully URL: https://typefully.com/?d=8071226&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2023668777091821638

AI Engineering Buildcamp is project-driven.

Projects you can you build during the course:

1. Documentation RAG Agent: A GitHub-powered documentation assistant with indexing, retrieval, and structured outputs. This becomes the base architecture for later systems.

2. FAQ Assistant: A production-style support chatbot with reusable RAG components and search integrations.

3. Tool-Using AI Agent: A typed, structured agent with a full tool-call loop using PydanticAI. This marks the shift from pipeline to autonomous system.

4. Web and YouTube Research Agent: A research assistant capable of web search, content extraction, and synthesis.

5. Production-Ready Agent with Testing Framework: A structured Python project with unit tests, cost tracking, and LLM-based evaluation.

6. Multi-Agent Architectures: Implementation of planner-executor patterns, orchestrators, and agents-as-tools for system design thinking.

7. Observable AI Application: Integration of tracing, logging, and monitoring tools to move from building to operating AI systems.

8. Evaluation Pipeline: A measurable evaluation system including synthetic data generation, retrieval testing, and prompt optimization experiments.

9. Complete AI Application: A fully integrated system with tools, testing, observability, evaluation, guardrails, and deployment. This becomes the main portfolio project.

Advanced Optional Projects

- Coding Agent (Django Scaffolder): A multi-agent coding assistant for project generation.
- Code Analysis Agent: An agent that reads repositories and explains architecture.
- Deep Research Agent: A multi-stage reasoning system for structured research workflows.
- Use Case Mini-Projects: Vertical implementations such as code explainers, FAQ bots, book writers, or generative pipelines.

The focus is not on one framework.

The focus is on designing, testing, operating, and deploying real AI systems end to end.

The next cohort starts on April 13. You can sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `da6d7a00-d9b5-41df-8050-21da11b48759`, `1b552c91-ddde-4a29-b005-e1d214bbbcc3`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7429434474377142272

AI Engineering Buildcamp is project-driven.

Projects you can you build during the course:

1. Documentation RAG Agent: A GitHub-powered documentation assistant with indexing, retrieval, and structured outputs. This becomes the base architecture for later systems.

2. FAQ Assistant: A production-style support chatbot with reusable RAG components and search integrations.

3. Tool-Using AI Agent: A typed, structured agent with a full tool-call loop using PydanticAI. This marks the shift from pipeline to autonomous system.

4. Web and YouTube Research Agent: A research assistant capable of web search, content extraction, and synthesis.

5. Production-Ready Agent with Testing Framework: A structured Python project with unit tests, cost tracking, and LLM-based evaluation.

6. Multi-Agent Architectures: Implementation of planner-executor patterns, orchestrators, and agents-as-tools for system design thinking.

7. Observable AI Application: Integration of tracing, logging, and monitoring tools to move from building to operating AI systems.

8. Evaluation Pipeline: A measurable evaluation system including synthetic data generation, retrieval testing, and prompt optimization experiments.

9. Complete AI Application: A fully integrated system with tools, testing, observability, evaluation, guardrails, and deployment. This becomes the main portfolio project.

Advanced Optional Projects

- Coding Agent (Django Scaffolder): A multi-agent coding assistant for project generation.
- Code Analysis Agent: An agent that reads repositories and explains architecture.
- Deep Research Agent: A multi-stage reasoning system for structured research workflows.
- Use Case Mini-Projects: Vertical implementations such as code explainers, FAQ bots, book writers, or generative pipelines.

The focus is not on one framework.

The focus is on designing, testing, operating, and deploying real AI systems end to end.

The next cohort starts on April 13. You can sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `27bf43e7-4df5-458f-a3e7-8917e181e8da`

## Building Safe AI Agents

- Typefully ID: `7986032`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-02T14:17:10.146Z
- Updated: 2026-02-10T10:47:44.534Z
- Scheduled: 2026-02-11T15:00:00Z
- Published: 2026-02-11T15:00:15.636Z
- Typefully URL: https://typefully.com/?d=7986032&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2021600160074379649

#### Post 1

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large FAQ for a Data Engineering course hosted on GitHub: 300+ questions, written by students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

Media IDs: `f745832d-49a0-47ab-8504-aaaf4d38dcc9`

#### Post 2

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7427365860933038080

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large FAQ for a Data Engineering course hosted on GitHub: 300+ questions, written by students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `93187a66-5345-4ddd-a777-2312760ba1da`

## AI Assistant Development Course

- Typefully ID: `8050590`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T11:56:51.453Z
- Updated: 2026-02-09T11:56:51.422Z
- Typefully URL: https://typefully.com/?d=8050590&a=188312

### linkedin

Build an AI agent you can use at work.

In my new hands-on course, you’ll progress from a basic assistant to production, covering testing, agentic behavior, and monitoring step by step.

By the end, you’ll have:

🔸 A fully functional AI assistant (RAG + OpenAI) that can search and answer from real documents.
🔸 A test-driven prompt engineering workflow using evaluation metrics and simulated queries.
🔸 Agentic behavior: function calling, Model Context Protocol (MCP), PydanticAI, OpenAI’s Agent SDK
🔸 A website-building AI agent that outputs complete Django projects.
🔸 Monitoring and guardrails for deployed AI apps: Grafana, Evidently, LangWatch
🔸 A capstone project: your own production-ready AI tool like a resume reviewer, a podcast summarizer, a search bot, etc.

Registration is open, enroll today: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `1476af29-93c8-4163-896c-aa474ca4c0bb`

## AI Coding Agent Workshop

- Typefully ID: `8050585`
- Status: draft
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-09T11:56:11.838Z
- Updated: 2026-02-09T11:56:11.785Z
- Typefully URL: https://typefully.com/?d=8050585&a=188312

### x

#### Post 1

Free tutorial: Build an LLM-based agent that will create Django apps from your text prompt.

I’ve published a recording of my latest workshop on building full AI-powered coding agents using Python and Django.

Watch the recording here: https://youtu.be/Sue_mn0JCsY?si=T4wXcEjF0EDuKtM6

Media IDs: `765d18ed-85d3-4ec8-a9b1-4cd5d2c7b3e0`

#### Post 2

What you’ll learn:

- Chatbots vs. Agents
- Setting up with GitHub Codespaces
- Utilizing OpenAI Agents SDK, Toy AI Kit, Pydantic AI
- Defining agent tools: file I/O, web search, more
- Switching LLM providers: OpenAI, Anthropic, Z.AI

#### Post 3

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Do you want to build an LLM-based agent that will create Django apps from your text prompt?

I’ve published a recording of my latest workshop on building full AI-powered coding agents using Python and Django.

What you’ll learn:

🔸 The difference between chatbots and agents
🔸 How to set up your dev environment using GitHub Codespaces
🔸 Using the OpenAI Agents SDK, Toy AI Kit, and Pydantic AI
🔸 How to define agent tools: file I/O, web search, and more
🔸 Switching LLM providers: OpenAI, Anthropic, Z.AI

Watch the recording here: https://youtu.be/Sue_mn0JCsY?si=T4wXcEjF0EDuKtM6

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `c6669e54-890b-4798-b6c6-2ed118017575`

## AI Agent Architecture Essentials (from workshop)

- Typefully ID: `7986033`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-02T14:17:24.058Z
- Updated: 2026-02-09T11:26:09.176Z
- Scheduled: 2026-02-09T18:00:00Z
- Published: 2026-02-09T18:00:17.125Z
- Typefully URL: https://typefully.com/?d=7986033&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2020920688983617692

#### Post 1

4 key components of AI agent architecture in its simplest form:

1. Brain: The LLM. It reasons, plans, and decides what to do next.

2. Instructions: The system prompt. It defines the agent's role, boundaries, and behavior.

3. Tools: Functions the agent can call to interact with the world:
reading files, writing code, running commands, searching data.

4. Memory: The conversation history and tool results that provide context across steps.

How this works together is what people call the agentic loop:

🔸 The user gives a task
🔸 The agent reasons based on instructions and memory
🔸 It decides to respond or call a tool
🔸 Tool results are added to memory
🔸 The loop continues until the task is complete

The agent decides when to stop.

Once you see this loop clearly, agent frameworks become much easier to reason about. They're mostly different ways of wiring these same components together.

If you want a hands-on walkthrough of this architecture, I've shared free workshop materials.

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

Media IDs: `f650fce2-41b3-40d5-a2c8-77717b0c24ee`

#### Post 2

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7426686381290303488

4 key components of AI agent architecture in its simplest form:

1. Brain: The LLM. It reasons, plans, and decides what to do next.

2. Instructions: The system prompt. It defines the agent's role, boundaries, and behavior.

3. Tools: Functions the agent can call to interact with the world:
reading files, writing code, running commands, searching data.

4. Memory: The conversation history and tool results that provide context across steps.

How this works together is what people call the agentic loop:

🔸 The user gives a task
🔸 The agent reasons based on instructions and memory
🔸 It decides to respond or call a tool
🔸 Tool results are added to memory
🔸 The loop continues until the task is complete

The agent decides when to stop.

Once you see this loop clearly, agent frameworks become much easier to reason about. They're mostly different ways of wiring these same components together.

If you want a hands-on walkthrough of this architecture, I've shared free workshop materials.

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `2ee539e6-28df-479b-b9fa-e1a01754ec9c`

## AI Engineering Buildcamp Module 1

- Typefully ID: `7986202`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-02-02T14:35:14.884Z
- Updated: 2026-02-02T14:46:27.516Z
- Scheduled: 2026-02-02T15:00:00Z
- Published: 2026-02-02T15:00:15.837Z
- Typefully URL: https://typefully.com/?d=7986202&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2018338681925583037

We've just finished Module 1 at the AI Engineering Buildcamp.

I fully reworked and re-recorded the content to focus more on practical engineering decisions and less on high-level introductions.

What we covered in Module 1:

1. RAG fundamentals

Used Evidently's documentation as a real, non-simplified example

2. Structured Output

I previously didn't spend enough time on this topic, but it's critical to building reliable LLM-based systems. As a result, it has been moved to the first week and covered in much greater depth.

3. Streaming and working with partial model responses

4. A new, extended section on alternatives to OpenAI

This material was not included in the first iteration of the course. The module now includes a detailed overview and a large list of alternative models and providers.

This first module establishes the technical foundation for the rest of the course.

From here, we will gradually increase complexity and move toward more agent-based and production-oriented systems.

You can learn more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `df6bbfa2-96df-4eeb-9f76-7ac2c0d8e802`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7424104365176619009

We've just finished Module 1 at the AI Engineering Buildcamp.

I fully reworked and re-recorded the content to focus more on practical engineering decisions and less on high-level introductions.

What we covered in Module 1:

1. RAG fundamentals

Used Evidently's documentation as a real, non-simplified example

2. Structured Output

I previously didn't spend enough time on this topic, but it's critical to building reliable LLM-based systems. As a result, it has been moved to the first week and covered in much greater depth.

3. Streaming and working with partial model responses

4. A new, extended section on alternatives to OpenAI

This material was not included in the first iteration of the course. The module now includes a detailed overview and a large list of alternative models and providers.

This first module establishes the technical foundation for the rest of the course.

From here, we will gradually increase complexity and move toward more agent-based and production-oriented systems.

You can learn more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `df6bbfa2-96df-4eeb-9f76-7ac2c0d8e802`

## Components of AI Agent

- Typefully ID: `7930339`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T09:17:59.210Z
- Updated: 2026-01-30T07:54:37.914Z
- Scheduled: 2026-01-30T12:15:00Z
- Published: 2026-01-30T12:15:06.760Z
- Typefully URL: https://typefully.com/?d=7930339&a=188312

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7422975646282375170

4 key components of AI agent architecture in its simplest form:

1. Brain: The LLM. It reasons, plans, and decides what to do next.

2. Instructions: The system prompt. It defines the agent's role, boundaries, and behavior.

3. Tools: Functions the agent can call to interact with the world:
reading files, writing code, running commands, searching data.

4. Memory: The conversation history and tool results that provide context across steps.

How this works together is what people call the agentic loop:

🔸 The user gives a task
🔸 The agent reasons based on instructions and memory
🔸 It decides to respond or call a tool
🔸 Tool results are added to memory
🔸 The loop continues until the task is complete

The agent decides when to stop.

Once you see this loop clearly, agent frameworks become much easier to reason about. They're mostly different ways of wiring these same components together.

If you want a hands-on walkthrough of this architecture, I've shared free workshop materials.

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `e1a2a6af-b4dd-4f71-a47e-506e7e8e98dd`

## Building Safe AI Agents

- Typefully ID: `7930468`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T09:37:53.175Z
- Updated: 2026-01-27T09:52:44.977Z
- Scheduled: 2026-01-31T08:00:00Z
- Published: 2026-01-31T08:00:12.371Z
- Typefully URL: https://typefully.com/?d=7930468&a=188312

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7423273885325791233

I recently ran a workshop on building safe AI agents with guardrails.

One part of it focuses on building a search engine for a real FAQ before adding any agent logic.

The example uses a large Data Engineering course FAQ stored on GitHub.
300+ questions, written by real students.

We go through this step by step:

🔸 Fetch the FAQ data directly from GitHub
🔸 Parse questions and answers into a clean Python structure
🔸 Index the content to make it searchable
🔸 Verify that search returns relevant results

Only after that do we add an agent on top.

Retrieval and data grounding are important parts of an agent's design, because an agent is only as good as its access to data.

If retrieval is weak, the agent will confidently answer incorrectly.

My workshop shows how to ground an agent in real, verifiable data before adding guardrails and agentic behavior.

Here are the materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `318a8565-c9af-49f8-90a4-fe83c9d805af`

## Connecting AI Agents to Tools

- Typefully ID: `7930537`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T09:46:00.772Z
- Updated: 2026-01-27T09:52:31.266Z
- Scheduled: 2026-02-01T08:00:00Z
- Published: 2026-02-01T08:00:21.689Z
- Typefully URL: https://typefully.com/?d=7930537&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2017870610995810310

#### Post 1

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

Media IDs: `a927f385-3a61-4a67-982c-ab5be15dc60e`

#### Post 2

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7423636259253727232

How to connect AI agents to tools?

Here's an example from a recent workshop where I built an FAQ assistant that answers student questions based on an FAQ document.

We start with a simple Python search function that queries an indexed FAQ.

The key step is turning that function into a tool and giving it to an agent.

Here's how to do it:

🔸 Define a search function over the FAQ index
🔸 Decorate it as a tool so the agent can call it
🔸 Create an agent with clear system instructions
🔸 Assign the tool to the agent

In my case, instructions tell the agent:

🔸 You are a teaching assistant
🔸 Your job is to answer questions using the FAQ
🔸 Use the search tool when needed

When a user asks a question, the agent:

🔸 Decides whether to call the tool
🔸 Generates a search query
🔸 Inspects the returned results
🔸 Produces the final answer

You can inspect every tool call to see exactly how the agent reasons and why it chose a particular answer.

This material comes from a free workshop on building safe AI agents, where we go from search to agents and then add guardrails on top.

Materials:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `a927f385-3a61-4a67-982c-ab5be15dc60e`

## Guardrails for AI

- Typefully ID: `7930379`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T09:25:52.744Z
- Updated: 2026-01-27T09:31:49.634Z
- Scheduled: 2026-01-29T08:00:00Z
- Published: 2026-01-29T08:00:22.318Z
- Typefully URL: https://typefully.com/?d=7930379&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2016783461995208760

What are guardrails for AI agents?
Here's a simple way to think about them:

1. What are guardrails?

Guardrails are mechanisms that control how the model reacts to user input and what the user ultimately sees.

2. Why are guardrails important?

An agent will try to be helpful, even when it shouldn't.

For example, imagine an agent built to answer questions about a course.

Without guardrails:
🔸 A student can ask for pizza recipes
🔸 The agent will try to answer
🔸 You spend tokens and money on completely off-topic requests

Guardrails prevent this.

They let you define what is allowed and what is not, before or after the model responds.

3. In practice, guardrails help you:

🔸 Block off-topic questions early
🔸 Refuse requests you don't want to support
🔸 Avoid unsafe or inappropriate outputs
🔸 Save money by stopping useless calls

You decide what the agent is for. Guardrails enforce that decision.

Once agents are exposed to real users, guardrails stop being optional. They become part of the system design.

I walk through this step by step in a free workshop:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `b7791b1c-5dea-4a46-8e3f-bca8f006fb36`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7422549107753500672

What are guardrails for AI agents?
Here's a simple way to think about them:

1. What are guardrails?

Guardrails are mechanisms that control how the model reacts to user input and what the user ultimately sees.

2. Why are guardrails important?

An agent will try to be helpful, even when it shouldn't.

For example, imagine an agent built to answer questions about a course.

Without guardrails:
🔸 A student can ask for pizza recipes
🔸 The agent will try to answer
🔸 You spend tokens and money on completely off-topic requests

Guardrails prevent this.

They let you define what is allowed and what is not, before or after the model responds.

3. In practice, guardrails help you:

🔸 Block off-topic questions early
🔸 Refuse requests you don't want to support
🔸 Avoid unsafe or inappropriate outputs
🔸 Save money by stopping useless calls

You decide what the agent is for. Guardrails enforce that decision.

Once agents are exposed to real users, guardrails stop being optional. They become part of the system design.

I walk through this step by step in a free workshop:

Video: https://youtu.be/Sk1aqwNJWT4?si=T6afVvKelro438OQ
Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop is also a preview of the AI Engineering Buildcamp, where we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `b7791b1c-5dea-4a46-8e3f-bca8f006fb36`

## Agents: Skills vs Commands

- Typefully ID: `7930253`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T09:05:55.934Z
- Updated: 2026-01-27T09:21:33.619Z
- Scheduled: 2026-01-28T08:00:00Z
- Published: 2026-01-28T08:00:12.504Z
- Typefully URL: https://typefully.com/?d=7930253&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2016421020513788090

#### Post 1

When building agents, what is the difference between skills and commands?
They look similar, but they serve different roles.

1. Commands are explicit. You can think of them as user-driven shortcuts

🔸 The user knows exactly what should happen
🔸 The user triggers it directly, for example /kit
🔸 The agent simply executes the instruction

2. Skills are implicit

🔸 The user describes a task in natural language
🔸 The agent decides whether a skill applies
🔸 The agent loads and uses the skill autonomously

The user never says, "Use this skill"

Skills encode operational knowledge. They tell the agent how to do something, so it doesn't have to guess.

3. The key distinction is who makes the decision:

🔸 Commands: the user decides
🔸 Skills: the agent decides

Commands are best when the intent is precise.

Skills are better when you want reusable, predictable agent behavior across tasks and projects.

If you want to go deeper, I've shared a free workshop on implementing skills from scratch:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

Media IDs: `6b5e25dd-d499-425b-b3f7-51e3c7c80e15`

#### Post 2

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up.

Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7422186717207576576

When building agents, what is the difference between skills and commands?
They look similar, but they serve different roles.

1. Commands are explicit. You can think of them as user-driven shortcuts

🔸 The user knows exactly what should happen
🔸 The user triggers it directly, for example /kit
🔸 The agent simply executes the instruction

2. Skills are implicit

🔸 The user describes a task in natural language
🔸 The agent decides whether a skill applies
🔸 The agent loads and uses the skill autonomously

The user never says, "Use this skill"

Skills encode operational knowledge. They tell the agent how to do something, so it doesn't have to guess.

3. The key distinction is who makes the decision:

🔸 Commands: the user decides
🔸 Skills: the agent decides

Commands are best when the intent is precise.

Skills are better when you want reusable, predictable agent behavior across tasks and projects.

If you want to go deeper, I've shared a free workshop on implementing skills from scratch:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/agent-skills

I also teach how to build production-ready AI agents in my AI Engineering Buildcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

We've just started the course, and you still have one buffer week to join and catch up. Sign up here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `0cdce6af-9df3-4a22-99fe-e8fcd20a8b19`

## AI Engineering Buildcamp: Cohort 2

- Typefully ID: `7929593`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-27T07:35:32.215Z
- Updated: 2026-01-27T07:39:31.465Z
- Scheduled: 2026-01-27T08:00:00Z
- Published: 2026-01-27T08:00:09.447Z
- Typefully URL: https://typefully.com/?d=7929593&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2016058632128143420

We started the second cohort of the AI Engineering Buildcamp yesterday.

Thank you to everyone who joined!

It was great to see you live, meet you, and get a feel for the group right from the first session.

I outlined the entire course structure, explained how everything connects, and detailed what we'll be building in the coming weeks.

If you're still considering joining:

🔸 I've extended the payment deadline to next week.
🔸 Week 2 is designed as a buffer week.
🔸 If you join a bit late, you can still catch up without stress.

You can enroll in the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

The start felt great. Thanks again to everyone who joined!

Looking forward to the upcoming sessions.

Media IDs: `1fd1cf2b-c0af-4091-a5a6-bb95a448fe08`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7421824324271198209

We started the second cohort of the AI Engineering Buildcamp yesterday.

Thank you to everyone who joined!

It was great to see you live, meet you, and get a feel for the group right from the first session.

I outlined the entire course structure, explained how everything connects, and detailed what we'll be building in the coming weeks.

If you're still considering joining:

🔸 I've extended the payment deadline to next week.
🔸 Week 2 is designed as a buffer week.
🔸 If you join a bit late, you can still catch up without stress.

You can enroll in the course here: https://maven.com/alexey-grigorev/from-rag-to-agents

The start felt great. Thanks again to everyone who joined!

Looking forward to the upcoming sessions.

Media IDs: `1fd1cf2b-c0af-4091-a5a6-bb95a448fe08`

## Utilize Learning Budget for AI

- Typefully ID: `7922384`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-26T13:38:22.595Z
- Updated: 2026-01-26T14:19:05.999Z
- Scheduled: 2026-01-26T15:00:00Z
- Published: 2026-01-26T15:00:37.014Z
- Typefully URL: https://typefully.com/?d=7922384&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2015802043487973764

#### Post 1

One of the course participants just shared that they joined AI Engineering Buildcamp using their learning budget through Maven.

This is a good reminder to use your learning budget!

How it typically works:

🔸 Many companies already cover Maven courses via L&D budgets
🔸 After enrollment, you receive a receipt you can forward for reimbursement
🔸 You also get a certificate of completion at the end

If your company offers an L&D or education budget and you haven't used it yet, this is a practical way to leverage it.

1/2

Media IDs: `5bea20fd-6849-408d-94d8-c1f9add9a2e8`

#### Post 2

Maven has an article about that (+email template to request approval): https://maven.com/expense

I've also prepared a short email you can reuse: https://docs.google.com/document/d/12LBC7KBR_NE-ehSf7YTOOTlMgPD_0g-KU7g5KxTxpbs/edit?usp=sharing

The course starts today, but you can still join. Week 1 is introductory, so it's easy to catch up: https://maven.com/alexey-grigorev/from-rag-to-agents

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7421567733181558784

One of the course participants just shared that they joined AI Engineering Buildcamp using their learning budget through Maven.

This is a good reminder to use your learning budget!

How it typically works:

🔸 Many companies already cover Maven courses via L&D budgets
🔸 After enrollment, you receive a receipt you can forward for reimbursement
🔸 You also get a certificate of completion at the end

If your company offers an L&D or education budget and you haven't used it yet, this is a practical way to leverage it.

Maven has an article about that (+email template to request approval): https://maven.com/expense

I've also prepared a short email you can reuse: https://docs.google.com/document/d/12LBC7KBR_NE-ehSf7YTOOTlMgPD_0g-KU7g5KxTxpbs/edit?usp=sharing

The course starts today, but you can still join. Week 1 is introductory, so it's easy to catch up: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `5bea20fd-6849-408d-94d8-c1f9add9a2e8`

## AI Bootcamp: Building Agentic Systems

- Typefully ID: `7868292`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-20T11:34:20.392Z
- Updated: 2026-01-24T07:01:22.940Z
- Scheduled: 2026-01-24T08:00:00Z
- Published: 2026-01-24T08:00:10.088Z
- Typefully URL: https://typefully.com/?d=7868292&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2014971458989265133

#### Post 1

The next cohort of my AI Engineering Buildcamp starts on Monday. But you still have one more week to enroll.

The second week of the course is a buffer week. If helps to catch up if environment setup takes longer than expected, you start a few days late, or you want more time with the foundations.

But it also includes optional content and more use cases for course participants who want to learn more.  

In this course, you will build:

🔸 A real RAG pipeline on your own data
🔸 Tool-using agents with function calling and MCP
🔸 Evaluation workflows to compare prompts, models, and retrieval strategies
🔸 Monitoring and guardrails for production use
🔸 A capstone project you can actually show
🔸 More than 8 projects in total

We already have 46 course participants for this cohort.

Join us too: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `48f8eeea-905e-4a65-8523-1d5cb4cffbe3`

#### Post 2

You can read more about the updated course curriculum here: 

https://alexeyondata.substack.com/p/ai-bootcamp-becomes-ai-engineering

(And there's a discount code inside)

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7420737150457085952

The next cohort of my AI Engineering Buildcamp starts on Monday. But you still have one more week to enroll.

The second week of the course is a buffer week. If helps to catch up if environment setup takes longer than expected, you start a few days late, or you want more time with the foundations.

But it also includes optional content and more use cases for course participants who want to learn more.  

In this course, you will build:

🔸 A real RAG pipeline on your own data
🔸 Tool-using agents with function calling and MCP
🔸 Evaluation workflows to compare prompts, models, and retrieval strategies
🔸 Monitoring and guardrails for production use
🔸 A capstone project you can actually show
🔸 More than 8 projects in total

We already have 46 course participants for this cohort.

Join us too: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `48f8eeea-905e-4a65-8523-1d5cb4cffbe3`

## AI Agents' Skills: GitHub Fetch

- Typefully ID: `7867816`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-01-20T10:46:16.709Z
- Updated: 2026-01-22T16:26:30.431Z
- Scheduled: 2026-01-25T08:00:00Z
- Published: 2026-01-25T08:00:10.835Z
- Typefully URL: https://typefully.com/?d=7867816&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2015333850130575586

#### Post 1

What are skills in AI agents?

In one of the workshops, I demo a GitHub Fetch skill.

The task seems simple: retrieve files from a GitHub repository. But without this skill, the agent must guess how to:

- Interact with GitHub
- Choose the right commands
- Navigate the repository structure

A skill provides a reusable set of instructions that guides the agent through tasks step by step.

Specifically, the GitHub Fetch skill instructs the agent on:

- Using the gh CLI
- Listing repository contents
- Navigating directories
- Downloading specific files

With these validated instructions, skills minimize reasoning errors by encoding operational knowledge.

In the demo, we used this skill to fetch two commands from a GitHub repo:

- /kid generates a wild project idea
- /parent implements it as code

These commands are stored in GitHub, and the agent uses the GitHub Fetch skill to automatically retrieve them.

Skills offer benefits like:

- Making behavior predictable
- Avoiding repeated prompts
- Reusing hard-won instructions
- Scaling beyond one-off demos

Media IDs: `eb75809b-56c7-4582-ad81-854b8249a499`

#### Post 2

I teach how to build production-ready AI agents in my AI Bootcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

The next cohort starts tomorrow: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7421099547382140928

What are skills in AI agents?

In one of the workshops, I demo a GitHub Fetch skill.

The task seems simple: retrieve files from a GitHub repository. But without this skill, the agent must guess how to:

- Interact with GitHub
- Choose the right commands
- Navigate the repository structure

A skill provides a reusable set of instructions that guides the agent through tasks step by step.

Specifically, the GitHub Fetch skill instructs the agent on:

- Using the gh CLI
- Listing repository contents
- Navigating directories
- Downloading specific files

With these validated instructions, skills minimize reasoning errors by encoding operational knowledge.

In the demo, we used this skill to fetch two commands from a GitHub repo:

- /kid generates a wild project idea
- /parent implements it as code

These commands are stored in GitHub, and the agent uses the GitHub Fetch skill to automatically retrieve them.

Skills offer benefits like:

- Making behavior predictable
- Avoiding repeated prompts
- Reusing hard-won instructions
- Scaling beyond one-off demos

I teach how to build production-ready AI agents in my AI Bootcamp. We go deeper into agent design, evaluation, monitoring, and guardrails as a system.

The next cohort starts tomorrow: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `1a7e1fac-02f8-406b-a586-9bf49bfbdda4`

## LangChain and LangGraph Integration

- Typefully ID: `7881440`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-21T15:03:46.270Z
- Updated: 2026-01-22T16:26:03.234Z
- Scheduled: 2026-01-23T08:00:00Z
- Published: 2026-01-23T08:00:07.328Z
- Typefully URL: https://typefully.com/?d=7881440&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2014609071392076100

"Will you cover LangChain and LangGraph in the course?"

I often get this question from participants in the AI Engineering Buildcamp.

That's why I've decided to include LangChain and LangGraph as optional material in Week 3.

The upcoming iteration of the course maintains a strong engineering focus, avoiding an overly broad scope across frameworks.

We emphasize building concepts from scratch, using frameworks only to clarify ideas.

In addition to LangChain and LangGraph, the course also incorporates:

🔸 OpenAI Agents SDK
🔸 Google's Agent Development Kit (ADK)
🔸 CrewAI

The main framework for the course is Pydantic AI.

Sign up for the course here: https://maven.com/alexey-grigorev/from-rag-to-agents. It starts in 2 days.

Media IDs: `2ba78c36-5399-4a8c-91e1-7353a38913c2`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7420374759823114240

"Will you cover LangChain and LangGraph in the course?"

I often get this question from participants in the AI Engineering Buildcamp.

That's why I've decided to include LangChain and LangGraph as optional material in Week 3.

The upcoming iteration of the course maintains a strong engineering focus, avoiding an overly broad scope across frameworks.

We emphasize building concepts from scratch, using frameworks only to clarify ideas.

In addition to LangChain and LangGraph, the course also incorporates:

🔸 OpenAI Agents SDK
🔸 Google's Agent Development Kit (ADK)
🔸 CrewAI

The main framework for the course is Pydantic AI.

Sign up for the course here: https://maven.com/alexey-grigorev/from-rag-to-agents. It starts in 2 days.

Media IDs: `2ba78c36-5399-4a8c-91e1-7353a38913c2`

## AI Engineering Buildcamp Revamp

- Typefully ID: `7881587`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-21T15:24:13.281Z
- Updated: 2026-01-21T18:04:53.442Z
- Scheduled: 2026-01-22T08:00:00Z
- Published: 2026-01-22T08:00:10.700Z
- Typefully URL: https://typefully.com/?d=7881587&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2014246697640272259

I'm restructuring the AI Engineering Buildcamp curriculum.

Some of the AI Engineering Buildcamp course participants from the first cohort shared this feedback with me:

"The content is extremely dense and valuable, but the pace felt too fast."

For people with full-time jobs, there wasn't always enough time to pause, process, and practice. At the same time, some learners wanted more depth, more tools, more comparisons.

That's why I decided to redesign the course to make it more focused.

That way:

🔸 Busy professionals can focus on what matters
🔸 Those who want to go deeper still have room to explore

The new structure will have a clear, mandatory path, with optional material layered on top.

The same principle applies to frameworks: One primary framework for depth and clarity, and other frameworks as optional context

The goal is not to teach every tool.

The goal is to understand agents well enough to:

🔸 Evaluate frameworks
🔸 Adopt them when needed
🔸 Replace them when necessary

I'll share a detailed breakdown of the new structure and the reasoning behind it in my upcoming Substack newsletter: https://alexeyondata.substack.com/

Media IDs: `29f56bf6-1b37-4e68-9b65-f5cb2ddfe28e`, `ec4c0e61-00bd-45f0-bc76-55d71bb9081d`, `a823f4a9-2c00-486b-8d67-3bf262e4c16a`, `d3dec37b-d280-4a74-bf5a-0c71f9822498`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7420012387925188609

I'm restructuring the AI Engineering Buildcamp curriculum.

Some of the AI Engineering Buildcamp course participants from the first cohort shared this feedback with me:

"The content is extremely dense and valuable, but the pace felt too fast."

For people with full-time jobs, there wasn't always enough time to pause, process, and practice. At the same time, some learners wanted more depth, more tools, more comparisons.

That's why I decided to redesign the course to make it more focused.

That way:

🔸 Busy professionals can focus on what matters
🔸 Those who want to go deeper still have room to explore

The new structure will have a clear, mandatory path, with optional material layered on top.

The same principle applies to frameworks: One primary framework for depth and clarity, and other frameworks as optional context

The goal is not to teach every tool.

The goal is to understand agents well enough to:

🔸 Evaluate frameworks
🔸 Adopt them when needed
🔸 Replace them when necessary

I'll share a detailed breakdown of the new structure and the reasoning behind it in my upcoming Substack newsletter: https://alexeyondata.substack.com/

Media IDs: `e863fa93-fe38-45a6-8fd7-f625a79dd434`

## Renaming to AI Engineering Buildcamp

- Typefully ID: `7880858`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-21T14:03:05.869Z
- Updated: 2026-01-21T14:40:44.370Z
- Scheduled: 2026-01-21T15:00:00Z
- Published: 2026-01-21T15:00:17.869Z
- Typefully URL: https://typefully.com/?d=7880858&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2013990024170348682

#### Post 1

I'm renaming AI Bootcamp to AI Engineering Buildcamp.

Why?

1. The Bootcamp term has become overloaded.

2. This course has always been about learning by doing and working on projects: agents, pipelines, systems with evaluation, monitoring, and guardrails.

The name Buildcamp reflects that focus much better:

🔸 Building real systems
🔸 An engineering mindset
🔸 A lot of hands-on work
🔸 Concrete, reusable results

The core material and focus of the course stay the same.

But I'm refining the outline to make it more focused and more engineering-driven

I'll explain the reasoning and what's changing in more detail in the next Substack post on Friday. Subscribe here: https://alexeyondata.substack.com/

Media IDs: `f3e81bbe-c0e7-450b-9342-e6f3108e86ea`

#### Post 2

The AI Engineering Buildcamp (formerly AI Bootcamp) is my course where I teach how to build production-ready AI agents. 

The next cohort starts in just 5 days: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7419755712731512832

I'm renaming AI Bootcamp to AI Engineering Buildcamp.

Why?

1. The Bootcamp term has become overloaded.

2. This course has always been about learning by doing and working on projects: agents, pipelines, systems with evaluation, monitoring, and guardrails.

The name Buildcamp reflects that focus much better:

🔸 Building real systems
🔸 An engineering mindset
🔸 A lot of hands-on work
🔸 Concrete, reusable results

The core material and focus of the course stay the same.

But I'm refining the outline to make it more focused and more engineering-driven

I'll explain the reasoning and what's changing in more detail in the next Substack post on Friday. Subscribe here: https://alexeyondata.substack.com/

Media IDs: `f3e81bbe-c0e7-450b-9342-e6f3108e86ea`

## Guardrails for AI Agents

- Typefully ID: `7867583`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-01-20T10:20:13.402Z
- Updated: 2026-01-20T10:31:06.128Z
- Scheduled: 2026-01-21T08:00:00Z
- Published: 2026-01-21T08:00:10.416Z
- Typefully URL: https://typefully.com/?d=7867583&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2013884308084359537

I recently ran a workshop on guardrails for AI agents.

The goal was to make agents safer and more predictable in real-world use.

We started by building a small FAQ assistant, then added guardrails on top:

🔸 Input guardrails to block irrelevant or unsafe requests before the agent runs
🔸 Output guardrails to prevent inappropriate promises, policy violations, or leakage

We also covered how to:

🔸 Cancel agent execution early when a guardrail trips
🔸 Run guardrails in parallel to avoid extra latency
🔸 Enforce boundaries like academic integrity and scope limits

Materials are public:
🔸 Video: https://www.youtube.com/watch?v=Sk1aqwNJWT4
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop covers one slice of a bigger picture.

In the AI Bootcamp: From RAG to Agents, we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Enrollment for the next cohort closes in 5 days: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `a60bd27b-b5e3-4d0d-bca6-ec66bd8a11c5`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7419650014010036225

I recently ran a workshop on guardrails for AI agents.

The goal was to make agents safer and more predictable in real-world use.

We started by building a small FAQ assistant, then added guardrails on top:

🔸 Input guardrails to block irrelevant or unsafe requests before the agent runs
🔸 Output guardrails to prevent inappropriate promises, policy violations, or leakage

We also covered how to:

🔸 Cancel agent execution early when a guardrail trips
🔸 Run guardrails in parallel to avoid extra latency
🔸 Enforce boundaries like academic integrity and scope limits

Materials are public:
🔸 Video: https://www.youtube.com/watch?v=Sk1aqwNJWT4
🔸 Code: https://github.com/alexeygrigorev/workshops/tree/main/guardrails

This workshop covers one slice of a bigger picture.

In the AI Bootcamp: From RAG to Agents, we go deeper into agent design, evaluation, monitoring, and guardrails as a system.

Enrollment for the next cohort closes in 5 days: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `ffa39014-ad79-4e26-a1c4-8ac97184eb61`

## Building Skills.md Workshop

- Typefully ID: `7867216`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-01-20T09:34:22.097Z
- Updated: 2026-01-20T10:14:01.242Z
- Published: 2026-01-20T10:15:16.776Z
- Typefully URL: https://typefully.com/?d=7867216&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2013555897499558266

#### Post 1

Last week, I hosted a workshop on Skills.md from scratch.

We didn't focus on "using Claude's skills." I showed how to implement them from scratch in your own coding agent.

Here's how we did it:

🔸 Began with a Django project builder created a few months ago
🔸 Extended it into a general-purpose coding agent
🔸 Added skills: modular capabilities that the agent loads on demand
🔸 Added commands: user-facing shortcuts

For workshop preparation, I reviewed OpenCode, an open-source alternative to Claude Code, and used it as a reference to propose a simpler, more transparent implementation in Python.

1/3

Media IDs: `172a5c32-3223-42d8-be98-305a43ec338c`

#### Post 2

The audience feedback was very positive.

You can replicate it too. Here are the workshop materials:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Notebook: https://github.com/alexeygrigorev/workshops/blob/main/agent-skills/README.md

2/3

#### Post 3

This workshop is a sneak peek into my upcoming AI Bootcamp course. Join it for a deeper coverage of the concepts behind AI agents: LLMs, RAG, MCP, and making your project production-ready.

Join the course if you're interested in learning how to build agents in depth, with a structured curriculum and direct support: https://maven.com/alexey-grigorev/from-rag-to-agents

3/3

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7419321587134464000

Last week, I hosted a workshop on Skills.md from scratch.

We didn't focus on "using Claude's skills." I showed how to implement them from scratch in your own coding agent.

Here's how we did it:

🔸 Began with a Django project builder created a few months ago
🔸 Extended it into a general-purpose coding agent
🔸 Added skills: modular capabilities that the agent loads on demand
🔸 Added commands: user-facing shortcuts

For workshop preparation, I reviewed OpenCode, an open-source alternative to Claude Code, and used it as a reference to propose a simpler, more transparent implementation in Python.

The audience feedback was very positive.

You can replicate it too. Here are the workshop materials:

🔸 Video: https://youtu.be/OhgDEZfHsvg
🔸 Notebook: https://github.com/alexeygrigorev/workshops/blob/main/agent-skills/README.md

This workshop is a sneak peek into my upcoming AI Bootcamp course. Join it for a deeper coverage of the concepts behind AI agents: LLMs, RAG, MCP, and making your project production-ready.

Media IDs: `172a5c32-3223-42d8-be98-305a43ec338c`

## Skills.md from Scratch: Build a Skill-Driven Coding Agent

- Typefully ID: `7796683`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-01-12T10:33:10.514Z
- Updated: 2026-01-12T10:40:01.183Z
- Scheduled: 2026-01-12T15:00:00Z
- Published: 2026-01-12T15:00:16.627Z
- Typefully URL: https://typefully.com/?d=7796683&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2010728540183105812

I'm running a live workshop on building skill-driven coding agents from first principles.

Date: Tue, Jan 13, 2026
Place: Online (Zoom)

In this session, I'll show how to structure agent behavior using explicit, reusable skills instead of large prompts or hidden logic.

We'll work step by step on:

🔸 How a skills file is structured, and why metadata-first design enables progressive loading
🔸 How to implement a simple skill registry that scans folders, parses metadata, and loads skills on demand
🔸 How to use these skills inside an agent loop to solve real coding tasks

Sign up for free: https://maven.com/p/1b423c/skills-md-from-scratch-build-a-skill-driven-coding-agent

Media IDs: `97c04842-a0d7-46ac-8fd3-89a10934a82f`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7416494229096591360

I'm running a live workshop on building skill-driven coding agents from first principles.

Date: Tue, Jan 13, 2026
Place: Online (Zoom)

In this session, I'll show how to structure agent behavior using explicit, reusable skills instead of large prompts or hidden logic.

We'll work step by step on:

🔸 How a skills file is structured, and why metadata-first design enables progressive loading
🔸 How to implement a simple skill registry that scans folders, parses metadata, and loads skills on demand
🔸 How to use these skills inside an agent loop to solve real coding tasks

Sign up for free: https://maven.com/p/1b423c/skills-md-from-scratch-build-a-skill-driven-coding-agent

Media IDs: `97c04842-a0d7-46ac-8fd3-89a10934a82f`

## AI Bootcamp Scholarship Opportunity

- Typefully ID: `7764303`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2026-01-08T10:52:33.200Z
- Updated: 2026-01-08T10:57:19.165Z
- Scheduled: 2026-01-08T11:00:00Z
- Published: 2026-01-08T11:00:11.012Z
- Typefully URL: https://typefully.com/?d=7764303&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2009218567464734930

Last change to apply for the scholarship for AI Bootcamp: from RAG to Agents

The course costs $1,799 but I'm offering full and partial scholarships 

I'm closing the form tomorrow and will contact the selected participants by Monday

If you haven't applied yet, here's the link:

https://forms.gle/u1SYszg4R6kzdjrS8

If you can read more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents/

See you soon on the course!

Media IDs: `40304abc-a918-4e81-9bcc-3716143200f6`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7414984257376337920

Last change to apply for the scholarship for AI Bootcamp: from RAG to Agents

The course costs $1,799 but I'm offering full and partial scholarships 

I'm closing the form tomorrow and will contact the selected participants by Monday

If you haven't applied yet, here's the link:

https://forms.gle/u1SYszg4R6kzdjrS8

If you can read more about the course here: https://maven.com/alexey-grigorev/from-rag-to-agents/

See you soon on the course!

Media IDs: `40304abc-a918-4e81-9bcc-3716143200f6`

## Building Safe AI Agents with Guardrails

- Typefully ID: `7723951`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2026-01-04T15:06:24.629Z
- Updated: 2026-01-04T15:12:59.705Z
- Scheduled: 2026-01-05T12:00:00Z
- Published: 2026-01-05T12:00:22.525Z
- Typefully URL: https://typefully.com/?d=7723951&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2008146551915565526

Guardrails are critical for AI agents

With AI agents that take actions, failures become real risks

Without guardrails, agents can:

🔶 Call the wrong tools
🔶 Let users misuse your product
🔶 Ignore hard constraints
🔶 Leak sensitive data
🔶 Fail silently while looking “successful”
🔶 Damage your company’s reputation

Prompts alone don’t solve this. We need a way to check whether the inputs and outputs of our agents conform to the standards we define.

That’s where guardrails come in. Tomorrow, we’ll learn how to add safety checks to your agents.

You’ll learn how to:

🔶 Build a working agent from scratch
🔶 Understand where guardrails actually sit
🔶 Apply production-ready input, tool, and output guardrails
🔶 Use a reusable mental model across agents and frameworks

If you’re moving from demos to production, this is a must.

Sign up here: https://maven.com/p/569db8/building-safe-ai-agents-with-guardrails

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7413912247942660097

Guardrails are critical for AI agents

With AI agents that take actions, failures become real risks

Without guardrails, agents can:

🔶 Call the wrong tools
🔶 Let users misuse your product
🔶 Ignore hard constraints
🔶 Leak sensitive data
🔶 Fail silently while looking “successful”
🔶 Damage your company’s reputation

Prompts alone don’t solve this. We need a way to check whether the inputs and outputs of our agents conform to the standards we define.

That’s where guardrails come in. Tomorrow, we’ll learn how to add safety checks to your agents.

You’ll learn how to:

🔶 Build a working agent from scratch
🔶 Understand where guardrails actually sit
🔶 Apply production-ready input, tool, and output guardrails
🔶 Use a reusable mental model across agents and frameworks

If you’re moving from demos to production, this is a must.

Sign up here: https://maven.com/p/569db8/building-safe-ai-agents-with-guardrails

## AI Agents: Modular Skills

- Typefully ID: `7646646`
- Status: published
- Tags: `workshop`, `ai-engineering-buildcamp`
- Created: 2025-12-25T06:23:18.811Z
- Updated: 2025-12-26T09:09:12.810Z
- Scheduled: 2025-12-29T08:00:00Z
- Published: 2025-12-29T08:00:09.109Z
- Typefully URL: https://typefully.com/?d=7646646&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2005549370482270481

#### Post 1

AI agents are moving beyond single-shot prompts and ad-hoc customization.

They shift toward modular, reusable procedural knowledge, now called agent skills.

Over the last few weeks, this trend has become very concrete:

1. Anthropic introduced Agent Skills as an open standard, extending the ideas behind MCP and making skills portable across tools and models

2. OpenAI adopted a similar concept for Codex

3. Visual Studio Code added support for the open Agent Skills spec, allowing skills to live next to code and be used directly by agents like GitHub Copilot

That motivated me to create a new live workshop on agent skills.

🔸 Tue, Jan 13, 2026
🔸 Online (Zoom)
🔸 Free to join

What we'll do during the workshop:

🔸 Understand the skills model
🔸 Implement a skill registry system
🔸 Apply skills inside an agent loop

Sign up for free: https://maven.com/p/1b423c/skills-md-from-scratch-build-a-skill-driven-coding-agent

Media IDs: `ede12933-1845-47ba-ac48-1e98d30519fe`, `e3da66b7-612c-40fc-882a-e59f66c459b2`

#### Post 2

If you want to go deeper afterward, I’ll also connect this to RAG-based systems and multi-agent setups in the AI Bootcamp: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7411315058405888000

AI agents are moving beyond single-shot prompts and ad-hoc customization.

They shift toward modular, reusable procedural knowledge, now called agent skills.

Over the last few weeks, this trend has become very concrete:

1. Anthropic introduced Agent Skills as an open standard, extending the ideas behind MCP and making skills portable across tools and models

2. OpenAI adopted a similar concept for Codex

3. Visual Studio Code added support for the open Agent Skills spec, allowing skills to live next to code and be used directly by agents like GitHub Copilot

That motivated me to create a new live workshop on agent skills.

🔸 Tue, Jan 13, 2026
🔸 Online (Zoom)
🔸 Free to join

What we'll do during the workshop:

🔸 Understand the skills model
🔸 Implement a skill registry system
🔸 Apply skills inside an agent loop

Sign up for free: https://maven.com/p/1b423c/skills-md-from-scratch-build-a-skill-driven-coding-agent

Media IDs: `ede12933-1845-47ba-ac48-1e98d30519fe`

## AI System for arXiv Research

- Typefully ID: `7646738`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-25T06:43:39.835Z
- Updated: 2025-12-25T06:47:46.717Z
- Scheduled: 2026-01-02T08:00:00Z
- Published: 2026-01-02T08:00:09.140Z
- Typefully URL: https://typefully.com/?d=7646738&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2006998934041014778

One of the recent final projects from my AI Bootcamp:

Sanjana Srinivasan built a full-stack agentic system for research question answering over arXiv papers, from retrieval to evaluation.

What the system does:

🔸 Searches and indexes arXiv research papers
🔸 Uses agents to retrieve, summarize, and answer research questions
🔸 Includes a search quality verification agent to improve answer reliability
🔸 Provides a Streamlit UI backed by a FastAPI service
🔸 Tracks logs, runs evaluations, and compares metrics across iterations

The project uses OpenAI models, PydanticAI, Elasticsearch, FastAPI, Streamlit, and Docker.

Project repo: https://github.com/sanjana14srini/capstone_project_ai-bootcamp

If you're curious what people can build after learning RAG, agents, tool calling, evaluations, and monitoring, this project is a great example.

The next AI Bootcamp cohort starts Jan 26, 2026. If you want to build systems like this, join the course: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `49736b9f-6a31-468b-9e68-3b5e3b04db03`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7412764623264956417

One of the recent final projects from my AI Bootcamp:

Sanjana Srinivasan built a full-stack agentic system for research question answering over arXiv papers, from retrieval to evaluation.

What the system does:

🔸 Searches and indexes arXiv research papers
🔸 Uses agents to retrieve, summarize, and answer research questions
🔸 Includes a search quality verification agent to improve answer reliability
🔸 Provides a Streamlit UI backed by a FastAPI service
🔸 Tracks logs, runs evaluations, and compares metrics across iterations

The project uses OpenAI models, PydanticAI, Elasticsearch, FastAPI, Streamlit, and Docker.

Project repo: https://github.com/sanjana14srini/capstone_project_ai-bootcamp

If you're curious what people can build after learning RAG, agents, tool calling, evaluations, and monitoring, this project is a great example.

The next AI Bootcamp cohort starts Jan 26, 2026. If you want to build systems like this, join the course: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `49736b9f-6a31-468b-9e68-3b5e3b04db03`

## AI Bootcamp Graduate Projects

- Typefully ID: `7600493`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-19T13:37:36.870Z
- Updated: 2025-12-23T16:26:11.554Z
- Scheduled: 2025-12-30T15:00:00Z
- Published: 2025-12-30T15:00:43.965Z
- Typefully URL: https://typefully.com/?d=7600493&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2006017526770327556

#### Post 1

4 AI agents built by AI Bootcamp graduates:

1. Cybersecurity Disclosure Agent
2. User Satisfaction Analyst
3. Habit Builder Agent
4. Intelligent Email Agent

🧵

Media IDs: `b19583d8-1543-4470-9e94-cb0fa9ab3121`, `c3dc4c3d-57ca-4938-9f3b-efa64ba3657c`, `186a2729-29d7-46bb-b7a1-9221c0945da2`, `fea5eae4-dae0-433f-a804-b54427540c33`

#### Post 2

1. Cybersecurity Disclosure Agent

Scott DeGeest built an ingestion pipeline for SEC filings. The system parses raw, often malformed XML and performs entity resolution to link subsidiaries to parent companies. The cleaned data is indexed in Elasticsearch for retrieval.

Media IDs: `e7038560-9855-437f-805e-e75208fe704e`

#### Post 3

2. User Satisfaction Analyst

Carlos Pumar-Frohberg implemented a multi-agent orchestrator. The main model routes queries based on intent. Unstructured text queries are sent to a MongoDB agent, while relationship questions are routed to a Neo4j graph agent.

Media IDs: `3514c481-5d2f-4ea2-a1c5-40d57fdcd53a`

#### Post 4

3. Habit Builder Agent

Vanchesca Dinh built a high-fidelity RAG pipeline. She used Faster Whisper to transcribe audio feeds and stored embeddings in Qdrant. She implemented query rewriting for better retrieval and used Pydantic to enforce guardrails on the output.

Media IDs: `3f2473bb-a157-4341-a625-cca359002c59`

#### Post 5

4. Intelligent Email Agent

Asia Amodeo integrated the Gmail API directly with Elasticsearch. The system fetches emails and indexes them, enabling semantic search over a personal inbox through a Streamlit interface.

Media IDs: `1b4c11ef-afc0-4953-9a61-86cd607671b7`

#### Post 6

I wrote a detailed breakdown of the architecture for these projects in my recent post: https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais

#### Post 7

A new iteration of the AI Bootcamp starts on January 26, 2026.

It's live, hands-on, and focused on building production-ready AI agents step by step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7411783215385919488

4 AI agents built by AI Bootcamp graduates:

1. Cybersecurity Disclosure Agent

Scott DeGeest built an ingestion pipeline for SEC filings. The system parses raw, often malformed XML and performs entity resolution to link subsidiaries to parent companies. The cleaned data is indexed in Elasticsearch for retrieval.

2. User Satisfaction Analyst

Carlos Pumar-Frohberg implemented a multi-agent orchestrator. The main model routes queries based on intent. Unstructured text queries are sent to a MongoDB agent, while relationship questions are routed to a Neo4j graph agent.

3. Habit Builder Agent

Vanchesca Dinh built a high-fidelity RAG pipeline. She used Faster Whisper to transcribe audio feeds and stored embeddings in Qdrant. She implemented query rewriting for better retrieval and used Pydantic to enforce guardrails on the output.

4. Intelligent Email Agent

Asia Amodeo integrated the Gmail API directly with Elasticsearch. The system fetches emails and indexes them, enabling semantic search over a personal inbox through a Streamlit interface.

I wrote a detailed breakdown of the architecture for these projects in my recent post: https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais

Media IDs: `e7038560-9855-437f-805e-e75208fe704e`, `3514c481-5d2f-4ea2-a1c5-40d57fdcd53a`, `3f2473bb-a157-4341-a625-cca359002c59`, `1b4c11ef-afc0-4953-9a61-86cd607671b7`

## Reminder: AI Bootcamp Scholarships

- Typefully ID: `7623368`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-22T12:03:38.331Z
- Updated: 2025-12-23T09:05:56.288Z
- Scheduled: 2025-12-24T15:00:00Z
- Published: 2025-12-24T15:00:11.946Z
- Typefully URL: https://typefully.com/?d=7623368&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2003843151010926820

Quick reminder: If you're interested in my next AI Bootcamp and haven't applied for a scholarship spot yet, now is your chance.

I understand that not everyone can afford a paid program, but many are highly motivated to learn and build.

This iteration includes several scholarship spots.

You can apply for a scholarship here: https://forms.gle/u1SYszg4R6kzdjrS8

Last time I shared this form, it spread widely, and I received thousands of applications, so don't wait too long.

🔸 Course starts: January 26, 2026
🔸 Format: Live, hands-on
🔸 Focus: Building production-ready AI agents, step by step

If you know someone who could benefit from a scholarship, please share this with them.

Media IDs: `2dc8aa5c-c50e-49ba-8343-45305714d3f6`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7409608833024733184

Quick reminder: If you're interested in my next AI Bootcamp and haven't applied for a scholarship spot yet, now is your chance.

I understand that not everyone can afford a paid program, but many are highly motivated to learn and build.

This iteration includes several scholarship spots.

You can apply for a scholarship here: https://forms.gle/u1SYszg4R6kzdjrS8

Last time I shared this form, it spread widely, and I received thousands of applications, so don't wait too long.

🔸 Course starts: January 26, 2026
🔸 Format: Live, hands-on
🔸 Focus: Building production-ready AI agents, step by step

If you know someone who could benefit from a scholarship, please share this with them.

Media IDs: `2dc8aa5c-c50e-49ba-8343-45305714d3f6`

## Maximize Learning Budget Benefits

- Typefully ID: `7587280`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-18T06:48:13.298Z
- Updated: 2025-12-18T07:53:02.452Z
- Scheduled: 2025-12-18T08:00:00Z
- Published: 2025-12-18T08:00:11.721Z
- Typefully URL: https://typefully.com/?d=7587280&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2001563126861537293

The end of the year is a good time to review your learning budget.

If your company offers a learning budget and you haven't used it yet, now is usually the easiest moment to do so.

If you're considering joining the next iteration of my AI Bootcamp, you can use your learning budget to sign up. The next cohort starts in January 2026.

I've prepared a short message you can send to your manager to request approval for expensing AI Bootcamp: https://docs.google.com/document/d/12LBC7KBR_NE-ehSf7YTOOTlMgPD_0g-KU7g5KxTxpbs/edit?usp=sharing

Thanks to Tereza Iofciu for the friendly reminder about the end of the year and the opportunity to use learning expenses!

Media IDs: `bac074c5-6cd9-4679-a024-9b4760f30b4a`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7407328816706146305

The end of the year is a good time to review your learning budget.

If your company offers a learning budget and you haven't used it yet, now is usually the easiest moment to do so.

If you're considering joining the next iteration of my AI Bootcamp, you can use your learning budget to sign up. The next cohort starts in January 2026.

I've prepared a short message you can send to your manager to request approval for expensing AI Bootcamp: https://docs.google.com/document/d/12LBC7KBR_NE-ehSf7YTOOTlMgPD_0g-KU7g5KxTxpbs/edit?usp=sharing

Thanks to Tereza Iofciu for the friendly reminder about the end of the year and the opportunity to use learning expenses!

Media IDs: `bac074c5-6cd9-4679-a024-9b4760f30b4a`

## Top Workshop of 2025

- Typefully ID: `7577469`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-17T07:29:47.705Z
- Updated: 2025-12-17T10:53:53.730Z
- Scheduled: 2025-12-19T08:00:00Z
- Published: 2025-12-19T08:00:10.471Z
- Typefully URL: https://typefully.com/?d=7577469&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2001925497610211698

#### Post 1

My "Build Your Own Coding Agent" workshop was recognized as one of Maven's top-performing lessons of 2025!

It will be featured in their "Maven Rewind: Best of 2025" series.

Thank you to everyone who participated, asked questions, and worked on building agents during the workshop!

Use this link to get the document containing all materials and links: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `f07485ac-5869-40bd-aed6-ffb533ff3b6b`

#### Post 2

This workshop was a preview for my AI Bootcamp course. Its next iteration will start on January 26, 2026.

The course is live, hands-on, and focuses on building production-ready AI agents step by step.

You can read more about it here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7407691190000857089

My "Build Your Own Coding Agent" workshop was recognized as one of Maven's top-performing lessons of 2025!

It will be featured in their "Maven Rewind: Best of 2025" series.

Thank you to everyone who participated, asked questions, and worked on building agents during the workshop!

Use this link to get the document containing all materials and links: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `f07485ac-5869-40bd-aed6-ffb533ff3b6b`

## AI Bootcamp new review

- Typefully ID: `7559369`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-15T12:02:02.376Z
- Updated: 2025-12-17T10:49:07.540Z
- Scheduled: 2025-12-23T08:00:00Z
- Published: 2025-12-23T08:00:22.205Z
- Typefully URL: https://typefully.com/?d=7559369&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2003375109969707081

Just got a new review for my AI Bootcamp.

What stood out to me in this feedback is the emphasis on:

🔸 Evaluation and testing
🔸 Software engineering practices
🔸 Building agentic systems that work beyond demos

The second iteration starts soon.

Start date: January 26, 2026
Format: live, hands-on
Focus: designing, building, and evaluating reliable AI agents

If you want to move from RAG prototypes to systems you can actually ship, this course might be useful.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `fc3e2994-03be-4d03-b7ed-53de2815887b`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7409140792818057216

Just got a new review for my AI Bootcamp.

What stood out to me in this feedback is the emphasis on:

🔸 Evaluation and testing
🔸 Software engineering practices
🔸 Building agentic systems that work beyond demos

The second iteration starts soon.

Start date: January 26, 2026
Format: live, hands-on
Focus: designing, building, and evaluating reliable AI agents

If you want to move from RAG prototypes to systems you can actually ship, this course might be useful.

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `fc3e2994-03be-4d03-b7ed-53de2815887b`

## Guide to AI Coding Agent

- Typefully ID: `7481850`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-07T13:16:09.728Z
- Updated: 2025-12-17T07:29:38.928Z
- Scheduled: 2025-12-17T08:00:00Z
- Published: 2025-12-17T08:00:09.603Z
- Typefully URL: https://typefully.com/?d=7481850&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/2001200729961472375

I have a guide on building your own AI coding agent from start to finish.

What's inside:

🔸 How to use function calling
🔸 Templates for all apps your agent will generate
🔸 A reusable set of file-operation functions
🔸 System prompt design

Get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `263f5890-4d44-4e61-ae65-b11599262467`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7406966418543456257

I have a guide on building your own AI coding agent from start to finish.

You can get it for free.

What's inside:

🔸 What function calling is and when to use it
🔸 Step-by-step guide to implementing function calling
🔸 A lightweight Python library to speed things up
🔸 A project template for all apps your agent will generate
🔸 A reusable set of file-operation functions for creating and modifying project files
🔸 System prompt design to keep the agent on task
🔸 Instructions on how to run everything locally

Get it via email here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `263f5890-4d44-4e61-ae65-b11599262467`

## AI Agents Course Scholarships

- Typefully ID: `7481590`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-07T12:36:47.578Z
- Updated: 2025-12-10T11:41:20.134Z
- Scheduled: 2025-12-12T08:00:00Z
- Published: 2025-12-12T08:00:23.335Z
- Typefully URL: https://typefully.com/?d=7481590&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1999388801400209501

#### Post 1

I'm launching a new iteration of my AI Bootcamp.

This time, I also offer several scholarship spots.

I understand that ot everyone has the budget for a paid program, but many are eager to learn, practice, and develop their skills.

1/5

Media IDs: `2eeb4fa0-ad86-4e6a-8821-49142ef103b8`

#### Post 2

The course starts on January 26, 2026. It's live, hands-on, and focused on building production-ready AI agents step by step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

I hope this makes the program more accessible to those who need it most.

2/5

#### Post 3

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/u1SYszg4R6kzdjrS8

3/5

#### Post 4

If you want to learn more about what you can build during this course, join the AI Bootcamp Demo Day next Monday: https://maven.com/p/599db5/ai-bootcamp-demo-day

4/5

#### Post 5

Please share it with your network so more people who need a scholarship can see it. Thank you for helping spread the word!

5/5

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7405154497238351873

I'm launching a new iteration of my AI Bootcamp.

This time, I also offer several scholarship spots.

I understand that ot everyone has the budget for a paid program, but many are eager to learn, practice, and develop their skills.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/u1SYszg4R6kzdjrS8.

Last time, this form went viral, and I got thousands of applications.

The course starts on January 26, 2026. It's live, hands-on, and focused on building production-ready AI agents step by step.

I hope this makes the program more accessible to those who need it most.

If you want to learn more about what you can build during this course, join the AI Bootcamp Demo Day next Monday: https://maven.com/p/599db5/ai-bootcamp-demo-day

Please share this with your network so more people in need of a scholarship can see it. Thank you for helping spread the word!

Media IDs: `b80b515a-9c10-4ab9-b1f2-ba6604b8006b`

## AI Bootcamp Demo Day

- Typefully ID: `7434740`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-02T18:02:43.414Z
- Updated: 2025-12-07T12:48:15.604Z
- Scheduled: 2025-12-11T08:00:00Z
- Published: 2025-12-11T08:00:16.097Z
- Typefully URL: https://typefully.com/?d=7434740&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1999026393683017940

#### Post 1

Join me next Monday for the AI Bootcamp Demo Day!

Course graduates will present their projects: end-to-end implementations of RAG and agentic systems.

🔸 Date: Monday, December 15
🔸 Time: 5 PM CET
🔸 Format: Online on Zoom, free to join
🔸 Link: https://maven.com/p/599db5/ai-bootcamp-demo-day

1/4

Media IDs: `d442531b-150d-4f21-a5c4-5afc701fd739`

#### Post 2

If you'd like to understand how modern AI systems work beyond simple demos, this session is a rare chance to see real projects built by practitioners.

2/4

#### Post 3

You'll see how they approached testing, evaluation, observability, and workflow design: the parts that most courses skip, but that make AI systems reliable in real environments.

3/4

#### Post 4

Register here: https://maven.com/p/599db5/ai-bootcamp-demo-day

4/4

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7404792081837428736

Join me next Monday for the AI Bootcamp Demo Day!

Course graduates will present the projects they’ve built over the past few weeks: practical, end-to-end implementations of RAG and agentic systems.

🔸 Date: Monday, December 15
🔸 Time: 5 PM CET
🔸 Format: Online on Zoom, free to join

Here are some of the examples of the projects graduates built:

🔸 A search-driven agent that helps teams understand client satisfaction by aggregating signals across documents and conversations.
🔸 An AI agent for public procurement transparency that collects, parses, and analyzes contracts from HTML and PDF documents. It extracts key fields, stores them in a structured knowledge base, and uses RAG to answer questions about public spending.

If you'd like to understand how modern AI systems work beyond simple demos, this session is a rare chance to see real projects built by practitioners.

Register here to receive a Zoom invite: https://maven.com/p/599db5/ai-bootcamp-demo-day

Media IDs: `d442531b-150d-4f21-a5c4-5afc701fd739`

## AI Bootcamp testimonial

- Typefully ID: `7371800`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-11-25T17:21:20.653Z
- Updated: 2025-12-07T12:31:22.257Z
- Scheduled: 2025-12-10T15:00:00Z
- Published: 2025-12-10T15:00:34.310Z
- Typefully URL: https://typefully.com/?d=7371800&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1998769779038105695

#### Post 1

Just received a new testimonial for the AI Bootcamp.

Scott submitted his review, and I wanted to share it here because feedback like this keeps me motivated.

1/4

Media IDs: `2b362c75-08f3-4557-a60a-06fe568af7fe`

#### Post 2

Course rating: 10/10

Public review:

"The course provides an excellent introduction to the core tools needed to develop an agentic tool. Worth the effort, especially given the comprehensiveness of the options and solutions available in the course."

2/4

#### Post 3

It's always great to see participants finding real value in the material, especially in a field that evolves as quickly as AI and agentic systems.

Thank you, Scott, and thanks to everyone who has shared feedback so far.

It helps improve the bootcamp for future cohorts.

3/4

#### Post 4

You can find my AI bootcamp here: https://maven.com/alexey-grigorev/from-rag-to-agents

4/4

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7404535443264040960

Just received a new testimonial for the AI Bootcamp.

Scott submitted his review, and I wanted to share it here because feedback like this keeps me motivated.

Course rating: 10/10

Public review:
"The course provides an excellent introduction to the core tools needed to develop an agentic tool. Worth the effort, especially given the comprehensiveness of the options and solutions available in the course."

It's always great to see participants finding real value in the material, especially in a field that evolves as quickly as AI and agentic systems.

Thank you, Scott, and thanks to everyone who has shared feedback so far.

It helps improve the bootcamp for future cohorts.

Media IDs: `2b362c75-08f3-4557-a60a-06fe568af7fe`

## AI Bootcamp Graduate Project

- Typefully ID: `7465926`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-05T16:27:17.135Z
- Updated: 2025-12-07T11:46:24.933Z
- Scheduled: 2025-12-09T08:00:00Z
- Published: 2025-12-09T08:00:18.710Z
- Typefully URL: https://typefully.com/?d=7465926&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1998301629926531370

#### Post 1

I'm really proud of our AI Bootcamp participants! The projects they've built are amazing.

Asia Amodeo, one of the course participants, developed an intelligent email assistant using Elasticsearch, GPT-4o-mini, Gmail API, Streamlit, and Docker.

1/4

Media IDs: `b24b6cc2-6d58-4497-a44d-5ed32acdc8bf`

#### Post 2

Features:

🔸 Fetch and search Gmail
🔸 Perform semantic searches across thousands of emails
🔸 Search within PDF, DOCX, and spreadsheet attachments
🔸 Retrieve full conversation threads
🔸 Auto-categorize emails
🔸 Prioritize the inbox by urgency

2/4

#### Post 3

They also added a Streamlit monitoring dashboard to track logs, success rates, latency, and evaluation scores. Additionally, there's a testing and evaluation setup featuring manual tests, judge-based tests, and a small ground-truth dataset.

3/4

#### Post 4

It's an impressive work and a great example of treating AI as an engineering problem.

Join our upcoming AI Bootcamp Demo Day to see what course participants built during the course: https://maven.com/p/599db5/ai-bootcamp-demo-day

4/4

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7404067321239130113

I'm really proud of our AI Bootcamp participants! The projects they've built are amazing.

Asia Amodeo, one of the course participants, developed an intelligent email assistant using Elasticsearch, GPT-4o-mini, Gmail API, Streamlit, and Docker.

Features:

🔸 Fetch and search Gmail
🔸 Perform semantic searches across thousands of emails
🔸 Search within PDF, DOCX, and spreadsheet attachments
🔸 Retrieve full conversation threads
🔸 Auto-categorize emails
🔸 Prioritize the inbox by urgency

They also added a Streamlit monitoring dashboard to track logs, success rates, latency, and evaluation scores. Additionally, there's a testing and evaluation setup featuring manual tests, judge-based tests, and a small ground-truth dataset.

It's an impressive work and a great example of treating AI as an engineering problem.

Join our upcoming AI Bootcamp Demo Day to see what course participants built during the course: https://maven.com/p/599db5/ai-bootcamp-demo-day

Media IDs: `b24b6cc2-6d58-4497-a44d-5ed32acdc8bf`

## AI Bootcamp Demo Day

- Typefully ID: `7434732`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-12-02T18:02:18.532Z
- Updated: 2025-12-03T11:27:40.262Z
- Scheduled: 2025-12-05T08:00:00Z
- Published: 2025-12-05T08:00:18.858Z
- Typefully URL: https://typefully.com/?d=7434732&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1996852079185527164

#### Post 1

Curious what participants of my AI Bootcamp have been working on?

Join me for the AI Bootcamp Demo Day: a free, open session where you can see real projects built during the course.

🔸 Dec 15, 5 PM CET
🔸 Zoom
🔸 Free to join
🔸 Registration link: https://maven.com/p/599db5/ai-bootcamp-demo-day

1/4

Media IDs: `bed40b14-3c0b-47c2-b932-cdc6505db6c0`

#### Post 2

Course graduates will share:

🔸 Agentic workflows that go far beyond chatbots
🔸 Practical tools they've built: coding assistants, research agents, and more
🔸 How they tested, evaluated, and monitored their systems
🔸 The engineering practices they applied

2/4

#### Post 3

A key theme across all projects is reliability.

Course participants approached AI as an engineering problem: measurable, testable, and observable.

If you're hiring, evaluating agentic patterns, or looking for project inspiration, this session will be valuable for you.

3/4

#### Post 4

Register here: https://maven.com/p/599db5/ai-bootcamp-demo-day

4/4

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7402617767427788800

Curious what participants of my AI Bootcamp have been working on?

Join us for the AI Bootcamp Demo Day: a free, open session where you can see real projects built during the course.

🔸 December 15, 5 PM CET
🔸 Online (Zoom)
🔸 Free to join
🔸 Registration link: https://maven.com/p/599db5/ai-bootcamp-demo-day

Course graduates will share:

🔸 Agentic workflows that go far beyond chatbots
🔸 Practical tools: coding assistants, research agents, automation flows
🔸 How they tested, evaluated, and monitored their systems
🔸 The engineering practices needed to build AI that doesn't break in production

A key theme across all projects is reliability.

Course participants approached AI as an engineering problem: measurable, testable, and observable.

If you're hiring, evaluating agentic patterns, or looking for project inspiration, this session will be valuable for you.

Media IDs: `bed40b14-3c0b-47c2-b932-cdc6505db6c0`

## AI Bootcamp Leads Engineering - 30% Discount

- Typefully ID: `7371928`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-11-25T17:34:38.595Z
- Updated: 2025-11-25T17:50:55.320Z
- Scheduled: 2025-11-26T08:00:00Z
- Published: 2025-11-26T08:00:21.529Z
- Typefully URL: https://typefully.com/?d=7371928&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1993590622373163124

#### Post 1

My AI Bootcamp leads the engineering category on @MavenHQ!

Thanks to everyone who joined.

Use EARLYBIRD at checkout for a 30% discount (default 25%).

30% discount ends this month.

1/2

Media IDs: `246f217f-1596-4f95-8dd4-1fc89b59b434`

#### Post 2

The next cohort begins on January 26, 2026.

Excited to launch a new edition and really appreciate your amazing support!

You can register here: https://maven.com/alexey-grigorev/from-rag-to-agents

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7399356309898174464

My AI Bootcamp is the top-performing course in the engineering category on @[Maven](urn:li:organization:71958848).

Thank you so much to everyone who recently joined the course!

Enjoy a 30% discount with the EARLYBIRD promo code at checkout. The default discount is currently 25%.

This offer is valid until the end of the month.

The next cohort begins on January 26, 2026.

Excited to launch a new edition and really appreciate your amazing support!

You can register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `246f217f-1596-4f95-8dd4-1fc89b59b434`

## AI Bootcamp: Black Friday 35% Off

- Typefully ID: `7291600`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-11-17T11:18:17.512Z
- Updated: 2025-11-17T11:32:40.035Z
- Scheduled: 2025-11-28T08:00:00Z
- Published: 2025-11-28T08:00:08.987Z
- Typefully URL: https://typefully.com/?d=7291600&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1994315357629349897

I'm running a Black Friday discount for the upcoming cohort of my AI Bootcamp.

Enroll with 35% off and build production-ready AI systems.

Use the code BLACKFRIDAY at checkout: https://maven.com/alexey-grigorev/from-rag-to-agents?promoCode=BLACKFRIDAY

The discount is available until Monday (Dec 1).

Media IDs: `64bee7c5-6342-47b5-915d-0d6f1c9a6eb1`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7400081044789481474

I'm running a Black Friday discount for the upcoming cohort of my AI Bootcamp.

If you want to join the program on building production-ready AI systems, you can now enroll with 35% off.

Join the course to build with RAG, use agentic workflows, and set up monitoring and evaluation for your projects.

Use the code BLACKFRIDAY at checkout: https://maven.com/alexey-grigorev/from-rag-to-agents?promoCode=BLACKFRIDAY

The discount is available until Monday (Dec 1).

Media IDs: `64bee7c5-6342-47b5-915d-0d6f1c9a6eb1`

## AI Bootcamp: EARLYBIRD for 30%

- Typefully ID: `7291474`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-11-17T11:00:47.380Z
- Updated: 2025-11-17T11:28:28.838Z
- Scheduled: 2025-11-19T08:00:00Z
- Published: 2025-11-19T08:00:12.318Z
- Typefully URL: https://typefully.com/?d=7291474&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1991053869510795351

#### Post 1

I'm opening a new cohort of my AI Bootcamp, a practical course that takes you from basic RAG setups to production-ready agents.

Use promo code EARLYBIRD at checkout for 30% off: https://maven.com/alexey-grigorev/from-rag-to-agents

The promo code is only valid during November.

Media IDs: `5b42dcae-3503-46e5-8c2b-dd72ed304a19`

#### Post 2

You'll build:

🔸 RAG prototype for FAQs, YouTube, and docs
🔸 Data-driven prompt testing
🔸 Agentic flows: function calls, searches, PydanticAI, MCP
🔸 An agent for Django websites
🔸 Monitoring with Grafana, LangWatch, Evidently

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7396819559527182337

I'm opening a new cohort of my AI Bootcamp, a practical course that takes you from basic RAG setups to production-ready agents.

I teach you to build, evaluate, and monitor AI assistants, create deep research and coding agents, and more.

You'll build:

🔸 RAG prototype for FAQs, YouTube, and docs
🔸 Data-driven prompt testing
🔸 Agentic flows: function calls, searches, PydanticAI, MCP
🔸 An agent for Django websites
🔸 Monitoring with Grafana, LangWatch, Evidently
🔸 Capstone: AI app for your portfolio

You'll have a portfolio you can demo to clients and recruiters.

Use promo code EARLYBIRD at checkout for 30% off: https://maven.com/alexey-grigorev/from-rag-to-agents

The promo code is only valid during November.

Media IDs: `5b42dcae-3503-46e5-8c2b-dd72ed304a19`

## Efficient AI Agent Building

- Typefully ID: `6473955`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T14:36:39.083Z
- Updated: 2025-10-03T16:33:44.713Z
- Scheduled: 2025-10-05T07:00:00Z
- Published: 2025-10-05T07:00:07.078Z
- Typefully URL: https://typefully.com/?d=6473955&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1974731294270685677

#### Post 1

Last chance to join my AI Bootcamp!

We start on Oct 6, and today is your only day to enroll.

Learn to:

✅ Build your own AI agents with RAG, MCP, and function calling
✅ Test and optimize them
✅ Deploy safely with monitoring and guardrails

Your 15% discount 👇🏼

1/2

Media IDs: `04d1a65c-4c97-478b-84dc-dbb0e5cccd5c`

#### Post 2

Your promo code for 15% off: LASTCALL

Join here: https://maven.com/alexey-grigorev/from-rag-to-agents

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7380496983041523712

Last chance to join my AI Bootcamp!

We start tomorrow, and today is your only day to enroll.

Over 2 months, you'll learn to:

✅ Build your own AI agents with RAG, MCP, and function calling
✅ Test and optimize them
✅ Deploy safely with monitoring and guardrails

Find your 15% discount in the comments. 👇🏼

Media IDs: `04d1a65c-4c97-478b-84dc-dbb0e5cccd5c`

## AI Bootcamp Curriculum Updates

- Typefully ID: `6864488`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-30T10:50:51.794Z
- Updated: 2025-09-30T13:25:27.952Z
- Scheduled: 2025-10-01T07:00:00Z
- Published: 2025-10-01T07:00:12.003Z
- Typefully URL: https://typefully.com/?d=6864488&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1973281740069490998

#### Post 1

I've spoken to many of you, and based on your feedback, I've decided to update my AI Bootcamp curriculum.

Here's what's new:

#### Post 2

➡️ Change 1: Additional unit on data pipelines

We'll add more information on the basics of preparing your data for AI 

🔸 How data pipelines work
🔸 More examples

#### Post 3

➡️ Change 2: Two AI Agents instead of one for Module 4

🔸 AI coding assistant with multiple agents (planning, requirements, execution)
🔸 Agent for reviewing GitHub repos

#### Post 4

➡️ Change 3: Final hackathon

We'll conclude with a hackathon that tackles real community challenges.

Thank you to everyone who interviewed! Your feedback was very useful for shaping the course curriculum.

Join here: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7379047436297646080

I've spoken to many of you, and based on your feedback, I've decided to update my AI Bootcamp curriculum.

Here's what's new:

➡️ Change 1: Additional unit on data pipelines

We'll add more information on the basics of preparing your data for AI 

🔸 How data pipelines work
🔸 More examples 

➡️ Change 2: Two AI Agents instead of one for Module 4

🔸 AI coding assistant with multiple agents (planning, requirements, execution)
🔸 Agent for reviewing GitHub repos

➡️ Change 3: Final hackathon

We'll conclude with a hackathon that tackles real community challenges.

Thank you to everyone who interviewed! Your feedback was very useful for shaping the course curriculum.

Join here: https://maven.com/alexey-grigorev/from-rag-to-agents

## Practical NLP Workshop with LLMs

- Typefully ID: `6822247`
- Status: published
- Tags: `cross-promo`, `ai-engineering-buildcamp`
- Created: 2025-09-25T08:30:39.245Z
- Updated: 2025-09-25T09:17:20.275Z
- Scheduled: 2025-09-26T07:00:00Z
- Published: 2025-09-26T07:00:11.293Z
- Typefully URL: https://typefully.com/?d=6822247&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1971469808412786873

#### Post 1

Text data is messy.

Traditional NLP: powerful, but slow.

LLMs: not perfect, fast.

And make "good enough" NLP accessible to any engineer.

Doug Turnbull, a principal AI engineer in search, will join me to share his insights into practical NLP with LLMs.

🧵

Media IDs: `512ffb45-b8b4-40cf-b78c-73c2aa37b496`

#### Post 2

Doug will show you how to:

1. Use LLMs to clean, correct, and interpret messy text
2. Extract structure and meaning to make unstructured data usable
3. Apply these methods in real engineering workflows, not just demonstrations

1/2

#### Post 3

Date: Monday, Sept 29, 2025
Time: 17:00 CET (1 hour)
Format: Online (Zoom)
Cost: Free to join

Register here: https://maven.com/p/452707/practical-nlp-with-ll-ms-from-messy-text-to-value

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7377235497934430208

Text data is often messy.

Traditional NLP is powerful but slow.

While LLMs don't deliver "perfect" results, they make "good enough" NLP accessible to any engineer.

Using LLMs for NLP tasks is much faster than traditional methods.

My friend Doug Turnbull, a principal AI engineer in search, will join me in the upcoming workshop to share his insights into practical NLP with LLMs.

Date: Monday, Sept 29, 2025
Time: 17:00 CET (1 hour)
Format: Online (Zoom)
Cost: Free to join

Doug will show you how to:

1. Use LLMs to clean, correct, and interpret messy text
2. Extract structure and meaning to make unstructured data usable
3. Apply these methods in real engineering workflows, not just demonstrations

Register here: https://maven.com/p/452707/practical-nlp-with-ll-ms-from-messy-text-to-value

Media IDs: `cddc0b4d-2a29-4ae0-bd5a-5f874b144b17`

## AI Agent Email Course

- Typefully ID: `6804218`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-23T07:18:40.129Z
- Updated: 2025-09-23T07:30:10.676Z
- Scheduled: 2025-09-23T14:00:00Z
- Published: 2025-09-23T14:00:10.001Z
- Typefully URL: https://typefully.com/?d=6804218&a=188312

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7376254050029240321

I've just created a 7-day free email course on AI agents.

Build a complete AI agent using any GitHub project, from data ingestion to deployment.

🔸 Delivered by email, step by step
🔸 Hands-on lessons with practical exercises
🔸 Certificate of completion to showcase your new skills

What you'll do in 7 days:

1. Ingest and index your project data
2. Process and chunk code/docs with AI
3. Add lexical, semantic, and hybrid search
4. Build an agentic RAG system with function calling
5. Test and evaluate your agent
6. Deploy it with a simple UI
7. Share your results and add to your portfolio

👉 Sign up here: https://alexeygrigorev.com/aihero/

Media IDs: `af1e31ef-b664-4ee3-92b6-158c2eb1e97e`, `37c93e96-5a25-46b5-a560-b6d737444d45`, `707435ca-8e17-4e75-9cb1-207428e26ef5`, `6a5e0f7b-7a6b-47c7-a0e5-57733e44fee5`

## AI Agent Email Course

- Typefully ID: `6803870`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-23T06:20:06.043Z
- Updated: 2025-09-23T07:05:17.838Z
- Published: 2025-09-23T07:09:15.690Z
- Typefully URL: https://typefully.com/?d=6803870&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1970384928346120285

#### Post 1

Join my 7-day free email course on AI agents!

Learn to build a full AI agent from any GitHub project, covering:

🔸 Step-by-step email guidance
🔸 Hands-on exercises
🔸 Completion certificate to flaunt your skills!

Ready to dive in?

1/3

Media IDs: `002437df-a5f1-4630-a4e0-858dc3187220`, `9a9d91f5-794e-4f93-98a5-071472874b9c`, `73db70e6-b249-45b2-a2ef-c972c400e98d`, `74f8f1d2-26a7-44af-b203-a506a5f74691`

#### Post 2

What you'll do in 7 days:

1. Ingest and index your project data
2. Process and chunk code/docs with AI
3. Add lexical, semantic, and hybrid search

2/3

#### Post 3

4. Build an agentic RAG system with function calling
5. Test and evaluate your agent
6. Deploy it with a simple UI
7. Share your results and add to your portfolio

👉 Sign up here: https://alexeygrigorev.com/aihero/

3/3

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7376150694845792256

I've just created a 7-day free email course on AI agents.

Build a complete AI agent using any GitHub project, from data ingestion to deployment.

🔸 Delivered by email, step by step
🔸 Hands-on lessons with practical exercises
🔸 Certificate of completion to showcase your new skills

What you'll do in 7 days:

1. Ingest and index your project data
2. Process and chunk code/docs with AI
3. Add lexical, semantic, and hybrid search
4. Build an agentic RAG system with function calling
5. Test and evaluate your agent
6. Deploy it with a simple UI
7. Share your results and add to your portfolio

👉 Sign up here: https://alexeygrigorev.com/aihero/

Media IDs: `193c6833-524d-44b8-aaf2-a39c7b9846c3`, `d76fb2bf-54e2-485c-aa2f-4cedd616d380`, `085c79cf-a5b0-4118-a94b-1cec078068eb`, `c98ec1ab-8aa8-4be9-9c53-fd0193d6e068`

## AI Agents Course Scholarships

- Typefully ID: `6764144`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-18T06:10:30.374Z
- Updated: 2025-09-18T06:27:12.171Z
- Scheduled: 2025-09-18T07:00:00Z
- Published: 2025-09-18T07:00:10.390Z
- Typefully URL: https://typefully.com/?d=6764144&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1968570698131276252

#### Post 1

Excited to share my new course on AI Agents.

I've received many requests about scholarships.

Not everyone can afford it, but everyone deserves a chance to learn and grow.

I'm opening up scholarship spots for you.

1/3

Media IDs: `237ca68c-259c-4b28-b047-c3b7a49daef2`

#### Post 2

The course starts on October 6 and runs for 7 weeks. It’s live, hands-on, and focused on building production-ready AI agents step-by-step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents

I hope this makes the program more accessible to those who need it most.

2/3

Media IDs: `43ec07f9-d70d-4a14-b2ae-3c29e179a8bc`

#### Post 3

If you’re motivated to learn but cost is a barrier, you can apply here: https://forms.gle/ud21RVPUn3hLv3Xw5

Please share it with your network so more people who need a scholarship can see it. Thank you for helping spread the word!

3/3

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7374336388357312512

When I announced my new paid course on AI Agents, I received many requests for scholarships.

I understand why. Not everyone has the budget for a paid program, but many are eager to learn, practice, and develop their skills.

That's why I've decided to offer several scholarship spots.

If you're motivated to learn but cost is a barrier, apply here: https://forms.gle/ud21RVPUn3hLv3Xw5.

The course starts on October 6 and runs for 7 weeks. It's live, hands-on, and focused on building production-ready AI agents step by step.

I hope this makes the program more accessible to those who need it most.

Please share this with your network so more people in need of a scholarship can see it. Thank you for helping spread the word!

Media IDs: `237ca68c-259c-4b28-b047-c3b7a49daef2`

## Practical NLP Workshop with LLMs

- Typefully ID: `6718375`
- Status: published
- Tags: `cross-promo`, `ai-engineering-buildcamp`
- Created: 2025-09-12T14:38:48.343Z
- Updated: 2025-09-15T09:39:47.364Z
- Scheduled: 2025-09-17T07:00:00Z
- Published: 2025-09-17T07:00:13.879Z
- Typefully URL: https://typefully.com/?d=6718375&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1968208316414525722

#### Post 1

Doug will join me in a free workshop on practical NLP with LLMs.

Date: Monday, Sept 29, 2025
Time: 17:00 CET (1 hour)
Format: Online (Zoom)
Cost: Free to join

1/4

Media IDs: `0cecddc9-bcc9-496e-ab8d-55b6078c169a`

#### Post 2

If you've worked with text data, you know the challenge: tickets, logs, chats, and documents can be messy.

Traditionally, cleaning and structuring this data required complex NLP pipelines.

But with LLMs, many of these problems can be solved more quickly.

2/4

#### Post 3

In this workshop, you will:

1. Use LLMs to clean, correct, and interpret messy text
2. Extract structure and meaning to make unstructured data usable
3. Apply these methods in real engineering workflows, not just demonstrations

3/4

#### Post 4

Register here: https://maven.com/p/452707/practical-nlp-with-ll-ms-from-messy-text-to-value

4/4

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7373974005738795008

If you've worked with text data, you know the challenge: tickets, logs, chats, and documents can be messy.

Traditionally, cleaning and structuring this data required complex NLP pipelines.

But with LLMs, many of these problems can be solved more quickly.

To show you how, Doug will join me in a free workshop on practical NLP with LLMs.

Date: Monday, Sept 29, 2025
Time: 17:00 CET (1 hour)
Format: Online (Zoom)
Cost: Free to join

In this workshop, you will:

1. Use LLMs to clean, correct, and interpret messy text
2. Extract structure and meaning to make unstructured data usable
3. Apply these methods in real engineering workflows, not just demonstrations

Register here: https://maven.com/p/452707/practical-nlp-with-ll-ms-from-messy-text-to-value

Media IDs: `0cecddc9-bcc9-496e-ab8d-55b6078c169a`

## AI Bootcamp Giveaway

- Typefully ID: `6710491`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-11T14:25:08.446Z
- Updated: 2025-09-11T15:54:35.505Z
- Scheduled: 2025-09-16T07:00:00Z
- Published: 2025-09-16T07:00:05.882Z
- Typefully URL: https://typefully.com/?d=6710491&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1967845930683748663

I'm giving away free spots for my new course:

AI Bootcamp: From RAG to Agents

To enter ⬇️

Post on social media:

1. Why you want to join
2. Tag friends
3. Add this link: https://maven.com/alexey-grigorev/from-rag-to-agents
4. Submit here: https://forms.gle/nBC8kyGPeekYxKKA7

Winners announced Sept 17!

Media IDs: `5805bc58-46ab-4d0e-9cc1-6f596a5d3e84`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7373611620121591808

I'm giving away several free seats for my upcoming course:

AI Bootcamp: From RAG to Agents

To participate ⬇️

Make a post on social media, answering:

1. Why do you want to join
2. Tag friends or colleagues who might be interested
3. Add this course link in your post: https://maven.com/alexey-grigorev/from-rag-to-agents
4. Submit your post here: https://forms.gle/nBC8kyGPeekYxKKA7

Winners will be selected randomly and announced on Wednesday, September 17

This is your chance to join the bootcamp for free and learn how to build, evaluate, and deploy production-ready AI agents.

Media IDs: `0a39752d-b5d5-47b0-bceb-0b5090096cbf`

## AI Bootcamp Giveaway

- Typefully ID: `6710866`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-11T15:10:18.731Z
- Updated: 2025-09-11T15:50:42.478Z
- Scheduled: 2025-09-13T07:00:00Z
- Published: 2025-09-13T07:00:03.494Z
- Typefully URL: https://typefully.com/?d=6710866&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1966758757700083981

I'm giving away free spots to my new paid course:

AI Bootcamp: From RAG to Agents

Winners will be selected on Wednesday, Sept 17

Check this form for more details: https://forms.gle/nBC8kyGPeekYxKKA7

Media IDs: `3113f460-e5e4-4146-8427-0e38e26b67ce`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7372524449281097728

I'm giving away free spots to my new paid course:

AI Bootcamp: From RAG to Agents

Winners will be selected on Wednesday, Sept 17

Check this form for more details: https://forms.gle/nBC8kyGPeekYxKKA7

Media IDs: `3113f460-e5e4-4146-8427-0e38e26b67ce`

## AI Assistant Development Course

- Typefully ID: `6622671`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-01T10:38:38.878Z
- Updated: 2025-09-01T10:39:11.021Z
- Scheduled: 2025-09-01T15:00:00Z
- Published: 2025-09-01T15:00:15.125Z
- Typefully URL: https://typefully.com/?d=6622671&a=188312

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7368296636961280009

Build an AI agent you can use at work.

In my new hands-on course, you’ll progress from a basic assistant to production, covering testing, agentic behavior, and monitoring step by step.

By the end, you’ll have:

🔸 A fully functional AI assistant (RAG + OpenAI) that can search and answer from real documents.
🔸 A test-driven prompt engineering workflow using evaluation metrics and simulated queries.
🔸 Agentic behavior: function calling, Model Context Protocol (MCP), PydanticAI, OpenAI’s Agent SDK
🔸 A website-building AI agent that outputs complete Django projects.
🔸 Monitoring and guardrails for deployed AI apps: Grafana, Evidently, LangWatch
🔸 A capstone project: your own production-ready AI tool like a resume reviewer, a podcast summarizer, a search bot, etc.

Registration is open, enroll today: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `04cfb4cd-4a91-4bfc-b49d-bc277f0987b5`

## Hands-On AI Workshop: MCP & Agents

- Typefully ID: `6622630`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-09-01T10:32:50.113Z
- Updated: 2025-09-01T10:35:32.885Z
- Published: 2025-09-01T10:38:04.111Z
- Typefully URL: https://typefully.com/?d=6622630&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1962464955711844581

#### Post 1

Last call: Join 700+ participants for today's workshop on MCP and Agents!

Learn to:

🔸 Implement an FAQ agent
🔸 Enable search functionality via function calls
🔸 Integrate it with MCP
🔸 Connect to the MCP server using tools like Cursor

Register here: https://maven.com/p/3b1afc/hands-on-with-ai-agents-and-model-context-protocol-mcp

#### Post 2

A quick demo of what we'll be doing during the workshop: 
https://www.loom.com/share/64185e333a3f48048cc63054a70fcffb

## AI Coding Agent Workshop

- Typefully ID: `6474242`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T15:05:14.235Z
- Updated: 2025-08-14T15:08:43.728Z
- Scheduled: 2025-08-25T07:00:00Z
- Published: 2025-08-25T07:00:10.403Z
- Typefully URL: https://typefully.com/?d=6474242&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1959873392926220769

#### Post 1

Free tutorial: Build an LLM-based agent that will create Django apps from your text prompt.

I’ve published a recording of my latest workshop on building full AI-powered coding agents using Python and Django.

Watch the recording here: https://youtu.be/Sue_mn0JCsY?si=T4wXcEjF0EDuKtM6

Media IDs: `9aef4389-d22d-4cba-a5e2-54b3eb3f4b9d`

#### Post 2

What you’ll learn:

- Chatbots vs. Agents
- Setting up with GitHub Codespaces
- Utilizing OpenAI Agents SDK, Toy AI Kit, Pydantic AI
- Defining agent tools: file I/O, web search, more
- Switching LLM providers: OpenAI, Anthropic, Z.AI

#### Post 3

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7365639084960038912

Do you want to build an LLM-based agent that will create Django apps from your text prompt?

I’ve published a recording of my latest workshop on building full AI-powered coding agents using Python and Django.

What you’ll learn:

🔸 The difference between chatbots and agents
🔸 How to set up your dev environment using GitHub Codespaces
🔸 Using the OpenAI Agents SDK, Toy AI Kit, and Pydantic AI
🔸 How to define agent tools: file I/O, web search, and more
🔸 Switching LLM providers: OpenAI, Anthropic, Z.AI

Watch the recording here: https://youtu.be/Sue_mn0JCsY?si=T4wXcEjF0EDuKtM6

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `a7db08f4-0611-46e8-a79a-f5c097c5cfd7`

## Building Your MCP Server

- Typefully ID: `6474220`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T15:03:25.729Z
- Updated: 2025-08-14T15:06:33.221Z
- Scheduled: 2025-08-27T07:00:00Z
- Published: 2025-08-27T07:00:10.421Z
- Typefully URL: https://typefully.com/?d=6474220&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1960598168397340691

#### Post 1

MCP is a new black. You probably hear a lot about it.

But how to use it? I’ll teach you to build your own MCP server 👇🏼

Media IDs: `526dd7ff-97f4-4c22-a180-627e3946ecb6`

#### Post 2

MCP (Model-Context Protocol) allows you to easily connect tools to your language model.

If you’re stuck and lost in the storm of MCP materials, join me on my hands-on workshop.

I’ll show you how to build your own MCP server using a real example project.

1/2

#### Post 3

You’ll learn to work with:

🔸 MCPs
🔸 PydanticAI
🔸 OpenAI Agents SDK

Join me on Monday, Sep 1, at 4:30 CET.

Register to receive an invite link: https://maven.com/p/3b1afc/hands-on-with-ai-agents-and-model-context-protocol-mcp

2/2

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7366363857113542656

MCP is a new black. You probably hear a lot about it.

But how to use it? I’ll teach you to build your own MCP server 👇🏼

MCP (Model-Context Protocol) allows you to easily connect tools to your language model.

If you’re stuck and lost in the storm of MCP materials, join me on my hands-on workshop.

I’ll show you how to build your own MCP server using a real example project.

You’ll learn to work with:

🔸 MCPs
🔸 PydanticAI
🔸 OpenAI Agents SDK

Join me on Monday, Sep 1, at 4:30 CET.

Register to receive an invite link: https://maven.com/p/3b1afc/hands-on-with-ai-agents-and-model-context-protocol-mcp

Media IDs: `526dd7ff-97f4-4c22-a180-627e3946ecb6`

## AI Coding Agent Workshop Part 2

- Typefully ID: `6474184`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T15:00:18.001Z
- Updated: 2025-08-14T15:02:58.989Z
- Scheduled: 2025-08-19T07:00:00Z
- Published: 2025-08-19T07:00:06.590Z
- Typefully URL: https://typefully.com/?d=6474184&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1957699061907353697

#### Post 1

My recent workshop on building an AI Coding Agent attracted over 1,500 registrants!

By popular demand, I'm hosting Part 2 on MCP (Model-Context Protocol).

Learn to integrate tools into your LLM agent with MCP and create your own MCP server!

Media IDs: `dc7fbed8-08fe-448d-9e9f-c8dc01fb4e95`

#### Post 2

I’ll cover how to:

🔸 Create agents with reasoning capabilities and tool usage for completing user assignments.
🔸 Engineer with PydanticAI and OpenAI Agents SDK
🔸 Build your own MCP server to plug in new tools into your agents

Register here for free: https://maven.com/p/3b1afc/hands-on-with-ai-agents-and-model-context-protocol-mcp

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7363464750313164801

My recent workshop on building an AI Coding Agent, it got 1,500+ registrations.

Based on numerous requests, I decided to do part 2 about MCP (Model-Context Protocol).

Date: Monday, September 1, 4:30 PM CET

This time, you’ll learn how to easily plug in tools into your LLM agent with MCP and build your own MCP server!

I’ll cover how to:

🔸 Create agents with reasoning capabilities and tool usage for completing user assignments.
🔸 Engineer with PydanticAI and OpenAI Agents SDK
🔸 Build your own MCP server to plug in new tools into your agents

Register here for free: https://maven.com/p/3b1afc/hands-on-with-ai-agents-and-model-context-protocol-mcp

Media IDs: `271b6e00-f2bd-468a-869b-e43824f5ddb7`

## Function Calling in Action

- Typefully ID: `6462489`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-13T11:50:18.493Z
- Updated: 2025-08-14T14:59:40.750Z
- Scheduled: 2025-09-10T07:00:00Z
- Published: 2025-09-10T07:00:39.122Z
- Typefully URL: https://typefully.com/?d=6462489&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1965671600340303998

#### Post 1

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.

Media IDs: `6cd4a472-4a16-4e84-af24-607d7abbf928`

#### Post 2

Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).

- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.

#### Post 3

1. Calendar & meetings

- Prompt: "Book 30 min with Alice tomorrow at 15:00."
- Tools: create_calendar_event(title, start, attendees)
- Effect: Event created; invite sent.

#### Post 4

2. Docs & notes

- Prompt: "Summarize this PDF and save the notes to Notion."
- Tools: extract_text(file), create_notion_page(title, content)
- Effect: Summary page appears in your workspace.

#### Post 5

3. CRM & sales ops

- Prompt: “Add this lead and enrich with company data.”
- Tools: create_crm_contact(data), enrich_with_clearbit(email)
- Effect: New contact with firmographics; owner assigned.

#### Post 6

4. Support triage

- Prompt: “Route this ticket and draft a first reply.”
- Tools: classify_ticket(text), create_ticket(queue), draft_reply(context)
- Effect: Ticket filed to the right queue with a suggested response.

#### Post 7

5. Data & reporting

- Prompt: “Revenue by region for the last 7 days—export to Sheets.”
- Tools: query_db(sql), create_google_sheet(name, rows)
- Effect: Fresh report in Google Sheets; link returned.

#### Post 8

6. Files & automation

- Prompt: “Rename these images, compress, and upload to S3.”
- Tools: transform_images(params), upload_s3(bucket, paths)
- Effect: Optimized assets live in your bucket.

#### Post 9

7. DevOps

- Prompt: “Is service X healthy? If not, roll back to the last stable.”
- Tools: get_status(service), rollback_deploy(service, version)
- Effect: Status reported; rollback executed if needed.

#### Post 10

8. HR & recruiting

- Prompt: “Schedule a loop with three interviewers next week.”
- Tools: find_slots(attendees), create_calendar_event(series)
- Effect: Calendar holds with invites and meeting links.

#### Post 11

9. Internal search + answer

- Prompt: “What’s our PTO policy?”
- Tools: semantic_search(kb, query), retrieve(doc_ids)
- Effect: Answer grounded in your knowledge base with citations.

#### Post 12

10. Email & comms

- Prompt: “Send the weekly update to the team and attach the report.”
- Tools: generate_summary(data), send_email(to, subject, body, attachments)
- Effect: Email sent with the latest metrics and file.

#### Post 13

Want to learn how to use function calling? I made a free guide on building your own AI coding agent with function calling and OpenAI API. You can get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7371437289450684416

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.

➡️ Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).
- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.

Want to learn how to use function calling? I made a free guide on building your own AI coding agent with function calling and OpenAI API. You can get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `3470006a-2003-4acf-bf53-919e581e7c1b`

## Coding Agent Guide

- Typefully ID: `6474010`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T14:42:16.231Z
- Updated: 2025-08-14T14:46:42.070Z
- Scheduled: 2025-08-21T07:00:00Z
- Published: 2025-08-21T07:00:07.785Z
- Typefully URL: https://typefully.com/?d=6474010&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1958423854164164769

Free guide: Build your own coding agent

What's inside:

🔸 Step-by-step guide for implementation
🔸 Project template for any app
🔸 Reusable file-ops functions
🔸 Local setup instructions

Get your free guide here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `68c49a84-4844-4ff0-91b0-dba8d452b593`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7364189546604818433

I created a guide on building your own coding agent (end-to-end).

What’s inside:

🔸 What function calling is and when to use it
🔸 Step-by-step: implementing function calling
🔸 A lightweight Python library to speed things up
🔸 A project template for all apps your agent will generate
🔸 A reusable set of file-ops functions (create/modify project files)
🔸 System prompt design that keeps the agent on task
🔸 How to run everything locally

You can get this guide for free here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide

Media IDs: `68c49a84-4844-4ff0-91b0-dba8d452b593`

## AI Bootcamp FAQs

- Typefully ID: `6473969`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T14:38:54.938Z
- Updated: 2025-08-14T14:41:21.620Z
- Scheduled: 2025-09-05T07:00:00Z
- Published: 2025-09-05T07:00:18.297Z
- Typefully URL: https://typefully.com/?d=6473969&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1963859681010741715

#### Post 1

What’s special about my new AI Bootcamp?

And other frequently asked questions 👇🏼

Media IDs: `36d314cf-2837-468c-ac74-4cf5150b16de`

#### Post 2

This is a new, live program with updated materials, live teaching, and direct interaction with me as an instructor.

Compared to the free LLM Zoomcamp, this AI Bootcamp covers advanced use cases, dives deeper into agents, testing, monitoring, and production safety.

#### Post 3

Other key facts:

🔸 All live sessions are recorded within 24 hours, meaning you can complete the course fully asynchronously.

🔸 The course takes ~5 hours/week for live sessions and exercises. Project work is flexible, and you can revisit extra materials later.

#### Post 4

Register now: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7369625370410627072

What’s special about my new AI Bootcamp?

And other frequently asked questions 👇🏼

This is a new, live program with updated materials, live teaching, and direct interaction with me as an instructor.

Compared to the free LLM Zoomcamp, this AI Bootcamp covers advanced use cases, dives deeper into agents, testing, monitoring, and production safety.

Other key facts about this course:

🔸 All live sessions are recorded within 24 hours, meaning you can complete the course fully asynchronously.
🔸 The course takes ~5 hours/week for live sessions and exercises. Project work is flexible, and you can revisit extra materials later.
🔸 Backed by Maven’s Satisfaction Guarantee. If you're not satisfied, you can request a refund.

Register now: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `36d314cf-2837-468c-ac74-4cf5150b16de`

## Building AI Agents: No Experience Needed

- Typefully ID: `6473821`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T14:23:28.496Z
- Updated: 2025-08-14T14:36:03.246Z
- Scheduled: 2025-08-28T07:00:00Z
- Published: 2025-08-28T07:00:09.705Z
- Typefully URL: https://typefully.com/?d=6473821&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1960960553867993525

#### Post 1

Can you build AI agents without prior AI experience? Yes!

You just need:

Media IDs: `3193f8d6-2509-466b-aa7e-8575d3c33d21`

#### Post 2

🔸 Comfort with Python and basic Git
🔸 Willingness to test and measure
🔸 Access to OpenAI or alternatives

With these, you can get started quickly without any heavy setup or research rabbit holes.

#### Post 3

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7366726244748505091

Can you build AI agents without prior AI experience? Yes!

You just need:

🔸 Comfort with Python and basic Git
🔸 Willingness to test and measure
🔸 Access to OpenAI or alternatives

With these, you can get started quickly without any heavy setup or research rabbit holes.

If you want more support and practice with 2 months' worth of content, my new AI Bootcamp is where you’ll learn to build, evaluate, and deploy your own AI agents step by step.

Registration is now open: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `a8fa07bc-44be-49d4-bf3c-636b8e9c81f0`

## AI Bootcamp: From RAG to Production

- Typefully ID: `6473546`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T13:48:58.416Z
- Updated: 2025-08-14T13:57:24.824Z
- Scheduled: 2025-09-08T07:00:00Z
- Published: 2025-09-08T07:00:10.690Z
- Typefully URL: https://typefully.com/?d=6473546&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1964946824835576082

#### Post 1

My new AI Bootcamp takes you from RAG to production-ready agents.

It covers monitoring, guardrails, and a capstone you can demo to clients and recruiters.

1/3

Media IDs: `36f557bf-8d63-46bc-b03c-701f615a1577`

#### Post 2

You'll build:

🔸 RAG prototype for FAQs, YouTube, and docs
🔸 Data-driven prompt testing
🔸 Agentic flows: function calls, searches, PydanticAI, MCP
🔸 Build an agent for Django websites
🔸 Monitoring with Grafana, LangWatch, Evidently
🔸 Capstone: AI app for your portfolio

2/3

#### Post 3

Want to join the course?

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

3/3

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:ugcPost:7370712547756236800

My new AI Bootcamp takes you from RAG to production-ready agents.

It covers monitoring, guardrails, and a capstone you can demo to clients and recruiters.

You'll build:

🔸 RAG prototype for FAQs, YouTube, and docs
🔸 Data-driven prompt testing
🔸 Agentic flows: function calls, searches, PydanticAI, MCP
🔸 Build an agent for Django websites
🔸 Monitoring with Grafana, LangWatch, Evidently
🔸 Capstone: AI app for your portfolio

Want to join the course?

Register here: https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `3f4867d4-5564-4727-a466-a1a302b1fcbb`

## AI Coding Agent Workshop

- Typefully ID: `6471357`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-08-14T09:40:12.099Z
- Updated: 2025-08-14T09:47:38.127Z
- Published: 2025-08-14T09:49:37.333Z
- Typefully URL: https://typefully.com/?d=6471357&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1955929794144821544

Missed my AI Coding Agent workshop?

No problem!

🔸 Watch the video: https://www.youtube.com/watch?v=Sue_mn0JCsY
🔸 Access materials: https://github.com/alexeygrigorev/workshops/tree/main/coding-agent
🔸 Bonus TODO app: https://www.loom.com/share/b4c47e3491504375b9244ea69fe095df
🔸 AI Bootcamp course: https://maven.com/alexeygrigorev/from-rag-to-agents

See you at future workshops!

Media IDs: `f02df380-ec85-4a80-b7b3-0982aa800cb1`

## Advanced AI Agents Course

- Typefully ID: `6310115`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-07-29T09:48:55.564Z
- Updated: 2025-07-30T08:59:53.120Z
- Scheduled: 2025-08-04T07:00:00Z
- Published: 2025-08-04T06:58:13.587Z
- Typefully URL: https://typefully.com/?d=6310115&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1952262752246137182

#### Post 1

I'm launching a new course focused entirely on AI agents.

This is the most advanced AI curriculum I’ve released so far, packed with practical content I never covered before.

What's new in this course:

Media IDs: `15d26772-6a22-4a68-8e66-846ff6f4af6b`

#### Post 2

🔸 New use cases
🔸 Overview of key frameworks: OpenAI Agents SDK, Pydantic AI, and more
🔸 Agent testing and evaluation
🔸 Monitoring and guardrails
🔸 Creating an agent from scratch

1/2

#### Post 3

If you want to learn to build modern AI applications, this course is for you.

Join here: 
https://maven.com/alexey-grigorev/from-rag-to-agents

2/2

Media IDs: `7662943b-e84a-4846-ad39-ba94a834174e`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7358028441671139328

I'm launching a new course focused entirely on AI agents.

This is the most advanced AI curriculum I’ve released so far, packed with practical content I never covered before.

What's new in this course:

🔸 New use cases
🔸 Overview of key frameworks: OpenAI Agents SDK, Pydantic AI, and more
🔸 Agent testing and evaluation
🔸 Monitoring and guardrails
🔸 Creating an agent from scratch

If you want to learn to build modern AI applications, this course is for you.

Join here: 
https://maven.com/alexey-grigorev/from-rag-to-agents

Media IDs: `3cb466a1-6280-4725-9544-c916fa7e1d3b`

## Agent AI Workshop: Coding Tool

- Typefully ID: `6309996`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-07-29T09:38:15.078Z
- Updated: 2025-07-29T10:31:30.024Z
- Scheduled: 2025-07-30T08:00:00Z
- Published: 2025-07-30T08:00:35.985Z
- Typefully URL: https://typefully.com/?d=6309996&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1950466460519915818

#### Post 1

I'm working on a new course about agents.

As a part of the course, I'm hosting a free workshop on designing and building an AI coding agent that generates Python applications from your text prompts.

Details in the 🧵

Media IDs: `802d6f4a-8c6c-4fbf-a6b3-8c997fa2c213`

#### Post 2

Build your own version of the vibe coding tool: set it up, understand its inner workings, and customize it to meet your needs.

When: Wed, August 13, 2025
Time: 4:30 PM GMT+2 (1.5 hours)
Where: Online (Zoom)

1/5

#### Post 3

What you'll learn:

🔸 Orchestrating agentic AI apps with function-calling
🔸 Scaffolding a Django project template for rapid development
🔸 Implementing a live coding agent end-to-end
🔸 Generalizing these patterns to FastAPI, Flask, and beyond

2/5

#### Post 4

Join if you're:

🔸 Python developers looking to boost productivity
🔸 AI/ML practitioners curious about agent architectures
🔸 Tech enthusiasts eager to experiment with intelligent assistants

3/5

#### Post 5

Register now and bring your questions! 👉🏼 https://maven.com/p/3cf911/build-your-own-coding-agent

Share this with your network, and let's build something cool together!

4/5

#### Post 6

If you're curious about the new course, it's available here: https://maven.com/alexey-grigorev/from-rag-to-agents.

I'll share more details about it soon!

5/5

Media IDs: `e647a47a-bfa8-433d-a99c-721b7b056bbf`

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7356232146480418816

I'm working on a new course about agents. As part of the course, I'm hosting a free workshop on designing and building an AI coding agent that generates Python applications from your text prompts.

Build your own version of the vibe coding tool: set it up, understand its inner workings, and customize it to meet your needs.

When: Wed, August 13, 2025
Time: 4:30 PM GMT+2 (1.5 hours)
Where: Online (Zoom)

What you'll learn:

🔸 Orchestrating agentic AI apps with function-calling
🔸 Scaffolding a Django project template for rapid development
🔸 Implementing a live coding agent end-to-end
🔸 Generalizing these patterns to FastAPI, Flask, and beyond

Join if you're:

🔸 Python developers looking to boost productivity
🔸 AI/ML practitioners curious about agent architectures
🔸 Tech enthusiasts eager to experiment with intelligent assistants

Register now and bring your questions! 👉🏼 https://maven.com/p/3cf911/build-your-own-coding-agent?utm_campaign=MzM1NTc5&utm_medium=ll_share_link&utm_source=instructor

Share this with your network, and let's build something cool together!

Media IDs: `15a8c898-e66c-4c2e-ac0e-c8f407aa98a3`

## Building Agent-like Assistants

- Typefully ID: `6271069`
- Status: published
- Tags: `ai-engineering-buildcamp`
- Created: 2025-07-25T10:32:03.210Z
- Updated: 2025-07-25T10:42:48.044Z
- Scheduled: 2025-07-28T09:00:00Z
- Published: 2025-07-28T09:00:18.304Z
- Typefully URL: https://typefully.com/?d=6271069&a=188312

### x

Published URL: https://x.com/Al_Grigor/status/1949756740586889398

#### Post 1

Remember the workshop on building a chat assistant powered by OpenAI's function calling?

I'm hosting part 2 to focus on the code behind agent-like assistants.

🧵

1/5

Media IDs: `cca28dd4-22c2-41ee-97ff-92ca2cb65724`

#### Post 2

During a previous workshop, I demonstrated how to quickly build such an assistant.

Now, I want to explain the code line by line and refactor it into a reusable library.

We will also cover the MCP protocol and create a simple MCP client from scratch.

2/5

#### Post 3

What you'll learn:

🔸 How OpenAI function calling works in practice
🔸 Building a basic assistant in Jupyter, step by step
🔸 Refactoring assistant logic into a clean, reusable Python class
🔸 Extending function calling with MCP

3/5

#### Post 4

Register here: https://lu.ma/z3yxyttg

4/5

#### Post 5

You can check part 1 of this workshop here: https://www.youtube.com/watch?v=GH3lrOsU3AU&t=6s&pp=0gcJCccJAYcqIYzv

5/5

### linkedin

Published URL: https://www.linkedin.com/feed/update/urn:li:share:7355522430234202115

Remember the workshop on building a chat assistant powered by OpenAI's function calling? I'm hosting part 2 to focus on the code behind agent-like assistants.

During a previous workshop, I demonstrated how to quickly build such an assistant.

Now, I want to explain the code line by line and refactor it into a reusable library.

We will also cover the MCP protocol and create a simple MCP client from scratch.

What you'll learn:

🔸 How OpenAI function calling works in practice
🔸 Building a basic assistant in Jupyter, step by step
🔸 Refactoring assistant logic into a clean, reusable Python class
🔸 Extending function calling with MCP

Register here: https://lu.ma/z3yxyttg

Media IDs: `f2bacfca-0410-4b0b-a950-010908c3ad50`
