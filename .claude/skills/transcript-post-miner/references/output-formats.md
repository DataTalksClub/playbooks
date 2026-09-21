# Output Formats

## Markdown Shortlist

Use this format for user review:

```markdown
# Transcript Post Ideas

Source: <video title or transcript path>

## 1. <Idea title>

Priority: 5/5
Platform fit: LinkedIn strong, X good
Confidence: high

Post angle:
<One paragraph explaining the post thesis.>

Why it is worth posting:
<One paragraph about audience value.>

Source moments:
- 00:05:37 - 00:08:18: <what this moment contributes>
- 00:14:18 - 00:19:20: <what this moment contributes>

Clip recommendation:
Use 00:05:50 - 00:07:30.

Clip reason:
<Why this excerpt works as a standalone clip.>

Writing brief:
Write a LinkedIn post for <audience> explaining <claim>. Include <specific points>. Keep it practical and grounded in the transcript.
```

## JSON Schema

Use this shape when the output will feed scripts:

```json
{
  "source": {
    "title": "",
    "video_id": "",
    "transcript_path": "",
    "duration_seconds": 0
  },
  "ideas": [
    {
      "id": "idea_001",
      "title": "",
      "priority": 5,
      "confidence": "high",
      "platform_fit": {
        "linkedin": "strong",
        "x": "good"
      },
      "post_angle": "",
      "why_worth_posting": "",
      "source_moments": [
        {
          "start": "00:05:37",
          "end": "00:08:18",
          "note": ""
        }
      ],
      "clip": {
        "recommended": true,
        "start": "00:05:50",
        "end": "00:07:30",
        "title": "",
        "reason": "",
        "quality": "high",
        "trim_notes": ""
      },
      "writing_brief": "",
      "status": "candidate"
    }
  ]
}
```

Allowed `status` values:

- `candidate`
- `approved`
- `rejected`
- `written`

## Social Writing Handoff Brief

Use this after the user approves an idea and before invoking `social-content-studio`.

```markdown
## Handoff Brief: <Idea title>

Topic:
<Short topic name.>

Timestamps:
- 00:22:21 - 00:26:50
- 00:26:50 - 00:30:27

Raw transcript excerpts:

### 00:22:21 - 00:26:50
<Verbatim transcript excerpt from this range.>

### 00:26:50 - 00:30:27
<Verbatim transcript excerpt from this range.>

Post angle:
<The approved angle.>

Clip recommendation:
<Clip range or "text-only".>

Writing brief for social-content-studio:
Write a LinkedIn/X post for <audience> explaining <claim>. Use only the angle and transcript excerpts above as source material.
```

Do not pass only a summary to `social-content-studio` when raw transcript excerpts are available.

## Clip Manifest CSV

Use `scripts/create_clip_manifest.py` to create this from `post-ideas.json`.

Columns:

- `idea_id`
- `title`
- `clip_start`
- `clip_end`
- `clip_quality`
- `clip_reason`
- `output_file`

Only ideas with `clip.recommended = true` are included.
