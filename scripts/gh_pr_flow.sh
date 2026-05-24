#!/usr/bin/env bash
set -euo pipefail

# Helper to create and optionally merge the PR using the GitHub CLI (`gh`).
# This script runs locally and uses your local SSH auth / gh auth session.

REPO="sigma-standards/sigma-index"
BRANCH=${1:-feat/progress-integration}
BASE=${2:-main}
PR_TITLE="feat(progress): generate and render data-driven project progress"
PR_BODY="Generates docs/PROJECT_PROGRESS.md and renders progress on site. See docs/PR_INSTRUCTIONS.md."

GH_CMD=${GH_CLI:-gh}

if ! command -v "$GH_CMD" >/dev/null 2>&1; then
  echo "gh CLI not found. Install from https://cli.github.com/ and authenticate first."
  exit 1
fi

echo "Ensuring branch '$BRANCH' is pushed to origin..."
git fetch origin || true
git checkout "$BRANCH"
git push -u origin "$BRANCH"

# Create PR if not exists
if ! $GH_CMD pr view --repo "$REPO" --head "$BRANCH" >/dev/null 2>&1; then
  echo "Creating PR on $REPO..."
  $GH_CMD pr create --repo "$REPO" --title "$PR_TITLE" --body "$PR_BODY" --base "$BASE" --head "$BRANCH"
else
  echo "PR already exists for branch $BRANCH."
fi

# Show PR URL
PR_URL=$($GH_CMD pr view --repo "$REPO" --head "$BRANCH" --json url -q .url 2>/dev/null || true)
if [ -n "$PR_URL" ]; then
  echo "PR URL: $PR_URL"
else
  echo "Unable to determine PR URL via gh; run 'gh pr view --repo $REPO --head $BRANCH' to find it." 
fi

read -r -p "Merge the PR now? [y/N]: " yn
if [[ "$yn" =~ ^[Yy]$ ]]; then
  echo "Merging PR (merge commit) and deleting branch..."
  $GH_CMD pr merge --repo "$REPO" --head "$BRANCH" --merge --delete-branch
  echo "Merged and remote branch deleted (if allowed)."
else
  echo "Skipping merge. You can review and merge the PR from the GitHub UI or run this script again to merge."
fi
