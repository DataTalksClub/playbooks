# Carousel Project Reference

Use this only after `alexey-carousel-generator` triggers.

## Local Renderer

- Project root: `/Users/valeria/carousel-automation`
- Renderer: `/Users/valeria/carousel-automation/src/render.js`
- Render helper: `/Users/valeria/.codex/skills/alexey-carousel-generator/scripts/render_post_media.py`

The renderer outputs:

- X/Twitter resource image: 1080 x 1350 px.
- LinkedIn square carousel: 1080 x 1080 px frames plus PDF.

## Content-Run Layout

For saved posts, write media beside the post drafts:

```text
posts/post_001/
  post.json
  linkedin.md
  x.md
  linkedin-carousel.json
  twitter-resource.json
  linkedin-carousel/
    frame-01.png
    ...
    carousel.pdf
  twitter-resource/
    twitter-resource.png
```

Update `post.json.files`:

```json
{
  "linkedin_carousel": "linkedin-carousel.json",
  "twitter_resource": "twitter-resource.json",
  "linkedin_carousel_output": "linkedin-carousel",
  "twitter_resource_image": "twitter-resource/twitter-resource.png"
}
```

## LinkedIn Carousel Schema

Use only implemented square frame types: `cover`, `title-paragraph`, and `outro`.

```json
{
  "title": "Deck title",
  "slides": [
    {
      "type": "cover",
      "author": "Alexey Grigorev",
      "title": "Hook/title",
      "subtitle": "One clear sentence.",
      "swipeLabel": "Swipe for more"
    },
    {
      "type": "title-paragraph",
      "title": "One idea",
      "body": "A compact explanation in two or three sentences."
    },
    {
      "type": "outro",
      "ctaText": "follow for more practical AI engineering notes",
      "supportingText": "Optional short supporting sentence.",
      "url": "Optional URL"
    }
  ]
}
```

Guidelines:

- Aim for 5-8 slides total.
- Use one idea per content slide.
- Keep title-paragraph bodies under about 280 characters.
- Use `variant: "light"` on selected `title-paragraph` slides for alternating dark/light slides.
- Convert lists into concise sentences or split them into multiple `title-paragraph` slides.

## X/Twitter Resource Schema

```json
{
  "resourceTitle": "Main Title",
  "subtitle": "Optional subtitle",
  "sections": [
    {
      "heading": "Section heading",
      "bullets": ["Bullet 1", "Bullet 2"]
    },
    {
      "heading": "Another heading",
      "body": "Short paragraph content."
    }
  ],
  "cta": "Optional CTA text"
}
```

Guidelines:

- Aim for 5-6 sections.
- Use 2-3 bullets per bullet section.
- Keep body paragraphs under about 120 characters when possible.
- Use `heading`, not `title`.
- If one image is too crowded, shorten first; accept renderer splits only when the content genuinely needs multiple images.

## Render Commands

Prefer the helper:

```bash
python3 /Users/valeria/.codex/skills/alexey-carousel-generator/scripts/render_post_media.py <content-run-or-post-folder>
```

Manual equivalents:

```bash
cd /Users/valeria/carousel-automation
node src/render.js <post-folder>/linkedin-carousel.json --square --output <post-folder>/linkedin-carousel
node src/render.js <post-folder>/twitter-resource.json --twitter --output <post-folder>/twitter-resource
```

## Validation

Before finishing:

- Parse all generated JSON.
- Confirm rendered files exist.
- Spot-check at least one resource image and one carousel cover/outro when practical.
- Report if visual inspection was not possible.
