#!/usr/bin/env python3
"""
Build SIGMA release artifacts from processed datasets.

Outputs are intentionally generated with the Python standard library so the
basic release build does not require pandas or a local database.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
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


def read_master_rows(processed_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(processed_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = reader.fieldnames or []
            if "sigma_id" not in fieldnames:
                continue
            for row in reader:
                rows.append({field: row.get(field, "") for field in MASTER_FIELDS})
    return rows


def read_relationship_rows(relationships_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(relationships_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            if "from_id" not in (reader.fieldnames or []):
                continue
            rows.extend(dict(row) for row in reader)
    return rows


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8") as json_file:
        json.dump(payload, json_file, ensure_ascii=False, indent=2)
        json_file.write("\n")


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as jsonl_file:
        for row in rows:
            jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_api_index(path: Path, rows: list[dict[str, str]], relationships: list[dict[str, str]]) -> None:
    domains = sorted({row["domain"] for row in rows if row.get("domain")})
    issuers = sorted({row["issuer"] for row in rows if row.get("issuer")})
    statuses = sorted({row["status"] for row in rows if row.get("status")})
    payload = {
        "dataset": "SIGMA Unified Global Standards Index",
        "entry_count": len(rows),
        "relationship_count": len(relationships),
        "formats": {
            "csv": "sigma_master.csv",
            "json": "sigma_master.json",
            "jsonl": "sigma_master.jsonl",
            "relationships_csv": "relationships.csv",
            "relationships_json": "relationships.json",
            "domain_taxonomy_csv": "domain_taxonomy.csv",
            "source_registry_csv": "source_registry.csv",
            "domain_coverage_csv": "domain_coverage.csv",
            "research_tasks_csv": "research_tasks.csv",
            "research_task_coverage_csv": "research_task_coverage.csv",
            "quality_gate_csv": "quality_gate.csv",
        },
        "facets": {
            "domains": domains,
            "issuers": issuers,
            "statuses": statuses,
        },
    }
    write_json(path, payload)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build SIGMA release artifacts.")
    parser.add_argument("--processed-dir", type=Path, default=Path("data/processed"))
    parser.add_argument("--relationships-dir", type=Path, default=Path("data/relationships"))
    parser.add_argument("--reference-dir", type=Path, default=Path("data/reference"))
    parser.add_argument("--reports-dir", type=Path, default=Path("data/reports"))
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    args = parser.parse_args()

    if not args.processed_dir.exists():
        print(f"Missing processed data directory: {args.processed_dir}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = read_master_rows(args.processed_dir)
    relationships = read_relationship_rows(args.relationships_dir)

    write_csv(args.output_dir / "sigma_master.csv", rows, MASTER_FIELDS)
    write_json(args.output_dir / "sigma_master.json", rows)
    write_jsonl(args.output_dir / "sigma_master.jsonl", rows)

    relationship_fields = ["from_id", "to_id", "relationship_type", "confidence", "source_url", "notes"]
    write_csv(args.output_dir / "relationships.csv", relationships, relationship_fields)
    write_json(args.output_dir / "relationships.json", relationships)

    for file_name in ["domain_taxonomy.csv", "source_registry.csv", "research_tasks.csv"]:
        source = args.reference_dir / file_name
        if source.exists():
            shutil.copyfile(source, args.output_dir / file_name)
    for file_name in ["domain_coverage.csv", "research_task_coverage.csv", "quality_gate.csv"]:
        source = args.reports_dir / file_name
        if source.exists():
            shutil.copyfile(source, args.output_dir / file_name)

    write_api_index(args.output_dir / "api_index.json", rows, relationships)

    print(f"Built {len(rows)} entries and {len(relationships)} relationships in {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
