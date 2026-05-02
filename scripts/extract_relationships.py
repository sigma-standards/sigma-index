#!/usr/bin/env python3
"""
Extract high-confidence relationship edges from processed SIGMA datasets.

Current extractors:
- ILO supersession links where a superseded instrument and a later active
  instrument share the same normalized title.
- ISO references discovered in source notes/scope text and resolved to known
  ISO SIGMA IDs.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


RELATIONSHIP_FIELDS = [
    "from_id",
    "to_id",
    "relationship_type",
    "confidence",
    "source_url",
    "notes",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        return list(csv.DictReader(csv_file))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=RELATIONSHIP_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize_title(title: str) -> str:
    value = title.lower()
    value = re.sub(r"\([^)]*revised[^)]*\)", "", value)
    value = re.sub(r",\s*\d{4}\b", "", value)
    value = re.sub(r"\b\d{4}\b", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def parse_year(row: dict[str, str]) -> int:
    value = row.get("year_published", "").strip()
    return int(value) if value.isdigit() else 0


def edge_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (
        row.get("from_id", "").strip(),
        row.get("to_id", "").strip(),
        row.get("relationship_type", "").strip(),
    )


def extract_ilo_supersedes(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_title: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen_sigma_ids: set[str] = set()

    for row in rows:
        sigma_id = row.get("sigma_id", "").strip()
        if not sigma_id or sigma_id in seen_sigma_ids:
            continue
        seen_sigma_ids.add(sigma_id)

        if row.get("issuer", "").strip() != "ILO":
            continue

        key = normalize_title(row.get("name_full", ""))
        if key:
            by_title[key].append(row)

    relationships: list[dict[str, str]] = []
    seen_edges: set[tuple[str, str, str]] = set()

    for grouped_rows in by_title.values():
        superseded = [row for row in grouped_rows if row.get("status", "").strip() == "Superseded"]
        active = [row for row in grouped_rows if row.get("status", "").strip() == "Active"]

        for old_row in superseded:
            old_year = parse_year(old_row)
            candidates = [
                row for row in active
                if parse_year(row) > old_year and row.get("standard_id", "") != old_row.get("standard_id", "")
            ]
            if not candidates:
                continue

            new_row = sorted(candidates, key=parse_year)[0]
            edge = (new_row["sigma_id"], old_row["sigma_id"], "supersedes")
            if edge in seen_edges:
                continue
            seen_edges.add(edge)

            relationships.append(
                {
                    "from_id": new_row["sigma_id"],
                    "to_id": old_row["sigma_id"],
                    "relationship_type": "supersedes",
                    "confidence": "curator-reviewed",
                    "source_url": new_row.get("official_url", ""),
                    "notes": (
                        f"Extracted from ILO records: {new_row.get('standard_id')} is a later active "
                        f"instrument with the same normalized title as superseded {old_row.get('standard_id')}."
                    ),
                }
            )

    return relationships


ISO_REF_PATTERN = re.compile(
    r"\b(ISO(?:/IEC)?)"
    r"(?:/[A-Z]+)?"
    r"(?:\s+(?:AWI|CD|DIS|FDIS|NP|PAS|PRF|TR|TS|WD)){0,3}"
    r"\s+(\d{1,6}(?:-\d+)?)"
    r"(?::\d{4})?",
    re.IGNORECASE,
)


def normalize_iso_ref(body: str, number: str) -> str:
    body = body.upper().replace(" ", "")
    number = number.upper().strip()
    return f"{body} {number}"


def iso_ref_keys(text: str) -> set[str]:
    return {
        normalize_iso_ref(match.group(1), match.group(2))
        for match in ISO_REF_PATTERN.finditer(text or "")
    }


def build_iso_index(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("issuer_type", "").strip() != "ISO":
            continue
        for key in iso_ref_keys(row.get("standard_id", "")):
            grouped[key].append(row)

    index: dict[str, dict[str, str]] = {}
    for key, candidates in grouped.items():
        candidates.sort(
            key=lambda row: (
                row.get("status") == "Active",
                parse_year(row),
                row.get("sigma_id", ""),
            ),
            reverse=True,
        )
        index[key] = candidates[0]
    return index


def extract_iso_references(rows: list[dict[str, str]], max_refs_per_entry: int = 25) -> list[dict[str, str]]:
    index = build_iso_index(rows)
    relationships: list[dict[str, str]] = []
    seen_edges: set[tuple[str, str, str]] = set()

    for row in rows:
        if row.get("issuer_type", "").strip() != "ISO":
            continue

        from_id = row.get("sigma_id", "").strip()
        if not from_id:
            continue

        source_text = " ".join(
            [
                row.get("name_full", ""),
                row.get("key_outputs", ""),
                row.get("notes", ""),
            ]
        )
        keys = sorted(iso_ref_keys(source_text) - iso_ref_keys(row.get("standard_id", "")))

        for key in keys[:max_refs_per_entry]:
            target = index.get(key)
            if not target:
                continue
            to_id = target.get("sigma_id", "").strip()
            if not to_id or to_id == from_id:
                continue

            relationship = {
                "from_id": from_id,
                "to_id": to_id,
                "relationship_type": "references",
                "confidence": "source-confirmed",
                "source_url": row.get("official_url", ""),
                "notes": f"Extracted from ISO source metadata text referencing {key}.",
            }
            key_tuple = edge_key(relationship)
            if key_tuple in seen_edges:
                continue
            seen_edges.add(key_tuple)
            relationships.append(relationship)

    return relationships


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract SIGMA relationship edges.")
    parser.add_argument(
        "--ilo",
        type=Path,
        default=Path("data/processed/ilo_standards.csv"),
        help="Processed ILO standards CSV.",
    )
    parser.add_argument(
        "--iso",
        type=Path,
        default=Path("data/processed/iso_all.csv"),
        help="Processed ISO standards CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/relationships/relationships_extracted.csv"),
        help="Output relationship CSV.",
    )
    args = parser.parse_args()

    for path in [args.ilo, args.iso]:
        if not path.exists():
            print(f"Missing input file: {path}", file=sys.stderr)
            return 1

    ilo_rows = read_rows(args.ilo)
    iso_rows = read_rows(args.iso)
    relationships = extract_ilo_supersedes(ilo_rows)
    relationships.extend(extract_iso_references(iso_rows))

    deduped_relationships: list[dict[str, str]] = []
    seen_edges: set[tuple[str, str, str]] = set()
    for relationship in relationships:
        key = edge_key(relationship)
        if key in seen_edges:
            continue
        seen_edges.add(key)
        deduped_relationships.append(relationship)

    deduped_relationships.sort(key=lambda row: (row["relationship_type"], row["from_id"], row["to_id"]))
    write_rows(args.output, deduped_relationships)

    print(f"Wrote {len(deduped_relationships)} relationship(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
