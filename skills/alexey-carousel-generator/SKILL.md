---
name: alexey-carousel-generator
description: Generate and render Alexey Grigorev style social media assets for saved post artifacts. Use when Codex needs to create LinkedIn carousel JSON, X/Twitter resource JSON, rendered carousel PNG/PDF files, or rendered Twitter resource images from post text, markdown drafts, content-run post folders, or Alexey social post records; also use when a post-generation workflow asks for media/carousels/resources to be produced with the posts.
---

# Alexey Carousel Generator

## Default Workflow

Use the content-run flow by default:

1. Read `references/carousel-project.md` only for schema and style details needed for the task.
2. For each post folder, read `linkedin.md`, `x.md`, and `post.json` when present.
3. Write media source files directly into that same post folder:
   - `linkedin-carousel.json`
   - `twitter-resource.json`
4. Render directly into that same post folder:
   - `linkedin-carousel/`
   - `twitter-resource/`
5. Update `post.json.files` with the source and rendered asset paths.
6. Validate JSON and rendered output files before finishing.

Avoid temporary staging/copy steps for normal content runs. Create files where they belong first.

## Generate

Create both formats for Alexey posts unless the user asks for only one:

- LinkedIn carousel: 5-8 square slides, one idea per slide.
- X/Twitter resource: one compact 1080 x 1350 resource image with 5-6 sections.

For square LinkedIn carousels, use only currently implemented frame types:

- `cover`
- `title-paragraph`
- `outro`

Do not use `bullet-list` for square carousels in this project; the template is not implemented.

## Render

After writing or editing media JSON, run:

```bash
python3 /Users/valeria/.codex/skills/alexey-carousel-generator/scripts/render_post_media.py <post-folder-or-content-run>
```

The script renders any existing `linkedin-carousel.json` and `twitter-resource.json`, then updates `post.json.files`.

If the script fails because Chromium is blocked by sandboxing, rerun the same command with approval/escalation. Do not replace this with manual copy/staging work.

## Style

- Keep Alexey's voice practical, specific, engineering-oriented, and clear.
- Avoid hype, grand claims, generic marketing copy, and em dashes.
- Prefer short sentences, concrete mechanisms, useful distinctions, and "what this means in practice" framing.
- Keep DataTalks.Club as a future separate style unless the user explicitly asks for that brand.

## Done Criteria

- `linkedin-carousel.json` and/or `twitter-resource.json` exist in each target post folder.
- Rendered files exist:
  - LinkedIn: `linkedin-carousel/frame-01.png` through final frame plus `linkedin-carousel/carousel.pdf`
  - X/Twitter: `twitter-resource/twitter-resource.png`
- `post.json.files` points to both source JSON and rendered output paths.
- JSON parses cleanly.
