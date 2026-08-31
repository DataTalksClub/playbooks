---
name: datatalks-event-promotion
description: Create campaign-style social media posts for DataTalks.Club events, including sponsored events. Use when drafting event announcements, reminders, or educational promotional posts for DataTalks.Club rather than Alexey's personal posts.
metadata:
  short-description: DataTalks.Club event campaigns
---

# DataTalks.Club Event Promotion

Use this skill to create staged social media campaigns for DataTalks.Club events, including sponsored events. It defines source handling and output structure for separate pre-event and post-event promotion stages. Apply any additional style guide the user provides.

## Workflow

1. Identify which stage the user is asking for based on available inputs.
2. Read `references/campaign-strategy.md` for the two-stage model and handoff rules.
3. Read `references/datatalks-style.md` for voice, formatting, CTAs, platform adaptation, and promotional restraint.
4. Read `references/audience.md` when choosing educational angles, selecting the primary audience segment, or deciding how technical the posts should be.
5. Read `references/channels.md` when drafting channel-specific deliverables, when the user asks for a distribution plan or posting schedule, or when the event category affects the campaign shape.
6. For LinkedIn or X, read `references/social-media.md` to route by account owner, then read `references/linkedin.md` or `references/x.md` for the platform requirements.
7. For DataTalks.Club LinkedIn or X, also read `references/datatalks-social-media.md`. For Alexey deliverables, hand the campaign brief and source material to `$social-content-studio`; do not apply DataTalks.Club voice rules to his post.
8. For newsletter deliverables, read `references/newsletter.md`. For DataTalks.Club newsletter copy, also read `references/datatalks-newsletter.md`; for Alexey's newsletter, hand the campaign brief to `$newsletter-editor`.
9. Read `references/slack.md` for DataTalks.Club Slack deliverables.
10. Read `references/telegram.md` for Telegram deliverables.
11. Read `references/youtube-community.md` for YouTube Community deliverables and `references/youtube-video.md` for YouTube titles, descriptions, pinned comments, or live-to-recording metadata updates.
12. For Stage 1, when the user provides an event description, product/tool description, speaker description, sponsor details, or registration link, read `references/stage-1-pre-event.md`.
13. For Stage 2, when the user provides a recording, transcript, notes, slides, Q&A, timestamps, or post-event takeaways, read `references/stage-2-post-event.md`.
14. Use `references/event-brief-template.md` when source material is incomplete or when the user asks for a reusable brief.
15. Read `references/examples.md` only when the user asks for examples, calibration, or a comparison against prior approved campaigns.
16. Draft only from supplied source material. Do not invent product capabilities, speaker achievements, event content, dates, links, claims, metrics, recording takeaways, timestamps, or sponsor approvals.

## Output

For Stage 1, create exactly two announcement posts:

- Main announcement.
- Reminder.

For course-related events, then create only the pre-event educational posts supported by distinct, strong source-backed angles. For general events, treat pre-event educational posts as optional unless the user asks for them; the default pre-event package is the announcement and reminder, with educational repurposing handled in Stage 2 from the recording or notes.

For Stage 2, create post-event assets only from the recording, transcript, notes, slides, Q&A, timestamps, or other post-event source material. Do not create recaps, repurposed text posts, or short-video ideas from the original event description alone.

If both Stage 1 and Stage 2 inputs are available, keep the campaign overview and outputs separated by stage.

When asked to save files, save them in the user's current project or requested folder, not inside this skill directory.

## Reference Map

- `references/campaign-strategy.md`: two-stage campaign model, stage-selection rules, lifecycle handoff, anti-repetition principles, and shared quality checks.
- `references/stage-1-pre-event.md`: pre-event strategy for main announcement, reminder, source-backed educational posts, product-led angles, expert-led angles, sponsored events, and Stage 1 output format.
- `references/stage-2-post-event.md`: post-event strategy for recaps, repurposed text posts, short-video ideas, recording/transcript handling, timing, and Stage 2 output format.
- `references/channels.md`: distribution channel plans for course-related events and general DataTalks.Club events.
- `references/social-media.md`: routing and ownership boundaries for Alexey vs DataTalks.Club social posts.
- `references/datatalks-social-media.md`: DataTalks.Club account voice, audience-centered storytelling, and LinkedIn/X post shapes.
- `references/linkedin.md`: LinkedIn format, owner adaptation, and event-post requirements.
- `references/x.md`: account-specific X limits, mandatory DTC threads, URL counting, thread construction, and delivery checks.
- `references/newsletter.md`: owner and recipient routing for Alexey and DataTalks.Club newsletter deliverables.
- `references/datatalks-newsletter.md`: DataTalks.Club newsletter mentions, dedicated blocks, and registrant follow-ups.
- `references/slack.md`: DataTalks.Club Slack style and requirements for announcements, reminders, engagement prompts, and recaps.
- `references/telegram.md`: Telegram-specific style, structure, link formatting, and requirements for course, module, event, reminder, recap, and operational announcement posts.
- `references/youtube-community.md`: YouTube Community style and adaptation rules for announcements, reminders, educational posts, and recaps.
- `references/youtube-video.md`: YouTube title, description, pinned-comment, and live-to-recording metadata requirements.
- `references/datatalks-style.md`: DataTalks.Club voice, formatting, CTA, platform, hashtag, emoji, and anti-hype guidance.
- `references/audience.md`: DataTalks.Club audience segments, funnel stage, JTBD, pains, barriers, topics, formats, CTAs, metrics, and angle-selection guidance.
- `references/event-brief-template.md`: reusable checklist for collecting event, speaker, product, sponsor, timing, and claim details.
- `references/examples.md`: curation rules and storage format for approved example campaigns.
