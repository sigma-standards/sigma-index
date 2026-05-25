# SIGMA Observability & Monitoring

**Status:** Production  
**Version:** 1.0  

---

## Metrics & KPIs

### Data Quality Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| Duplicate sigma_id count | 0 | Data integrity |
| Malformed URL % | 0% | Source health |
| Missing required fields % | 0% | Schema compliance |
| Unique domains represented | 40/40 | Coverage |
| Average relationship confidence | ≥ 0.85 | Quality |

### Operational Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| CI success rate | ≥ 99% | Pipeline health |
| Test coverage | ≥ 80% | Code quality |
| Agent execution time | < 5m avg | Performance |
| PR review latency | < 24h median | Process speed |
| Release frequency | Weekly | Velocity |

### Research Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| Research tasks completed | 60/60 | Project status |
| Standards ingested per week | ≥ 50 | Ingestion rate |
| New domains identified | Progressive | Scope expansion |
| Source coverage breadth | 40 domains | Completeness |

---

## Dashboards

### Release Dashboard

Located in `docs/OPERATOR_DASHBOARD.md`:

- Latest release tag
- Standards count by domain
- Relationship graph stats
- Quality gate status
- Last ingestion timestamp

### CI/CD Dashboard

GitHub Actions Status:
- All workflow runs
- Success/failure rates
- Average execution time
- Failed job details

### Data Health Dashboard

Located in `data/reports/`:

- `domain_coverage.csv` - Standards per domain
- `quality_gate.csv` - Quality metrics
- `relationship_quality.csv` - Confidence scores
- `url_health_report.csv` - Broken link detection
- `project_progress.csv` - Phase completion

---

## Alerting

### High Priority Alerts

🔴 **Critical Failure**
- Any quality gate failure
- Release build timeout
- Schema validation failure
- Duplicate ID detection

### Medium Priority Alerts

🟠 **Warnings**
- Test coverage drop < 80%
- CI success rate < 95%
- PR review latency > 48h
- Broken URL detected

### Low Priority Alerts

🟡 **Informational**
- Research task completed
- New domain identified
- Weekly statistics summary
- Dependency update available

---

## Log Aggregation

### Agent Memory System

Location: `docs/agent-memory/`

Each agent maintains:
- Execution history
- Task status
- Error logs
- Decision rationale

### GitHub Audit Log

Visible at: `Settings → Audit log`

Includes:
- All PR reviews and merges
- Branch protection changes
- Secrets access
- Workflow executions

---

## Performance Monitoring

### Build Performance

Track in CI logs:
- Checkout time
- Dependency installation time
- Validation time
- Release artifact generation time
- Total CI duration

### Runtime Performance

Agent execution metrics:
- Average per-agent duration
- Total workflow duration
- Timeout incidents
- Retry count

---

## Health Checks

### Weekly Health Report

Run manually:
```bash
make health-check
```

Generates report with:
- ✅ Passing checks
- ⚠️ Degraded services
- ❌ Failed components
- 📊 Trending metrics

### Monthly Compliance Audit

Run governance auditor agent:
```bash
gh aw run .github/agentic/governance-auditor.md
```

Reports on:
- Branch protection compliance
- Secret hygiene
- Workflow security
- Permission configuration

---

## Debugging

### Enable Verbose Logging

```bash
export DEBUG=1
make validate
```

### Inspect Agent Execution

View workflow logs:
```bash
gh run list --workflow=agent_cycle.yml --limit 5
gh run view <run-id>
```

### Local Testing

```bash
.venv/bin/pytest -vv tests/test_*
```

---

## Escalation Path

Issue severity determines escalation:

| Severity | Response Time | Escalation |
|----------|---------------|-----------|
| Critical | Immediate | All maintainers |
| High | 4 hours | Lead maintainer |
| Medium | 24 hours | Triage team |
| Low | 1 week | Backlog |
