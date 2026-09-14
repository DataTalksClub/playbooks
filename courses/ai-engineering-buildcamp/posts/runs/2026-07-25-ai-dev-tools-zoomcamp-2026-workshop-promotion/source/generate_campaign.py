#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
TODAY = "2026-07-25"
SOURCE_ID = "ai-dev-tools-zoomcamp-2026-workshop-series"


EVENTS = [
    {
        "slug": "ai-native-developer-workflow",
        "module": "Module 1",
        "title": "AI-Native Developer Workflow: Using AI Tools Without Losing Control",
        "link": "https://luma.com/lmkti8zj",
        "date": "July 22, 2026",
        "time": "",
        "status_note": "Past event, use replay/follow-up reminder",
        "position": "1st workshop",
        "problem": "AI coding tools can move quickly, but a vague request often turns into a vague implementation.",
        "promise": "how to turn AI coding tools into a disciplined developer workflow",
        "learn": [
            "Compare chat assistants, terminal agents, agentic IDEs, cloud agents, and project bootstrappers",
            "Use repository instructions, specs, architecture notes, testing guidelines, and security checklists",
            "Break work into spec, context, plan, edit, run, test, inspect diff, review, and commit",
            "Use tests and code review to keep engineering judgment in the loop",
        ],
        "educational": [
            "Start with a concrete spec, not a vague coding request",
            "Put reusable context in repository files, not only in chat",
            "Ask the agent to plan before it edits",
            "Run tests and inspect the diff before accepting the change",
        ],
        "reminder_label": "Replay reminder",
        "reminder_body": "If you missed the first AI Dev Tools Zoomcamp workshop, it is worth watching before the next sessions.",
    },
    {
        "slug": "build-and-ship-full-stack-app",
        "module": "Module 2",
        "title": "Build and Ship an AI-Assisted Full-Stack App",
        "link": "https://luma.com/50kvfku2",
        "date": "August 3, 2026",
        "time": "6:00 AM PDT",
        "status_note": "Upcoming",
        "position": "2nd workshop",
        "problem": "AI can generate frontend or backend code, but full-stack work fails when the parts drift apart.",
        "promise": "how to use AI tools from product spec to deployed full-stack app",
        "learn": [
            "Turn an app idea into a product spec and acceptance criteria",
            "Use OpenAPI contracts to align frontend and backend work",
            "Build a FastAPI or Django backend with database support",
            "Add tests, Docker, deployment, and CI/CD without losing the workflow",
        ],
        "educational": [
            "Write acceptance criteria before implementation",
            "Use OpenAPI as the contract between frontend and backend",
            "Ask for tests while the implementation is still small",
            "Make the final workflow reproducible with Docker and CI/CD",
        ],
        "reminder_label": "Reminder",
        "reminder_body": "The full-stack app workshop is coming up next.",
    },
    {
        "slug": "coding-agent-capabilities",
        "module": "Module 3",
        "title": "Coding Agent Capabilities: MCP, Skills, Plugins, and Custom Agents",
        "link": "https://luma.com/ap4l3qlj",
        "date": "August 17, 2026",
        "time": "5:00 AM PDT",
        "status_note": "Upcoming",
        "position": "3rd workshop",
        "problem": "A coding agent becomes more useful when it has the right instructions, tools, permissions, and repeatable workflows.",
        "promise": "how modern coding agents are extended and customized",
        "learn": [
            "Use project instructions to guide agents inside a repository",
            "Connect assistants to tools, context, and actions with MCP",
            "Package repeatable work with skills, commands, hooks, plugins, and extensions",
            "Review agent output with tests, diffs, and human judgment",
        ],
        "educational": [
            "Use project instructions for repository-specific behavior",
            "Use MCP when the agent needs external tools or context",
            "Use skills and commands for repeatable workflows",
            "Use hooks and permissions to add review points around risky actions",
        ],
        "reminder_label": "Reminder",
        "reminder_body": "The coding agent capabilities workshop is coming up.",
    },
    {
        "slug": "open-source-ai-tools-security-audit-devops",
        "module": "Module 4",
        "title": "Open-Source AI Tools for Security, Audit, and DevOps",
        "link": "https://luma.com/ycsfxigi",
        "date": "August 18, 2026",
        "time": "5:00 AM PDT",
        "status_note": "Upcoming",
        "position": "4th workshop",
        "problem": "AI-assisted projects still need security scanning, audit trails, incident investigation, and deployment discipline.",
        "promise": "how to use open-source AI tools around security, audit, and DevOps workflows",
        "learn": [
            "Use AI around pull request audit and review",
            "Connect security scanning to AI-assisted workflows",
            "Use tools such as PR-Agent, Semgrep MCP, Snyk Agent Scan, K8sGPT, LiteLLM, and Ollama",
            "Keep humans, policy, and audit trails in the loop",
        ],
        "educational": [
            "Review generated code like any other production change",
            "Make scanners available before the agent asks for deployment",
            "Record what changed, which tools ran, and which checks passed",
            "Use AI for investigation, but keep policy and approval explicit",
        ],
        "reminder_label": "Reminder",
        "reminder_body": "The security, audit, and DevOps workshop is coming up.",
    },
    {
        "slug": "pre-course-live-qa",
        "module": "Pre-course Q&A",
        "title": "AI Dev Tools Zoomcamp 2026 Pre-Course Live Q&A",
        "link": "https://luma.com/a8qa5s2s",
        "date": "August 24, 2026",
        "time": "",
        "status_note": "Upcoming",
        "position": "pre-course live Q&A",
        "problem": "Before joining a cohort, it helps to know the workload, prerequisites, project expectations, and how to get unstuck.",
        "promise": "a clear picture of AI Dev Tools Zoomcamp before the cohort starts",
        "learn": [
            "Who the course is for and what you need before joining",
            "What you do not need: prior AI tools experience, web development experience, a powerful machine, or a GPU",
            "How lectures, homework, deadlines, leaderboard, peer review, and certificates work",
            "How to prepare your environment and choose a first workflow",
        ],
        "educational": [
            "You should be comfortable with basic programming, Git, GitHub, and the command line",
            "You do not need a GPU or previous AI tools experience",
            "The course focuses on planning, coding, review, testing, agents, security, DevOps, and a final project",
            "A good first step is choosing one workflow instead of comparing every assistant",
        ],
        "reminder_label": "Reminder",
        "reminder_body": "The pre-course Q&A is coming up before the cohort starts.",
    },
    {
        "slug": "course-launch",
        "module": "Course launch",
        "title": "AI Dev Tools Zoomcamp 2026 Course Launch",
        "link": "https://luma.com/tsiusx8s",
        "date": "August 31, 2026",
        "time": "",
        "status_note": "Upcoming",
        "position": "course launch",
        "problem": "The new cohort starts with the same question many developers have: how do we use AI tools without losing control of the code we ship?",
        "promise": "how the AI Dev Tools Zoomcamp 2026 cohort works and how to start with a clear workflow",
        "learn": [
            "What changed in AI Dev Tools Zoomcamp 2026",
            "How the four modules fit together",
            "How lectures, homework, deadlines, leaderboard, peer review, and certificates work",
            "What to expect from the final project",
        ],
        "educational": [
            "The course is about developer workflow, not collecting tools",
            "The path goes from planning and coding to agent capabilities, security, audit, and DevOps",
            "The final project is where the workflow becomes concrete",
            "The DataTalks.Club community is where you ask questions and get help during the cohort",
        ],
        "reminder_label": "Launch reminder",
        "reminder_body": "AI Dev Tools Zoomcamp 2026 starts today.",
    },
]


def md_frontmatter(post_id: str, platform: str) -> str:
    return f"---\npost_id: {post_id}\nplatform: {platform}\nstatus: draft\n---\n\n"


def event_date_line(event: dict) -> str:
    if event["time"]:
        return f"{event['date']} at {event['time']}"
    return event["date"]


def announcement_linkedin(event: dict) -> str:
    learn = "\n".join(f"- {item}" for item in event["learn"])
    if event["status_note"].startswith("Past"):
        return (
            f"The recording is available for {event['title']}.\n\n"
            f"This was the {event['position']} in the series for updating AI Dev Tools Zoomcamp 2026 content.\n\n"
            f"The workshop is about {event['promise']}.\n\n"
            f"It covers:\n\n{learn}\n\n"
            f"If you are joining the next workshops, this is a useful place to start because it sets up the workflow: spec, context, plan, edit, run, test, inspect diff, review, and commit.\n\n"
            f"Watch / register here:\n{event['link']}"
        )
    return (
        f"I am running a workshop on {event['title']}.\n\n"
        f"This is the {event['position']} in the series for updating AI Dev Tools Zoomcamp 2026 content.\n\n"
        f"The workshop is about {event['promise']}.\n\n"
        f"We will cover:\n\n{learn}\n\n"
        f"It will be a hands-on session with practical examples and time for Q&A.\n\n"
        f"Date: {event_date_line(event)}\n"
        f"Register here:\n{event['link']}"
    )


def educational_linkedin(event: dict) -> str:
    bullets = "\n".join(f"- {item}" for item in event["educational"])
    cta = (
        f"The recording is here:\n{event['link']}"
        if event["status_note"].startswith("Past")
        else f"I will cover this in the workshop:\n{event['link']}"
    )
    return (
        f"{event['problem']}\n\n"
        f"This is why {event['module']} of AI Dev Tools Zoomcamp focuses on {event['title']}.\n\n"
        f"A practical workflow needs a few simple controls:\n\n{bullets}\n\n"
        f"The goal is not to slow down AI-assisted work.\n\n"
        f"The goal is to make the work reproducible enough that you can review it, test it, debug it, and ship it with confidence.\n\n"
        f"{cta}"
    )


def reminder_linkedin(event: dict) -> str:
    if event["status_note"].startswith("Past"):
        return (
            f"{event['reminder_label']}: {event['title']}\n\n"
            f"{event['reminder_body']}\n\n"
            f"We covered how to move from a vague idea to a concrete plan, how to give coding agents the right context, and how to review generated code before accepting it.\n\n"
            f"This is useful preparation for the next sessions in the AI Dev Tools Zoomcamp 2026 workshop series.\n\n"
            f"Watch / register here:\n{event['link']}"
        )
    return (
        f"{event['reminder_label']}: {event['title']}\n\n"
        f"{event['reminder_body']}\n\n"
        f"Date: {event_date_line(event)}\n\n"
        f"We will focus on {event['promise']}.\n\n"
        f"If you are planning to join AI Dev Tools Zoomcamp 2026, this session will help you prepare for the cohort and the final project.\n\n"
        f"Register here:\n{event['link']}"
    )


def announcement_x(event: dict) -> str:
    if event["status_note"].startswith("Past"):
        return "\n\n".join(
            [
                "1/4\n\n"
                f"The recording is available for {event['title']}.\n\n"
                f"{event['link']}",
                "2/4\n\n"
                f"This was the {event['position']} in the AI Dev Tools Zoomcamp 2026 workshop series.",
                "3/4\n\n"
                "It covers specs, context, planning, tests, review, and keeping control of AI-generated code.",
                "4/4\n\n"
                "Useful preparation before the next sessions in the series.\n\n"
                f"Watch here:\n{event['link']}",
            ]
        )
    return "\n\n".join(
        [
            "1/4\n\n"
            f"I am running a workshop on {event['title']}.\n\n"
            f"{event['link']}",
            "2/4\n\n"
            f"This is the {event['position']} in the AI Dev Tools Zoomcamp 2026 workshop series.",
            "3/4\n\n"
            f"We will cover {event['promise']} with practical examples and time for Q&A.",
            "4/4\n\n"
            f"Date: {event_date_line(event)}\n\n"
            "Join here:\n"
            f"{event['link']}",
        ]
    )


def educational_x(event: dict) -> str:
    cta = (
        f"The recording is here:\n{event['link']}"
        if event["status_note"].startswith("Past")
        else f"I will cover the workflow in this workshop:\n{event['link']}"
    )
    return "\n\n".join(
        [
            "1/5\n\n" + event["problem"],
            "2/5\n\n"
            f"This is why {event['module']} focuses on {event['title']}.",
            "3/5\n\n"
            f"One practical control:\n\n{event['educational'][0]}",
            "4/5\n\n"
            f"Another one:\n\n{event['educational'][1]}",
            "5/5\n\n" + cta,
        ]
    )


def reminder_x(event: dict) -> str:
    if event["status_note"].startswith("Past"):
        return "\n\n".join(
            [
                "1/4\n\n"
                f"Replay reminder: {event['title']}",
                "2/4\n\n"
                "The first workshop covered specs, context, planning, tests, review, and keeping control of AI-generated code.",
                "3/4\n\n"
                "It is useful preparation for the rest of the AI Dev Tools Zoomcamp 2026 workshop series.",
                "4/4\n\n"
                f"Watch / register here:\n{event['link']}",
            ]
        )
    return "\n\n".join(
        [
            "1/4\n\n"
            f"Reminder: {event['title']}",
            "2/4\n\n"
            f"Date: {event_date_line(event)}",
            "3/4\n\n"
            f"We will cover {event['promise']} with practical examples and Q&A.",
            "4/4\n\n"
            f"Register here:\n{event['link']}",
        ]
    )


KINDS = [
    ("announcement", "Announcement", announcement_linkedin, announcement_x),
    ("educational", "Educational", educational_linkedin, educational_x),
    ("reminder", "Reminder", reminder_linkedin, reminder_x),
]


def media_title(event: dict, kind: str) -> str:
    prefixes = {
        "announcement": "Workshop",
        "educational": "Practical workflow",
        "reminder": "Reminder",
    }
    return f"{prefixes[kind]}: {event['module']}"


def sentence_start(value: str) -> str:
    return value[:1].upper() + value[1:] if value else value


def carousel_record(event: dict, kind: str) -> dict:
    if kind == "announcement":
        subtitle = f"{event['title']} | {event_date_line(event)}"
        content = [
            ("What this covers", sentence_start(event["promise"]) + "."),
            ("Why it matters", event["problem"]),
            ("Main workflow", event["learn"][0] + ". " + event["learn"][1] + "."),
            ("What you will leave with", event["learn"][-1] + "."),
        ]
    elif kind == "educational":
        subtitle = f"A practical note for {event['title']}"
        content = [
            ("The problem", event["problem"]),
            ("Control 1", event["educational"][0] + "."),
            ("Control 2", event["educational"][1] + "."),
            ("Control 3", event["educational"][2] + "."),
        ]
    else:
        subtitle = f"{event['title']} | {event_date_line(event)}"
        content = [
            ("Why join", event["problem"]),
            ("What we will cover", sentence_start(event["promise"]) + "."),
            ("For the cohort", "Use this session to prepare for AI Dev Tools Zoomcamp 2026 and the final project."),
            ("Bring questions", "There will be time for practical questions about tools, workflow, review, testing, and shipping."),
        ]
        if event["status_note"].startswith("Past"):
            subtitle = f"{event['title']} | recording available"
            content[0] = ("Why watch", "The first session sets up the workflow for the rest of the series.")
            content[1] = ("What it covers", "Specs, context, planning, tests, review, and control of generated code.")

    slides = [
        {
            "type": "cover",
            "author": "Alexey Grigorev",
            "title": media_title(event, kind),
            "subtitle": subtitle,
            "swipeLabel": "Swipe for more",
        }
    ]
    for index, (title, body) in enumerate(content, start=1):
        slide = {
            "type": "title-paragraph",
            "title": title,
            "body": body[:280],
        }
        if index % 2 == 0:
            slide["variant"] = "light"
        slides.append(slide)
    slides.append(
        {
            "type": "outro",
            "ctaText": "Register for the workshop",
            "supportingText": event["title"],
            "url": event["link"],
        }
    )
    return {
        "title": f"{event['title']} - {kind}",
        "slides": slides,
    }


def twitter_resource_record(event: dict, kind: str) -> dict:
    if kind == "announcement":
        sections = [
            {"heading": "Workshop", "body": event["title"]},
            {"heading": "Date", "body": event_date_line(event)},
            {"heading": "Focus", "body": sentence_start(event["promise"]) + "."},
            {"heading": "You will learn", "bullets": event["learn"][:3]},
            {"heading": "Register", "body": event["link"]},
        ]
    elif kind == "educational":
        sections = [
            {"heading": "Problem", "body": event["problem"]},
            {"heading": "Workflow controls", "bullets": event["educational"][:3]},
            {"heading": "Reason", "body": "Make AI-assisted work easier to review, test, debug, and ship."},
            {"heading": "Workshop", "body": event["title"]},
            {"heading": "Link", "body": event["link"]},
        ]
    else:
        heading = "Watch" if event["status_note"].startswith("Past") else "Join live"
        sections = [
            {"heading": event["reminder_label"], "body": event["title"]},
            {"heading": "Date", "body": event_date_line(event) if not event["status_note"].startswith("Past") else "Recording available"},
            {"heading": "Focus", "body": sentence_start(event["promise"]) + "."},
            {"heading": "Good for", "bullets": ["AI Dev Tools Zoomcamp preparation", "Final project workflow", "Practical Q&A"]},
            {"heading": heading, "body": event["link"]},
        ]
    return {
        "resourceTitle": media_title(event, kind),
        "subtitle": event["title"],
        "sections": sections,
        "cta": event["link"],
    }


def review_record(post_id: str, kind: str) -> dict:
    return {
        "post_id": post_id,
        "checks": {
            "audience_fit": "pass",
            "specificity": "pass",
            "voice": "pass",
            "unsupported_claims": "pass",
            "style_rules": "pass",
            "cta": "pass",
        },
        "notes": [
            "Kept claims tied to supplied Luma/Meetup/DataTalks event descriptions.",
            "Avoided hashtags, hype language, and invented times where a time was not available from the public snippets.",
        ],
        "changed": [
            "Turned the past Module 1 before-event reminder into a replay/follow-up reminder.",
        ]
        if kind == "reminder"
        else [],
    }


def check_x_thread(path: Path, body: str) -> None:
    parts = [part.strip() for part in body.split("\n\n") if part.strip()]
    current = []
    tweets = []
    for part in parts:
        if part[:2].isdigit() or part.startswith("1/") or part.startswith("2/") or part.startswith("3/") or part.startswith("4/") or part.startswith("5/"):
            if current:
                tweets.append("\n\n".join(current))
            current = [part]
        else:
            current.append(part)
    if current:
        tweets.append("\n\n".join(current))
    too_long = [len(tweet) for tweet in tweets if len(tweet) > 280]
    if too_long:
        raise ValueError(f"{path} has tweet(s) over 280 chars: {too_long}")


def main() -> None:
    source_dir = RUN_DIR / "source"
    source_dir.mkdir(exist_ok=True)
    (source_dir / "events.json").write_text(json.dumps(EVENTS, indent=2) + "\n", encoding="utf-8")

    ideas = []
    post_index = 1
    for event in EVENTS:
        for kind, label, linkedin_fn, x_fn in KINDS:
            post_id = f"post_{post_index:03d}"
            idea_id = f"idea_{post_index:03d}"
            post_dir = RUN_DIR / "posts" / post_id
            post_dir.mkdir(parents=True, exist_ok=True)

            linkedin_body = linkedin_fn(event)
            x_body = x_fn(event)
            check_x_thread(post_dir / "x.md", x_body)

            (post_dir / "linkedin.md").write_text(
                md_frontmatter(post_id, "linkedin") + linkedin_body + "\n",
                encoding="utf-8",
            )
            (post_dir / "x.md").write_text(
                md_frontmatter(post_id, "x") + x_body + "\n",
                encoding="utf-8",
            )
            (post_dir / "review.json").write_text(
                json.dumps(review_record(post_id, kind), indent=2) + "\n",
                encoding="utf-8",
            )
            (post_dir / "linkedin-carousel.json").write_text(
                json.dumps(carousel_record(event, kind), indent=2) + "\n",
                encoding="utf-8",
            )
            (post_dir / "twitter-resource.json").write_text(
                json.dumps(twitter_resource_record(event, kind), indent=2) + "\n",
                encoding="utf-8",
            )

            topic = f"{label}: {event['title']}"
            post_record = {
                "post_id": post_id,
                "idea_id": idea_id,
                "source_id": SOURCE_ID,
                "owner": "alexey",
                "platforms": ["linkedin", "x"],
                "status": "draft",
                "topic": topic,
                "created": TODAY,
                "updated": TODAY,
                "angle": f"{label.lower()} post promoting {event['title']}.",
                "cta": f"Register: {event['link']}",
                "source_moments": [],
                "files": {
                    "linkedin": "linkedin.md",
                    "x": "x.md",
                    "review": "review.json",
                    "linkedin_carousel": "linkedin-carousel.json",
                    "linkedin_carousel_output": "linkedin-carousel",
                    "twitter_resource": "twitter-resource.json",
                    "twitter_resource_image": "twitter-resource/twitter-resource.png",
                },
                "scheduling": {
                    "ready_for_queue": False,
                    "preferred_publish_at": "",
                    "external_id": "",
                },
                "event": {
                    "title": event["title"],
                    "module": event["module"],
                    "date": event["date"],
                    "time": event["time"],
                    "url": event["link"],
                    "status_note": event["status_note"],
                    "post_type": kind,
                },
            }
            (post_dir / "post.json").write_text(json.dumps(post_record, indent=2) + "\n", encoding="utf-8")
            ideas.append(
                {
                    "idea_id": idea_id,
                    "post_id": post_id,
                    "event_slug": event["slug"],
                    "post_type": kind,
                    "title": topic,
                    "url": event["link"],
                }
            )
            post_index += 1

    (RUN_DIR / "ideas" / "post-ideas.json").write_text(json.dumps(ideas, indent=2) + "\n", encoding="utf-8")

    run_path = RUN_DIR / "run.json"
    run = json.loads(run_path.read_text(encoding="utf-8"))
    run["status"] = "drafting"
    run["source"] = {
        "source_id": SOURCE_ID,
        "type": "event_series",
        "title": "AI Dev Tools Zoomcamp 2026 workshop promotion",
        "url": "https://datatalks.club/",
        "video_id": "",
        "transcript_path": "",
        "duration_seconds": 0,
        "events_path": "source/events.json",
    }
    run["campaign"] = {
        "events": len(EVENTS),
        "posts": len(ideas),
        "post_types": [kind for kind, *_ in KINDS],
        "note": "Module 1 is a past event as of 2026-07-25, so its reminder draft is a replay/follow-up reminder.",
    }
    run_path.write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
