import csv
from pathlib import Path


MASTER_HEADER = [
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


def write_master_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def complete_row(sigma_id: str, official_url: str = "https://example.org/standard") -> dict[str, str]:
    return {
        "sigma_id": sigma_id,
        "entry_type": "Standard",
        "meta_layer": "Life Sciences & Health",
        "domain": "Health & Medical",
        "sub_domain": "Quality gate test",
        "name_full": f"Quality Gate Test {sigma_id}",
        "name_short": sigma_id,
        "standard_id": sigma_id,
        "issuer": "SIGMA Test",
        "issuer_type": "NGO",
        "governance_layer": "International",
        "geographic_scope": "Global",
        "year_published": "2026",
        "year_first": "2026",
        "status": "Active",
        "mandate": "Voluntary",
        "sector_applicability": "Testing",
        "why_it_matters": "Quality gate fixture",
        "key_outputs": "Fixture row",
        "official_url": official_url,
        "data_source": "Unit test",
        "notes": "",
    }


def test_build_quality_gate_reports_clean_processed_data(tmp_path):
    from scripts.build_quality_gate import build_quality_gate

    write_master_csv(tmp_path / "data/processed/example.csv", [complete_row("QA-1"), complete_row("QA-2")])

    report_path = build_quality_gate(tmp_path)
    rows = read_rows(report_path)

    assert report_path == tmp_path / "data/reports/quality_gate.csv"
    assert rows == [
        {"check_id": "processed_duplicate_sigma_ids", "severity": "critical", "status": "pass", "detail": "0 duplicate sigma_id values"},
        {"check_id": "processed_required_fields", "severity": "critical", "status": "pass", "detail": "0 missing required field values"},
        {"check_id": "processed_url_shape", "severity": "critical", "status": "pass", "detail": "0 non-http official_url values"},
    ]
    assert (tmp_path / "docs/QUALITY_GATE.md").exists()


def test_build_quality_gate_fails_on_duplicate_ids_missing_fields_and_bad_urls(tmp_path):
    from scripts.build_quality_gate import build_quality_gate

    missing_required = complete_row("QA-2", official_url="not-a-url")
    missing_required["issuer"] = ""
    write_master_csv(
        tmp_path / "data/processed/example.csv",
        [complete_row("QA-1"), complete_row("QA-1"), missing_required],
    )

    report_path = build_quality_gate(tmp_path)
    rows = {row["check_id"]: row for row in read_rows(report_path)}

    assert rows["processed_duplicate_sigma_ids"]["status"] == "fail"
    assert rows["processed_duplicate_sigma_ids"]["detail"] == "1 duplicate sigma_id values: QA-1"
    assert rows["processed_required_fields"]["status"] == "fail"
    assert rows["processed_required_fields"]["detail"] == "1 missing required field values"
    assert rows["processed_url_shape"]["status"] == "fail"
    assert rows["processed_url_shape"]["detail"] == "1 non-http official_url values"
