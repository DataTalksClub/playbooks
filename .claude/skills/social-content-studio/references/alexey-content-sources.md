# Alexey Content Sources

Where Alexey's posts come from, and how one source becomes several posts. Use it to plan a week, to fill an empty slot, or to turn a new piece of work into posts. For voice and format, use `alexey-style.md`; this file is about what to post.

Built from 603 published posts on Alexey's Typefully account (social set 188312), August 29, 2024 to October 12, 2026. The export is in `research/typefully/all-posts/` (raw and filtered folders are gitignored). Refresh it with the read-only exporter:

```bash
set -a && . ./.env && set +a
python3 research/typefully/scripts/download_posts.py --social-set-id 188312 --hydrate-details --term " " --limit 50 --max-pages 100 --output-dir research/typefully/all-posts
```

## Before Planning A Week

1. Read Alexey's posts from the last two to three weeks (refresh the export, or check Typefully). A source he already promoted needs a new angle or a pause. In the week of October 12, 2026, three planned Kubernetes posts repeated an October 9 post that had already covered all three talks.
2. List this week's inputs: running course modules, events he hosts, recordings published, his latest newsletter issue, research updates, product launches or deadlines, and community milestones.
3. Pick one or two inputs to multiply (see Repurposing below), and fill the remaining slots from the evergreen bank.
4. Cadence: about one post per weekday at 09:00 CEST (07:00 UTC). Busy weeks add a second slot around 16:00 CEST, and some weekends get a post. 2026 has averaged 40 to 50 posts a month.

## Source Categories

Shares are rough, from keyword matching over the 603 posts.

### 1. Zoomcamp courses (about 1 in 6 posts)

Free courses Alexey teaches or runs: ML, Data Engineering, LLM, MLOps, AI Dev Tools Zoomcamps. Sources: `courses/<course>/`, module folders on GitHub, course Telegram, the course platform.

| Angle | Example hooks |
| --- | --- |
| Registration and launch countdown | "Our free ML Zoomcamp starts in less than a month!", "Data Engineering Zoomcamp starts today!" |
| Weekly module | "This week in LLM Zoomcamp: AI orchestration with Kestra.", "In the Data Engineering Zoomcamp, we begin Module 4: Analytics Engineering." |
| Micro-lesson from a module | "5 Kubernetes core concepts", "One important Docker concept that often causes confusion: containers are stateless." |
| Curriculum update, behind the scenes | "For ML Zoomcamp 2025, I'll refresh Module 5 with insights on deploying ML models using FastAPI and uv." |
| FAQ and who it's for | "A common question I receive is: Should I take the Data Engineering Zoomcamp?", "Who is AI Dev Tools Zoomcamp for?" |
| Milestones | GitHub stars, registrations, certificates, "5,000+ people submitted at least one homework in our free Zoomcamps in 2025." |
| Learner outcomes and outside praise | "Saw this comment on Reddit about Data Engineering Zoomcamp:", "Nice to see ML Zoomcamp ranked #1 in ...'s review", homework demos from participants |
| Partners in the course | Kestra and dlt modules, Bruin project competition and winners, sponsor thank-yous at the end of a cohort |
| Phase changes | Midterm projects, peer review, "Data Engineering Zoomcamp 2026 is officially complete!" |

Multiplier: one module gives a weekly announcement plus one to three micro-lessons from its lessons (October 2025 Kubernetes, November 2025 MCP, January 2026 Docker).

### 2. Workshops and events he hosts (the largest share, about 3 in 10)

Hands-on workshops (own and guest), the weekly podcast, live Q&As, pre-course event series, offline meetups, conference talks. Sources: Luma pages, `events-archive/`, recordings, transcripts.

| Stage | Example hooks |
| --- | --- |
| Announcement, problem first | "Long-running agents have a context problem.", "Adding a human approval step to an agent looks small in code." |
| Guest introduction | "On March 3, Aleksey Komissarov will join me on a live workshop on ...", "I invited Bhavani Ravi to lead a workshop ..." |
| Social proof before the event | "870+ people have already registered", "Join 700+ participants for today's workshop" |
| Reminder | "Tomorrow: ...", "I'm starting a live workshop in 3 hours on ..." |
| Recap | "I ran the third workshop for AI Dev Tools Zoomcamp: ...", "Louis Amaudruz built a team of agents ... during our DataTalksClub workshop." |
| Lessons from the recording (weeks later) | "When a multi-agent workflow stalls, check permissions and handoffs ...", "With function calling, the LLM does not run your Python function." |
| Code roundup | "10 AI agent workshops I created with public code.", "I published the code from 10 AI Shipping Labs workshops." |
| In-person | Meetup recaps ("Third offline DataTalksClub meetup in 2026: done!"), conference trips (PyConDE, Data Makers Fest, WebSummit), free tickets and promo codes |

Multiplier: one workshop yields 4 to 12 posts over one to eight weeks. The May and June 2026 RAG workshops produced about a dozen lesson posts ("Don't start a RAG project with vector search by default.", "Why retrieve top 5 documents instead of only top 1 in RAG?", "Hard truth: You don't always need an agent."), each ending with the recording link.

### 3. His newsletter: Alexey On Data, now AI Shipping Blog (about 1 in 10, rising)

Sources: `aishippingblog.com` (earlier `alexeyondata.substack.com`).

| Angle | Example hooks |
| --- | --- |
| Personal build | "I built my own Gmail AI reply assistant.", "I built a system that generates children's books for my son with AI.", "I built a Telegram assistant that transforms voice notes ..." |
| Experiment or how-to | "What happens if you ask Claude Code to run slash commands forever?", "I tried using Claude Code as an orchestrator for AI agents team." |
| Incident and lesson | "Claude Code wiped our production database with a Terraform command.", "A coding agent should never have a path to production." |
| Teaser and announcement | "My next Substack post is going out tomorrow!", "I just published a new edition of my weekly newsletter." |
| Newsletter milestones | "0 -> almost 4,000 subscribers in 2 months", referral program, rebrand to a new domain |
| Event preview, sponsored | Kubernetes Automation Day posts (October 2026), with a disclosure line |

Multiplier: one issue gives an announcement plus one to three angle posts. Each angle post opens with a different section's lesson and links the issue. Space them out, check what already went out, and drop angles already used.

### 4. Research and data (about 1 in 20, but the posts recur for months)

The AI Engineer role research: job description analysis (1,765, then 2,445, then about 5,000 postings), the AI Engineering Field Guide, take-home assignment repos, the Awesome AI Engineering hub, interview patterns, forward-deployed engineer growth, community surveys.

Hooks: "I analyzed 1,765 AI Engineer job descriptions ...", "Evaluation is the number one skill across 4,894 AI engineering job descriptions I analyzed.", "Forward-deployed engineer job postings grew 4x in 6 months ...", "I updated the AI Engineering Field Guide."

Multiplier: every data refresh is a new post. Single findings become standalone posts: top skills, interview format, take-homes, role comparisons.

### 5. His products: AI Engineering Buildcamp, AI Shipping Labs, free lead magnets (about 3 in 10 in 2025 to 2026)

| Angle | Example hooks |
| --- | --- |
| Launch and dates | "The next cohort of my AI Engineering Buildcamp starts on Apr 13." |
| What's inside | "What does AI Engineering Buildcamp cover?", "What does the weekly schedule ... look like?", "AI Engineering Buildcamp is project-driven." |
| Objection answers | "Will you cover LangChain and LangGraph in the course?", "Want to join ... but worried about the cost?", employer learning budgets |
| Proof | Reviews ("I just got a new course review from Leo, a machine learning researcher at TNO"), graduate projects ("13 AI projects created by AI Engineering Buildcamp graduates"), Demo Day, enrollment numbers ("25 people joined AI Engineering Buildcamp last week.") |
| Scholarships and deadlines | "Last chance to apply for the scholarship ...", "5 days left ...", "I contacted everyone selected ..." |
| Lead magnets | "Free 25+ page guide on building your own coding agent ...", 7-day AI Hero email course, the coding agent cheatsheet |
| Community building in public | "AI Shipping Labs now has 79 members.", sprint launches and recaps, membership tiers, website migration |
| Concept teasers that sell the course | "The difference between a chatbot and an agent comes down to one thing: function calling.", "How function calling works in 4 steps:" |

### 6. DataTalksClub community (about 1 in 20)

Anniversaries ("DataTalksClub turned 6 on September 19."), Slack and YouTube milestones, year-in-review, Book of the Week, Hacktoberfest, new sponsors ("I'm happy to welcome Snowplow as a long-term sponsor"), community member messages, podcast guest insights ("During one of our recent podcasts, Xia He-Bleinagel ... shared her journey ...").

### 7. Tools, news, and other people's work (about 1 in 30)

Trying a new model or tool ("Gemini 3 is out, so I decided to give it a try.", Antigravity, Nano Banana), papers ("Pathway just released a paper ..."), open-source finds ("Atomic Agents is a lightweight framework ..."), friends' books and courses (Soledad Galli, Towards AI, Khuyen Tran), coding challenges as a daily diary ("Day 2 of @Cloudflare version control competition"), sponsored tool posts (Rasa, Actian, Jev).

### 8. Opinions, career, and learning (a small share, but the most reposted)

Learning in public, "we teach concepts, not tools", entry-level job market, transition paths ("How do I transition from Data engineer to AI engineer?"), role definitions ("How do AI Engineering, ML Engineering, and Data Science relate?", "How do you tell an AI hobbyist from an AI engineer?").

## Repurposing

### One source, many posts

| Source | Sequence |
| --- | --- |
| Workshop | Problem-first announcement, guest intro, reminder with the registration count, "today in N hours", recap, 3 to 10 lesson posts over the following weeks, then a code roundup that lists it with other workshops |
| Newsletter issue | Teaser, announcement with the main lesson, one to three posts on other sections (different hooks), a follow-up when the story continues ("In my previous posts, I wrote about the agent team ...") |
| Course module | Weekly module post, a micro-lesson per strong lesson, a learner outcome or homework demo |
| Research | First finding, field guide release, one post per finding, an update post at every data refresh |
| Product cohort | Launch, curriculum, schedule, objection answers, reviews, scholarships, last call, enrollment numbers, Demo Day, graduate projects |
| Podcast episode | Today/tomorrow announcement, then one guest insight per post once the recording is up (underused, see Gaps) |

### Reposting evergreen posts

58 published posts share their opening with at least one other post (27 distinct openings). Lessons, guides, and career posts come back 4 to 12 weeks later, unchanged or lightly edited:

- "How do I transition from Data engineer to AI engineer?" (three times)
- "AI Engineering Buildcamp is project-driven." (three times)
- "Free 25+ page guide on building your own coding agent ..."
- "4 key components of AI agent architecture in its simplest form:"
- "A basic RAG application is just three steps."
- "Your first RAG implementation should be easy to replace."

When a week is thin, repost a strong evergreen post from at least six weeks earlier, ideally one tied to something live that week, such as a course module or product launch.

## Hook Patterns

From the openings of the 603 posts:

- **A claim or rule:** "Don't start a RAG project with vector search by default.", "Hard truth: You don't always need an agent."
- **A question the audience asks:** about 1 in 10 posts open with a question. "What are guardrails for AI agents?", "When do you actually need Kubernetes?"
- **A number list:** "5 Kubernetes core concepts", "10 examples of function calling in practice", "13 AI projects created by ..."
- **"I built / I tried / I analyzed":** personal work first, then what it shows.
- **A concrete scenario:** "Your coding agent is already producing a dataset.", "Adding a human approval step to an agent looks small in code."
- **A milestone number:** "90,000 people are now in the DataTalksClub Slack 🎉"
- **Timing:** "Tomorrow:", "Last chance ...", "Today, I'm hosting ..."

## Sponsored Posts

Alexey's sponsored posts end with a disclosure line. Use the same wording:

- "This post is made in collaboration with [Sponsor]. Thank you for supporting our community!"
- "This post is sponsored by @[Sponsor]. Thank you for supporting our community!"

Add it to every post built from sponsored material, including angle posts from a sponsored newsletter issue.

## Gaps And Opportunities

- **Podcast episodes:** DataTalksClub runs a weekly podcast, but few of Alexey's posts draw on episode content after it airs. Each recording can give a guest-insight post, framed as "Here's an answer from [guest], our guest on the podcast: ...".
- **Book of the Week:** it appears only a few times since 2025. The authors are often recent guests, as with Suhas Suresha and Dewang Sultania in October 2026.
- **DataTalksClub workshop recordings by guests:** the Switch workshop showed that one guest recording gives 5 or more posts. Most guest recordings get only an announcement.
- **Course micro-lessons:** strong in 2025 (Kubernetes, MCP, Docker), fewer in 2026. Every running module can give at least one.
