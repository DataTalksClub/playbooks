# Stage 2: Post-Event Repurposing

Use this stage when the user provides a recording, transcript, notes, slides, code, demo links, audience questions, speaker follow-up notes, timestamps, or approved post-event takeaways.

Stage 2 happens after the event. It should extend the value of the event instead of simply saying that the event happened.

## Inputs

Use only supplied post-event source material:

- Notes.
- Recording link.
- Transcript.
- Slides.
- Code or demo links.
- Audience questions.
- Speaker follow-up notes.
- Key takeaways approved for public use.
- Timestamps for short-video candidates.
- Recording or transcript sections that should not be used.

If only the original event description is available, do not write Stage 2 assets. Instead, return a Stage 2 plan and list the missing inputs.

## Required Stage 2 Outputs

Create post-event assets as source material allows:

- Event recap: publish within 2 days after the event date. Use notes and the event recording link when available.
- Repurposed text posts: publish after the event date. Create as many strong, distinct posts as the notes or recording support.
- Repurposed short videos: prepare around 5 days after the event date. Create as many strong, distinct short-video ideas as the notes, transcript, or recording support.

For general events, also prepare channel variants described in `channels.md`: a DTC newsletter recap for event registrants and YouTube Community adaptations of every Alexey/DTC social asset. These variants do not count as separate content angles.

Quality matters more than quantity. Do not create multiple assets from the same idea just to increase the count.

## Who Posts What From A Recording

Decide the owner of each idea before writing, using these defaults. The user can move an idea to the other owner.

| | DataTalks.Club | Alexey |
| --- | --- | --- |
| Which ideas | The recap, and educational posts about what the speaker explained or built. Formal, organizational voice. | Ideas where Alexey took part in the conversation: questions he asked, points he raised, his own experience said on the call. First person. |
| Copy | `linkedin.md` for LinkedIn and a separate `x.md` thread (no X Premium, 280 characters per post). | `linkedin.md` only; the same copy goes to LinkedIn, X, and Substack Notes. |
| Media | A clip per post where the recording supports one. No carousels or images. | A clip, plus a carousel and a resource image. They become two Typefully drafts with the same copy: `clip` (clip on every platform) and `visual` (carousel on LinkedIn, image on X). |
| CTA | The recording link with a reason to watch tied to the post's idea, plus the tool or repo link when the event has one. | Same. |

- Alexey's first-person statements must come from something he said in the recording. When the transcript does not make it clear who said a line, attribute it to the speaker or leave it out.
- The same idea is not posted by both owners.
- Put every owner's posts in one content run (see the `social-content-studio` skill, `references/output-formats.md`). Machine-readable versions of these rules live in `social-content-studio/references/profiles.json`.

## Event Recap

Timing: within 2 days after the event date.

Inputs: notes and event recording link when available.

Goal: summarize what happened and make it easy for people who missed the event to catch up.

Open with what the speaker built or showed, then say the recording is up. Do not open with "The recording of <title> is now available"; see the published example in `examples.md`.

Include:

- Event topic and speaker.
- The main ideas, lessons, demo moments, or questions covered.
- Recording link when available.
- A natural CTA to watch, read notes, or follow the next step.

Avoid:

- Generic "thanks for joining" copy as the whole post.
- Claiming outcomes, audience reactions, or highlights that are not in the notes.
- Repeating the original event announcement as if the event has not happened.

For a general event, distinguish two recap variants when both are needed:

- Public recording recap for Alexey social, DTC social, and YouTube Community after the recording is available.
- Registrant follow-up through the DTC newsletter system for people who registered, with the recording or notes and a concise reminder of what they can revisit.

## Repurposed Text Posts

Timing: after the event date.

Inputs: notes, transcript, recording link, slides, audience questions, demo details, or speaker follow-up notes.

Goal: turn the event into standalone educational posts. Create as many strong, distinct text posts as the post-event source material supports.

Good repurposed text post angles include:

- A useful answer from the Q&A.
- A technical misconception corrected during the event.
- A workflow or decision explained by the speaker.
- A demo step that reveals a broader lesson.
- A practical takeaway from the recording.
- A comparison, trade-off, failure mode, or implementation detail discussed during the event.

Each repurposed text post should be useful even for people who do not watch the full recording. Link back to the recording or notes as the natural next step.

## Repurposed Short Videos

Timing: around 5 days after the event date.

Inputs: recording, transcript, notes, timestamps, slides, or demo moments.

Goal: identify short clips that can stand alone and point people back to the full event or community.

Create as many strong, distinct short-video ideas as the recording or transcript supports. Prioritize moments with a clear hook, a complete thought, and a practical takeaway.

Good short-video candidates include:

- A concise answer to a common question.
- A surprising mistake or failure mode.
- A useful technical explanation.
- A strong demo moment.
- A before/after workflow explanation.
- A practical recommendation from the speaker.

For each short-video idea, include the core idea, why it works, and timestamps if available. If timestamps are not available, describe what to search for in the recording.

## Stage 2 Output Format

First provide a post-event overview.

```markdown
## Post-Event Overview

**Stage:**
Stage 2 - Post-event

**Event:**
[Event title]

**Primary audience segment:**
[Segment name and why it fits]

**Source material used:**
[Recording / transcript / notes / slides / Q&A / timestamps]

**Recommended assets:**
[Total number]

**Repurposing opportunities identified:**

1. [Idea]
   - Type: Event recap / Repurposed text / Short video
   - Source: Notes / Recording / Transcript / Slides / Q&A
   - Timing: [...]

**Channel plan, if requested:**
[Use channels.md to map Stage 2 content pieces to timing, links, and channels]
```

Then write the assets:

```markdown
## Post-Event Asset 1: Event Recap

**Type:** Event recap
**Timing:** Within 2 days after the event
**Source:** [Notes, recording link, transcript, or other source]

[Final recap post]

---

## Post-Event Asset 2: [Descriptive title]

**Type:** Repurposed text
**Timing:** After the event
**Source:** [Transcript section, notes, Q&A, or recording link]

[Final text post]

---

## Short-Video Idea 1: [Descriptive title]

**Type:** Repurposed short video
**Timing:** Around 5 days after the event
**Source:** [Recording/transcript/timestamps]
**Timestamp:** [Timestamp or what to search for]

[Hook, core idea, suggested clip arc, CTA]
```

Continue only while there are strong, distinct post-event assets.
