#!/usr/bin/env python3
"""Render a cut clip with burned-in captions, as a branded vertical video or as-is.

- vertical (1080x1920): label pill and title above, the landscape clip at full
  width in the middle, word-by-word captions below it with the spoken word highlighted.
- horizontal: the clip at its own size, no frame or title, captions in a box at
  the bottom of the picture.
Audio is normalized to -14 LUFS. Brand styles live in references/clip-styles.json.

Run through `uv` so nothing needs installing:
    uv run --with mlx-whisper --with pillow python3 \
      .claude/skills/video-clip-cutter/scripts/render_social_clip.py CLIP \
      --style datatalksclub --title "..." --label workshop --names "Louis Amaudruz, Switch"
    ... CLIP --style datatalksclub --format horizontal --names "Louis Amaudruz, Switch"

- Captions come from transcribing the clip itself with word timestamps, saved as
  `captions/<clip>.words.json` next to the clip and shared by both formats. Fix
  misheard words in that file and rerun: an existing words file is reused.
- Needs an ffmpeg built with libass (Homebrew `ffmpeg-full`); found automatically.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
STYLES_PATH = SKILL_DIR / "references" / "clip-styles.json"
FFMPEG_FULL = Path("/opt/homebrew/opt/ffmpeg-full/bin")
WIDTH, HEIGHT = 1080, 1920


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a clip as a branded vertical video.")
    parser.add_argument("clip", type=Path, help="A landscape clip cut by cut_video_clips.py.")
    parser.add_argument("--style", required=True, help="Style name from references/clip-styles.json.")
    parser.add_argument("--format", choices=["vertical", "horizontal"], default="vertical")
    parser.add_argument("--title", default="", help="Title text above the video (vertical only, required there).")
    parser.add_argument("--label", default="", help="Optional pill above the title, for example 'workshop'.")
    parser.add_argument("--logo", type=Path, help="Optional logo image placed at the bottom.")
    parser.add_argument("--names", default="", help="Names and terms to prime Whisper, for example 'Louis Amaudruz, Switch'.")
    parser.add_argument("--output-dir", type=Path, help="Defaults to a vertical/ or horizontal/ folder next to the clip.")
    parser.add_argument("--retranscribe", action="store_true", help="Ignore an existing words file.")
    parser.add_argument("--model", default="mlx-community/whisper-large-v3-turbo")
    return parser.parse_args()


def find_ffmpeg() -> tuple[str, str]:
    for folder in (FFMPEG_FULL, None):
        ffmpeg = str(folder / "ffmpeg") if folder else shutil.which("ffmpeg")
        if not ffmpeg or not Path(ffmpeg).exists():
            continue
        filters = subprocess.run([ffmpeg, "-hide_banner", "-filters"], capture_output=True, text=True).stdout
        if " ass " in filters:
            return ffmpeg, str(Path(ffmpeg).with_name("ffprobe"))
    raise SystemExit("No ffmpeg with libass found. Install it with: brew install ffmpeg-full")


def probe(ffprobe: str, clip: Path) -> tuple[int, int, float]:
    out = subprocess.run(
        [ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
         "-of", "json", str(clip)], check=True, capture_output=True, text=True).stdout
    info = json.loads(out)
    stream = info["streams"][0]
    return stream["width"], stream["height"], float(info["format"]["duration"])


def transcribe_words(clip: Path, words_path: Path, names: str, model: str, retranscribe: bool) -> list[dict]:
    if words_path.exists() and not retranscribe:
        print(f"reusing {words_path.name}")
        return json.loads(words_path.read_text(encoding="utf-8"))["words"]
    try:
        import mlx_whisper  # noqa: PLC0415
    except ImportError:
        raise SystemExit("mlx-whisper is not available. Run through: uv run --with mlx-whisper --with pillow python3 ...")
    result = mlx_whisper.transcribe(str(clip), path_or_hf_repo=model, word_timestamps=True, language="en",
                                    initial_prompt=f"{names}." if names else None)
    words = [{"word": w["word"].strip(), "start": round(w["start"], 2), "end": round(w["end"], 2)}
             for seg in result["segments"] for w in seg.get("words", []) if w["word"].strip()]
    words_path.write_text(json.dumps({"clip": clip.name, "words": words}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {words_path.name}: {len(words)} words")
    return words


def chunk_words(words: list[dict], max_words: int = 4, max_chars: int = 26, max_gap: float = 0.6) -> list[list[dict]]:
    """Group words into short caption chunks, breaking at sentence ends and pauses."""
    chunks: list[list[dict]] = []
    current: list[dict] = []
    for word in words:
        if current:
            text = " ".join(w["word"] for w in current + [word])
            if len(current) >= max_words or len(text) > max_chars or word["start"] - current[-1]["end"] > max_gap:
                chunks.append(current)
                current = []
        current.append(word)
        if word["word"].endswith((".", "?", "!")) or (word["word"].endswith(",") and len(current) >= 2):
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)
    return chunks


def ass_color(hex_color: str) -> str:
    r, g, b = hex_color[1:3], hex_color[3:5], hex_color[5:7]
    return f"&H00{b}{g}{r}&".upper()


def ass_time(seconds: float) -> str:
    cs = max(0, round(seconds * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def ass_escape(text: str) -> str:
    return text.replace("\\", "/").replace("{", "(").replace("}", ")")


def caption_style(style: dict, fmt: str, width: int, height: int, caption_top: int) -> tuple[str, str, str]:
    """Return the ASS style line and the tags that switch the spoken word on and off."""
    font = style["font_family"]
    if fmt == "vertical":
        text, accent = ass_color(style["text"]), ass_color(style["accent"])
        line = (f"Style: Caption,{font},{style['caption_size']},{text},{text},{text},{text},-1,0,0,0,100,100,0,0,"
                f"1,0,0,8,{style['margin']},{style['margin']},{caption_top},1")
        return line, f"{{\\c{accent}}}", f"{{\\c{text}}}"
    # Horizontal: white words in an accent-coloured box; words not being spoken are dimmed.
    size = round(height * style["overlay_caption_ratio"])
    box, dim = ass_color(style["accent"]), style["overlay_dim_alpha"]
    white = f"&H{dim}FFFFFF&"
    margin_x, margin_v = round(width * 0.1), round(height * 0.06)
    line = (f"Style: Caption,{font},{size},{white},{white},{box},{box},-1,0,0,0,100,100,0,0,"
            f"3,{round(size * 0.25)},0,2,{margin_x},{margin_x},{margin_v},1")
    return line, "{\\1a&H00&}", f"{{\\1a&H{dim}&}}"


def write_ass(chunks: list[list[dict]], style_line: str, on: str, off: str, res: tuple[int, int],
              duration: float, path: Path) -> None:
    lines = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {res[0]}", f"PlayResY: {res[1]}",
        "WrapStyle: 0", "ScaledBorderAndShadow: yes", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
        "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding",
        style_line,
        "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    for i, chunk in enumerate(chunks):
        next_start = chunks[i + 1][0]["start"] if i + 1 < len(chunks) else duration
        # Hold the chunk until the next one starts, unless there is a long pause.
        chunk_end = next_start if next_start - chunk[-1]["end"] <= 0.6 else chunk[-1]["end"] + 0.3
        for j, word in enumerate(chunk):
            start = word["start"]
            end = chunk[j + 1]["start"] if j + 1 < len(chunk) else chunk_end
            text = " ".join(
                f"{on}{ass_escape(w['word'])}{off}" if k == j else ass_escape(w["word"])
                for k, w in enumerate(chunk))
            lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(min(end, duration))},Caption,,0,0,0,,{text}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def wrap(draw, text: str, font, max_width: int) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        if lines and draw.textlength(f"{lines[-1]} {word}", font=font) <= max_width:
            lines[-1] = f"{lines[-1]} {word}"
        else:
            lines.append(word)
    return lines


def render_frame(style: dict, title: str, label: str, logo: Path | None, video_top: int, video_h: int, path: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont  # noqa: PLC0415
    except ImportError:
        raise SystemExit("Pillow is not available. Run through: uv run --with mlx-whisper --with pillow python3 ...")
    font_path = str(SKILL_DIR / style["font_file"])
    title_font = ImageFont.truetype(font_path, style["title_size"])
    label_font = ImageFont.truetype(font_path, style["label_size"])
    image = Image.new("RGB", (WIDTH, HEIGHT), style["background"])
    draw = ImageDraw.Draw(image)
    max_width = WIDTH - 2 * style["margin"]

    title_lines = wrap(draw, title, title_font, max_width)
    line_h = round(style["title_size"] * style["title_line_height"])
    pad_y, pad_x = style["label_padding"]
    label = label.upper()
    label_h = style["label_size"] + 2 * pad_y if label else 0
    block_h = label_h + (style["label_gap"] if label else 0) + line_h * len(title_lines)
    y = (video_top - block_h) // 2

    if label:
        label_w = round(draw.textlength(label, font=label_font)) + 2 * pad_x
        x = (WIDTH - label_w) // 2
        draw.rounded_rectangle((x, y, x + label_w, y + label_h), radius=style["label_radius"], fill=style["accent"])
        draw.text((WIDTH // 2, y + label_h // 2), label, font=label_font, fill=style["label_text"], anchor="mm")
        y += label_h + style["label_gap"]
    for line in title_lines:
        draw.text((WIDTH // 2, y + line_h // 2), line, font=title_font, fill=style["text"], anchor="mm")
        y += line_h

    if logo:
        mark = Image.open(logo).convert("RGBA")
        mark.thumbnail((max_width, 90))
        image.paste(mark, ((WIDTH - mark.width) // 2, HEIGHT - 70 - mark.height), mark)
    image.save(path)


def filter_path(path: Path) -> str:
    return str(path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'").replace(",", "\\,")


def main() -> None:
    args = parse_args()
    styles = json.loads(STYLES_PATH.read_text(encoding="utf-8"))
    if args.style not in styles:
        raise SystemExit(f"Unknown style {args.style!r}. Known: {', '.join(styles)}. Add it to {STYLES_PATH}.")
    style = styles[args.style]
    if args.format == "vertical" and not args.title:
        raise SystemExit("--title is required for the vertical format.")
    clip = args.clip.expanduser().resolve()
    out_dir = (args.output_dir or clip.parent / args.format).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg, ffprobe = find_ffmpeg()
    os.environ["PATH"] = f"{Path(ffmpeg).parent}{os.pathsep}{os.environ['PATH']}"  # Whisper loads audio via ffmpeg

    src_w, src_h, duration = probe(ffprobe, clip)
    if src_h >= src_w:
        raise SystemExit(f"{clip.name} is {src_w}x{src_h}; this layout expects a landscape clip.")

    stem = clip.stem
    captions_dir = clip.parent / "captions"
    captions_dir.mkdir(exist_ok=True)
    words = transcribe_words(clip, captions_dir / f"{stem}.words.json", args.names, args.model, args.retranscribe)
    ass_path, output = out_dir / f"{stem}.ass", out_dir / f"{stem}.mp4"
    subs = f"ass=filename={filter_path(ass_path)}:fontsdir={filter_path((SKILL_DIR / style['font_file']).parent)}"
    audio = ["-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-ar", "48000"]
    video = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-movflags", "+faststart"]

    if args.format == "horizontal":
        line, on, off = caption_style(style, "horizontal", src_w, src_h, 0)
        write_ass(chunk_words(words), line, on, off, (src_w, src_h), duration, ass_path)
        cmd = ["-i", str(clip), "-vf", f"{subs},format=yuv420p", *audio, *video, str(output)]
    else:
        video_h = round(WIDTH * src_h / src_w / 2) * 2
        video_top = (HEIGHT - video_h) // 2
        line, on, off = caption_style(style, "vertical", WIDTH, HEIGHT, video_top + video_h + style["caption_gap"])
        write_ass(chunk_words(words), line, on, off, (WIDTH, HEIGHT), duration, ass_path)
        frame_path = out_dir / f"{stem}.frame.png"
        render_frame(style, args.title, args.label, args.logo, video_top, video_h, frame_path)
        graph = (f"[1:v]scale={WIDTH}:{video_h},setsar=1[clip];"
                 f"[0:v][clip]overlay=0:{video_top}:shortest=1,{subs},format=yuv420p[out]")
        cmd = ["-loop", "1", "-framerate", "30", "-i", str(frame_path), "-i", str(clip),
               "-filter_complex", graph, "-map", "[out]", "-map", "1:a", *audio, *video, "-r", "30", "-shortest",
               str(output)]
    subprocess.run([ffmpeg, "-v", "error", "-stats", "-y", *cmd], check=True)
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
