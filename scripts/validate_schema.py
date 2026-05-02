#!/usr/bin/env python3
"""
Validate SIGMA processed CSV files against the master schema.

The default mode fails only on structural errors. Use --strict to treat
warnings, such as duplicate IDs or non-standard enum values, as failures.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass, field
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

ENUMS = {
    "entry_type": {
        "Standards Body",
        "Standard",
        "Framework",
        "Treaty",
        "Guideline",
        "Regulation",
        "Classification",
        "Code of Practice",
        "Recommendation",
    },
    "issuer_type": {
        "UN Agency",
        "Treaty Body",
        "ISO",
        "IEC",
        "ITU",
        "Industry SDO",
        "Professional Body",
        "NGO",
        "Intergovernmental",
        "National Government",
    },
    "governance_layer": {"International", "Regional", "National"},
    "status": {"Active", "Withdrawn", "Superseded", "Under Development", "Under Review"},
    "mandate": {
        "Mandatory",
        "Voluntary",
        "Voluntary-with-regulatory-adoption",
        "Treaty-binding",
    },
}


@dataclass
class ValidationReport:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _is_non_empty(value: str | None) -> bool:
    return value is not None and str(value).strip() != ""


def validate_file(path: Path) -> ValidationReport:
    report = ValidationReport(path=path)

    try:
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
    except Exception as exc:
        report.errors.append(f"could not read CSV: {exc}")
        return report

    columns = reader.fieldnames or []
    missing = [field for field in MASTER_FIELDS if field not in columns]
    if missing:
        report.errors.append(f"missing master schema fields: {', '.join(missing)}")
        return report

    extra = [field for field in columns if field not in MASTER_FIELDS]
    if extra:
        report.warnings.append(f"extra fields not in master schema: {', '.join(extra)}")

    for field_name in REQUIRED_FIELDS:
        empty_count = sum(1 for row in rows if not _is_non_empty(row.get(field_name)))
        if empty_count:
            report.errors.append(f"{field_name} has {empty_count} empty value(s)")

    seen_ids: set[str] = set()
    duplicate_ids = 0
    for row in rows:
        sigma_id = row.get("sigma_id", "").strip()
        if not sigma_id:
            continue
        if sigma_id in seen_ids:
            duplicate_ids += 1
        seen_ids.add(sigma_id)
    if duplicate_ids:
        report.warnings.append(f"sigma_id has {duplicate_ids} duplicate value(s)")

    for field_name, allowed_values in ENUMS.items():
        values = {row.get(field_name, "").strip() for row in rows if _is_non_empty(row.get(field_name))}
        invalid_values = sorted(values - allowed_values)
        if invalid_values:
            preview = ", ".join(invalid_values[:10])
            suffix = "..." if len(invalid_values) > 10 else ""
            report.warnings.append(f"{field_name} has non-standard values: {preview}{suffix}")

    for field_name in ["year_published", "year_first"]:
        invalid_years = []
        for row in rows:
            value = row.get(field_name, "").strip()
            if value and not re.fullmatch(r"\d{4}", value):
                invalid_years.append(value)
        if invalid_years:
            report.warnings.append(f"{field_name} has {len(invalid_years)} non-YYYY value(s)")

    invalid_urls = [
        row.get("official_url", "").strip()
        for row in rows
        if _is_non_empty(row.get("official_url"))
        and not row.get("official_url", "").strip().startswith(("http://", "https://"))
    ]
    if invalid_urls:
        report.errors.append(f"official_url has {len(invalid_urls)} non-http(s) value(s)")

    return report


def is_master_entry_file(path: Path) -> bool:
    try:
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, [])
    except Exception:
        return True
    return "sigma_id" in header


def discover_csv_files(paths: list[Path]) -> list[Path]:
    csv_files: list[Path] = []
    for path in paths:
        if path.is_dir():
            csv_files.extend(sorted(file for file in path.glob("*.csv") if is_master_entry_file(file)))
        elif path.suffix.lower() == ".csv":
            if is_master_entry_file(path):
                csv_files.append(path)
    return csv_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SIGMA processed CSV schema.")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("data/processed")],
        help="CSV files or directories to validate. Defaults to data/processed.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as failures.",
    )
    args = parser.parse_args()

    csv_files = discover_csv_files(args.paths)
    if not csv_files:
        print("No CSV files found to validate.")
        return 1

    reports = [validate_file(path) for path in csv_files]
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
        if report.ok and not report.warnings:
            print("  ok")

    if has_errors or (args.strict and has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
