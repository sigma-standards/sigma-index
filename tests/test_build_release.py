import csv
import json
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


def write_master_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MASTER_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def row(sigma_id: str, domain: str) -> dict[str, str]:
    return {
        "sigma_id": sigma_id,
        "entry_type": "Standard",
        "meta_layer": "Technology & Infrastructure",
        "domain": domain,
        "sub_domain": "Fixture",
        "name_full": f"Fixture {sigma_id}",
        "name_short": sigma_id,
        "standard_id": sigma_id,
        "issuer": "SIGMA Test",
        "issuer_type": "Standards body",
        "governance_layer": "Global",
        "geographic_scope": "Global",
        "year_published": "2026",
        "year_first": "2026",
        "status": "Active",
        "mandate": "Voluntary",
        "sector_applicability": "Testing",
        "why_it_matters": "Fixture row for release normalization.",
        "key_outputs": "Fixture",
        "official_url": "https://example.org/fixture",
        "data_source": "Unit test",
        "notes": "",
    }


def test_build_release_normalizes_legacy_domain_labels(tmp_path):
    from scripts.build_release import main

    processed_dir = tmp_path / "data" / "processed"
    relationships_dir = tmp_path / "data" / "relationships"
    reference_dir = tmp_path / "data" / "reference"
    reports_dir = tmp_path / "data" / "reports"
    output_dir = tmp_path / "dist"

    write_master_csv(
        processed_dir / "legacy.csv",
        [
            row("DG-IETF-RFC0001-1969", "Information Technology"),
            row("TECH-ISO-1234-2026", "Technology"),
            row("CY-NIST-CSF-20", "Cybersecurity & Data Privacy"),
        ],
    )
    relationships_dir.mkdir(parents=True)
    reference_dir.mkdir(parents=True)
    reports_dir.mkdir(parents=True)
    (reports_dir / "relationship_quality.csv").write_text(
        "check_id,severity,status,detail\nrelationship_total_edges,info,pass,3 relationship edges\n",
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--processed-dir",
            str(processed_dir),
            "--relationships-dir",
            str(relationships_dir),
            "--reference-dir",
            str(reference_dir),
            "--reports-dir",
            str(reports_dir),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert exit_code == 0

    with (output_dir / "sigma_master.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    api_index = json.loads((output_dir / "api_index.json").read_text(encoding="utf-8"))

    assert {record["domain"] for record in rows} == {
        "Information & Communications Technology (ICT)",
        "Cybersecurity & Data Privacy",
    }
    assert "Information Technology" not in api_index["facets"]["domains"]
    assert "Technology" not in api_index["facets"]["domains"]
    assert "Information & Communications Technology (ICT)" in api_index["facets"]["domains"]
    assert (output_dir / "relationship_quality.csv").exists()
