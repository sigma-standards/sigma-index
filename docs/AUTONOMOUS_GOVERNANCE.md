# SIGMA Autonomous Governance Framework

**Status:** Production-Ready  
**Version:** 2.0  
**Last Updated:** 2026-05-25  

---

## Prime Directive

All autonomous agents operating on SIGMA must adhere to these principles:

1. **Deterministic Execution** - Same inputs always produce identical outputs
2. **Human-Governed Approvals** - Humans retain final authority on releases
3. **Schema Integrity** - All data adheres to strict validation rules
4. **Reproducibility** - All operations can be verified and replayed
5. **Auditability** - Complete action logs for compliance and review
6. **Safe Automation** - Default to most restrictive permissions
7. **Open Infrastructure** - Public repository, transparent operations
8. **Transparent Provenance** - All data sources and derivations documented
9. **Zero Destructive Automation** - No automatic deletions or overwrites
10. **Production Reliability** - All changes pass deterministic gates

---

## Autonomous Constraints

### What Agents CAN Do

✅ Create PRs with proposed changes  
✅ Comment with analysis and recommendations  
✅ Apply labels and triage issues  
✅ Generate reports and metrics  
✅ Validate data against schemas  
✅ Suggest improvements  
✅ Run tests and CI checks  

### What Agents CANNOT Do

❌ Merge to main automatically  
❌ Modify GitHub secrets  
❌ Change repository permissions  
❌ Deploy to production infrastructure  
❌ Delete issues or PRs  
❌ Force push to any branch  
❌ Execute destructive operations  

### What Requires Human Approval

🔒 Release tagging (v1.x.x)  
🔒 Schema modifications  
🔒 Deleting standards records  
🔒 Workflow permission changes  
🔒 Branch protection changes  
🔒 Pages deployment config changes  

---

## Quality Gates

All changes must pass these gates before advancing:

### Gate 1: Schema Validation
```bash
.venv/bin/python scripts/validate_schema.py
```
- Every field matches schema
- All required fields present
- Type validation passes

### Gate 2: Relationship Integrity
```bash
.venv/bin/python scripts/validate_relationships.py
```
- Relationships are logically consistent
- No circular dependencies
- Relationship confidence scores valid

### Gate 3: Uniqueness Check
```bash
.venv/bin/python scripts/check_duplicate_ids.py
```
- Zero duplicate sigma_id values
- All URLs are unique
- No orphaned records

### Gate 4: URL Health
```bash
.venv/bin/python scripts/check_urls.py
```
- All URLs return 2xx or 3xx status
- No broken references
- Redirects are followed

### Gate 5: Test Suite
```bash
.venv/bin/pytest -q tests/
```
- All unit tests pass
- Integration tests pass
- Coverage ≥ 80%

### Gate 6: Release Build
```bash
make release
```
- All artifacts generated
- Checksums correct
- Metadata complete

### Gate 7: Pages Deployment
```bash
make pagefind-search
```
- Search index generates
- All links resolve
- Documentation builds

---

## Approval Workflow

```
Agent Creates PR
    ↓
Automated CI Runs
    ↓
All Gates Pass?
    ├─ No  → Fix Required → Rerun CI
    └─ Yes → Ready for Review
    ↓
Human Reviews
    ├─ Approve → Can Merge
    ├─ Request Changes → Agent Fixes
    └─ Dismiss → PR Closed
    ↓
Human Merges to main
    ↓
Release Automation Triggers
    ↓
Publish to GitHub Pages
```

---

## Incident Response

If an agent detects an issue:

1. **Immediate Actions**
   - Create detailed Issue
   - Stop related workflows
   - Notify maintainers

2. **Investigation**
   - Reproduce issue deterministically
   - Document root cause
   - Propose fix

3. **Resolution**
   - Implement fix with tests
   - Verify all gates pass
   - Create PR for review

4. **Post-Incident**
   - Document findings
   - Update procedures
   - Improve detection

---

## Observability

Every agent action is logged with:

- Timestamp (ISO 8601)
- Agent identifier
- Action type
- Input data hash
- Output data hash
- Result (success/failure)
- Duration (ms)
- Error details (if any)

Logs available at:
```
docs/agent-memory/
```

---

## Compliance

This framework complies with:

- ✅ CC BY 4.0 License requirements
- ✅ Data integrity best practices
- ✅ Open science principles
- ✅ GitHub platform guidelines
- ✅ Humanitarian data standards
