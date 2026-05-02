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


def test_process_etsi_priority_writes_ict_standards_rows(tmp_path):
    from scripts.process_etsi_priority import process_etsi_priority

    output_path = process_etsi_priority(
        Path("."),
        source_path=Path("data/reference/etsi_priority_sources.csv"),
        output_path=tmp_path / "etsi_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "ICT-ETSI-EN301549" in sigma_ids
    assert "ICT-ETSI-EN303645" in sigma_ids
    assert "ICT-ETSI-TS123501" in sigma_ids
    assert "ICT-ETSI-NFV-SOL003" in sigma_ids
    assert {row["issuer"] for row in rows} == {"European Telecommunications Standards Institute"}
    assert {row["issuer_type"] for row in rows} == {"Industry SDO"}
    assert {row["domain"] for row in rows} == {"Information & Communications Technology (ICT)"}
    assert all(row["official_url"].startswith("https://www.etsi.org/") for row in rows)


def test_process_etsi_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_etsi_priority import process_etsi_priority

    source_path = tmp_path / "etsi_priority_sources.csv"
    original = Path("data/reference/etsi_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_etsi_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate ETSI priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate ETSI priority rows should fail validation")
