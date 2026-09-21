# Stage 1: Pre-Event Campaign

Use this stage when the user provides an event description, tool or product description, speaker description, sponsor details, registration link, or other pre-event source material.

Stage 1 happens before the event. It cannot produce event recaps, recording-based takeaways, repurposed text posts from the talk, or short-video ideas from the recording unless the user also provides post-event source material.

## Inputs

Use only supplied source material:

- Event description: title, format, date and time, main topic, agenda, learning outcomes, registration link, sponsor.
- Product or tool description: what it does, what problem it solves, how it works, capabilities, use cases, technical details, examples, public claims or metrics.
- Speaker description: name, role, company, expertise, relevant projects, products or systems, solved problems, technical experience, previous talks, writing, research.

Do not assume product capabilities, event content, or speaker background that is not provided.

## Required Stage 1 Outputs

Create exactly two announcement posts for every event:

- Main announcement.
- Reminder.

For course-related events, then create additional educational posts based on the strongest available content angles. Educational posts can be product-led or expert-led.

For general DataTalks.Club events, the default Stage 1 package is the main announcement and reminder. Pre-event educational posts are optional and should be created only when the user asks for them or a custom campaign plan includes them. The default educational repurposing for general events belongs in Stage 2, once the recording, transcript, or notes are available.

When pre-event educational posts are part of the campaign, generate as many as the source material supports, prioritizing quality over quantity. As a general target, look for 2-4 strong educational posts. Generate fewer if there are not enough distinct ideas. Do not stretch one idea into several repetitive posts.

Each educational post must have a distinct problem, lesson, mechanism, use case, or technical question at its center.

## Main Announcement

Goal: introduce the event and give readers a clear reason to attend. This is the primary informational announcement.

Include:

- What the event is about.
- Who is speaking.
- Why the topic matters.
- What participants will learn, build, explore, or see.
- Date and time.
- Registration CTA.

When relevant, mention the product or sponsor, but keep the focus on the event and what the audience can learn.

Typical structure:

- Context or event introduction.
- What participants will learn, using specific examples or a short list when useful.
- Speaker and why their experience is relevant.
- Event details and CTA.

Avoid:

- Generic promotional openings.
- Overstating the importance of the event.
- Repeating the event description verbatim.
- Listing every possible detail from the source material.
- Making the sponsor the main subject unless the event is specifically about the sponsor's product.

## Reminder

Goal: remind people shortly before the event and give them one strong reason to register or attend. The reminder should not simply repeat the main announcement.

The post will usually be published several days before the event or one day before it. Use the actual timing provided when writing the post.

Choose one strong reason to attend, such as:

- A specific problem the speaker will solve.
- Something participants will build.
- A live demonstration.
- A technical question that will be answered.
- A useful part of the speaker's experience.
- A practical use case.

Structure:

- Reason to attend.
- Event reminder.
- Essential details: speaker, date, time, and registration CTA.

Do not rewrite the main announcement with a reminder label added.

## Educational Posts

Educational posts should work as useful standalone content. Do not begin by promoting the event.

Instead:

1. Identify a real problem, question, misconception, workflow, or technical challenge related to the event.
2. Teach the reader something about it.
3. Connect that lesson naturally to either the product or the speaker.
4. Introduce the event as the place where readers can learn more, see the approach in practice, or understand how the problem is solved.

The promotional part should follow from the educational content.

## Product-Led Posts

Goal: teach readers about a problem and use the product involved in the event to show one way of solving it. The post should not read like product advertising.

The product enters the post because its design, workflow, architecture, or capabilities are relevant to the problem being explained.

Core structure:

1. Start with a concrete problem the target audience may encounter, such as a scaling issue, technical limitation, failure mode, repetitive engineering task, architectural problem, prototype-to-production gap, or misconception.
2. Explain why the problem happens, what makes it difficult, what engineers need to consider, why obvious solutions may fail, or what trade-offs are involved.
3. Introduce the product through the relevant mechanism or approach. Use wording like "One way to handle this is...", "This is the problem X was designed to address...", or "X approaches this by...".
4. Connect it to the event by explaining what participants will learn, build, explore, or see in practice.

Focus only on capabilities relevant to the problem described in the post.

The normal sequence is: problem, explanation, approach/product, event.

Avoid opening with product-first language such as "X is a powerful platform for...". Do not use the sequence: product, features, event.

## Expert-Led Posts

Goal: teach readers about a problem and use the speaker's relevant experience to establish why the event can help them understand or solve it. The speaker is the bridge between the educational topic and the event.

Core structure:

1. Start with a problem directly connected to the speaker's expertise, such as a technical challenge, engineering decision, common failure mode, operational problem, design trade-off, recurring team question, or a problem the speaker has worked on.
2. Explain what makes the problem difficult and what someone working on it needs to understand.
3. Introduce the expert with factual evidence from the speaker description. Prefer concrete work they have built, researched, operated, or solved over generic credentials.
4. Connect the expertise to what the speaker will show, explain, demonstrate, or discuss during the event.

The normal sequence is: problem, explanation, relevant speaker experience, event.

The speaker's biography is not the post. Only include background that explains why their experience matters for the specific problem discussed.

Do not imply that the speaker personally worked on a product or problem unless the supplied speaker information supports that connection.

## Finding Educational Angles

Before writing educational posts, analyze all available source material and identify potential:

- Problems.
- Failure modes.
- Misconceptions.
- Technical mechanisms.
- Use cases.
- Architectural decisions.
- Trade-offs.
- Workflows.
- Questions.
- Lessons.
- Interesting implementation details.

For each idea, determine whether it works better as product-led, expert-led, or both.

A strong educational angle is:

- Relevant: directly connected to the event.
- Specific: focused on a concrete problem or idea rather than a broad topic.
- Educational: useful even without attending the event.
- Supported: accurate based on supplied materials.
- Distinct: not substantially repeating another post in the campaign.

Do not decide the number of educational posts before analyzing the source material. First identify candidate angles, then remove weak ideas, generic ideas, unsupported claims, angles requiring speculation, near-duplicates, and ideas with too little substance for a standalone post.

There does not need to be an equal number of product-led and expert-led posts.

## Sponsored Events

For sponsored events, the objective is still to create useful content for the DataTalks.Club audience. Do not turn every post into an advertisement for the sponsor.

The sponsor or product should appear where it is relevant to the story. Use approved product claims and terminology from the supplied materials.

Educational posts should normally follow:

Audience problem, useful explanation, relevant product or expertise, event.

They should not follow:

Sponsor, product features, promotional claims, event.

## Stage 1 Output Format

First provide a campaign overview. This makes the content strategy visible before the final posts.

```markdown
## Campaign Overview

**Stage:**
Stage 1 - Pre-event

**Event:**
[Event title]

**Primary audience segment:**
[Segment name and why it fits]

**Secondary audience segment, if useful:**
[Segment name or "None"]

**Recommended posts:**
[Total number]

**Educational angles identified:**

1. [Angle]
   - Type: Product-led / Expert-led
   - Core problem or question: [...]
   - Connection to event: [...]

**Stage 2 handoff:**
[What recording/transcript/notes would be useful after the event]

**Channel plan, if requested:**
[Use channels.md to map Stage 1 content pieces to timing, links, and channels]
```

Then write the posts:

```markdown
## Post 1: Main Announcement

**Type:** Announcement
**Angle:** [Short description]

[Final post copy]

---

## Post 2: Reminder

**Type:** Reminder
**Angle:** [Short description]

[Final post copy]

---

## Post 3: [Descriptive title]

**Type:** Product-led educational / Expert-led educational
**Angle:** [Short description]

[Final post copy]
```

Continue only while there are strong, distinct educational angles.

When channel-specific versions are requested, use `channels.md`. Newsletter mentions and YouTube Community adaptations are channel variants of the core campaign assets; do not count them as additional announcement concepts.
