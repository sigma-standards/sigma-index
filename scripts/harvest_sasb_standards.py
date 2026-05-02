#!/usr/bin/env python3
"""Compatibility entrypoint for SASB sustainability reporting records."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from scripts.process_sustainability_reporting import process_sustainability_reporting
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from process_sustainability_reporting import process_sustainability_reporting


def main() -> int:
    parser = argparse.ArgumentParser(description="Build curated SASB sustainability reporting records.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-path", type=Path)
    parser.add_argument("--output-path", type=Path, default=Path("data/processed/sasb_standards.csv"))
    args = parser.parse_args()

    try:
        output_path = process_sustainability_reporting(
            args.repo_root,
            source_path=args.source_path,
            output_path=args.output_path,
            source_family="SASB",
        )
    except Exception as exc:
        print(f"SASB sustainability reporting ingestion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote SASB sustainability reporting records to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
