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


def write_processed_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def row(sigma_id: str, official_url: str) -> dict[str, str]:
    return {field: "" for field in MASTER_HEADER} | {
        "sigma_id": sigma_id,
        "official_url": official_url,
    }


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_collect_url_records_uses_csv_and_deduplicates_http_urls(tmp_path):
    from scripts.check_urls import collect_url_records

    processed_dir = tmp_path / "data" / "processed"
    write_processed_csv(
        processed_dir / "example.csv",
        [
            row("SIGMA-1", "https://example.org/one"),
            row("SIGMA-2", "not-a-url"),
            row("SIGMA-3", "https://example.org/one"),
            row("SIGMA-4", ""),
        ],
    )
    write_processed_csv(
        processed_dir / "second.csv",
        [row("SIGMA-5", "https://example.org/two")],
    )

    records = collect_url_records(processed_dir)

    assert records == [
        {
            "sigma_id": "SIGMA-1",
            "official_url": "https://example.org/one",
            "source_file": "example.csv",
        },
        {
            "sigma_id": "SIGMA-5",
            "official_url": "https://example.org/two",
            "source_file": "second.csv",
        },
    ]


def test_run_url_health_check_writes_report_with_injected_checker(tmp_path):
    from scripts.check_urls import run_url_health_check

    processed_dir = tmp_path / "data" / "processed"
    report_path = tmp_path / "data" / "reports" / "url_health_report.csv"
    write_processed_csv(
        processed_dir / "example.csv",
        [
            row("SIGMA-1", "https://example.org/ok"),
            row("SIGMA-2", "https://example.org/missing"),
        ],
    )

    def fake_checker(url: str) -> tuple[int, str, str]:
        if url.endswith("/ok"):
            return 200, url, "ok"
        return 404, url, "dead_404"

    summary = run_url_health_check(
        processed_dir=processed_dir,
        output_file=report_path,
        checker=fake_checker,
        checked_at="2026-05-04T00:00:00Z",
        delay=0,
    )

    assert summary == {"total": 2, "ok": 1, "redirect": 0, "dead_or_error": 1}
    assert read_rows(report_path) == [
        {
            "checked_at": "2026-05-04T00:00:00Z",
            "sigma_id": "SIGMA-1",
            "official_url": "https://example.org/ok",
            "final_url": "https://example.org/ok",
            "http_status": "200",
            "health": "ok",
            "redirected": "False",
            "source_file": "example.csv",
        },
        {
            "checked_at": "2026-05-04T00:00:00Z",
            "sigma_id": "SIGMA-2",
            "official_url": "https://example.org/missing",
            "final_url": "https://example.org/missing",
            "http_status": "404",
            "health": "dead_404",
            "redirected": "False",
            "source_file": "example.csv",
        },
    ]
