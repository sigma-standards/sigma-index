#!/usr/bin/env python3
"""Fail when processed SIGMA datasets contain duplicate sigma_id values."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def collect_sigma_ids(processed_dir: Path) -> dict[str, list[str]]:
    locations: dict[str, list[str]] = defaultdict(list)
    for path in sorted(processed_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if "sigma_id" not in (reader.fieldnames or []):
                continue
            for line_number, row in enumerate(reader, start=2):
                sigma_id = (row.get("sigma_id") or "").strip()
                if sigma_id:
                    locations[sigma_id].append(f"{path}:{line_number}")
    return locations


def main() -> int:
    parser = argparse.ArgumentParser(description="Check processed SIGMA datasets for duplicate sigma_id values.")
    parser.add_argument("--processed-dir", type=Path, default=Path("data/processed"))
    args = parser.parse_args()

    locations = collect_sigma_ids(args.processed_dir)
    duplicates = {sigma_id: refs for sigma_id, refs in locations.items() if len(refs) > 1}
    if duplicates:
        print(f"Found {len(duplicates)} duplicate sigma_id value(s):", file=sys.stderr)
        for sigma_id, refs in sorted(duplicates.items()):
            print(f"- {sigma_id}: {', '.join(refs)}", file=sys.stderr)
        return 1

    print(f"Duplicate sigma_id check passed for {len(locations)} processed record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
