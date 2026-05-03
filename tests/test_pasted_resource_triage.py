import csv
from pathlib import Path


TRIAGE_DOC = Path("docs") / "PASTED_RESOURCE_TRIAGE.md"
STAGING_DIR = Path("data") / "staging"


def read_csv_rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_pasted_resource_triage_documents_safe_incorporation():
    content = TRIAGE_DOC.read_text(encoding="utf-8")

    assert "rejected-sensitive-raw" in content
    assert "data/staging/master_directory_global_standards_v2_0.csv" in content
    assert "raw document removed, not committed" in content
    assert "full-ig.zip" in content


def test_pasted_resource_staging_extracts_expected_counts():
    master_rows = read_csv_rows(STAGING_DIR / "master_directory_global_standards_v2_0.csv")
    fhir_rows = read_csv_rows(STAGING_DIR / "bangladesh_fhir_canonical_resources.csv")
    link_rows = read_csv_rows(STAGING_DIR / "bangladesh_shr_link_inventory.csv")

    assert len(master_rows) == 516
    assert len(fhir_rows) >= 60
    assert len(link_rows) == 211
    assert {"ID", "Domain", "Entry Type", "Name (Full)", "Official URL"}.issubset(
        master_rows[0]
    )
    assert {"id", "type", "url", "source_archive"}.issubset(fhir_rows[0])
    assert {"idx", "description", "url", "source_file"}.issubset(link_rows[0])


def test_pasted_resource_inventory_records_rejections_and_conversions():
    inventory_rows = read_csv_rows(STAGING_DIR / "pasted_resource_inventory.csv")
    actions = {row["file_name"]: row["action"] for row in inventory_rows}

    assert actions["HRIS API For SHR.docx"] == "rejected-sensitive-raw"
    assert actions["full-ig.zip"] == "converted-to-staging-csv"
    assert actions["links.json"] == "converted-to-staging-csv"
    assert actions["CATALOGS.md"] == "rejected-out-of-scope"


def test_raw_pasted_sources_were_removed_from_repository_root():
    removed_paths = [
        Path("HRIS API For SHR.docx"),
        Path("MASTER_DIRECTORY_Global_Standards_v2_0.xlsx"),
        Path("full-ig.zip"),
        Path("files.zip"),
        Path("Shared Health Record technical architecture overview - Claude_files"),
    ]

    for path in removed_paths:
        assert not path.exists()
