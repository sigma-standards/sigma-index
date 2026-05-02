#!/usr/bin/env python3
"""Stage UN Treaty Collection and OHCHR treaty candidates for curator review."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


STAGING_FIELDS = [
    "source_id",
    "title",
    "chapter",
    "depositary",
    "adoption_date",
    "entry_into_force",
    "record_type",
    "official_url",
    "parties_url",
    "review_status",
    "notes",
]

REQUIRED_FIELDS = [
    "source_id",
    "title",
    "chapter",
    "depositary",
    "record_type",
    "official_url",
    "review_status",
]


def read_source_rows(source_path: Path) -> list[dict[str, str]]:
    with source_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing = [field for field in STAGING_FIELDS if field not in fieldnames]
        if missing:
            raise ValueError(f"{source_path} missing staging fields: {', '.join(missing)}")
        return [{field: (row.get(field) or "").strip() for field in STAGING_FIELDS} for row in reader]


def validate_rows(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("UN treaty source has no rows")

    seen_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    for row in rows:
        for field in REQUIRED_FIELDS:
            if not row.get(field):
                raise ValueError(f"{row.get('source_id') or '<missing source_id>'} missing required field {field}")
        source_id = row["source_id"]
        if source_id in seen_ids:
            duplicate_ids.add(source_id)
        seen_ids.add(source_id)
        if not row["official_url"].startswith("https://treaties.un.org/"):
            raise ValueError(f"{source_id} official_url must start with https://treaties.un.org/")
        if row["parties_url"] and not row["parties_url"].startswith("https://"):
            raise ValueError(f"{source_id} parties_url must start with https://")

    if duplicate_ids:
        raise ValueError(f"duplicate UN treaty source_id values: {', '.join(sorted(duplicate_ids))}")


def write_rows(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=STAGING_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["source_id"]))


def stage_un_treaties(
    repo_root: Path,
    source_path: Path | None = None,
    output_path: Path | None = None,
) -> Path:
    source = source_path or repo_root / "data" / "reference" / "un_treaty_priority_sources.csv"
    output = output_path or repo_root / "data" / "staging" / "un_treaty_candidates.csv"

    rows = read_source_rows(source)
    validate_rows(rows)
    write_rows(output, rows)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Stage UN treaty candidates for curator review.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-path", type=Path)
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()

    try:
        output_path = stage_un_treaties(args.repo_root, args.source_path, args.output_path)
    except Exception as exc:
        print(f"UN treaty staging failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote UN treaty candidates to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
