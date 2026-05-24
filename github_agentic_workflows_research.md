# GitHub Agentic Workflows Research

## Overview
GitHub Agentic Workflows (GH-AW) is a new framework developed by GitHub and Microsoft that allows running AI coding agents (like Copilot, Claude, Gemini, or Codex) directly within GitHub Actions. It uses natural language markdown files to define automation tasks, which are then compiled into hardened GitHub Actions YAML workflows.

## Key Features
- **Automated Markdown Workflows**: Write automation in markdown instead of complex YAML.
- **AI-Powered Decision Making**: Agents can understand context and adapt to situations.
- **Deep GitHub Integration**: Works with Actions, Issues, PRs, Discussions, and repository management.
- **Safety First**: Sandboxed execution with minimal permissions and safe output processing.
- **Multi-Agent Support**: Support for various AI engines.

## Core Commands (gh aw extension)
- `gh aw init`: Set up your repository for agentic workflows.
- `gh aw add-wizard`: Add workflows with interactive guided setup.
- `gh aw compile`: Convert markdown to GitHub Actions YAML.
- `gh aw run`: Execute workflows immediately in GitHub Actions.
- `gh aw status`: Check current state of all workflows.

## Implementation Strategy for SIGMA-INDEX
1. **Initialize GH-AW**: Use `gh aw init` to set up the repo.
2. **Define Agentic Tasks**: Create markdown files for tasks like issue triage, data validation, and automated reporting.
3. **Configure Secrets**: Use the provided `GH_TOKEN` and other API keys in the repository secrets.
4. **Schedule Cycles**: Set up scheduled agent cycles using the `agent_cycle.yml` pattern already present in the repo, but enhanced with GH-AW capabilities.
5. **Human-in-the-Loop**: Maintain the PR-based workflow for safety and review.

## Benefits for SIGMA-INDEX
- **100% Free**: Leverages GitHub Actions' free tier for public repositories.
- **Autonomous**: Agents can handle routine tasks without manual intervention.
- **Scalable**: Easy to add new domain agents by creating new markdown files.
