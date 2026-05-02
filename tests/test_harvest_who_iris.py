import csv
from pathlib import Path


STAGING_FIELDS = [
    "source_id",
    "title",
    "year",
    "record_type",
    "official_url",
    "matched_terms",
    "review_status",
]


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_harvest_who_iris_filters_normative_oai_records(tmp_path):
    from scripts.harvest_who_iris import harvest_who_iris

    output_path = harvest_who_iris(
        Path("."),
        input_xml=Path("data/reference/who_iris_oai_sample.xml"),
        output_path=tmp_path / "who_iris_filtered.csv",
    )

    rows = read_rows(output_path)
    titles = {row["title"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == STAGING_FIELDS
    assert "WHO guideline on self-care interventions for health and well-being" in titles
    assert "International classification of functioning, disability and health" in titles
    assert "World health statistics 2024: monitoring health for the SDGs" not in titles
    assert {row["review_status"] for row in rows} == {"needs-curator-review"}


def test_harvest_who_iris_labels_record_types(tmp_path):
    from scripts.harvest_who_iris import harvest_who_iris

    output_path = harvest_who_iris(
        Path("."),
        input_xml=Path("data/reference/who_iris_oai_sample.xml"),
        output_path=tmp_path / "who_iris_filtered.csv",
    )

    rows = read_rows(output_path)
    by_title = {row["title"]: row for row in rows}

    assert by_title["WHO guideline on self-care interventions for health and well-being"]["record_type"] == "Guideline"
    assert by_title["International classification of functioning, disability and health"]["record_type"] == "Classification"
