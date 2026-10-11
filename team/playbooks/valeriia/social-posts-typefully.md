# Playbook: Social posts via Typefully (Valeriia)

Source: `team/telegram-analysis/reports/valeriia-analysis.md` §3A, §3D, §3E,
§3F, playbooks 3/5/11/12. Evidence dates cited there.

**Surface**: X @Al_Grigor (primary), LinkedIn, Substack notes, Threads
(added 2026-10-03, Alexey drove the account setup), Instagram (experiment,
access lost). DTC accounts handled separately.

## The core loop (event/workshop/podcast posts)

1. **Trigger**: Alexey's voice note or an event link — "сделай пост(ы) про
   это", often with counts ("4-5 постов на этой неделе и 2-3 на следующей").
2. Read the event description; extract the essence + audience value + CTA.
3. Draft 1–3 posts into Typefully (team workspace since 2026-05-27).
4. Schedule at the standard slots: 09:00, 12:00, 16:00/17:00 CET.
5. Tag companies: X immediately, LinkedIn after publish. Hold other
   LinkedIn posts on a sponsor's paid day (2026-03-05).
6. Report back with the scheduled screenshot or published URLs (2026-10-09
   shows the four-platform URL bundle: X, LinkedIn, Substack note, Threads).

**Queue discipline**: keep the Typefully queue filled 1–2 weeks ahead;
tag every sponsored post with the sponsor name for analytics
("мы их тегаем с именем спонсора", 2026-02-18). Typefully API key shared
with Alexey for archive/evergreen analysis (2026-05-27).

## Video clips → posts (now semi-automated)

History: Grace cut clips by NotebookLM timestamps → Valeriia watched, fed
transcripts to ChatGPT, wrote posts (early 2026). Her March automation
(`kavaivaleri/short-video-automation`): YouTube transcript → GPT-5-mini
clean (~$0.13–0.30/video) → GPT-5.4 chapters → ffmpeg cuts → drafts +
manual style edit.

**Current state (since 2026-09-23)** — skills she shipped into this repo:
- `social-content-studio`: transcript → select moments → clips → drafts +
  Twitter image + LinkedIn carousel → **Typefully upload including media**.
- `video-clip-cutter`: vertical cuts + burned subtitles.
Alexey's extension (2026-10-07): Zoom-cloud recordings + transcripts
auto-forward to an agent (Zoom transcripts preferred — speaker-separated).

**Next step already identified**: close the loop — new recording → agent →
Typefully draft with media, no human trigger.

## Recurring post types

- **Milestone posts**: round numbers + screenshot + gratitude across
  channels; sponsor-thanks variant. Examples: 1,700 live viewers
  (2026-01-12), 90k→100k Slack (2026-03-15/09-29), 564 certificates
  (2026-04-30), 101 ASL members (2026-07-17), DTC's 6th birthday
  (2026-09-16). ~Monthly.
- **Evergreen reposts**: top past posts from analytics on slow weeks;
  refresh dates/numbers; X reposts of Substack articles with ~1 week lag;
  FDE-post rerun (praised 2026-08-26). "Lightning Lessons… информация не
  устаревает".
- **Trend explainers**: hot topic (his weekly Reddit/HN digest agent since
  2026-09-25, or his ping) → research article → style edit → Substack
  (optionally paid) → promo posts. Staleness judgment matters (declined a
  leaked doc as stale 2026-04-16; accepted Karpathy autoresearch
  2026-03-16).
- **Q&A/engagement bait**: "попросить у них в комментах писать какие задачи
  дают на собеседованиях" (2026-02-02).

## Stats collection (monthly or on request)

X/LinkedIn recap (impressions, follower deltas), LinkedIn engagement
trends + hypotheses, newsletter open/CTR decay investigation, YouTube
subscriber sources, Mailchimp sponsor stats, course funnel via promo codes,
registration counts. Output: numbers + deltas + one insight + hypothesis +
screenshots (2026-05-29, 2026-09-08).
