# Playbook: Video upload & YouTube finishing (Grace)

Source: `team/telegram-analysis/reports/dtc-chat-grace-analysis.md` (P5,
taxonomy 3.4).

**Trigger**: Alexey forwards a Zoom/Loom link (often with passcode) or says
"I'm already uploading … please take it from here".

**Frequency**: ~2–4 videos/week across the DTC channel and Alexey's personal
channel (workshops, podcasts, office hours, book club, Maven LLs, AI
Shipping Labs).

## Steps

1. Download the recording.
2. Upload to the target channel with the title; visibility per instruction
   (public/unlisted).
3. Cut the beginning / breaks per Alexey's timestamps
   ("I had two breaks - at 14:54 and at 16:05 … Please find them and remove
   them"). He supplies timestamps; cutting itself is terminal-based.
4. Wait for the YouTube auto-transcript:
   - for Luma events, copy description + timecodes from the Luma recording
     page;
   - if the transcript hasn't appeared in ~24h, use the fallback: extract
     audio, split it, transcribe via Groq, merge (proven 2026-03-11,
     re-approved 2026-09-21).
5. Write the description + timecodes.
6. Send the link to Alexey (status caveat when transcript still pending:
   "will wait for transcript to show in order to add description and
   timecodes") and to the content channel (Valeriia).
7. Chop highlight clips for socials — since 2026-08-19 this applies to ALL
   content: sponsored workshops, Maven, all workshops and webinars, and
   podcasts ("Let's also do it for podcasts").
8. Announce where appropriate (Maven/Slack for office-hours content).

**Known failure modes**
- Transcripts not appearing (14 mentions in 2026) — use the Groq fallback.
- Proactive status digests on stuck processing: "up until now the videos in
  youtube are still processing" — report rather than wait silently.

**Alexey decisions**: visibility, what to cut (he gives timestamps), cover
image (via Valeriia).

**Evidence**: YouTube link + transcript status note; playlist confirmations
("videos are added on both playlists").
