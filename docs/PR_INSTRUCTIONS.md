PR title: Integrate data-driven project progress into static site

Summary:
- Generate `docs/PROJECT_PROGRESS.md` and `data/reports/project_progress.csv` from `data/reference/research_tasks.csv` and `data/reference/domain_taxonomy.csv` via `scripts/build_research_task_report.py`.
- Compute project progress dynamically in `scripts/build_static_site.py` and render it on the homepage.
- Include `docs/PROJECT_PROGRESS.md` in the rendered docs set and update documentation.

Suggested commit message:

feat(progress): generate and render data-driven project progress

- Add progress generation to `scripts/build_research_task_report.py` (writes `data/reports/project_progress.csv` and `docs/PROJECT_PROGRESS.md`).
- Add `compute_project_progress()` to `scripts/build_static_site.py` and wire it into `build_site()`.
- Include `docs/PROJECT_PROGRESS.md` in site docs and restore roadmap label.
- Add local `venv` instructions and test notes to README/CHANGELOG.

Commands to create a branch, commit, and prepare a patch (run from repo root):

```bash
# create feature branch
git checkout -b feat/progress-integration
# add files and commit
git add -A
git commit -m "feat(progress): generate and render data-driven project progress"
# create a patch file for PR review
git format-patch origin/main --stdout > ../project-progress-integration.patch || git format-patch main --stdout > ../project-progress-integration.patch
# push branch and open PR via GitHub UI
git push --set-upstream origin feat/progress-integration
```

Notes:
- If this repository is not yet a git clone locally, run `git init`, add the remote, then create the branch as above.
- The provided patch file command attempts to format a patch against `origin/main` then `main` as fallback.
