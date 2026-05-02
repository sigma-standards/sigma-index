import csv
from pathlib import Path


STAGING_FIELDS = [
    "source_id",
    "title",
    "chapter",
    "depositary",
    "adoption_date",
    "entry_into_force",
    "record_type",
    "official_url",
    "parties_url",
    "review_status",
    "notes",
]


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def test_stage_un_treaties_writes_core_human_rights_candidates(tmp_path):
    from scripts.stage_un_treaties import stage_un_treaties

    output_path = stage_un_treaties(
        Path("."),
        source_path=Path("data/reference/un_treaty_priority_sources.csv"),
        output_path=tmp_path / "un_treaty_candidates.csv",
    )

    rows = read_rows(output_path)
    source_ids = {row["source_id"] for row in rows}
    titles = {row["title"] for row in rows}

    assert output_path.exists()
    assert list(rows[0].keys()) == STAGING_FIELDS
    assert "UNTC-IV-3-ICESCR" in source_ids
    assert "UNTC-IV-4-ICCPR" in source_ids
    assert "UNTC-IV-11-CRC" in source_ids
    assert "Convention on the Rights of Persons with Disabilities" in titles
    assert {row["depositary"] for row in rows} == {"Secretary-General of the United Nations"}
    assert {row["review_status"] for row in rows} == {"needs-curator-review"}
    assert all(row["official_url"].startswith("https://treaties.un.org/") for row in rows)


def test_stage_un_treaties_rejects_duplicate_source_ids(tmp_path):
    from scripts.stage_un_treaties import stage_un_treaties

    source_path = tmp_path / "un_treaty_priority_sources.csv"
    original = Path("data/reference/un_treaty_priority_sources.csv").read_text(encoding="utf-8")
    lines = original.splitlines()
    source_path.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")

    try:
        stage_un_treaties(Path("."), source_path=source_path, output_path=tmp_path / "out.csv")
    except ValueError as exc:
        assert "duplicate UN treaty source_id values" in str(exc)
    else:
        raise AssertionError("duplicate UN treaty staging rows should fail validation")
