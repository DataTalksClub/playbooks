---
name: video-clip-cutter
description: Cut local video files into timestamped clips with ffmpeg. Use when the user asks to extract, split, trim, cut, or concatenate video sections from timestamps for social posts, YouTube chapters, workshop highlights, or clip manifests.
---

# Video Clip Cutter

## Overview

Use this skill to turn timestamp ranges into local video clips. It is designed for social content workflows where transcript mining or post briefs produce clip ranges, and the next step is to generate reusable `ffmpeg` commands or run them safely.

## Workflow

1. Identify the source video path, output directory, and clip ranges.
2. Check that the video file exists and `ffmpeg` is available.
3. Make sure every final clip is shorter than 600 seconds. For multi-segment clips, sum all segment durations.
4. Create a clip manifest when there are multiple clips or any clip has multiple disjoint segments.
5. Use `scripts/cut_video_clips.py` to dry-run commands first when the user only asks for code or commands.
6. Run the script without `--dry-run` only when the user asks to actually create the video files.
7. Report the output directory and generated filenames.

## Duration Requirement

Every generated video must be shorter than 600 seconds. Treat 600 seconds as too long. If a requested clip is 600 seconds or longer, ask the user to choose a tighter range or split it into multiple shorter clips.

The script validates all clip durations before running `ffmpeg`, so it will not create partial output when one of the requested clips is too long.

## Cutting Defaults

Default to stream copy:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json --dry-run
python3 scripts/cut_video_clips.py clip-manifest.json
```

Stream copy is fast and preserves quality, but cuts may land on nearby keyframes instead of the exact frame. When precision matters, use re-encoding:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json --reencode
```

Re-encoding is slower, but it is usually better for exact social clips.

## Multi-Segment Clips

If one post uses several separate parts of a video, define one clip with multiple `segments`. The script will cut each part, write a concat list, and create a combined final clip.

Keep the intermediate part files when they may be useful for manual review. The script does not delete generated files automatically.

## Captioned Social Versions

After cutting, burn word-by-word captions into each clip and normalize loudness to -14 LUFS. There are two formats:

- `vertical`: a 1080x1920 frame with a label pill and title above, the clip at full width in the middle, and captions below it with the spoken word in the accent colour. Captions sit under the video, so they never cover a shared screen.
- `horizontal`: the clip at its own size with no frame or title, and captions in an accent-coloured box at the bottom of the picture, with the spoken word at full white.

### In a content run

`scripts/render_run_clips.py` handles every post in a run in two passes:

```bash
# 1. Right after cutting: one transcript per clip, for writing the posts and clip titles.
uv run --with mlx-whisper --with pillow python3 .claude/skills/video-clip-cutter/scripts/render_run_clips.py content-runs/<run> --transcribe-only

# 2. After clip.title and clip.label are written in post.json: both captioned versions.
uv run --with mlx-whisper --with pillow python3 .claude/skills/video-clip-cutter/scripts/render_run_clips.py content-runs/<run>
```

- Transcripts go to `clips/captions/<clip>.words.json` (word timings, used for captions) and `<clip>.txt` (for reading), recorded as `clip.transcript` in `post.json`. Renders go to `clips/horizontal/` and `clips/vertical/`, recorded as `media.clip_horizontal` and `media.clip_vertical`.
- Captions always come from this per-clip Whisper pass, never from the recording transcript (such as a Zoom VTT): a VTT times whole phrases, not words, and hears names worse. Misheard names in the recording transcript are still a good start for `caption_names`.
- Before the first pass, add `caption_names` to `source/source.json`: every product, company, and tool name the speakers mention (the speaker, host, and title are added automatically).
- Read every `.txt` after the first pass. Put each misheard phrase in `source/source.json` as `caption_fixes` (`{"Cloud Code": "Claude Code"}`) and rerun: fixes apply to every clip, keep the word timings, and are reapplied on every run. Use `--retranscribe --post <id>` only when a whole clip transcript is wrong.
- A name you cannot verify from the source (for example, a first name heard only in the clip) stays as heard; flag it to the user instead of guessing.
- The vertical version is skipped when `clip.title` is empty. Posts whose owner has no style in `references/clip-styles.json` are transcribed only. Rejected and archived posts are skipped.
- `--post` and `--format` narrow a run.

### One clip

`scripts/render_social_clip.py` renders a single clip, outside a content run:

```bash
uv run --with mlx-whisper --with pillow python3 .claude/skills/video-clip-cutter/scripts/render_social_clip.py \
  <clip.mp4> --style datatalksclub --format vertical --title "<title>" --label workshop \
  --names "Louis Amaudruz, Switch, SandboxAQ" --fix "Cloud Code=Claude Code"
```

### Styles and setup

- Styles live in `references/clip-styles.json`, keyed by owner. Only `datatalksclub` exists; ask for Alexey's style before rendering his clips.
- The `.ass` caption file (and, for vertical, `.frame.png`) is kept next to each video for review.
- Needs an ffmpeg with libass: Homebrew `ffmpeg-full` (keg-only), which the scripts find on their own.

## Output Rules

- Use descriptive, filesystem-safe filenames such as `post-01-plain-llm-vs-rag.mp4`.
- Put all generated files into a dedicated output directory.
- Keep every final output clip under 600 seconds.
- Prefer manifest-based cutting over one-off shell commands when there are more than two clips.
- Preserve the user's original video file. Do not overwrite it.

## Resources

- `scripts/cut_video_clips.py`: manifest-driven ffmpeg runner for single clips and combined multi-part clips.
- `scripts/render_social_clip.py`: captioned vertical (1080x1920, with title) and horizontal versions of one clip, with loudness normalization.
- `scripts/render_run_clips.py`: clip transcripts and both captioned versions for every post in a content run.
- `references/clip-manifest-format.md`: manifest format, examples, and command options.
- `references/clip-styles.json`: per-owner fonts, colours, and sizes for the captioned versions.
- `assets/fonts/`: Ubuntu Bold (Ubuntu Font Licence, `UFL.txt`) for the DataTalks.Club style.
