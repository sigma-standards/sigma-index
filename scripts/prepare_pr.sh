#!/usr/bin/env bash
set -euo pipefail

# Helper: prepare a git branch and patch for the progress integration
BRANCH=${1:-feat/progress-integration}
MSG=${2:-"feat(progress): generate and render data-driven project progress"}

if [ ! -d .git ]; then
  echo "This directory is not a git repository. Initialize and add a remote before running this script."
  echo "To init: git init; git remote add origin <your-remote-url>"
  exit 1
fi

git checkout -b "$BRANCH"
 git add -A
 git commit -m "$MSG" || echo "No changes to commit or already committed."

# Produce a patch against origin/main or main
if git rev-parse --verify origin/main >/dev/null 2>&1; then
  git format-patch origin/main --stdout > ../project-progress-integration.patch
else
  git format-patch main --stdout > ../project-progress-integration.patch || echo "Unable to produce patch against main; create one manually with git format-patch"
fi

echo "Branch prepared: $BRANCH"
echo "Patch created at ../project-progress-integration.patch (if git format-patch succeeded)"
