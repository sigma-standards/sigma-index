#!/usr/bin/env python3
"""Build deterministic release quality-gate reports."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


PROCESSED_DIR = Path("data/processed")
REPORT_OUTPUT = Path("data/reports/quality_gate.csv")
DOC_OUTPUT = Path("docs/QUALITY_GATE.md")

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

REPORT_FIELDS = ["check_id", "severity", "status", "detail"]


def read_processed_rows(processed_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(processed_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if "sigma_id" not in (reader.fieldnames or []):
                continue
            rows.extend({field: (row.get(field) or "").strip() for field in MASTER_FIELDS} for row in reader)
    return rows


def build_checks(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    sigma_ids = [row["sigma_id"] for row in rows if row.get("sigma_id")]
    duplicate_ids = sorted(sigma_id for sigma_id, count in Counter(sigma_ids).items() if count > 1)
    missing_required = [
        (row.get("sigma_id") or "<missing sigma_id>", field)
        for row in rows
        for field in REQUIRED_FIELDS
        if not row.get(field)
    ]
    bad_urls = [
        row.get("sigma_id") or "<missing sigma_id>"
        for row in rows
        if row.get("official_url") and not row["official_url"].startswith(("http://", "https://"))
    ]

    return [
        {
            "check_id": "processed_duplicate_sigma_ids",
            "severity": "critical",
            "status": "fail" if duplicate_ids else "pass",
            "detail": _count_detail(duplicate_ids, "duplicate sigma_id values"),
        },
        {
            "check_id": "processed_required_fields",
            "severity": "critical",
            "status": "fail" if missing_required else "pass",
            "detail": f"{len(missing_required)} missing required field values",
        },
        {
            "check_id": "processed_url_shape",
            "severity": "critical",
            "status": "fail" if bad_urls else "pass",
            "detail": f"{len(bad_urls)} non-http official_url values",
        },
    ]


def _count_detail(values: list[str], label: str) -> str:
    if not values:
        return f"0 {label}"
    preview = ", ".join(values[:10])
    suffix = "..." if len(values) > 10 else ""
    return f"{len(values)} {label}: {preview}{suffix}"


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# SIGMA Quality Gate",
        "",
        "This file is generated from `scripts/build_quality_gate.py`.",
        "It summarizes deterministic release checks that do not require live network access.",
        "",
        "| Check | Severity | Status | Detail |",
        "|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['check_id']} | {row['severity']} | {row['status']} | {row['detail']} |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def build_quality_gate(root: Path | str = Path(".")) -> Path:
    root = Path(root)
    rows = read_processed_rows(root / PROCESSED_DIR)
    checks = build_checks(rows)
    report_path = root / REPORT_OUTPUT
    write_csv(report_path, checks)
    write_markdown(root / DOC_OUTPUT, checks)
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic SIGMA quality-gate reports.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()

    report_path = build_quality_gate(args.repo_root)
    print(f"Wrote quality gate report to {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
