import csv
from pathlib import Path


def test_research_tasks_cover_all_registered_domains():
    from scripts.build_research_task_report import build_report

    report_path = build_report(Path("."))

    with Path("data/reference/domain_taxonomy.csv").open(newline="", encoding="utf-8") as handle:
        domains = {row["domain_name"] for row in csv.DictReader(handle)}

    with report_path.open(newline="", encoding="utf-8") as handle:
        report_rows = list(csv.DictReader(handle))

    reported_domains = {row["domain_name"] for row in report_rows if row["domain_name"]}
    assert reported_domains == domains
    assert all(int(row["task_count"]) >= 1 for row in report_rows)


def test_research_task_report_includes_all_program_phases():
    from scripts.build_research_task_report import load_all_tasks

    tasks = load_all_tasks(Path("."))
    phases = {task["phase"] for task in tasks}

    assert {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "19"} <= phases
    assert {task["status"] for task in tasks} <= {"done", "active", "planned", "blocked"}
