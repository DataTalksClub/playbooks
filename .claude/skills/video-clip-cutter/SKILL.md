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

After cutting, `scripts/render_social_clip.py` burns word-by-word captions into a landscape clip and normalizes loudness to -14 LUFS. It has two formats:

- `vertical` (default): a 1080x1920 frame with a label pill and title above, the clip at full width in the middle, and captions below it with the spoken word in the accent colour. Captions sit under the video, so they never cover a shared screen.
- `horizontal`: the clip at its own size with no frame or title, and captions in an accent-coloured box at the bottom of the picture, with the spoken word at full white.

```bash
uv run --with mlx-whisper --with pillow python3 .claude/skills/video-clip-cutter/scripts/render_social_clip.py \
  content-runs/<run>/clips/dtc-post-001-software-factory.mp4 \
  --style datatalksclub --title "<title from the post>" --label workshop \
  --names "Louis Amaudruz, Switch, SandboxAQ, DataTalks.Club"

uv run --with mlx-whisper --with pillow python3 .claude/skills/video-clip-cutter/scripts/render_social_clip.py \
  content-runs/<run>/clips/dtc-post-001-software-factory.mp4 --style datatalksclub --format horizontal
```

- Output goes to `clips/vertical/` or `clips/horizontal/`, with the `.ass` caption file (and, for vertical, `.frame.png`) next to the video for review.
- Both formats share one transcript per clip: `clips/captions/<clip>.words.json`. Pass every speaker, product and sponsor name in `--names` on the first run, then read that file. To fix a misheard word, edit it and rerun: the edited file is reused. `--retranscribe` starts over.
- The vertical title is copy. Take it from the owner's post (the hook), in the owner's voice; do not invent a new claim for it.
- Styles live in `references/clip-styles.json`, keyed by owner. Only `datatalksclub` exists; ask for Alexey's style before rendering his clips.
- Needs an ffmpeg with libass: Homebrew `ffmpeg-full` (keg-only), which the script finds on its own.

## Output Rules

- Use descriptive, filesystem-safe filenames such as `post-01-plain-llm-vs-rag.mp4`.
- Put all generated files into a dedicated output directory.
- Keep every final output clip under 600 seconds.
- Prefer manifest-based cutting over one-off shell commands when there are more than two clips.
- Preserve the user's original video file. Do not overwrite it.

## Resources

- `scripts/cut_video_clips.py`: manifest-driven ffmpeg runner for single clips and combined multi-part clips.
- `scripts/render_social_clip.py`: captioned vertical (1080x1920, with title) and horizontal versions, with loudness normalization.
- `references/clip-manifest-format.md`: manifest format, examples, and command options.
- `references/clip-styles.json`: per-owner fonts, colours, and sizes for the captioned versions.
- `assets/fonts/`: Ubuntu Bold (Ubuntu Font Licence, `UFL.txt`) for the DataTalks.Club style.
