---
post_id: post_005
platform: linkedin
status: draft
---

Project-level specs are not enough for coding agents.

Each feature still needs grooming.

In the workshop, after creating GitHub issues from the project plan, I took one issue and made it more precise.

This is the product manager role.

The PM turns a rough task into something an engineer, human or agent, can implement without guessing the user-facing behavior.

For each feature, I want:

- Goal
- Description
- Acceptance criteria
- Edge cases
- Out-of-scope items

The acceptance criteria are the most important part.

They should be checkable.

Someone should be able to point at the screen and say:

"Yes, this passes."

or

"No, this does not pass."

Example:

For "authentication without email", the groomed issue says the visitor can register with username, display name, and password.

It also says what should not exist:

- No email backend
- No verification flow
- No password reset
- No account settings

This matters because agents like to add reasonable-sounding extras.

Out-of-scope sections protect the MVP.

Feature specs are where we remove ambiguity before implementation.

Workshop recording:
https://www.youtube.com/live/VUJxJGpaDEs?si=AKuzzOhHXCGps0ts
