# SIGMA Repository Instructions

Follow `AGENTS.md` first.

SIGMA is a GitHub-first global standards index. Prefer Makefile targets over ad hoc script calls, keep generated runtime folders out of commits, and validate before publishing.

Use local Python as `.venv/bin/python` when running on this machine. In GitHub Actions, use `make PYTHON=python3 ...`.

Do not commit secrets or raw Codex runtime memory. Store optional provider keys only in GitHub repository secrets. Use `docs/GITHUB_AGENTIC_SETUP_GUIDE.md` for setup details.

When changing domain automation, keep the safety model intact:

- no direct writes to `main`
- pull request review gates
- state artifacts without secret values
- validation before merge
