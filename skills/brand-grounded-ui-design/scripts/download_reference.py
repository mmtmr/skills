#!/usr/bin/env python3
"""Download and validate one UI reference image with provenance metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


MAGIC_TYPES = (
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"RIFF", "image/webp"),
)
MAX_IMAGE_BYTES = 25 * 1024 * 1024


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Archive one UI screenshot and its provenance.")
    parser.add_argument("--image-url", required=True)
    parser.add_argument("--source-url", required=True, help="Canonical page URL, not the CDN URL")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--screen-id")
    parser.add_argument("--app-name")
    return parser.parse_args()


def detected_type(data: bytes) -> str | None:
    for signature, media_type in MAGIC_TYPES:
        if data.startswith(signature):
            if media_type == "image/webp" and data[8:12] != b"WEBP":
                continue
            return media_type
    return None


def main() -> int:
    args = parse_args()
    output = args.output.expanduser().resolve()
    metadata = output.with_suffix(output.suffix + ".json")
    if output.exists() or metadata.exists():
        print(f"error: refusing to overwrite archived reference {output}", file=sys.stderr)
        return 2

    request = urllib.request.Request(
        args.image_url,
        headers={"User-Agent": "brand-grounded-ui-design/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(MAX_IMAGE_BYTES + 1)
            response_type = response.headers.get_content_type()
            final_url = response.geturl()
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"error: download failed: {error}", file=sys.stderr)
        return 1

    if len(data) > MAX_IMAGE_BYTES:
        print("error: image exceeds the 25 MiB archive limit", file=sys.stderr)
        return 1

    media_type = detected_type(data)
    if media_type is None:
        print("error: response is not a recognized JPEG, PNG, or WebP image", file=sys.stderr)
        return 1
    if response_type.startswith("image/") and response_type != media_type:
        print(
            f"warning: response declared {response_type}, detected {media_type}",
            file=sys.stderr,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)
    record = {
        "source_url": args.source_url,
        "image_url": args.image_url,
        "resolved_image_url": final_url,
        "screen_id": args.screen_id,
        "app_name": args.app_name,
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "media_type": media_type,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    metadata.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
