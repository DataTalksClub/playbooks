# Examples

Use this reference only for approved DataTalks.Club event-promotion examples. Do not treat drafts, rejected campaigns, or arbitrary prior posts as style examples unless the user explicitly approves them.


## How To Add Examples

When adding examples, include enough context for future calibration:

- Event title.
- Event type.
- Sponsor or product, if any.
- Speaker.
- Source material summary.
- Why the campaign worked.
- Final approved posts.

Keep examples concise and representative. Prefer a few high-quality examples over a large archive.

## Example Entry Format

```markdown
## [Event Title]

**Event type:**

**Sponsor/product:**

**Speaker:**

**Why this is a good example:**

### Main Announcement

[Approved post]

### Reminder

[Approved post]

### Educational Post: [Angle]

[Approved post]
```

## Building AI Agent Workflows with Switch (recording recap, published 2026-09-23)

**Event type:** Hands-on workshop, recording repurposing (Stage 2)

**Sponsor/product:** Switch, open source, github.com/sandbox-quantum/switch

**Speaker:** Louis Amaudruz, AI Engineer at SandboxAQ

**Why this is a good example:** The published version of a recap, after Valeriia's edits. It opens with what was built rather than with the recording, gives the speaker's credentials their own sentence, lists what was built as bullets, and ends with a reason to open each link. The X version shows the thread shape: one idea per post, a blank line before bullets, five posts rather than four.

### Recap, LinkedIn

Louis Amaudruz built a team of AI agents in Slack, live, during our workshop. They worked together on GitHub issues for the Switch repository.

The recording is now up.

Louis is an AI Engineer at SandboxAQ. He started with an empty Slack workspace and walked through each agent:

- A Claude Code coder agent that fixes an issue and opens a pull request
- A Codex reviewer agent that reviews the fix in the same channel
- A lead agent that runs the code-review loop, with a maximum of two cycles
- An issue manager that creates one channel per issue and starts the work in each of them

Louis also showed how the Switch team uses the same pattern for its own work, with rooms for bug reports, feature work, local deployments, releases, and staging deployments.

The Q&A covered agent permissions and sandboxing, prompt injection through GitHub issues, bringing custom agents, and agent protocols such as AG-UI and ACP.

Watch the recording to follow the full build, including the setup and the fixes made along the way:
https://www.youtube.com/watch?v=vl00W8eEtZg

Switch is open source. Explore the repository:
https://github.com/sandbox-quantum/switch

### Recap, X thread

1/5

Louis Amaudruz built a team of AI agents in Slack, live, during our workshop.

They worked together on GitHub issues for the Switch repository.

The recording is now up.

2/5

What was built, step by step:

- Claude Code coder that opens a PR
- Codex reviewer in the same channel
- Lead agent running up to two code-review cycles
- Issue manager that opens one channel per issue

3/5

Louis also showed how the Switch team uses the same pattern for its own work, with rooms for bug reports, feature work, local deployments, releases, and staging deployments.

4/5

The Q&A covered agent permissions and sandboxing, prompt injection through GitHub issues, bringing custom agents, and agent protocols such as AG-UI and ACP.

5/5

Watch the full build:
https://www.youtube.com/watch?v=vl00W8eEtZg

Switch is open source:
https://github.com/sandbox-quantum/switch
