#!/usr/bin/env python3
"""
Validate SIGMA relationship map CSV files.

Relationship files are allowed to be header-only templates. Once rows are
added, this script checks graph edge fields, provenance, and known SIGMA IDs.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass, field
from pathlib import Path


RELATIONSHIP_FIELDS = [
    "from_id",
    "to_id",
    "relationship_type",
    "confidence",
    "source_url",
    "notes",
]

REQUIRED_FIELDS = [
    "from_id",
    "to_id",
    "relationship_type",
    "confidence",
    "source_url",
]

RELATIONSHIP_TYPES = {
    "references",
    "supersedes",
    "adopted_by",
    "implements",
    "aligned_with",
    "referenced_by",
    "harmonised_with",
    "national_adoption_of",
    "inspires",
}

CONFIDENCE_VALUES = {
    "source-confirmed",
    "curator-reviewed",
    "llm-suggested",
}


@dataclass
class RelationshipReport:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        return reader.fieldnames or [], list(reader)


def is_non_empty(value: str | None) -> bool:
    return value is not None and value.strip() != ""


def load_sigma_ids(processed_dir: Path) -> set[str]:
    sigma_ids: set[str] = set()
    if not processed_dir.exists():
        return sigma_ids

    for path in sorted(processed_dir.glob("*.csv")):
        try:
            header, rows = read_csv(path)
        except Exception:
            continue
        if "sigma_id" not in header:
            continue
        for row in rows:
            value = row.get("sigma_id", "").strip()
            if value:
                sigma_ids.add(value)
    return sigma_ids


def validate_file(path: Path, sigma_ids: set[str]) -> RelationshipReport:
    report = RelationshipReport(path=path)

    try:
        header, rows = read_csv(path)
    except Exception as exc:
        report.errors.append(f"could not read CSV: {exc}")
        return report

    missing = [field for field in RELATIONSHIP_FIELDS if field not in header]
    if missing:
        report.errors.append(f"missing relationship fields: {', '.join(missing)}")
        return report

    extra = [field for field in header if field not in RELATIONSHIP_FIELDS]
    if extra:
        report.warnings.append(f"extra fields not in relationship schema: {', '.join(extra)}")

    if not rows:
        return report

    seen_edges: set[tuple[str, str, str]] = set()
    duplicate_edges = 0
    unknown_ids: set[str] = set()

    for line_number, row in enumerate(rows, start=2):
        for field_name in REQUIRED_FIELDS:
            if not is_non_empty(row.get(field_name)):
                report.errors.append(f"line {line_number}: {field_name} is required")

        from_id = row.get("from_id", "").strip()
        to_id = row.get("to_id", "").strip()
        relationship_type = row.get("relationship_type", "").strip()
        confidence = row.get("confidence", "").strip()
        source_url = row.get("source_url", "").strip()

        if from_id and to_id and from_id == to_id:
            report.errors.append(f"line {line_number}: from_id and to_id must be different")

        if relationship_type and relationship_type not in RELATIONSHIP_TYPES:
            report.errors.append(f"line {line_number}: invalid relationship_type '{relationship_type}'")

        if confidence and confidence not in CONFIDENCE_VALUES:
            report.errors.append(f"line {line_number}: invalid confidence '{confidence}'")

        if source_url and not source_url.startswith(("http://", "https://")):
            report.errors.append(f"line {line_number}: source_url must start with http:// or https://")

        edge = (from_id, to_id, relationship_type)
        if all(edge):
            if edge in seen_edges:
                duplicate_edges += 1
            seen_edges.add(edge)

        if sigma_ids:
            for value in [from_id, to_id]:
                if value and value not in sigma_ids:
                    unknown_ids.add(value)

    if duplicate_edges:
        report.warnings.append(f"found {duplicate_edges} duplicate edge(s)")

    if unknown_ids:
        preview = ", ".join(sorted(unknown_ids)[:10])
        suffix = "..." if len(unknown_ids) > 10 else ""
        report.warnings.append(f"IDs not found in processed master entries: {preview}{suffix}")

    return report


def discover_relationship_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.glob("*.csv")))
        elif path.suffix.lower() == ".csv":
            files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SIGMA relationship CSV files.")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("data/relationships")],
        help="Relationship CSV files or directories. Defaults to data/relationships.",
    )
    parser.add_argument(
        "--processed-dir",
        type=Path,
        default=Path("data/processed"),
        help="Directory containing processed master-entry CSV files.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as failures.",
    )
    args = parser.parse_args()

    files = discover_relationship_files(args.paths)
    if not files:
        print("No relationship CSV files found.")
        return 1

    sigma_ids = load_sigma_ids(args.processed_dir)
    reports = [validate_file(path, sigma_ids) for path in files]
    has_errors = False
    has_warnings = False

    for report in reports:
        print(f"\n{report.path}")
        if report.errors:
            has_errors = True
            print("  errors:")
            for error in report.errors:
                print(f"  - {error}")
        if report.warnings:
            has_warnings = True
            print("  warnings:")
            for warning in report.warnings:
                print(f"  - {warning}")
        if not report.errors and not report.warnings:
            print("  ok")

    if has_errors or (args.strict and has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
