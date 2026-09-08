---
platform: x
date: 2026-07-31
url: "https://x.com/Al_Grigor/status/2083085257776238805?s=20"
media: "image"
analytics:
  likes: 7
  reposts: 3
  comments: 1
  impressions: 1003
  engagements: 59
  detail_expands: 6
  profile_visits: 1
---

10 examples of function calling in practice

Function calling lets LLMs connect with tools and take actions using these tools.
9:00 AM · Jul 31, 2026
·
1,003
 Views

Alexey Grigorev
@Al_Grigor
·
Jul 31
Quick distinction:

- Function is an implementation in your runtime (Python/JS/API).

- Tool is the contract you register for the LLM (name + typed schema + permissions). A tool is usually backed by one function, but it can orchestrate many.
Alexey Grigorev
@Al_Grigor
·
Jul 31
1. Calendar & meetings

- Prompt: "Book 30 min with Alice tomorrow at 15:00."
- Tools: create_calendar_event(title, start, attendees)
- Effect: Event created; invite sent.
Alexey Grigorev
@Al_Grigor
·
Jul 31
2. Docs & notes

- Prompt: "Summarize this PDF and save the notes to Notion."
- Tools: extract_text(file), create_notion_page(title, content)
- Effect: Summary page appears in your workspace.
Alexey Grigorev
@Al_Grigor
·
Jul 31
3. CRM & sales ops

- Prompt: “Add this lead and enrich with company data.”
- Tools: create_crm_contact(data), enrich_with_clearbit(email)
- Effect: New contact with firmographics; owner assigned.
Alexey Grigorev
@Al_Grigor
·
Jul 31
4. Support triage

- Prompt: “Route this ticket and draft a first reply.”
- Tools: classify_ticket(text), create_ticket(queue), draft_reply(context)
- Effect: Ticket filed to the right queue with a suggested response.
Alexey Grigorev
@Al_Grigor
·
Jul 31
5. Data & reporting

- Prompt: “Revenue by region for the last 7 days—export to Sheets.”
- Tools: query_db(sql), create_google_sheet(name, rows)
- Effect: Fresh report in Google Sheets; link returned.
Alexey Grigorev
@Al_Grigor
·
Jul 31
6. Files & automation

- Prompt: “Rename these images, compress, and upload to S3.”
- Tools: transform_images(params), upload_s3(bucket, paths)
- Effect: Optimized assets live in your bucket.
Alexey Grigorev
@Al_Grigor
·
Jul 31
7. DevOps

- Prompt: “Is service X healthy? If not, roll back to the last stable.”
- Tools: get_status(service), rollback_deploy(service, version)
- Effect: Status reported; rollback executed if needed.
Alexey Grigorev
@Al_Grigor
·
Jul 31
8. HR & recruiting

- Prompt: “Schedule a loop with three interviewers next week.”
- Tools: find_slots(attendees), create_calendar_event(series)
- Effect: Calendar holds with invites and meeting links.
Alexey Grigorev
@Al_Grigor
·
Jul 31
9. Internal search + answer

- Prompt: “What’s our PTO policy?”
- Tools: semantic_search(kb, query), retrieve(doc_ids)
- Effect: Answer grounded in your knowledge base with citations.
