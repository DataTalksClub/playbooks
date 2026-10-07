#!/usr/bin/env python3
"""Burn supplied SRT captions, optionally aligned and highlighted word by word."""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


def parse_srt(path):
    pattern = re.compile(
        r"(?m)^\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*"
        r"(\d{2}:\d{2}:\d{2}[,.]\d{3})[^\n]*\n"
    )
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    cues = []
    for block in re.split(r"\n\s*\n", text.strip()):
        match = pattern.search(block)
        if not match:
            raise ValueError("Invalid SRT cue: " + block[:80])
        caption = " ".join(block[match.end():].split())
        start, end = (seconds(t) for t in match.groups())
        if end <= start or not caption:
            raise ValueError("Empty or invalid-duration subtitle cue")
        cues.append(dict(start=start, end=end, text=caption))
    if not cues:
        raise ValueError("No subtitle cues found")
    for previous, following in zip(cues, cues[1:]):
        if following["start"] <= previous["start"]:
            raise ValueError("SRT cues must have increasing start times")
        previous["end"] = min(previous["end"], following["start"])
    return cues


def seconds(value):
    h, m, s, ms = map(int, re.split(r"[:,.]", value))
    return h * 3600 + m * 60 + s + ms / 1000


def stamp(value):
    cs = max(0, round(value * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02}:{cs // 100 % 60:02}.{cs % 100:02}"


def escape(value):
    # Treat caption content as text, not executable ASS override tags.
    value = re.sub(r"</?(?:b|i|u|font)(?:\s[^>]*)?>", "", value, flags=re.I)
    return value.replace("\\", "/").replace("{", "(").replace("}", ")")


def ass_color(value):
    value = value.lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError("Color must be six hexadecimal digits")
    return f"&H00{value[4:6]}{value[2:4]}{value[0:2]}&"


def chunks(words, max_words, max_chars):
    result, current = [], []
    for word in words:
        if current and (
            len(current) >= max_words
            or len(" ".join(w["word"] for w in current + [word])) > max_chars
            or word["start"] - current[-1]["end"] > 0.6
        ):
            result.append(current)
            current = []
        current.append(word)
        if word["word"].endswith((".", "?", "!")):
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result


def aligned_words(args, cues, cache, ffmpeg):
    stat = args.video.stat()
    identity = dict(
        video=str(args.video.resolve()), size=stat.st_size, mtime_ns=stat.st_mtime_ns,
        subtitle_sha256=hashlib.sha256(args.subtitles.read_bytes()).hexdigest(),
        model=args.model, language=args.language,
    )
    if cache.exists() and not args.realign:
        saved = json.loads(cache.read_text(encoding="utf-8"))
        if saved.get("source") == identity:
            print("Reusing word timing:", cache)
            return saved["words"]
    try:
        import torch
        import stable_whisper
    except ImportError as error:
        raise ValueError("Follow mode requires stable-ts and PyTorch; see SKILL.md") from error
    torch.set_num_threads(4)
    audio = cache.with_suffix(".wav")
    subprocess.run([ffmpeg, "-v", "error", "-y", "-i", str(args.video),
                    "-vn", "-ar", "16000", "-ac", "1", str(audio)], check=True)
    model = stable_whisper.load_model(args.model, device="cpu")
    result = model.align_words(str(audio), cues, args.language, regroup=False, verbose=False)
    words = [dict(word=w.word.strip(), start=float(w.start), end=float(w.end))
             for segment in result.segments for w in segment.words if w.word.strip()]
    if not words:
        raise ValueError("Speech alignment returned no words")
    cache.write_text(json.dumps(dict(source=identity, words=words), indent=2), encoding="utf-8")
    return words


def write_ass(args, cues, words, path, width, height, duration):
    size = args.font_size or round(height * 64 / 1080)
    margin = args.margin_bottom if args.margin_bottom is not None else round(height * 0.05)
    mx = round(width * 0.064)
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,{args.font},{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,{max(2, round(height / 360))},1,2,{mx},{mx},{margin},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []

    def event(start, end, text):
        start, end = max(0, start), min(end, duration)
        if round(end * 100) > round(start * 100):
            events.append(f"Dialogue: 0,{stamp(start)},{stamp(end)},Caption,,0,0,0,,{text}")

    if args.mode == "static":
        for cue in cues:
            event(cue["start"], cue["end"], escape(cue["text"]))
    else:
        groups = chunks(words, args.max_words, args.max_chars)
        on, off = "{\\c" + ass_color(args.highlight_color) + "}", r"{\c&H00FFFFFF&}"
        for i, group in enumerate(groups):
            next_start = groups[i + 1][0]["start"] if i + 1 < len(groups) else duration
            hold_end = min(next_start, group[-1]["end"] + 0.3)
            for j, word in enumerate(group):
                end = group[j + 1]["start"] if j + 1 < len(group) else hold_end
                text = " ".join(on + escape(w["word"]) + off if j == k else escape(w["word"])
                                for k, w in enumerate(group))
                event(word["start"], end, text)
        instant = [w["word"] for w in words if w["end"] <= w["start"]]
        if instant:
            print("Review zero-duration word timings in the JSON:", instant)
    path.write_text(header + "\n".join(events) + "\n", encoding="utf-8-sig")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("subtitles", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=["static", "follow"], default="static")
    parser.add_argument("--font-size", type=int)
    parser.add_argument("--font", default="Arial")
    parser.add_argument("--margin-bottom", type=int)
    parser.add_argument("--highlight-color", default="#FFFF00")
    parser.add_argument("--max-words", type=int, default=5)
    parser.add_argument("--max-chars", type=int, default=48)
    parser.add_argument("--model", default="base.en")
    parser.add_argument("--language", default="en")
    parser.add_argument("--name", help="Output stem, without extension")
    parser.add_argument("--realign", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--ffmpeg", default=shutil.which("ffmpeg"))
    parser.add_argument("--ffprobe", default=shutil.which("ffprobe"))
    args = parser.parse_args()
    try:
        args.video, args.subtitles = args.video.resolve(), args.subtitles.resolve()
        if not args.video.is_file() or not args.subtitles.is_file():
            raise ValueError("Video and subtitle paths must be existing files")
        if not args.ffmpeg or not args.ffprobe:
            raise ValueError("ffmpeg and ffprobe are required")
        if args.font_size is not None and args.font_size <= 0:
            raise ValueError("Font size must be positive")
        if args.max_words <= 0 or args.max_chars <= 0 or (args.margin_bottom or 0) < 0:
            raise ValueError("Invalid phrase length or margin")
        if any(c in args.font for c in ",\r\n"):
            raise ValueError("Invalid font name")
        ass_color(args.highlight_color)
        name = args.name or f"{args.video.stem}-subtitled-{args.mode}"
        if not re.fullmatch(r"[\w.-]+", name) or name in (".", ".."):
            raise ValueError("Output name must be a filesystem-safe stem")
        folder = args.output_dir.resolve()
        output = folder / (name + ".mp4")
        if output.resolve() == args.video:
            raise ValueError("Refusing to overwrite the source video")
        if output.exists() and not args.overwrite:
            raise ValueError("Output exists; choose --name or explicitly use --overwrite")
        cues = parse_srt(args.subtitles)
        ffmpeg = str(Path(shutil.which(args.ffmpeg) or args.ffmpeg).resolve())
        ffprobe = str(Path(shutil.which(args.ffprobe) or args.ffprobe).resolve())
        probe = json.loads(subprocess.check_output([
            ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries",
            "stream=width,height:format=duration", "-of", "json", str(args.video)]))
        stream = probe["streams"][0]
        duration = float(probe["format"]["duration"])
        if cues[-1]["start"] >= duration:
            raise ValueError("Subtitle cues extend beyond the video")
        folder.mkdir(parents=True, exist_ok=True)
        words = aligned_words(args, cues, folder / (name + ".words.json"), ffmpeg) if args.mode == "follow" else None
        captions = folder / (name + ".ass")
        write_ass(args, cues, words, captions, stream["width"], stream["height"], duration)
        # A safe relative filename avoids Windows drive-colon escaping in libass filters.
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "warning",
                        "-y" if args.overwrite else "-n", "-i", str(args.video),
                        "-vf", "ass=" + captions.name, "-c:v", "libx264", "-preset", "medium",
                        "-crf", "18", "-c:a", "copy", "-movflags", "+faststart", str(output)],
                       cwd=folder, check=True)
        print("Created:", output)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
