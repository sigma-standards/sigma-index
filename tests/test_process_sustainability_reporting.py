import csv
import subprocess
import sys
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


def test_process_sustainability_reporting_writes_gri_and_sasb_rows(tmp_path):
    from scripts.process_sustainability_reporting import process_sustainability_reporting

    output_path = process_sustainability_reporting(
        Path("."),
        source_path=Path("data/reference/sustainability_reporting_sources.csv"),
        output_path=tmp_path / "sustainability_reporting_standards.csv",
    )

    rows = read_rows(output_path)
    sigma_ids = {row["sigma_id"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == MASTER_FIELDS
    assert "SE-GRI-1-2021" in sigma_ids
    assert "SE-SASB-EM-EP-2023" in sigma_ids
    assert {row["domain"] for row in rows} == {"Sustainability, ESG & Circular Economy"}


def test_process_sustainability_reporting_filters_source_family(tmp_path):
    from scripts.process_sustainability_reporting import process_sustainability_reporting

    output_path = process_sustainability_reporting(
        Path("."),
        source_path=Path("data/reference/sustainability_reporting_sources.csv"),
        output_path=tmp_path / "gri_standards.csv",
        source_family="GRI",
    )

    rows = read_rows(output_path)

    assert rows
    assert {row["issuer"] for row in rows} == {"Global Reporting Initiative"}
    assert all(row["sigma_id"].startswith("SE-GRI-") for row in rows)


def test_legacy_harvester_entrypoints_run_without_pandas(tmp_path):
    commands = [
        [
            sys.executable,
            "scripts/harvest_gri_standards.py",
            "--output-path",
            str(tmp_path / "gri.csv"),
        ],
        [
            sys.executable,
            "scripts/harvest_sasb_standards.py",
            "--output-path",
            str(tmp_path / "sasb.csv"),
        ],
    ]

    for command in commands:
        result = subprocess.run(command, check=False, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr

    assert (tmp_path / "gri.csv").exists()
    assert (tmp_path / "sasb.csv").exists()
