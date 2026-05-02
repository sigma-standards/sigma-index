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


def test_process_sports_priority_writes_sports_governance_rows(tmp_path):
    from scripts.process_sports_priority import process_sports_priority

    output_path = process_sports_priority(
        Path("."),
        source_path=Path("data/reference/sports_priority_sources.csv"),
        output_path=tmp_path / "sports_recreation_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "SPT-WADA-CODE-2021" in sigma_ids
    assert "SPT-WADA-PROHIBITED-LIST-2026" in sigma_ids
    assert "SPT-IOC-OLYMPIC-CHARTER-2025" in sigma_ids
    assert "SPT-IFAB-LOTG-2025-26" in sigma_ids
    assert "SPT-WA-COMP-TECH-RULES-2026" in sigma_ids
    assert "SPT-CAS-CODE-2020" in sigma_ids
    assert "SPT-FIBA-RULES-2024" in sigma_ids
    assert "SPT-ITF-RULES-TENNIS-2025" in sigma_ids
    assert {row["domain"] for row in rows} == {"Sports & Recreation"}
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_process_sports_priority_rejects_duplicate_ids(tmp_path):
    from scripts.process_sports_priority import process_sports_priority

    source_path = tmp_path / "sports_priority_sources.csv"
    original = Path("data/reference/sports_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        process_sports_priority(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate sports priority sigma_id values" in str(exc)
    else:
        raise AssertionError("duplicate sports priority rows should fail validation")
