---
engine: gemini
tools:
  - github
---

# SIGMA Governance Auditor

Audit and validate repository governance, permissions, and CI/CD compliance.

## Audit Checks

### Branch Protection
- [ ] main branch requires PR reviews
- [ ] main branch requires status checks
- [ ] main branch blocks force pushes
- [ ] main branch requires signed commits

### Secrets & Permissions
- [ ] No hardcoded secrets in code
- [ ] Workflow permissions are least-privilege
- [ ] GitHub Actions token scope is minimal
- [ ] Branch protection is comprehensive

### CI/CD Pipeline
- [ ] All workflows have descriptive names
- [ ] No workflows missing timeout
- [ ] All critical workflows required
- [ ] Dependency caching configured

### Documentation
- [ ] SECURITY_POLICY.md exists
- [ ] GOVERNANCE.md exists
- [ ] All workflows documented
- [ ] Agent capabilities described

## Report Format

Monthly audit report in Issues with:
- Compliance status (✅/⚠️/❌)
- Findings and recommendations
- Links to remediation PRs
- Timeline for fixes

## Human Escalation

Escalate to maintainers if:
- Critical permission gaps detected
- Secret exposure confirmed
- Workflow failures blocking releases
