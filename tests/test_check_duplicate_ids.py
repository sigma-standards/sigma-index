import csv
from pathlib import Path

from scripts.check_duplicate_ids import collect_sigma_ids


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sigma_id", "name_full"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def test_collect_sigma_ids_reports_locations(tmp_path):
    processed_dir = tmp_path / "processed"
    write_csv(processed_dir / "one.csv", [{"sigma_id": "HL-WHO-IHR-2005", "name_full": "A"}])
    write_csv(processed_dir / "two.csv", [{"sigma_id": "HL-WHO-IHR-2005", "name_full": "B"}])

    locations = collect_sigma_ids(processed_dir)

    assert locations["HL-WHO-IHR-2005"] == [
        f"{processed_dir / 'one.csv'}:2",
        f"{processed_dir / 'two.csv'}:2",
    ]
