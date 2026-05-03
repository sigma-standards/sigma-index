import csv
from pathlib import Path
from urllib.parse import urlparse


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


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def is_iso_data_source(data_source):
    _, separator, source_url = data_source.partition(": ")
    parsed = urlparse(source_url if separator else data_source)
    return (
        parsed.scheme == "https"
        and parsed.hostname is not None
        and (parsed.hostname == "www.iso.org" or parsed.hostname.endswith(".iso.org"))
    )


def test_process_national_standards_bodies_writes_master_schema_records(tmp_path):
    from scripts.process_national_standards_bodies import process_national_standards_bodies

    output_path = process_national_standards_bodies(Path("."), output_path=tmp_path / "nsb.csv")

    rows = read_rows(output_path)
    acronyms = {row["name_short"] for row in rows}

    assert output_path.exists()
    assert len(rows) >= 10
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert {row["entry_type"] for row in rows} == {"Standards Body"}
    assert {row["domain"] for row in rows} == {"Governance, Transparency & Anti-Corruption"}
    assert {"ANSI", "BSI", "DIN", "BIS", "JISC"} <= acronyms
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_national_standards_body_ids_are_unique_and_source_linked(tmp_path):
    from scripts.process_national_standards_bodies import process_national_standards_bodies

    output_path = process_national_standards_bodies(Path("."), output_path=tmp_path / "nsb.csv")
    rows = read_rows(output_path)
    sigma_ids = [row["sigma_id"] for row in rows]

    assert len(sigma_ids) == len(set(sigma_ids))
    assert all(row["sigma_id"].startswith("NSB-") for row in rows)
    assert all(is_iso_data_source(row["data_source"]) for row in rows)
