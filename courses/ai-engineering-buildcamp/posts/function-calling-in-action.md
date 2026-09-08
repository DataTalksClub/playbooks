---
platform: x
status: published
typefully_id: 6462489
date: 2025-09-10
url: "https://x.com/Al_Grigor/status/1965671600340303998"
typefully_url: "https://typefully.com/?d=6462489&a=188312"
title: "Function Calling in Action"
tags: ["ai-engineering-buildcamp"]
media_ids: ["6cd4a472-4a16-4e84-af24-607d7abbf928"]
---

1/13

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.

2/13

Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).

- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.

3/13

1. Calendar & meetings

- Prompt: "Book 30 min with Alice tomorrow at 15:00."
- Tools: create_calendar_event(title, start, attendees)
- Effect: Event created; invite sent.

4/13

2. Docs & notes

- Prompt: "Summarize this PDF and save the notes to Notion."
- Tools: extract_text(file), create_notion_page(title, content)
- Effect: Summary page appears in your workspace.

5/13

3. CRM & sales ops

- Prompt: “Add this lead and enrich with company data.”
- Tools: create_crm_contact(data), enrich_with_clearbit(email)
- Effect: New contact with firmographics; owner assigned.

6/13

4. Support triage

- Prompt: “Route this ticket and draft a first reply.”
- Tools: classify_ticket(text), create_ticket(queue), draft_reply(context)
- Effect: Ticket filed to the right queue with a suggested response.

7/13

5. Data & reporting

- Prompt: “Revenue by region for the last 7 days—export to Sheets.”
- Tools: query_db(sql), create_google_sheet(name, rows)
- Effect: Fresh report in Google Sheets; link returned.

8/13

6. Files & automation

- Prompt: “Rename these images, compress, and upload to S3.”
- Tools: transform_images(params), upload_s3(bucket, paths)
- Effect: Optimized assets live in your bucket.

9/13

7. DevOps

- Prompt: “Is service X healthy? If not, roll back to the last stable.”
- Tools: get_status(service), rollback_deploy(service, version)
- Effect: Status reported; rollback executed if needed.

10/13

8. HR & recruiting

- Prompt: “Schedule a loop with three interviewers next week.”
- Tools: find_slots(attendees), create_calendar_event(series)
- Effect: Calendar holds with invites and meeting links.

11/13

9. Internal search + answer

- Prompt: “What’s our PTO policy?”
- Tools: semantic_search(kb, query), retrieve(doc_ids)
- Effect: Answer grounded in your knowledge base with citations.

12/13

10. Email & comms

- Prompt: “Send the weekly update to the team and attach the report.”
- Tools: generate_summary(data), send_email(to, subject, body, attachments)
- Effect: Email sent with the latest metrics and file.

13/13

Want to learn how to use function calling? I made a free guide on building your own AI coding agent with function calling and OpenAI API. You can get it here: https://maven.com/p/f2d4cd/build-your-own-coding-agent-free-guide
