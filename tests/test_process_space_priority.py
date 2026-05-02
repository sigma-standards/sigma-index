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


def test_process_space_priority_writes_ccsds_and_ecss_rows(tmp_path):
    from scripts.process_space_priority import process_space_priority

    output_path = process_space_priority(
        Path("."),
        source_path=Path("data/reference/space_priority_sources.csv"),
        output_path=tmp_path / "space_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}
    issuers = {row["issuer"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "SP-CCSDS-133-0-B" in sigma_ids
    assert "SP-CCSDS-727-0-B" in sigma_ids
    assert "SP-ECSS-E-ST-10C" in sigma_ids
    assert "SP-ECSS-Q-ST-70-08C" in sigma_ids
    assert {"Consultative Committee for Space Data Systems", "European Cooperation for Space Standardization"} <= issuers
    assert {row["domain"] for row in rows} == {"Space & Satellite"}
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_process_space_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_space_priority import process_space_priority

    source_path = tmp_path / "space_priority_sources.csv"
    original = Path("data/reference/space_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_space_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate space priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate space priority rows should fail validation")
