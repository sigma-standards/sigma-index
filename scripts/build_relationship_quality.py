#!/usr/bin/env python3
"""Build relationship graph quality and traceability reports."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
from typing import Iterable


REPORT_FIELDS = ["check_id", "severity", "status", "detail"]
PUBLICATION_READY_CONFIDENCE = {"source-confirmed", "curator-reviewed"}


def read_relationship_rows(relationships_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(relationships_dir.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if "from_id" not in (reader.fieldnames or []):
                continue
            rows.extend(dict(row) for row in reader)
    return rows


def report_row(check_id: str, severity: str, status: str, detail: str) -> dict[str, str]:
    return {
        "check_id": check_id,
        "severity": severity,
        "status": status,
        "detail": detail,
    }


def build_rows(relationships: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    rows = list(relationships)
    total = len(rows)
    confidence_counts = Counter((row.get("confidence") or "").strip() for row in rows)
    missing_source_url = sum(1 for row in rows if not (row.get("source_url") or "").strip())
    missing_confidence = sum(1 for row in rows if not (row.get("confidence") or "").strip())
    llm_suggested = confidence_counts.get("llm-suggested", 0)
    publication_ready = sum(
        1 for row in rows
        if (row.get("confidence") or "").strip() in PUBLICATION_READY_CONFIDENCE
        and (row.get("source_url") or "").strip()
    )

    return [
        report_row("relationship_total_edges", "info", "pass", f"{total} relationship edges"),
        report_row(
            "relationship_publication_ready_edges",
            "critical",
            "pass" if publication_ready == total else "fail",
            f"{publication_ready} of {total} edges are source-confirmed or curator-reviewed",
        ),
        report_row(
            "relationship_missing_source_url",
            "critical",
            "pass" if missing_source_url == 0 else "fail",
            f"{missing_source_url} edges missing source_url",
        ),
        report_row(
            "relationship_missing_confidence",
            "critical",
            "pass" if missing_confidence == 0 else "fail",
            f"{missing_confidence} edges missing confidence",
        ),
        report_row(
            "relationship_llm_suggested_edges",
            "warning",
            "pass" if llm_suggested == 0 else "warn",
            f"{llm_suggested} llm-suggested edges require review before publication",
        ),
    ]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# SIGMA Relationship Quality Report",
        "",
        "| Check | Severity | Status | Detail |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['check_id']} | {row['severity']} | {row['status']} | {row['detail']} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def build_relationship_quality(repo_root: Path = Path(".")) -> Path:
    relationships_dir = repo_root / "data" / "relationships"
    report_path = repo_root / "data" / "reports" / "relationship_quality.csv"
    markdown_path = repo_root / "docs" / "RELATIONSHIP_QUALITY.md"
    relationships = read_relationship_rows(relationships_dir)
    rows = build_rows(relationships)
    write_csv(report_path, rows)
    write_markdown(markdown_path, rows)
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build relationship graph quality reports.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()

    report_path = build_relationship_quality(args.repo_root)
    print(f"Wrote relationship quality report to {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
