---
engine: gemini
tools:
  - github
  - web
---

# SIGMA PR Review Agent

Automatically review pull requests for quality, security, and standards compliance.

## Review Scope

- ✓ Schema compliance
- ✓ Data integrity
- ✓ Relationship consistency
- ✓ Performance impact
- ✓ Security risks
- ✓ Documentation updates
- ✓ Test coverage

## Decision Logic

### Schema Violations
- BLOCK if any data field missing required value
- BLOCK if sigma_id not unique
- BLOCK if official_url malformed
- SUGGEST fix if relationship incomplete

### Security Issues
- BLOCK if secrets detected in PR
- WARN if unencrypted sensitive data
- RECOMMEND if dependency outdated

### Quality Gates
- PASS if test coverage ≥ 80%
- PASS if all validation gates pass
- PASS if no duplicate IDs detected

## Output

Comment summary with:
- ✅ Passing checks
- ⚠️ Warnings and suggestions
- ❌ Blocking issues with remediation steps
