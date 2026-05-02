import csv
from pathlib import Path


RELATIONSHIP_FIELDS = ["from_id", "to_id", "relationship_type", "confidence", "source_url", "notes"]


def write_relationships(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RELATIONSHIP_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_relationship_quality_report_marks_publication_ready_graph(tmp_path):
    from scripts.build_relationship_quality import build_relationship_quality

    write_relationships(
        tmp_path / "data" / "relationships" / "relationships_extracted.csv",
        [
            {
                "from_id": "A",
                "to_id": "B",
                "relationship_type": "references",
                "confidence": "source-confirmed",
                "source_url": "https://example.org/a",
                "notes": "fixture",
            },
            {
                "from_id": "C",
                "to_id": "D",
                "relationship_type": "supersedes",
                "confidence": "curator-reviewed",
                "source_url": "https://example.org/c",
                "notes": "fixture",
            },
        ],
    )
    write_relationships(tmp_path / "data" / "relationships" / "relationships_template.csv", [])

    report_path = build_relationship_quality(tmp_path)
    rows = {row["check_id"]: row for row in read_rows(report_path)}

    assert report_path == tmp_path / "data" / "reports" / "relationship_quality.csv"
    assert rows["relationship_total_edges"]["detail"] == "2 relationship edges"
    assert rows["relationship_publication_ready_edges"]["status"] == "pass"
    assert rows["relationship_publication_ready_edges"]["detail"] == "2 of 2 edges are source-confirmed or curator-reviewed"
    assert rows["relationship_missing_source_url"]["status"] == "pass"
    assert rows["relationship_missing_confidence"]["status"] == "pass"
    assert rows["relationship_llm_suggested_edges"]["status"] == "pass"
    assert (tmp_path / "docs" / "RELATIONSHIP_QUALITY.md").exists()


def test_relationship_quality_report_flags_traceability_gaps(tmp_path):
    from scripts.build_relationship_quality import build_relationship_quality

    write_relationships(
        tmp_path / "data" / "relationships" / "relationships_extracted.csv",
        [
            {
                "from_id": "A",
                "to_id": "B",
                "relationship_type": "references",
                "confidence": "llm-suggested",
                "source_url": "",
                "notes": "fixture",
            },
            {
                "from_id": "C",
                "to_id": "D",
                "relationship_type": "references",
                "confidence": "",
                "source_url": "https://example.org/c",
                "notes": "fixture",
            },
        ],
    )

    report_path = build_relationship_quality(tmp_path)
    rows = {row["check_id"]: row for row in read_rows(report_path)}

    assert rows["relationship_publication_ready_edges"]["status"] == "fail"
    assert rows["relationship_publication_ready_edges"]["detail"] == "0 of 2 edges are source-confirmed or curator-reviewed"
    assert rows["relationship_missing_source_url"]["status"] == "fail"
    assert rows["relationship_missing_source_url"]["detail"] == "1 edges missing source_url"
    assert rows["relationship_missing_confidence"]["status"] == "fail"
    assert rows["relationship_missing_confidence"]["detail"] == "1 edges missing confidence"
    assert rows["relationship_llm_suggested_edges"]["status"] == "warn"
    assert rows["relationship_llm_suggested_edges"]["detail"] == "1 llm-suggested edges require review before publication"
