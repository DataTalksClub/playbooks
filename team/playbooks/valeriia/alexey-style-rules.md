# Alexey's style rules for content (extracted from 2026 feedback to Valeriia)

Every rule below was stated by Alexey when correcting drafts. These are the
style gate any content-producing agent must pass. Source:
`team/telegram-analysis/reports/valeriia-analysis.md` §2.4 (dates cited
there). Related machine checks: his `stylint` repo and
`editing-playbook.md`; Valeriia's counterpart artifact is
`alexey_newsletter_style_guide.md`.

## Text

1. **No bold emphasis** in newsletters/READMEs — "мне жирно форматирование
   не нравится… сразу это видно, что это ЛЛМ писала" (2026-02-19).
2. **No topic-introducer openers** — cut "The flow is simple." before "I
   open the app…" (2026-05-22; encoded later as stylint rule
   `prompt-noun-phrase-smell`).
3. **Cut labeling/abstract noun phrases** — "a fitness tracker was a clear
   idea" → "I thought about a fitness tracker" (2026-06-26).
4. **Halve oversized text** without losing meaning; attention spans are
   short (2026-02-06); he routinely cuts intros in half (2026-07-10).
5. **No semicolons** — rewrite with periods (2026-06-26).
6. **Headlines are not questions** — "Choosing a portfolio project. The
   definite guide", never "How to…" (2026-07-03).
7. **Simple words** — "main path" > "mandatory path"; "another" >
   "different"; avoid "my audience", "emerging" (2026-01-23, 2026-01-07,
   2026-01-30, 2026-02-06).
8. **Story-first intros** — start with the story/origin, motivation early
   (2026-01-30, 2026-02-13).
9. **Concrete numbers in hooks** — "250 vacancies" makes posts attractive
   (2026-02-03).
10. **Sponsor copy must not use "we/us/our"** — confuses readers about who
    is speaking (house rule, 2026-05-25); ≤6 lines, clear CTA, working
    links.
11. **AI-detector must read 0%** — he edits Substack posts until the
    built-in detector is clean (2026-08-07).

## Links, images, formatting of posts

12. **Never hide links in X comments** — put them in the post (2026-01-23).
13. **Text before image** — people get confused otherwise (2026-04-02).
14. **Commands in monospace; captions short** — "Подпись длинная. Давай
    укоротим" (2026-01-16).
15. **Screenshots over generic AI art** — generated art signals no effort
    ("ассоциации с презентациями макинзи", 2026-02-26); mermaid diagrams
    are the cheap good default (Figma Jam converts them to editable).
16. **No stretched images** — broken proportions read unprofessional
    (2026-05-08).
17. **Keep UTM links verbatim**; CTA "read and subscribe" for Substack
    (2026-01-30, 2026-07-25).

## Process rules around editing

- First draft is an **idea/fact check**, not a polish pass (Valeriia's
  proposal he accepted, 2026-04-24): his comments come before her deep edit.
- Avoid double-editing: rougher brain-dumps + single-edit pass
  (policy after the 2026-03-26 double-edit waste).
- His named law: "Чем больше времени у тебя есть на редактуру, тем больше
  ты редактируешь" — time-box the review.
- Weak sponsor copy → proactively send our rewrite: "ваш вариант не очень,
  вот наш, если вам ок, то мы его используем" (2026-02-09).
