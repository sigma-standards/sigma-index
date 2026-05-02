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


def test_process_culture_priority_writes_unesco_icomos_icom_iccrom_rows(tmp_path):
    from scripts.process_culture_priority import process_culture_priority

    output_path = process_culture_priority(
        Path("."),
        source_path=Path("data/reference/culture_priority_sources.csv"),
        output_path=tmp_path / "culture_heritage_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "CU-UNESCO-WHC-1972" in sigma_ids
    assert "CU-UNESCO-ICH-2003" in sigma_ids
    assert "CU-UNESCO-HAGUE-1954" in sigma_ids
    assert "CU-ICOMOS-VENICE-1964" in sigma_ids
    assert "CU-ICOMOS-NARA-1994" in sigma_ids
    assert "CU-ICOM-CODE-ETHICS" in sigma_ids
    assert "CU-ICCROM-FAC-2018" in sigma_ids
    assert {row["domain"] for row in rows} == {"Culture, Heritage & Arts"}
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_process_culture_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_culture_priority import process_culture_priority

    source_path = tmp_path / "culture_priority_sources.csv"
    original = Path("data/reference/culture_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_culture_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate culture priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate culture priority rows should fail validation")
