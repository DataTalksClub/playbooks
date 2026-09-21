# Newsletter Routing

Use this reference when a campaign includes Alexey's newsletter, the DataTalks.Club newsletter, or a follow-up sent through the DataTalks.Club newsletter system. Choose the sender and recipient before drafting.

## Alexey's Newsletter

Use the `newsletter-editor` skill as the source of truth for Alexey's first-person newsletter voice, editing process, audience, and long-form structure.

The event-promotion skill supplies the campaign angle, source material, event facts, and CTA. Do not derive Alexey's newsletter voice from `datatalks-style.md`, and do not invent why Alexey recommends an event or how he relates to a speaker.

## DataTalks.Club Newsletter

For content in the weekly issue (DataTalks.Club Weekly), use the `dtc-newsletter` skill. It owns the issue structure and every slot format: promos, Zoomcamp slots, event details, the events list, Book of the Week, Alexey on Data mentions, and recordings. A campaign that needs a newsletter mention should produce the matching slot.

For a registrant recap, read `datatalks-newsletter.md`. It is a targeted follow-up to people who registered, not automatically a broadcast newsletter item.

## Shared Handoff Rules

- Preserve the event name, speaker, date, time, timezone, claims, and link from the source.
- Keep the same campaign angle across senders, but rewrite the narration for the owner.
- Do not assume a subject line, preview text, button, or recipient segment unless the user requests it or the campaign source defines it.
- Make the CTA and destination appropriate to the stage: registration before the event; recording, notes, or materials after it.
