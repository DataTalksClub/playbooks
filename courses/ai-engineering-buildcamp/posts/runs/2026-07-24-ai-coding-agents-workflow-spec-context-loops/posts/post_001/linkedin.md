---
post_id: post_001
platform: linkedin
status: draft
---

A working agent-built app can still be the wrong app.

In the workshop, I tried a one-shot prompt:

"Implement tool for weekly feedback for projects."

The agent built something. It chose a stack, created a CLI, and produced a tool for tracking weekly project health.

The problem: this was not the product I wanted.

What I had in mind was a team retrospective workflow:

- Team members submit start/stop/continue feedback
- People can submit anonymously
- Feedback is revealed at the right time
- Cards are clustered
- The team votes on discussion topics
- Actions and decisions are captured after the meeting

The short prompt did not contain any of this.

So the agent had to make product decisions for me.

This is the main reason I prefer spec-driven development with coding agents.

Before asking an agent to implement, write down:

- Who the users are
- What workflow they follow
- What is in the MVP
- What is explicitly out of scope
- What decisions the agent should not make

The code can be technically fine and still miss the product.

Specification is how we reduce that risk.

Workshop recording:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
