# Google Drive Sync Map

This document maps the SIGMA local checkout, GitHub repository, and Google Drive project folder shared by `zarishsphere@gmail.com`.

## Linked Locations

| Layer | Location |
|---|---|
| Local checkout | `/home/health-pm/sigma-index` |
| GitHub repository | `https://github.com/sigma-standards/sigma-index` |
| Google Drive public folder | `https://drive.google.com/drive/folders/1-ot23dLe23gS-lBKrelmsGeF9OCwnVzJ?usp=drive_link` |
| Mounted Drive path | `/run/user/1000/gvfs/google-drive:host=gmail.com,user=zarishsphere/0ADhYGIfiBrsuUk9PVA/1-ot23dLe23gS-lBKrelmsGeF9OCwnVzJ` |
| Drive sync folder | `SIGMA_GITHUB_SYNC` |

## Current Snapshot

| Field | Value |
|---|---|
| Synced commit | `eae40766cf7bd6512cf2bcfc0872823b2d438695` |
| Branch | `main` |
| Git-tracked file count | `181` |
| Drive snapshot folder | `SIGMA_GITHUB_SYNC/snapshots` |
| Drive manifest folder | `SIGMA_GITHUB_SYNC/manifests` |

## Drive Artifacts

The Drive sync folder stores compressed snapshots instead of a raw expanded mirror. This is intentional: the Google Drive GVFS mount exposes many files as Drive IDs and does not support normal Linux permission or timestamp operations.

| Artifact | Purpose |
|---|---|
| `sigma-index-eae40766cf7b-git-tracked.tar.gz` | Exact Git-tracked repository snapshot from `HEAD`; excludes `.git`, `.venv`, caches, ignored build folders, and local runtime files. |
| `sigma-index-eae40766cf7b-dist.tar.gz` | Generated release/API artifacts from `dist/`. |
| `sigma-index-eae40766cf7b-public.tar.gz` | Generated static site and downloads from `public/`. |
| `SHA256SUMS.txt` | Checksum file for verifying the Drive snapshots. |
| `google_drive_sync_manifest.csv` | Repo and Drive artifact manifest with sizes, paths, and SHA-256 hashes. |
| `google_drive_project_sigma_inventory.csv` | Inventory of visible Drive entries, including GVFS/Drive-ID entries and friendly sync-folder aliases. |

## Repository Manifests

- `data/reports/google_drive_sync_manifest.csv`
- `data/reports/google_drive_project_sigma_inventory.csv`

## Safety Rules

- Do not sync `.venv/`, `.git/`, `.pytest_cache/`, `__pycache__/`, local IDE secrets, or raw runtime memory.
- Do not place API tokens or provider secrets in Google Drive files.
- GitHub remains the source of truth for source history and automation.
- Google Drive is a portable snapshot and handoff layer for the current project state.
- If a Drive file appears as a long ID in terminal listings, use the friendly path documented here or the CSV manifests.
