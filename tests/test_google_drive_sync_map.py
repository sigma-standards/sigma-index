import csv
from pathlib import Path


SYNC_MAP = Path("docs") / "GOOGLE_DRIVE_SYNC_MAP.md"
SYNC_MANIFEST = Path("data") / "reports" / "google_drive_sync_manifest.csv"
DRIVE_INVENTORY = Path("data") / "reports" / "google_drive_project_sigma_inventory.csv"


def test_google_drive_sync_map_links_drive_local_and_github():
    content = SYNC_MAP.read_text(encoding="utf-8")

    assert "https://github.com/sigma-standards/sigma-index" in content
    assert "https://drive.google.com/drive/folders/1-ot23dLe23gS-lBKrelmsGeF9OCwnVzJ" in content
    assert "/home/health-pm/sigma-index" in content
    assert "SIGMA_GITHUB_SYNC" in content
    assert "Do not sync `.venv/`" in content
    assert "Do not place API tokens" in content


def test_google_drive_sync_manifest_lists_snapshot_artifacts():
    rows = list(csv.DictReader(SYNC_MANIFEST.read_text(encoding="utf-8").splitlines()))
    artifacts = {row["artifact"]: row for row in rows}

    assert "sigma-index-eae40766cf7b-git-tracked.tar.gz" in artifacts
    assert "sigma-index-eae40766cf7b-dist.tar.gz" in artifacts
    assert "sigma-index-eae40766cf7b-public.tar.gz" in artifacts
    assert "SHA256SUMS.txt" in artifacts
    assert all(row["sha256"] for row in rows)
    assert all(int(row["size_bytes"]) > 0 for row in rows)


def test_google_drive_inventory_exposes_friendly_sync_paths():
    rows = list(csv.DictReader(DRIVE_INVENTORY.read_text(encoding="utf-8").splitlines()))
    paths = {row["relative_path"] for row in rows}

    assert "SIGMA_GITHUB_SYNC" in paths
    assert "SIGMA_GITHUB_SYNC/snapshots" in paths
    assert "SIGMA_GITHUB_SYNC/manifests" in paths
