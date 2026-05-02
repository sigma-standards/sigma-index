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


def test_process_humanitarian_priority_writes_domain17_records(tmp_path):
    from scripts.process_humanitarian_priority import process_humanitarian_priority

    output_path = process_humanitarian_priority(Path("."), output_path=tmp_path / "humanitarian.csv")

    rows = read_rows(output_path)
    assert output_path.exists()
    assert len(rows) >= 5
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert {row["domain"] for row in rows} == {"Humanitarian & Emergency Response"}
    assert {"CHS", "INEE Minimum Standards", "WHO EMT minimum standards"} <= {
        row["name_short"] for row in rows
    }
    assert all(row["official_url"].startswith("https://") for row in rows)


def test_humanitarian_priority_ids_do_not_duplicate_domain_seed_ids(tmp_path):
    from scripts.process_humanitarian_priority import process_humanitarian_priority

    output_path = process_humanitarian_priority(Path("."), output_path=tmp_path / "humanitarian.csv")
    humanitarian_ids = {row["sigma_id"] for row in read_rows(output_path)}
    seed_ids = {row["sigma_id"] for row in read_rows(Path("data/processed/domain_seed_standards.csv"))}

    assert humanitarian_ids.isdisjoint(seed_ids)
