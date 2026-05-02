#!/usr/bin/env python3
"""Build processed Phase 8A national standards body records."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


SOURCE_FIELDS = [
    "nsb_id",
    "country",
    "region",
    "acronym",
    "name_full",
    "membership_type",
    "issuer_type",
    "year_first",
    "official_url",
    "iso_member_url",
    "notes",
]

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

REQUIRED_SOURCE_FIELDS = [
    "nsb_id",
    "country",
    "acronym",
    "name_full",
    "membership_type",
    "issuer_type",
    "official_url",
    "iso_member_url",
]


def read_source_rows(source_path: Path) -> list[dict[str, str]]:
    with source_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing = [field for field in SOURCE_FIELDS if field not in fieldnames]
        if missing:
            raise ValueError(f"{source_path} missing source fields: {', '.join(missing)}")
        return [{field: (row.get(field) or "").strip() for field in SOURCE_FIELDS} for row in reader]


def validate_source_rows(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("national standards body source has no rows")

    seen_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    for row in rows:
        for field in REQUIRED_SOURCE_FIELDS:
            if not row.get(field):
                raise ValueError(f"{row.get('nsb_id') or '<missing nsb_id>'} missing required field {field}")

        nsb_id = row["nsb_id"]
        if nsb_id in seen_ids:
            duplicate_ids.add(nsb_id)
        seen_ids.add(nsb_id)

        for field in ["official_url", "iso_member_url"]:
            if not row[field].startswith(("http://", "https://")):
                raise ValueError(f"{nsb_id} {field} must start with http:// or https://")

    if duplicate_ids:
        raise ValueError(f"duplicate national standards body IDs: {', '.join(sorted(duplicate_ids))}")


def to_master_row(row: dict[str, str]) -> dict[str, str]:
    country = row["country"]
    acronym = row["acronym"]
    membership = row["membership_type"]
    return {
        "sigma_id": row["nsb_id"],
        "entry_type": "Standards Body",
        "meta_layer": "Society, Governance & Law",
        "domain": "Governance, Transparency & Anti-Corruption",
        "sub_domain": "National standards infrastructure",
        "name_full": row["name_full"],
        "name_short": acronym,
        "standard_id": f"{country} national standards body",
        "issuer": row["name_full"],
        "issuer_type": row["issuer_type"],
        "governance_layer": "National",
        "geographic_scope": country,
        "year_published": row["year_first"],
        "year_first": row["year_first"],
        "status": "Active",
        "mandate": "Voluntary",
        "sector_applicability": "National standardization system and ISO participation",
        "why_it_matters": f"{acronym} is the {membership.lower()} representing {country} in the ISO standards ecosystem.",
        "key_outputs": "National standards body registry record",
        "official_url": row["official_url"],
        "data_source": f"ISO member profile: {row['iso_member_url']}",
        "notes": row["notes"],
    }


def write_rows(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["sigma_id"]))


def process_national_standards_bodies(
    repo_root: Path,
    source_path: Path | None = None,
    output_path: Path | None = None,
) -> Path:
    source = source_path or repo_root / "data" / "reference" / "national_standards_bodies_sources.csv"
    output = output_path or repo_root / "data" / "processed" / "national_standards_bodies.csv"

    source_rows = read_source_rows(source)
    validate_source_rows(source_rows)
    write_rows(output, [to_master_row(row) for row in source_rows])
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Phase 8A national standards body records.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-path", type=Path)
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()

    try:
        output_path = process_national_standards_bodies(args.repo_root, args.source_path, args.output_path)
    except Exception as exc:
        print(f"national standards body ingestion failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote national standards body records to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
