#!/usr/bin/env python3
"""Run a registered SIGMA domain worker from GitHub Actions or locally."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_REGISTRY = Path("data/reference/domain_worker_registry.csv")
DEFAULT_STATE_PATH = Path("data/reports/domain_agent_state.json")


def load_registry(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["agent_id"]: row for row in rows}


def parse_secret_names(row: dict[str, str]) -> list[str]:
    names = []
    for field in ("requires_secrets", "optional_secrets"):
        value = row.get(field, "")
        if value and value not in {"false", "true"}:
            names.extend(part.strip() for part in value.split(";") if part.strip())
    return names


def build_state(row: dict[str, str], mode: str, command: list[str]) -> dict[str, object]:
    return {
        "agent_id": row["agent_id"],
        "domain_group": row["domain_group"],
        "mode": mode,
        "make_target": row["make_target"],
        "planned_command": command,
        "output_paths": row["output_paths"].split(";"),
        "retry_limit": int(row["retry_limit"]),
        "fallback_agent_id": row["fallback_agent_id"] or None,
        "human_review_required": row["human_review_required"] == "true",
        "writes_directly_to_main": row["writes_directly_to_main"] == "true",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


def write_state(path: Path, state: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_with_retry(command: list[str], retry_limit: int) -> int:
    last_returncode = 1
    for attempt in range(1, retry_limit + 2):
        print(f"Attempt {attempt}: {' '.join(command)}", flush=True)
        completed = subprocess.run(command, check=False)
        last_returncode = completed.returncode
        if completed.returncode == 0:
            return 0
    return last_returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a SIGMA domain worker")
    parser.add_argument("--agent", required=True, help="Agent id from domain_worker_registry.csv")
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY), help="Registry CSV path")
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH), help="State JSON output path")
    parser.add_argument("--python", default="python3", help="Python executable passed to Make")
    parser.add_argument("--dry-run", action="store_true", help="Write state and print command without executing Make")
    args = parser.parse_args()

    registry = load_registry(Path(args.registry))
    if args.agent not in registry:
        print(f"Unknown domain agent: {args.agent}", file=sys.stderr)
        print("Known agents: " + ", ".join(sorted(registry)), file=sys.stderr)
        return 2

    row = registry[args.agent]
    command = ["make", f"PYTHON={args.python}", row["make_target"]]
    state = build_state(row, "dry-run" if args.dry_run else "execute", command)
    write_state(Path(args.state_path), state)

    if row["writes_directly_to_main"] != "false":
        print("Refusing to run an agent configured for direct main writes.", file=sys.stderr)
        return 3

    if args.dry_run:
        print(f"DRY RUN domain agent: {args.agent}")
        print("Planned command: " + " ".join(command))
        return 0

    return run_with_retry(command, int(row["retry_limit"]))


if __name__ == "__main__":
    raise SystemExit(main())
