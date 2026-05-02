#!/usr/bin/env python3
"""Build processed GRI and SASB sustainability reporting records."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


MASTER_FIELDS = [
    "sigma_id",
    "entry_type",
    "meta_layer",
    "domain",
    "sub_domain",
    "name_full",
    "name_short",
    "standard_id",
    "issuer",
    "issuer_type",
    "governance_layer",
    "geographic_scope",
    "year_published",
    "year_first",
    "status",
    "mandate",
    "sector_applicability",
    "why_it_matters",
    "key_outputs",
    "official_url",
    "data_source",
    "notes",
]

REQUIRED_FIELDS = [
    "sigma_id",
    "entry_type",
    "domain",
    "name_full",
    "standard_id",
    "issuer",
    "status",
    "official_url",
    "data_source",
]


def read_source_rows(source_path: Path, source_family: str | None = None) -> list[dict[str, str]]:
    with source_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing = [field for field in ["source_family", *MASTER_FIELDS] if field not in fieldnames]
        if missing:
            raise ValueError(f"{source_path} missing source fields: {', '.join(missing)}")
        rows = []
        for row in reader:
            if source_family and (row.get("source_family") or "").strip() != source_family:
                continue
            rows.append({field: (row.get(field) or "").strip() for field in MASTER_FIELDS})
        return rows


def validate_rows(rows: list[dict[str, str]], label: str) -> None:
    if not rows:
        raise ValueError(f"{label} source has no rows")

    seen_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    for row in rows:
        for field in REQUIRED_FIELDS:
            if not row.get(field):
                raise ValueError(f"{row.get('sigma_id') or '<missing sigma_id>'} missing required field {field}")
        sigma_id = row["sigma_id"]
        if sigma_id in seen_ids:
            duplicate_ids.add(sigma_id)
        seen_ids.add(sigma_id)
        if not row["official_url"].startswith(("http://", "https://")):
            raise ValueError(f"{sigma_id} official_url must start with http:// or https://")

    if duplicate_ids:
        raise ValueError(f"duplicate sustainability sigma_id values: {', '.join(sorted(duplicate_ids))}")


def write_rows(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["sigma_id"]))


def process_sustainability_reporting(
    repo_root: Path,
    source_path: Path | None = None,
    output_path: Path | None = None,
    source_family: str | None = None,
) -> Path:
    source = source_path or repo_root / "data" / "reference" / "sustainability_reporting_sources.csv"
    output = output_path or repo_root / "data" / "processed" / "sustainability_reporting_standards.csv"

    rows = read_source_rows(source, source_family)
    validate_rows(rows, source_family or "sustainability reporting")
    write_rows(output, rows)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build GRI/SASB sustainability reporting records.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-path", type=Path)
    parser.add_argument("--output-path", type=Path)
    parser.add_argument("--source-family", choices=["GRI", "SASB"])
    args = parser.parse_args()

    try:
        output_path = process_sustainability_reporting(
            args.repo_root,
            source_path=args.source_path,
            output_path=args.output_path,
            source_family=args.source_family,
        )
    except Exception as exc:
        print(f"Sustainability reporting ingestion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote sustainability reporting records to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
