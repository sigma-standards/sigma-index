#!/usr/bin/env python3
"""Stage filtered WHO IRIS OAI-PMH metadata for curator review."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


OAI_ENDPOINT = "https://iris.who.int/oai/request?verb=ListRecords&metadataPrefix=oai_dc"

STAGING_FIELDS = [
    "source_id",
    "title",
    "year",
    "record_type",
    "official_url",
    "matched_terms",
    "review_status",
]

INCLUDE_TERMS = [
    "guideline",
    "guidelines",
    "standard",
    "standards",
    "classification",
    "model list",
    "manual",
    "framework",
]


def _first_text(element: ET.Element, path: str, namespaces: dict[str, str]) -> str:
    found = element.find(path, namespaces)
    return (found.text or "").strip() if found is not None else ""


def _record_type(title: str) -> str:
    lowered = title.lower()
    if "classification" in lowered:
        return "Classification"
    if "guideline" in lowered:
        return "Guideline"
    if "standard" in lowered:
        return "Standard"
    if "framework" in lowered:
        return "Framework"
    if "manual" in lowered:
        return "Manual"
    return "Candidate"


def _matched_terms(title: str) -> list[str]:
    lowered = title.lower()
    return [term for term in INCLUDE_TERMS if term in lowered]


def parse_oai_records(xml_text: str) -> list[dict[str, str]]:
    namespaces = {
        "oai": "http://www.openarchives.org/OAI/2.0/",
        "dc": "http://purl.org/dc/elements/1.1/",
    }
    root = ET.fromstring(xml_text)
    rows: list[dict[str, str]] = []

    for record in root.findall(".//oai:record", namespaces):
        title = _first_text(record, ".//dc:title", namespaces)
        matches = _matched_terms(title)
        if not matches:
            continue

        source_id = _first_text(record, "./oai:header/oai:identifier", namespaces)
        date = _first_text(record, ".//dc:date", namespaces)
        year_match = re.search(r"\d{4}", date)
        identifier_values = [
            (element.text or "").strip()
            for element in record.findall(".//dc:identifier", namespaces)
            if (element.text or "").strip().startswith(("http://", "https://"))
        ]

        rows.append(
            {
                "source_id": source_id,
                "title": title,
                "year": year_match.group(0) if year_match else "",
                "record_type": _record_type(title),
                "official_url": identifier_values[0] if identifier_values else "",
                "matched_terms": "; ".join(matches),
                "review_status": "needs-curator-review",
            }
        )

    return sorted(rows, key=lambda row: (row["record_type"], row["title"]))


def write_rows(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=STAGING_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fetch_oai_xml(endpoint: str = OAI_ENDPOINT) -> str:
    with urllib.request.urlopen(endpoint, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def harvest_who_iris(
    repo_root: Path,
    input_xml: Path | None = None,
    output_path: Path | None = None,
    endpoint: str = OAI_ENDPOINT,
) -> Path:
    xml_text = input_xml.read_text(encoding="utf-8") if input_xml else fetch_oai_xml(endpoint)
    rows = parse_oai_records(xml_text)
    output = output_path or repo_root / "data" / "staging" / "who_iris_filtered_metadata.csv"
    write_rows(output, rows)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Stage filtered WHO IRIS OAI-PMH metadata.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--input-xml", type=Path)
    parser.add_argument("--output-path", type=Path)
    parser.add_argument("--endpoint", default=OAI_ENDPOINT)
    args = parser.parse_args()

    try:
        output_path = harvest_who_iris(args.repo_root, args.input_xml, args.output_path, args.endpoint)
    except Exception as exc:
        print(f"WHO IRIS harvest failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote WHO IRIS filtered metadata to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
