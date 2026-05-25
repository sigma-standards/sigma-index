# SIGMA Autonomous Agents

This directory contains GitHub Agentic Workflow definitions for autonomous issue processing, PR review, standards research, and governance.

## Agent Registry

| Agent | File | Responsibility | Trigger |
|-------|------|-----------------|---------|
| Issue Processor | issue-processor.md | Classify, label, triage issues | Issue opened/edited |
| PR Reviewer | pr-reviewer.md | Automated code review | PR opened/synchronized |
| Standards Researcher | standards-researcher.md | Monitor and ingest new standards | Nightly schedule |
| Schema Validator | schema-validator.md | Validate data schema compliance | Every commit |
| Relationship Quality | relationship-quality.md | Score relationship confidence | Release build |
| Governance Auditor | governance-auditor.md | Audit workflows and permissions | Weekly schedule |
| Release Manager | release-manager.md | Manage releases and versioning | Manual trigger |

## Architecture

```
Trigger Event
    ↓
GH-AW Router
    ↓
Select Agent(s)
    ↓
Execute Agent Logic
    ↓
Validation Gate
    ↓
Action (comment, label, PR, etc.)
    ↓
Audit Log
```

## Governance Rules

1. **No Auto-Merge**: Agents never auto-merge to main
2. **Human Gates**: Release actions require human approval
3. **Schema Enforcement**: All data transformations validate schema
4. **Audit Trail**: Every action logged for review
5. **Deterministic Execution**: Same inputs always produce same outputs
6. **Safety First**: Default to most restrictive permissions

## Development

To compile agents:
```bash
gh aw compile
```

To test agent logic locally:
```bash
.venv/bin/python -m pytest tests/test_agent_*.py -v
```
