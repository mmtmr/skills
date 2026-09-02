#!/usr/bin/env python3
"""Fetch a public GetDesign template into an isolated evidence directory."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


SLUG_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive a public GetDesign DESIGN.md without touching the project root."
    )
    parser.add_argument("slug", help="GetDesign template slug returned by the current catalog")
    parser.add_argument("--output", required=True, type=Path, help="Evidence output directory")
    parser.add_argument(
        "--package",
        default="getdesign@latest",
        help="npm package selector; pin a version for reproducible automation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not SLUG_PATTERN.fullmatch(args.slug):
        print("error: slug may contain only letters, numbers, dot, underscore, and hyphen", file=sys.stderr)
        return 2
    if shutil.which("npx") is None:
        print("error: npx is required (GetDesign requires Node 18+)", file=sys.stderr)
        return 2

    output_dir = args.output.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    design_path = output_dir / "DESIGN.md"
    temporary_path = output_dir / ".DESIGN.md.partial"
    metadata_path = output_dir / "provenance.json"

    if design_path.exists() or metadata_path.exists() or temporary_path.exists():
        print(f"error: refusing to overwrite archived evidence in {output_dir}", file=sys.stderr)
        return 2

    command = ["npx", "--yes", args.package, "add", args.slug, "--out", str(temporary_path)]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        temporary_path.unlink(missing_ok=True)
        print(result.stdout, end="", file=sys.stderr)
        print(result.stderr, end="", file=sys.stderr)
        print(
            "error: template may be absent, request-only, or unavailable; do not fabricate DESIGN.md evidence",
            file=sys.stderr,
        )
        return result.returncode or 1
    if not temporary_path.is_file() or temporary_path.stat().st_size == 0:
        temporary_path.unlink(missing_ok=True)
        print("error: GetDesign returned success but no non-empty DESIGN.md was produced", file=sys.stderr)
        return 1
    temporary_path.replace(design_path)

    version_result = subprocess.run(
        ["npx", "--yes", args.package, "--version"],
        text=True,
        capture_output=True,
        check=False,
    )
    resolved_version = version_result.stdout.strip() if version_result.returncode == 0 else None

    provenance = {
        "brand_slug": args.slug,
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "package": args.package,
        "resolved_version": resolved_version,
        "catalog_url": f"https://getdesign.md/{args.slug}/design-md",
        "preview_url": f"https://getdesign.md/design-md/{args.slug}/preview",
        "command": command,
        "scope_warning": (
            "Independently observed reference; verify whether rules describe marketing or product UI."
        ),
    }
    metadata_path.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(design_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
