#!/usr/bin/env python3
"""Build reports from the SIGMA research task matrix."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


DOMAIN_REGISTRY = Path("data/reference/domain_taxonomy.csv")
TASK_REGISTRY = Path("data/reference/research_tasks.csv")
SOURCE_REGISTRY = Path("data/reference/source_registry.csv")
REPORT_OUTPUT = Path("data/reports/research_task_coverage.csv")
DOC_OUTPUT = Path("docs/RESEARCH_TASKS.md")

TASK_FIELDS = [
    "task_id",
    "phase",
    "phase_name",
    "domain_id",
    "domain_name",
    "meta_layer",
    "task_type",
    "source_targets",
    "deliverable",
    "status",
    "priority",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def load_tasks(path: Path = TASK_REGISTRY) -> list[dict[str, str]]:
    tasks = read_csv(path)
    missing_fields = [field for field in TASK_FIELDS if field not in (tasks[0].keys() if tasks else [])]
    if missing_fields:
        raise ValueError(f"research task registry is missing fields: {', '.join(missing_fields)}")
    return tasks


def load_all_tasks(root: Path | str = Path(".")) -> list[dict[str, str]]:
    root = Path(root)
    tasks = load_tasks(root / TASK_REGISTRY)
    tasks.extend(synthesize_domain_tasks(root, tasks))
    return tasks


def synthesize_domain_tasks(root: Path, existing_tasks: list[dict[str, str]]) -> list[dict[str, str]]:
    domains = read_csv(root / DOMAIN_REGISTRY)
    sources = {row["domain_id"]: row for row in read_csv(root / SOURCE_REGISTRY)}
    existing_domain_ids = {task["domain_id"] for task in existing_tasks if task.get("domain_id")}
    tasks: list[dict[str, str]] = []
    for domain in domains:
        if domain["domain_id"] in existing_domain_ids:
            continue
        source = sources.get(domain["domain_id"], {})
        phase, phase_name = _phase_for_domain(int(domain["domain_id"]))
        tasks.append(
            {
                "task_id": f"D{int(domain['domain_id']):02d}-EXPAND",
                "phase": phase,
                "phase_name": phase_name,
                "domain_id": domain["domain_id"],
                "domain_name": domain["domain_name"],
                "meta_layer": domain["meta_layer"],
                "task_type": "domain-expansion",
                "source_targets": source.get("primary_free_sources", ""),
                "deliverable": f"{domain['domain_name']} verified catalogue",
                "status": "planned",
                "priority": _priority_for_domain(int(domain["domain_id"])),
            }
        )
    return tasks


def _phase_for_domain(domain_id: int) -> tuple[str, str]:
    if domain_id in {1, 5, 15, 16, 17, 20}:
        return "2", "Priority domains complete"
    if 36 <= domain_id <= 40 and domain_id != 39:
        return "3", "Environment climate and natural systems"
    if 23 <= domain_id <= 27:
        return "4", "Finance trade and economic governance"
    if 28 <= domain_id <= 30:
        return "5", "ICT digital AI and cybersecurity"
    if 7 <= domain_id <= 14 or 31 <= domain_id <= 34:
        return "6", "Transport energy manufacturing and built environment"
    if domain_id in {18, 19, 21, 22, 35, 39, 40}:
        return "7", "Society culture sports and specialised domains"
    return "1", "Seed from free bulk sources"


def _priority_for_domain(domain_id: int) -> str:
    if domain_id in {1, 2, 15, 16, 17, 23, 24, 26, 28, 29, 30, 33, 36}:
        return "critical"
    if domain_id in {3, 4, 5, 6, 13, 14, 20, 25, 31, 32, 37, 38, 39}:
        return "high"
    return "medium"


def build_report(root: Path | str = Path(".")) -> Path:
    root = Path(root)
    domains = read_csv(root / DOMAIN_REGISTRY)
    tasks = load_all_tasks(root)
    tasks_by_domain: dict[str, list[dict[str, str]]] = defaultdict(list)
    for task in tasks:
        if task.get("domain_id"):
            tasks_by_domain[task["domain_id"]].append(task)

    output = root / REPORT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "domain_id",
            "domain_name",
            "meta_layer",
            "task_count",
            "done",
            "active",
            "planned",
            "blocked",
            "highest_priority",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for domain in domains:
            domain_tasks = tasks_by_domain.get(domain["domain_id"], [])
            statuses = Counter(task["status"] for task in domain_tasks)
            priorities = [task["priority"] for task in domain_tasks]
            writer.writerow(
                {
                    "domain_id": domain["domain_id"],
                    "domain_name": domain["domain_name"],
                    "meta_layer": domain["meta_layer"],
                    "task_count": len(domain_tasks),
                    "done": statuses.get("done", 0),
                    "active": statuses.get("active", 0),
                    "planned": statuses.get("planned", 0),
                    "blocked": statuses.get("blocked", 0),
                    "highest_priority": _highest_priority(priorities),
                }
            )
    write_markdown(root / DOC_OUTPUT, tasks)
    return output


def _highest_priority(priorities: list[str]) -> str:
    rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    if not priorities:
        return ""
    return sorted(priorities, key=lambda priority: rank.get(priority, 99))[0]


def write_markdown(path: Path, tasks: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_phase: dict[str, list[dict[str, str]]] = defaultdict(list)
    for task in tasks:
        by_phase[task["phase"]].append(task)

    lines = [
        "# SIGMA Research Task Matrix",
        "",
        "This file is generated from `data/reference/research_tasks.csv` by `scripts/build_research_task_report.py`.",
        "It turns the research plan into an executable task matrix across all phases, domains, levels, and publication workstreams.",
        "",
        "## Current Interpretation",
        "",
        "- `done`: implemented in the repository and covered by validation or generated data.",
        "- `active`: wired into the pipeline, but still awaiting more source rows or enrichment.",
        "- `planned`: accepted scope from the research plan that still needs source-specific ingestion and verification.",
        "- `blocked`: cannot proceed until access, licensing, or source availability is resolved.",
        "",
    ]

    for phase in sorted(by_phase, key=lambda value: int(value) if value.isdigit() else 999):
        phase_tasks = by_phase[phase]
        lines.extend(
            [
                f"## Phase {phase}: {phase_tasks[0]['phase_name']}",
                "",
                "| Task | Domain | Type | Status | Priority | Deliverable |",
                "|---|---|---|---|---|---|",
            ]
        )
        for task in sorted(phase_tasks, key=lambda row: row["task_id"]):
            domain = task["domain_name"] or "Program"
            lines.append(
                "| {task_id} | {domain} | {task_type} | {status} | {priority} | {deliverable} |".format(
                    task_id=task["task_id"],
                    domain=domain,
                    task_type=task["task_type"],
                    status=task["status"],
                    priority=task["priority"],
                    deliverable=task["deliverable"],
                )
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    output = build_report(Path("."))
    print(f"Wrote research task coverage report to {output}")
    print(f"Wrote research task documentation to {DOC_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
