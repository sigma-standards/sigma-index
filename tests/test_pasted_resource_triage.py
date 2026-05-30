from pathlib import Path


TRIAGE_DOC = Path("docs") / "PASTED_RESOURCE_TRIAGE.md"


def test_pasted_resource_triage_documents_safe_incorporation():
    content = TRIAGE_DOC.read_text(encoding="utf-8")

    assert "rejected-sensitive-raw" in content
    assert "data/staging/master_directory_global_standards_v2_0.csv" in content
    assert "raw document removed, not committed" in content
    assert "full-ig.zip" in content


def test_pasted_resource_staging_extracts_are_external_archives():
    content = TRIAGE_DOC.read_text(encoding="utf-8")

    assert "516 standards-body/framework entries" in content
    assert "211 public SHR/DGHS link records" in content
    assert "External archived copy" in content
    assert "Keep `data/staging/` ignored in Git" in content


def test_pasted_resource_inventory_records_rejections_and_conversions():
    content = TRIAGE_DOC.read_text(encoding="utf-8")

    assert "| `HRIS API For SHR.docx` | rejected-sensitive-raw |" in content
    assert "| `full-ig.zip` | converted-to-staging-csv |" in content
    assert "| `links.json` | converted-to-staging-csv |" in content
    assert "| `CATALOGS.md` | rejected-out-of-scope |" in content


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
