# Alexey Good Posts

Use these as calibration examples for structure, directness, audience fit, and topic framing. Do not copy wording unless the user asks to reuse a specific post.

## Incident / Lessons Learned

Claude Code wiped our production database with a Terraform command.

It took down the DataTalksClub course platform and 2.5 years of submissions: homework, projects, and leaderboards.

Automated snapshots were gone too.

In the newsletter, I wrote the full timeline + what I changed so this doesn't happen again.

If you use Terraform (or let agents touch infra), this is a good story for you to read.

## Learning In Public

I don't really understand this shaming culture around people sharing what they learn

Posts like this are valuable. They show real life mistakes. And others can learn from these mistakes

I'm a big advocate for learning in public, but this kind of reaction is exactly why people hesitate to share things online

They're afraid of being judged

We should be encouraging more openness, not discouraging it

## Tool Comparison

Why choose PyTorch over Keras for deep learning in 2025?

Keras still holds its ground.

It's fantastic for education, prototyping, and TensorFlow-native environments.

But for most modern deep learning workloads, PyTorch leads in industry adoption.

Here's why:

1. Most modern deep learning libraries are built PyTorch-first. You'll find faster updates, better documentation, and more active communities.

2. Almost every new deep learning paper, model, or open-source repo is released in PyTorch.

3. Dynamic computation graphs, native Python control flow, and easy debugging make PyTorch ideal for experimentation and custom architectures.

4. Distributed training, mixed precision, quantization, and production runtimes are well-integrated and mature.

5. From startups to Big Tech, PyTorch is the default stack across computer vision, NLP, multimodal models, and edge deployment.

## Scholarship / Deadline

Last chance to apply for the scholarship for AI Bootcamp: from RAG to Agents

The course costs $1,799 but I'm offering full and partial scholarships

I'm closing the form tomorrow and will contact the selected participants by Monday

If you haven't applied yet, here's the link.

## Community Outcome

One of the DataTalksClub members shared this review:

After a career break of more than seven years, the participant secured an AI Engineer role at a startup, thanks to their practical work on course projects from ML Zoomcamp and the AI Hero email course.

Being able to clearly explain what they built, why it works, and how it applies helped them stand out in the interview.

It's valuable to receive reviews like this! Seeing such outcomes is the strongest evidence that our free courses are benefiting participants.

## Course Announcement

Build an AI agent you can use at work.

In my new hands-on course, you'll progress from a basic assistant to production, covering testing, agentic behavior, and monitoring step by step.

By the end, you'll have:

- A fully functional AI assistant that can search and answer from real documents.
- A test-driven prompt engineering workflow using evaluation metrics and simulated queries.
- Agentic behavior: function calling, MCP, PydanticAI, and OpenAI Agents SDK.
- Monitoring and guardrails for deployed AI apps.
- A capstone project: your own production-ready AI tool.

## Research / Field Guide

I analyzed 1,765 AI Engineer job descriptions and turned it into an open Field Guide.

It covers:

- What AI engineer roles actually look like
- Skills that keep showing up in hiring
- Interview questions and patterns
- Learning paths + resources

It's a work in progress, and I'm adding more sections regularly.

If you have feedback or want to contribute, I'd love your input.

## Concept Explanation

One important Docker concept that often causes confusion: containers are stateless.

A Docker image is a snapshot of an operating system.

Every time you run docker run, Docker creates a new container from that snapshot.

What this means in practice:

- You can create files inside a container
- You can install packages
- You can modify the filesystem

But as soon as you exit the container, all those changes are gone.

When you start the container again, you're back to exactly what's defined in the image.

It's the core idea behind Docker for reproducibility, clean environments, and predictable behavior.

If you want data to persist, you need to be explicit about it: volumes, mounted paths, databases.

## Career Transition

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
- Structured outputs

Step 4: Evaluation for generative systems

- Golden sets
- Automated checks
- Human review loops when it matters

Step 5: Tool integration + agentic flows

- Function/tool calling
- Guardrails
- Tracing what the agent did and why

Step 6: Build 1-2 small projects end-to-end

For an experienced data engineer, this is usually not a multi-year shift. With focused effort and hands-on work, 3-4 months can be enough to become interview-ready.

## AI Engineer Skills

AI engineer = someone who makes AI testable, observable, versioned, and continuously improving.

Prompting is maybe 5%.
The other 95% is making AI behave reliably after you ship it.

Core skills:

1. Evaluation + testing

Turn model behavior into something measurable:

- small eval sets
- clear metrics
- regression tests after every change

2. Controlled iteration

- prompt versioning
- experiment tracking
- A/B tests and gradual rollouts

3. Monitoring + observability

- failure types
- latency and cost
- logs + traces for debugging
- alerts when things drift

4. Feedback loops

- ratings and thumbs up/down
- human review samples
- bad cases added back into the eval set

5. CI/CD for AI

Every change should run evals and block deploys when metrics drop.

6. Product integration

Retries, timeouts, fallbacks, UX edge cases.
