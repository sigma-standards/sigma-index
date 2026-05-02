#!/usr/bin/env python3
"""Validate that SIGMA has a complete 40-domain registry."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


DOMAIN_REGISTRY = Path("data/reference/domain_taxonomy.csv")
SOURCE_REGISTRY = Path("data/reference/source_registry.csv")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        return list(csv.DictReader(csv_file))


def main() -> int:
    errors: list[str] = []

    domains = read_rows(DOMAIN_REGISTRY)
    sources = read_rows(SOURCE_REGISTRY)

    domain_ids = [row["domain_id"] for row in domains]
    source_ids = [row["domain_id"] for row in sources]

    if len(domains) != 40:
        errors.append(f"expected 40 domains, found {len(domains)}")
    if len(set(domain_ids)) != 40:
        errors.append("domain_id values must be unique across domain taxonomy")
    if set(domain_ids) != {str(number) for number in range(1, 41)}:
        errors.append("domain taxonomy must contain domain_id values 1 through 40")
    if set(source_ids) != set(domain_ids):
        errors.append("source registry must have exactly one row per domain")

    missing_names = [row["domain_id"] for row in domains if not row.get("domain_name")]
    if missing_names:
        errors.append(f"domain rows missing names: {', '.join(missing_names)}")

    if errors:
        print("Domain registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Domain registry ok: 40 domains and 40 source-map rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
