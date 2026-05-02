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


def test_process_iaea_priority_writes_safety_standards_rows(tmp_path):
    from scripts.process_iaea_priority import process_iaea_priority

    output_path = process_iaea_priority(
        Path("."),
        source_path=Path("data/reference/iaea_priority_sources.csv"),
        output_path=tmp_path / "iaea_safety_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "EU-IAEA-SF-1" in sigma_ids
    assert "EU-IAEA-GSR-PART-3" in sigma_ids
    assert "EU-IAEA-GSR-PART-7" in sigma_ids
    assert "EU-IAEA-SSR-2-1" in sigma_ids
    assert {row["issuer"] for row in rows} == {"International Atomic Energy Agency"}
    assert {row["domain"] for row in rows} == {"Energy & Utilities"}
    assert all(row["official_url"].startswith("https://www.iaea.org/") for row in rows)


def test_process_iaea_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_iaea_priority import process_iaea_priority

    source_path = tmp_path / "iaea_priority_sources.csv"
    original = Path("data/reference/iaea_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_iaea_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate IAEA priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate IAEA priority rows should fail validation")
