# Campaign Workspaces

Course folders and campaign folders have different ownership.

- `courses/<course>/` is the reusable reference source for the course: durable facts, positioning, audience, curriculum, FAQs, proof, and reusable copy patterns.
- `courses/campaigns/<course>-<year>/` contains cohort-specific decisions, dates, links, events, processes, and finished campaign copy.

## Source Precedence

When creating campaign content:

1. Start with the reusable course reference in `courses/<course>/`.
2. Apply explicit overrides from the campaign workspace.
3. Use confirmed event and cohort sources for dates, deadlines, speakers, and event links.
4. Keep the final campaign asset in the campaign `copy-bank/`.

Do not copy an unchanged course reference file into a campaign folder. Add a campaign version only when the cohort genuinely changes the value or needs a historical snapshot. A campaign-specific file should make its difference from the reusable course source clear.

## Suggested Shape

```text
courses/campaigns/<course>-<year>/
|-- processes/          Cohort brief, checklist, calendar, and retrospective
|-- copy-bank/          Final cohort-specific channel copy and event sources
|-- proof-library/      Proof collected or selected specifically for the campaign
|-- course.yaml         Optional cohort-specific overrides or deliberate snapshot
`-- positioning.md      Optional campaign-specific positioning
```

The existing `ai-dev-tools-zoomcamp-2026` workspace predates this rule and still contains unchanged copies. Migrate those copies separately after deciding which files must remain as historical snapshots.
