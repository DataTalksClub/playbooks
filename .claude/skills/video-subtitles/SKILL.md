---
name: video-subtitles
description: Burn supplied SRT subtitles into a local video, resize captions, or highlight each word in sync with speech. Use for subtitle overlays and karaoke-style captions; use video-clip-cutter for trimming or branded social frames.
---

# Video Subtitles

Use the supplied video and SRT as the source of truth. Keep the original video and subtitle file intact and write a new video into a dedicated output directory. Do not rewrite the transcript or add branding unless requested.

## Render

The helper supports ordinary subtitles (`static`) and audio-aligned word highlighting (`follow`). Choose `follow` when the user asks for text to follow their speech, karaoke captions, or the current word to light up. It uses the existing SRT segment boundaries and aligns the words against the audio, rather than dividing each segment into equal time intervals.

Run from the repository root:

```bash
python .claude/skills/video-subtitles/scripts/render_subtitles.py video.mp4 subtitles.srt --output-dir captioned
python .claude/skills/video-subtitles/scripts/render_subtitles.py video.mp4 subtitles.srt --output-dir captioned --mode follow --font-size 64
```

Requires `ffmpeg` with libass and `ffprobe` on PATH (or pass `--ffmpeg` and `--ffprobe`). Static captions need only Python's standard library. For word alignment, use a project-local environment:

```bash
uv venv .venv
uv pip install --python .venv/bin/python torch torchaudio --index-url https://download.pytorch.org/whl/cpu
uv pip install --python .venv/bin/python stable-ts
```

On Windows, the environment's Python is `.venv/Scripts/python.exe`. Run the helper with that interpreter. The first alignment downloads the selected Whisper model (`base.en` by default); `--model` and `--language` support other speech. Audio processing stays local.

## Appearance and revisions

- Defaults: bold white text with a black outline, centered near the bottom. Font size scales with video height (64 at 1080p). `--font-size`, `--font`, and `--margin-bottom` control it.
- Follow mode shows short phrases and highlights the spoken word in yellow. Configure `--highlight-color`, `--max-words`, and `--max-chars` when needed. Preserve requested font and placement when changing timing behavior.
- Static mode keeps the supplied subtitle segments. Overlapping cues are shortened in the generated caption file to avoid simultaneous stacked captions; the source SRT is untouched.
- Cached word timing is reused for appearance changes. The cache records the subtitle hash, source video identity, language, and model; changing these causes realignment. Edit `words` in the JSON to correct timing, then rerun. `--realign` discards cached timing.
- Use a new `--name` for a review variant, or `--overwrite` when the user asks to replace an existing generated version. The helper refuses to overwrite the source video.

## Verify and deliver

Decode the finished video with `ffmpeg -v error -i OUTPUT.mp4 -f null -` and inspect captioned frames, including a long phrase, for clipping and readability. For follow mode, review a short passage in motion when playback is available; inspect the timestamp JSON for zero-duration words or suspicious gaps and correct them when necessary. Do not claim a listening check from a still image.

Return a clickable link to the video. The output directory also contains the editable `.ass` file and, in follow mode, `.words.json` timing data. Generated media, audio, model weights, and environments belong outside tracked skill files.
