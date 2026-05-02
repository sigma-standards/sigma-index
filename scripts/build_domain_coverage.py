#!/usr/bin/env python3
"""Build a domain coverage report for the current processed datasets."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


DOMAIN_REGISTRY = Path("data/reference/domain_taxonomy.csv")
PROCESSED_DIR = Path("data/processed")
OUTPUT = Path("data/reports/domain_coverage.csv")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        return list(csv.DictReader(csv_file))


def load_processed_counts() -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in sorted(PROCESSED_DIR.glob("*.csv")):
        with path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            if "sigma_id" not in (reader.fieldnames or []):
                continue
            for row in reader:
                domain = row.get("domain", "").strip()
                if domain:
                    counts[domain] += 1
    return counts


def main() -> int:
    domains = read_rows(DOMAIN_REGISTRY)
    counts = load_processed_counts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["domain_id", "domain_name", "meta_layer", "entry_count", "coverage_status"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for domain in domains:
            count = counts.get(domain["domain_name"], 0)
            writer.writerow(
                {
                    "domain_id": domain["domain_id"],
                    "domain_name": domain["domain_name"],
                    "meta_layer": domain["meta_layer"],
                    "entry_count": count,
                    "coverage_status": "seeded" if count else "missing",
                }
            )

    print(f"Wrote domain coverage report to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
