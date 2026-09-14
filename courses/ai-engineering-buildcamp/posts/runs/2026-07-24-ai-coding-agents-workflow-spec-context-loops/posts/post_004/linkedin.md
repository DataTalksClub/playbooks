---
post_id: post_004
platform: linkedin
status: draft
---

Context engineering for coding agents is mostly documentation discipline.

When you start a new agent session, the agent has to figure out:

- What project is this?
- Which commands should it run?
- Where are tasks tracked?
- What process should it follow?
- Which files explain testing, UI, API, or deployment rules?
- Which decisions were already made?

You can repeat this in every prompt.

Or you can put the context in the repository.

In the workshop, I used a small `AGENTS.md` file as the root context.

For Claude Code, I also keep a tiny `CLAUDE.md` that points to `AGENTS.md`, so the setup stays tool-agnostic.

The important part is to keep the root file short.

Do not dump everything there.

Use it as a map:

- Process lives in `docs/process.md`
- PM role lives in a role file
- Engineer role lives in a role file
- QA role lives in a role file
- Testing guidelines can live in a separate doc
- UI/design rules can live in a separate doc

Then the agent can load the context needed for the current task.

This saves tokens and reduces confusion.

For me, this is the practical version of context engineering:

Put durable project knowledge where the agent can find it.

Workshop recording:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
