# SIGMA Security Policy

**Status:** Active  
**Last Reviewed:** 2026-05-25  

---

## Security Principles

1. **Public Data Only** - SIGMA contains only open, non-sensitive data
2. **No Personal Information** - Zero PII storage
3. **No Secrets in Code** - All secrets in GitHub secrets, never in repos
4. **Minimal Permissions** - Least-privilege GitHub Actions tokens
5. **Dependency Monitoring** - Automated security updates via Dependabot
6. **Code Scanning** - CodeQL on every PR and push

---

## Threat Model

### Potential Threats

- **Secret Exposure**: Accidental commit of API keys or tokens
- **Dependency Vulnerabilities**: Compromised packages in supply chain
- **Data Injection**: Malicious data in standards sources
- **Unauthorized Access**: Compromised repository credentials
- **Tampering**: Unauthorized modifications to releases

### Mitigations

| Threat | Mitigation |
|--------|-----------|
| Secret Exposure | Pre-commit hooks, secret scanning, code review |
| Supply Chain Risk | Dependabot updates, lockfile pinning, SCA scanning |
| Data Injection | Schema validation, URL health checks, source verification |
| Unauthorized Access | Branch protection, required reviews, signed commits |
| Tampering | Release signatures, artifact checksums, audit logs |

---

## Security Scanning

### Enabled Tools

| Tool | Purpose | Frequency |
|------|---------|-----------|
| CodeQL | SAST analysis | Every push |
| Dependabot | Dependency updates | Daily |
| Gitleaks | Secret detection | Every push |
| Trivy | Container scanning | Weekly |
| Scorecard | Supply chain | Weekly |

### Configuration

**CodeQL**: Automatic on push/PR  
**Dependabot**: `.github/dependabot.yml`  
**Gitleaks**: Runs in CI workflow  

---

## Secrets Management

### GitHub Secrets (Never Commit)

```
GITHUB_TOKEN (auto-provided)
SLACK_WEBHOOK_URL (if configured)
DISCORD_WEBHOOK_URL (if configured)
```

### No Secrets Used

SIGMA deliberately uses only free, no-authentication APIs:
- ✅ GitHub API (with GITHUB_TOKEN)
- ✅ Wikidata SPARQL
- ✅ Web scraping (public data)
- ✅ ODATA feeds (W3C, IETF, etc.)

---

## Incident Response

### Report Security Issues

**DO NOT** create public GitHub issues for security vulnerabilities.

Instead: Email `sigma-standards@github.com` with:
- Vulnerability description
- Affected components
- Proof of concept (if safe)
- Suggested remediation

### Response Timeline

- **Confirmation**: Within 24 hours
- **Initial Assessment**: Within 48 hours
- **Fix Development**: ASAP (typically 1-2 weeks)
- **Coordinated Disclosure**: Post-patch release

---

## Code Review Checklist

Every PR must check:

- [ ] No secrets committed
- [ ] All tests passing
- [ ] CodeQL findings resolved
- [ ] Dependency updates reviewed
- [ ] No new vulnerabilities introduced

---

## Release Signing

All releases are signed:

```bash
git tag -s v1.0.0 -m "Release v1.0.0"
```

Verify signature:

```bash
git tag -v v1.0.0
```

---

## Compliance

This policy complies with:
- OWASP Top 10
- CWE Top 25
- NIST Cybersecurity Framework
