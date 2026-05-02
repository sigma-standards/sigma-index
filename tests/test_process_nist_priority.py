import csv
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


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_process_nist_priority_writes_cybersecurity_and_ai_rows(tmp_path):
    from scripts.process_nist_priority import process_nist_priority

    output_path = process_nist_priority(
        Path("."),
        source_path=Path("data/reference/nist_priority_sources.csv"),
        output_path=tmp_path / "nist_priority_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "CY-NIST-SP800-53R5" in sigma_ids
    assert "AI-NIST-AI-RMF-1-2023" in sigma_ids
    assert {row["issuer"] for row in rows} == {"National Institute of Standards and Technology"}
    assert {"Cybersecurity & Data Privacy", "Artificial Intelligence & Emerging Technologies"} <= {
        row["domain"] for row in rows
    }


def test_process_nist_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_nist_priority import process_nist_priority

    source_path = tmp_path / "nist_priority_sources.csv"
    original = Path("data/reference/nist_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_nist_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate NIST priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate NIST priority rows should fail validation")
