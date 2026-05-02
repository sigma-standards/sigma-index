#!/usr/bin/env python3
"""Sync the public SIGMA Google Sheet into a processed master-schema CSV."""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import parse_qs, urlparse


DEFAULT_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "12B83jPjlKSbk9QX8IQjAJylqwby8puiwabHwHoFBj0Q/edit?gid=0#gid=0"
)
DEFAULT_OUTPUT = Path("data/processed/google_sheet_master.csv")

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


def extract_sheet_reference(sheet_url: str) -> tuple[str, str]:
    match = re.search(r"/spreadsheets/d/([^/]+)", sheet_url)
    if not match:
        raise ValueError("Could not find a Google Sheet ID in the provided URL")

    parsed = urlparse(sheet_url)
    query_gid = parse_qs(parsed.query).get("gid", [""])[0]
    fragment_gid = parse_qs(parsed.fragment).get("gid", [""])[0]
    gid = query_gid or fragment_gid or "0"
    return match.group(1), gid


def build_export_url(sheet_id: str, gid: str = "0") -> str:
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"


def fetch_csv_text(export_url: str, timeout: int = 30) -> str:
    with urllib.request.urlopen(export_url, timeout=timeout) as response:
        return response.read().decode("utf-8-sig")


def normalize_rows(csv_text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(csv_text))
    if reader.fieldnames is None:
        raise ValueError("CSV export has no header row")

    missing = [field for field in MASTER_FIELDS if field not in reader.fieldnames]
    if missing:
        raise ValueError(f"CSV export is missing master schema fields: {', '.join(missing)}")

    rows: list[dict[str, str]] = []
    for row in reader:
        normalized = {field: (row.get(field) or "").strip() for field in MASTER_FIELDS}
        if any(normalized.values()):
            rows.append(normalized)
    return rows


def write_normalized_csv(csv_text: str, output_path: Path) -> int:
    rows = normalize_rows(csv_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def sync_google_sheet(sheet_url: str, output_path: Path, timeout: int = 30) -> int:
    sheet_id, gid = extract_sheet_reference(sheet_url)
    csv_text = fetch_csv_text(build_export_url(sheet_id, gid), timeout=timeout)
    return write_normalized_csv(csv_text, output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync public SIGMA Google Sheet rows into data/processed.")
    parser.add_argument("--sheet-url", default=DEFAULT_SHEET_URL, help="Google Sheet edit/share URL.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Processed CSV output path.")
    parser.add_argument("--timeout", type=int, default=30, help="Network timeout in seconds.")
    args = parser.parse_args()

    try:
        row_count = sync_google_sheet(args.sheet_url, args.output, args.timeout)
    except Exception as exc:
        print(f"Google Sheet sync failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {row_count} row(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
