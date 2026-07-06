#!/usr/bin/env python3
"""Download Typefully posts and export matches for course copy research."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_BASE_URL = "https://api.typefully.com"
DEFAULT_OUTPUT_DIR = Path("ai-dev-tools-zoomcamp/copy-bank/social-media/typefully")
DEFAULT_TERMS = ["zoomcamp", "free course"]
DEFAULT_ENDPOINT = "/v2/social-sets/{social_set_id}/drafts"
DEFAULT_DETAIL_ENDPOINT = "/v2/social-sets/{social_set_id}/drafts/{id}"
SOCIAL_SETS_ENDPOINT = "/v2/social-sets"


def utc_timestamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_api_key(args: argparse.Namespace) -> str:
    if args.api_key_stdin:
        api_key = sys.stdin.readline().strip()
    else:
        api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise SystemExit(
            f"Missing API key. Set {args.api_key_env} or pass --api-key-stdin."
        )
    return api_key


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def api_get(url: str, api_key: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GET {url} failed with {exc.code}: {error_body}") from exc
    if not body:
        return {}
    return json.loads(body)


def merge_query(url: str, params: dict[str, str]) -> str:
    parsed = urllib.parse.urlparse(url)
    query = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    query.update({key: value for key, value in params.items() if value})
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query)))


def endpoint_url(base_url: str, endpoint: str, social_set_id: str | None) -> str:
    endpoint = endpoint.format(social_set_id=social_set_id or "")
    if endpoint.startswith("http://") or endpoint.startswith("https://"):
        return endpoint
    return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"


def detail_endpoint_url(
    base_url: str,
    endpoint: str,
    social_set_id: str | None,
    item_id: str,
) -> str:
    endpoint = endpoint.format(social_set_id=social_set_id or "", id=item_id)
    if endpoint.startswith("http://") or endpoint.startswith("https://"):
        return endpoint
    return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"


def list_payload_items(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return []
    for key in ["data", "items", "results", "posts", "drafts", "published_posts"]:
        value = payload.get(key)
        if isinstance(value, list):
            return value
    return []


def pagination_next_url(payload: Any) -> str:
    if not isinstance(payload, dict):
        return ""
    for key in ["next", "next_url", "next_page_url"]:
        value = payload.get(key)
        if isinstance(value, str) and value:
            return value
    links = payload.get("links")
    if isinstance(links, dict):
        value = links.get("next")
        if isinstance(value, str) and value:
            return value
    return ""


def pagination_next_cursor(payload: Any) -> str:
    if not isinstance(payload, dict):
        return ""
    for key in ["next_cursor", "cursor", "after"]:
        value = payload.get(key)
        if isinstance(value, str) and value:
            return value
    pagination = payload.get("pagination")
    if isinstance(pagination, dict):
        for key in ["next_cursor", "cursor", "after"]:
            value = pagination.get(key)
            if isinstance(value, str) and value:
                return value
    meta = payload.get("meta")
    if isinstance(meta, dict):
        for key in ["next_cursor", "cursor", "after"]:
            value = meta.get(key)
            if isinstance(value, str) and value:
                return value
    return ""


def fetch_paginated(
    *,
    start_url: str,
    api_key: str,
    limit_param: str,
    limit: int,
    cursor_param: str,
    max_pages: int,
    pause_seconds: float,
) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    url = merge_query(start_url, {limit_param: str(limit)} if limit_param else {})
    seen_urls: set[str] = set()

    for page_number in range(1, max_pages + 1):
        if url in seen_urls:
            break
        seen_urls.add(url)
        payload = api_get(url, api_key)
        pages.append({"page": page_number, "url": url, "payload": payload})

        next_url = pagination_next_url(payload)
        if next_url:
            url = urllib.parse.urljoin(url, next_url)
        else:
            cursor = pagination_next_cursor(payload)
            if not cursor or not cursor_param:
                break
            url = merge_query(start_url, {limit_param: str(limit), cursor_param: cursor})
        time.sleep(pause_seconds)
    return pages


def social_set_text(record: Any) -> str:
    if not isinstance(record, dict):
        return str(record)
    values: list[str] = []
    for key in ["id", "name", "title", "display_name", "handle", "username", "slug"]:
        value = record.get(key)
        if isinstance(value, str):
            values.append(value)
    values.extend(collect_strings(record.get("accounts")))
    values.extend(collect_strings(record.get("profiles")))
    values.extend(collect_strings(record.get("platforms")))
    return " ".join(values)


def social_set_id(record: Any) -> str:
    if not isinstance(record, dict):
        return ""
    for key in ["id", "social_set_id"]:
        value = record.get(key)
        if isinstance(value, str) and value:
            return value
        if isinstance(value, int):
            return str(value)
    return ""


def post_id(record: Any) -> str:
    if not isinstance(record, dict):
        return ""
    for key in ["id", "draft_id", "post_id"]:
        value = record.get(key)
        if isinstance(value, str) and value:
            return value
        if isinstance(value, int):
            return str(value)
    return ""


def discover_social_set_ids(
    *,
    base_url: str,
    api_key: str,
    name_match: str,
    limit_param: str,
    limit: int,
    cursor_param: str,
    max_pages: int,
    pause_seconds: float,
) -> tuple[list[str], list[dict[str, Any]], list[Any]]:
    start_url = endpoint_url(base_url, SOCIAL_SETS_ENDPOINT, None)
    pages = fetch_paginated(
        start_url=start_url,
        api_key=api_key,
        limit_param=limit_param,
        limit=limit,
        cursor_param=cursor_param,
        max_pages=max_pages,
        pause_seconds=pause_seconds,
    )
    items = flatten_items({"pages": pages})
    needle = name_match.lower()
    matched = [
        item
        for item in items
        if needle in social_set_text(item).lower() and social_set_id(item)
    ]
    return [social_set_id(item) for item in matched], pages, matched


def hydrate_item_details(
    *,
    items: list[Any],
    base_url: str,
    detail_endpoint: str,
    social_set_id: str | None,
    api_key: str,
    pause_seconds: float,
) -> list[dict[str, Any]]:
    details: list[dict[str, Any]] = []
    for item in items:
        item_id = post_id(item)
        if not item_id:
            continue
        url = detail_endpoint_url(base_url, detail_endpoint, social_set_id, item_id)
        details.append({"id": item_id, "url": url, "payload": api_get(url, api_key)})
        time.sleep(pause_seconds)
    return details


def flatten_items(raw_payload: Any) -> list[Any]:
    if isinstance(raw_payload, dict) and isinstance(raw_payload.get("details"), list):
        return [
            detail["payload"]
            for detail in raw_payload["details"]
            if isinstance(detail, dict) and "payload" in detail
        ]
    if isinstance(raw_payload, dict) and isinstance(raw_payload.get("pages"), list):
        items: list[Any] = []
        for page in raw_payload["pages"]:
            if isinstance(page, dict):
                items.extend(list_payload_items(page.get("payload")))
        return items
    return list_payload_items(raw_payload)


def collect_strings(value: Any) -> list[str]:
    strings: list[str] = []
    if isinstance(value, str):
        strings.append(value)
    elif isinstance(value, list):
        for item in value:
            strings.extend(collect_strings(item))
    elif isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in {
                "text",
                "body",
                "content",
                "preview",
                "tweet",
                "caption",
                "thread",
                "posts",
                "platforms",
            }:
                strings.extend(collect_strings(item))
    return strings


def first_string(record: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = record.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def nested_platform_text(record: dict[str, Any]) -> str:
    texts: list[str] = []
    platforms = record.get("platforms")
    if isinstance(platforms, dict):
        for platform_payload in platforms.values():
            texts.extend(collect_strings(platform_payload))
    return "\n\n".join(text for text in texts if text).strip()


def normalize_post(record: Any, index: int) -> dict[str, Any]:
    if not isinstance(record, dict):
        return {
            "id": f"item_{index:04d}",
            "platform": "",
            "status": "",
            "published_at": "",
            "created_at": "",
            "updated_at": "",
            "url": "",
            "text": str(record),
            "raw": record,
        }

    text = first_string(record, ["text", "body", "content", "tweet", "caption"])
    if not text:
        text = nested_platform_text(record)
    if not text:
        text = first_string(record, ["preview", "scratchpad_text"])
    if not text:
        text = "\n\n".join(collect_strings(record)).strip()

    return {
        "id": str(record.get("id") or record.get("post_id") or record.get("draft_id") or f"item_{index:04d}"),
        "platform": first_string(record, ["platform", "network", "service"]),
        "status": first_string(record, ["status", "state"]),
        "published_at": first_string(record, ["published_at", "posted_at", "sent_at"]),
        "created_at": first_string(record, ["created_at", "created"]),
        "updated_at": first_string(record, ["updated_at", "updated"]),
        "url": first_string(
            record,
            [
                "url",
                "post_url",
                "public_url",
                "share_url",
                "x_published_url",
                "linkedin_published_url",
                "private_url",
            ],
        ),
        "text": text,
        "raw": record,
    }


def term_matches(text: str, terms: list[str]) -> list[str]:
    haystack = text.lower()
    return [term for term in terms if term.lower() in haystack]


def filter_posts(items: list[Any], terms: list[str]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for index, item in enumerate(items, start=1):
        post = normalize_post(item, index)
        matches_for_post = term_matches(post["text"], terms)
        if matches_for_post:
            post["matched_terms"] = matches_for_post
            matches.append(post)
    return matches


def write_csv(path: Path, posts: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "id",
        "platform",
        "status",
        "published_at",
        "created_at",
        "updated_at",
        "url",
        "matched_terms",
        "text",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for post in posts:
            row = {field: post.get(field, "") for field in fields}
            row["matched_terms"] = ", ".join(post.get("matched_terms") or [])
            writer.writerow(row)


def markdown_escape_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().replace("\n", " ")


def write_markdown(path: Path, posts: list[dict[str, Any]], terms: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Typefully Posts Matching Course Terms",
        "",
        f"- Exported: {dt.datetime.now(dt.UTC).isoformat()}",
        f"- Terms: {', '.join(terms)}",
        f"- Matches: {len(posts)}",
        "",
    ]
    for post in posts:
        title = post.get("published_at") or post.get("created_at") or post["id"]
        lines.extend(
            [
                f"## {markdown_escape_heading(str(title))}",
                "",
                f"- ID: `{post['id']}`",
                f"- Platform: {post.get('platform') or '-'}",
                f"- Status: {post.get('status') or '-'}",
                f"- Matched terms: {', '.join(post.get('matched_terms') or [])}",
            ]
        )
        if post.get("url"):
            lines.append(f"- URL: {post['url']}")
        lines.extend(["", post.get("text", "").strip(), ""])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Typefully posts and store posts containing selected terms."
    )
    parser.add_argument(
        "--social-set-id",
        action="append",
        help="Typefully social set ID. Can be repeated. Required for the default endpoint.",
    )
    parser.add_argument(
        "--social-set-name-match",
        help=(
            "Discover social sets with /v2/social-sets and use IDs whose "
            "name/handle/profile text contains this value, for example 'alexey'."
        ),
    )
    parser.add_argument(
        "--endpoint",
        default=DEFAULT_ENDPOINT,
        help=(
            "Typefully posts endpoint or full URL. May include {social_set_id}. "
            f"Defaults to {DEFAULT_ENDPOINT!r}."
        ),
    )
    parser.add_argument("--base-url", default=API_BASE_URL, help="Typefully API base URL.")
    parser.add_argument(
        "--hydrate-details",
        action="store_true",
        help="Fetch each listed item by ID before filtering so matches use full post text.",
    )
    parser.add_argument(
        "--detail-endpoint",
        default=DEFAULT_DETAIL_ENDPOINT,
        help=(
            "Detail endpoint used with --hydrate-details. May include {social_set_id} "
            f"and {{id}}. Defaults to {DEFAULT_DETAIL_ENDPOINT!r}."
        ),
    )
    parser.add_argument(
        "--term",
        action="append",
        default=[],
        help="Case-insensitive term to match. Can be repeated. Defaults to zoomcamp and free course.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Folder where raw and filtered exports will be written.",
    )
    parser.add_argument(
        "--input-json",
        type=Path,
        help="Filter a previously saved raw JSON export instead of calling the API.",
    )
    parser.add_argument(
        "--api-key-env",
        default="TYPEFULLY_API_KEY",
        help="Environment variable containing the Typefully API key.",
    )
    parser.add_argument(
        "--api-key-stdin",
        action="store_true",
        help="Read the Typefully API key from stdin instead of an environment variable.",
    )
    parser.add_argument("--limit-param", default="limit", help="Pagination page-size parameter.")
    parser.add_argument("--limit", type=int, default=100, help="Pagination page size.")
    parser.add_argument(
        "--cursor-param",
        default="cursor",
        help="Pagination cursor parameter when the API returns a next cursor.",
    )
    parser.add_argument("--max-pages", type=int, default=100, help="Maximum API pages to fetch.")
    parser.add_argument(
        "--pause-seconds",
        type=float,
        default=0.2,
        help="Pause between paginated API requests.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    terms = args.term or DEFAULT_TERMS
    output_dir = args.output_dir.resolve()
    stamp = utc_timestamp()

    if args.input_json:
        raw_export = load_json(args.input_json)
        raw_path = args.input_json.resolve()
    else:
        social_set_ids = args.social_set_id or []
        if (
            "{social_set_id}" in args.endpoint
            and not social_set_ids
            and not args.social_set_name_match
        ):
            raise SystemExit("Pass at least one --social-set-id for this endpoint.")
        if not social_set_ids:
            social_set_ids = [None]

        api_key = read_api_key(args)
        social_set_discovery: dict[str, Any] | None = None
        if (
            "{social_set_id}" in args.endpoint
            and social_set_ids == [None]
            and args.social_set_name_match
        ):
            discovered_ids, discovery_pages, matched_sets = discover_social_set_ids(
                base_url=args.base_url,
                api_key=api_key,
                name_match=args.social_set_name_match,
                limit_param=args.limit_param,
                limit=args.limit,
                cursor_param=args.cursor_param,
                max_pages=args.max_pages,
                pause_seconds=args.pause_seconds,
            )
            social_set_ids = discovered_ids
            social_set_discovery = {
                "name_match": args.social_set_name_match,
                "pages": discovery_pages,
                "matched_sets": matched_sets,
            }
            if not social_set_ids:
                raise SystemExit(
                    f"No Typefully social sets matched {args.social_set_name_match!r}."
                )
        exports: list[dict[str, Any]] = []
        for social_set_id in social_set_ids:
            start_url = endpoint_url(args.base_url, args.endpoint, social_set_id)
            pages = fetch_paginated(
                start_url=start_url,
                api_key=api_key,
                limit_param=args.limit_param,
                limit=args.limit,
                cursor_param=args.cursor_param,
                max_pages=args.max_pages,
                pause_seconds=args.pause_seconds,
            )
            export: dict[str, Any] = {
                "social_set_id": social_set_id,
                "endpoint": start_url,
                "pages": pages,
            }
            if args.hydrate_details:
                export["detail_endpoint_template"] = args.detail_endpoint
                export["details"] = hydrate_item_details(
                    items=flatten_items({"pages": pages}),
                    base_url=args.base_url,
                    detail_endpoint=args.detail_endpoint,
                    social_set_id=social_set_id,
                    api_key=api_key,
                    pause_seconds=args.pause_seconds,
                )
            exports.append(export)
        raw_export = {
            "exported_at": dt.datetime.now(dt.UTC).isoformat(),
            "source": "typefully",
            "endpoint_template": args.endpoint,
            "social_set_discovery": social_set_discovery,
            "exports": exports,
        }
        raw_path = output_dir / "raw" / f"typefully-raw-{stamp}.json"
        write_json(raw_path, raw_export)

    items: list[Any] = []
    if isinstance(raw_export, dict) and isinstance(raw_export.get("exports"), list):
        for export in raw_export["exports"]:
            items.extend(flatten_items(export))
    else:
        items.extend(flatten_items(raw_export))

    matches = filter_posts(items, terms)
    compact_matches = [{key: value for key, value in post.items() if key != "raw"} for post in matches]

    json_path = output_dir / "filtered" / f"typefully-matches-{stamp}.json"
    csv_path = output_dir / "filtered" / f"typefully-matches-{stamp}.csv"
    markdown_path = output_dir / "filtered" / f"typefully-matches-{stamp}.md"
    manifest_path = output_dir / "manifest.json"

    write_json(json_path, compact_matches)
    write_csv(csv_path, compact_matches)
    write_markdown(markdown_path, compact_matches, terms)
    write_json(
        manifest_path,
        {
            "updated_at": dt.datetime.now(dt.UTC).isoformat(),
            "source": "typefully",
            "raw_path": display_path(raw_path),
            "filtered_json_path": display_path(json_path),
            "filtered_csv_path": display_path(csv_path),
            "filtered_markdown_path": display_path(markdown_path),
            "terms": terms,
            "downloaded_items": len(items),
            "matches": len(compact_matches),
        },
    )

    print(f"downloaded_items={len(items)}")
    print(f"matches={len(compact_matches)}")
    print(f"raw={raw_path}")
    print(f"json={json_path}")
    print(f"csv={csv_path}")
    print(f"markdown={markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
