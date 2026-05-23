---
# Trigger - when should this workflow run?
on:
  issues:
    types: [opened, reopened]

# Permissions - what can this workflow access?
permissions:
  contents: read

  issues: read
  pull-requests: read

# AI engine to use for this workflow
engine: gemini

# Tools - GitHub API access via toolsets (context, repos, issues, pull_requests)
tools:
  github:
    toolsets: [default]

# Network access
network: defaults

# Outputs - what APIs and tools can the AI use?
safe-outputs:
  add-comment:
  add-labels:
  close-issue:
  create-issue:
  update-issue:
---

# issue-processor

This workflow uses the Gemini AI engine to automatically process newly opened or reopened GitHub issues.

## Instructions

1.  **Analyze the issue**: Read the issue title, description, and any existing comments to understand the problem or request.
2.  **Categorize and Label**: Based on the issue content, suggest and apply relevant labels (e.g., `bug`, `enhancement`, `question`, `documentation`, `priority: high`, `priority: medium`, `priority: low`).
3.  **Provide Initial Response**: If the issue is a common question or can be resolved with a simple answer, add a comment with the solution or relevant links.
4.  **Identify Actionable Steps**: If the issue requires further action, suggest next steps, such as requesting more information from the user, assigning it to a specific team/person, or creating a sub-task.
5.  **Close Trivial Issues**: If the issue is a duplicate, spam, or can be immediately closed, close it with an appropriate comment.
6.  **Update Issue Details**: If necessary, update the issue title or description for clarity.

## Notes

-   Run `gh aw compile` to generate the GitHub Actions workflow
-   See https://github.github.com/gh-aw/ for complete configuration options and tools documentation
