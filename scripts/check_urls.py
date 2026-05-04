#!/usr/bin/env python3
"""Check URL health for processed SIGMA records."""

from __future__ import annotations

import csv
import datetime
import sys
import time
from pathlib import Path
from typing import Callable

import requests


PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = Path("data/reports/url_health_report.csv")
TIMEOUT = 15
DELAY = 0.5
MAX_URLS = 5000

UrlCheckResult = tuple[int, str, str]
UrlChecker = Callable[[str], UrlCheckResult]


def collect_url_records(processed_dir: Path = PROCESSED_DIR, max_urls: int = MAX_URLS) -> list[dict[str, str]]:
    """Collect unique http(s) official_url records from processed CSV files."""
    records: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    for csv_file in sorted(processed_dir.glob("*.csv")):
        with csv_file.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                url = (row.get("official_url") or "").strip()
                if not url.startswith("http") or url in seen_urls:
                    continue
                seen_urls.add(url)
                records.append(
                    {
                        "sigma_id": (row.get("sigma_id") or "").strip(),
                        "official_url": url,
                        "source_file": csv_file.name,
                    }
                )
                if len(records) >= max_urls:
                    return records

    return records


def check_url(url: str, timeout: int = TIMEOUT) -> UrlCheckResult:
    """Return status code, final URL, and a compact health label."""
    headers = {
        "User-Agent": "SIGMA-Standards-Bot/1.0 (https://github.com/sigma-standards/sigma-index; health check)",
        "Accept": "text/html,application/xhtml+xml,*/*",
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    except requests.exceptions.ConnectionError:
        return 0, url, "connection_error"
    except requests.exceptions.Timeout:
        return 0, url, "timeout"
    except requests.RequestException as exc:
        return 0, url, f"error_{type(exc).__name__}"

    status = response.status_code
    if status == 200:
        health = "ok"
    elif status in {301, 302, 303, 307, 308}:
        health = "redirect"
    elif status == 404:
        health = "dead_404"
    elif status == 403:
        health = "blocked_403"
    elif status == 429:
        health = "rate_limited_429"
    else:
        health = f"http_{status}"
    return status, response.url, health


def run_url_health_check(
    processed_dir: Path = PROCESSED_DIR,
    output_file: Path = OUTPUT_FILE,
    checker: UrlChecker = check_url,
    checked_at: str | None = None,
    delay: float = DELAY,
) -> dict[str, int]:
    """Check URLs, write a CSV report, and return summary counts."""
    timestamp = checked_at or datetime.datetime.now(datetime.UTC).isoformat().replace("+00:00", "Z")
    records = collect_url_records(processed_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "checked_at",
        "sigma_id",
        "official_url",
        "final_url",
        "http_status",
        "health",
        "redirected",
        "source_file",
    ]

    summary = {"total": 0, "ok": 0, "redirect": 0, "dead_or_error": 0}
    with output_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for index, record in enumerate(records):
            status, final_url, health = checker(record["official_url"])
            redirected = final_url.rstrip("/") != record["official_url"].rstrip("/")
            writer.writerow(
                {
                    "checked_at": timestamp,
                    "sigma_id": record["sigma_id"],
                    "official_url": record["official_url"],
                    "final_url": final_url,
                    "http_status": status,
                    "health": health,
                    "redirected": redirected,
                    "source_file": record["source_file"],
                }
            )

            summary["total"] += 1
            if health == "ok":
                summary["ok"] += 1
            elif health == "redirect":
                summary["redirect"] += 1
            else:
                summary["dead_or_error"] += 1

            if delay and index < len(records) - 1:
                time.sleep(delay)

    return summary


def main() -> int:
    summary = run_url_health_check()
    total = summary["total"]
    print(f"SIGMA URL Health Check: checked {total} URLs")
    print(f"  OK: {summary['ok']}")
    print(f"  Redirect: {summary['redirect']}")
    print(f"  Dead/Error: {summary['dead_or_error']}")
    print(f"  Report saved: {OUTPUT_FILE}")

    dead_ratio = summary["dead_or_error"] / max(total, 1)
    return 1 if dead_ratio > 0.05 else 0


if __name__ == "__main__":
    sys.exit(main())
