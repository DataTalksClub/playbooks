#!/usr/bin/env python3
"""Cut video clips from a JSON manifest with ffmpeg."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import Any


TIMESTAMP_RE = re.compile(r"^(?:(\d{1,2}):)?([0-5]?\d):([0-5]\d)(?:\.\d{1,3})?$")
MAX_CLIP_DURATION_SECONDS = 600.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Cut one or more timestamped clips from a local video file."
    )
    parser.add_argument("manifest", type=Path, help="Path to a JSON clip manifest.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print ffmpeg commands without executing them.",
    )
    parser.add_argument(
        "--reencode",
        action="store_true",
        help="Re-encode clips for more accurate cuts instead of using stream copy.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Override the output_dir field from the manifest.",
    )
    return parser.parse_args()


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    if "input" not in manifest:
        raise ValueError("Manifest is missing required field: input.")
    if "clips" not in manifest or not isinstance(manifest["clips"], list):
        raise ValueError("Manifest must contain a clips list.")

    return manifest


def validate_timestamp(value: str, field: str) -> None:
    if not isinstance(value, str) or not TIMESTAMP_RE.match(value):
        raise ValueError(f"Invalid {field} timestamp: {value!r}")


def timestamp_to_seconds(value: str) -> float:
    validate_timestamp(value, "timestamp")
    parts = value.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        hours = "0"
    else:
        hours, minutes, seconds = parts
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def segment_duration_seconds(segment: dict[str, Any]) -> float:
    start = segment.get("start")
    end = segment.get("end")
    validate_timestamp(start, "start")
    validate_timestamp(end, "end")

    duration = timestamp_to_seconds(end) - timestamp_to_seconds(start)
    if duration <= 0:
        raise ValueError(f"Segment end must be after start: {start!r} -> {end!r}")
    return duration


def validate_clip_duration(clip: dict[str, Any]) -> None:
    output_name = clip.get("output")
    if not isinstance(output_name, str) or not output_name.strip():
        raise ValueError("Each clip must define a non-empty output filename.")

    segments = clip.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError(f"Clip {output_name!r} must contain at least one segment.")

    total_duration = 0.0
    for segment in segments:
        if not isinstance(segment, dict):
            raise ValueError(f"Clip {output_name!r} contains an invalid segment.")
        total_duration += segment_duration_seconds(segment)

    if total_duration >= MAX_CLIP_DURATION_SECONDS:
        raise ValueError(
            f"Clip {output_name!r} is {total_duration:.1f} seconds. "
            f"Clips must be shorter than {MAX_CLIP_DURATION_SECONDS:.0f} seconds."
        )


def validate_all_clips(clips: list[Any]) -> None:
    for clip in clips:
        if not isinstance(clip, dict):
            raise ValueError("Each item in clips must be an object.")
        validate_clip_duration(clip)


def safe_label(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    cleaned = cleaned.strip(".-")
    return cleaned or "segment"


def run_command(command: list[str], dry_run: bool) -> None:
    print(shlex.join(command))
    if not dry_run:
        subprocess.run(command, check=True)


def cut_command(
    input_path: Path,
    start: str,
    end: str,
    output_path: Path,
    reencode: bool,
) -> list[str]:
    command = [
        "ffmpeg",
        "-y",
        "-ss",
        start,
        "-to",
        end,
        "-i",
        str(input_path),
    ]

    if reencode:
        command.extend(
            [
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "18",
                "-c:a",
                "aac",
                "-b:a",
                "192k",
            ]
        )
    else:
        command.extend(["-c", "copy"])

    command.append(str(output_path))
    return command


def concat_command(list_path: Path, output_path: Path) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_path),
        "-c",
        "copy",
        str(output_path),
    ]


def write_concat_list(list_path: Path, part_paths: list[Path], dry_run: bool) -> None:
    print(f"# write concat list: {list_path}")
    if dry_run:
        for part_path in part_paths:
            print(f"file {shlex.quote(str(part_path))}")
        return

    with list_path.open("w", encoding="utf-8") as f:
        for part_path in part_paths:
            escaped = str(part_path).replace("'", "'\\''")
            f.write(f"file '{escaped}'\n")


def cut_clip(
    input_path: Path,
    output_dir: Path,
    clip: dict[str, Any],
    reencode: bool,
    dry_run: bool,
) -> Path:
    output_name = clip.get("output")
    if not isinstance(output_name, str) or not output_name.strip():
        raise ValueError("Each clip must define a non-empty output filename.")

    output_path = output_dir / safe_label(output_name)
    segments = clip.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError(f"Clip {output_name!r} must contain at least one segment.")

    for segment in segments:
        if not isinstance(segment, dict):
            raise ValueError(f"Clip {output_name!r} contains an invalid segment.")
        validate_timestamp(segment.get("start"), "start")
        validate_timestamp(segment.get("end"), "end")

    if len(segments) == 1:
        segment = segments[0]
        command = cut_command(
            input_path,
            segment["start"],
            segment["end"],
            output_path,
            reencode,
        )
        run_command(command, dry_run)
        return output_path

    parts_dir = output_dir / "_parts"
    if not dry_run:
        parts_dir.mkdir(parents=True, exist_ok=True)

    prefix = safe_label(str(clip.get("parts_prefix") or Path(output_name).stem))
    suffix = output_path.suffix or ".mp4"
    part_paths: list[Path] = []

    for index, segment in enumerate(segments, start=1):
        label = safe_label(str(segment.get("label") or f"part-{index:02d}"))
        part_path = parts_dir / f"{prefix}_part{index:02d}_{label}{suffix}"
        part_paths.append(part_path)
        command = cut_command(
            input_path,
            segment["start"],
            segment["end"],
            part_path,
            reencode,
        )
        run_command(command, dry_run)

    list_path = output_dir / f"{Path(output_name).stem}-concat.txt"
    write_concat_list(list_path, part_paths, dry_run)
    run_command(concat_command(list_path, output_path), dry_run)
    return output_path


def main() -> int:
    args = parse_args()
    manifest = load_manifest(args.manifest)

    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        raise SystemExit("ffmpeg was not found on PATH.")

    input_path = Path(manifest["input"]).expanduser()
    if not input_path.exists():
        raise SystemExit(f"Input video does not exist: {input_path}")

    validate_all_clips(manifest["clips"])

    output_dir = args.output_dir or Path(manifest.get("output_dir", "clips"))
    output_dir = output_dir.expanduser()
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    generated: list[Path] = []
    for clip in manifest["clips"]:
        generated.append(
            cut_clip(
                input_path=input_path,
                output_dir=output_dir,
                clip=clip,
                reencode=args.reencode,
                dry_run=args.dry_run,
            )
        )

    print("# generated outputs")
    for output_path in generated:
        print(output_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
