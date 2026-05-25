# SIGMA Sandbox Setup Guide

**Quick Start for Local Development**

---

## Option 1: Using DevContainer (Recommended)

### Requirements
- Docker or Docker Desktop
- VS Code with Remote - Containers extension

### Setup Steps

1. **Clone repository**
   ```bash
   git clone https://github.com/sigma-standards/sigma-index.git
   cd sigma-index
   ```

2. **Open in VS Code**
   ```bash
   code .
   ```

3. **Open in container**
   - VS Code will prompt: "Reopen in Container"
   - Click "Reopen in Container"
   - Wait for container build and post-create script

4. **Verify setup**
   ```bash
   make validate
   pytest -q
   ```

---

## Option 2: Local Setup (Manual)

### Requirements
- Python 3.11+
- Node.js 18+
- Make
- git

### Setup Steps

1. **Clone repository**
   ```bash
   git clone https://github.com/sigma-standards/sigma-index.git
   cd sigma-index
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install requests beautifulsoup4 SPARQLWrapper pandas openpyxl pyarrow lxml pytest
   npm install -g pagefind
   ```

4. **Configure git**
   ```bash
   git config user.email "your.email@example.com"
   git config user.name "Your Name"
   ```

5. **Install GH CLI (optional)**
   ```bash
   # macOS
   brew install gh
   
   # Ubuntu/Debian
   sudo apt-get install gh
   ```

6. **Authenticate GitHub**
   ```bash
   gh auth login
   ```

---

## Verify Setup

Run these commands to verify everything works:

```bash
# Validate schema
python3 scripts/validate_schema.py

# Validate relationships
python3 scripts/validate_relationships.py

# Check duplicate IDs
python3 scripts/check_duplicate_ids.py

# Run test suite
pytest -q tests/

# Try a make command
make validate
```

---

## Common Tasks

### Running Validation Gates

```bash
# Run all gates
make validate

# Individual gates
python3 scripts/validate_schema.py
python3 scripts/validate_relationships.py
python3 scripts/check_urls.py
```

### Building Release

```bash
make release
```

Output in: `dist/`

### Building Static Site

```bash
python3 scripts/build_static_site.py
npx pagefind --site public/
```

Output in: `public/`

### Running Tests

```bash
# All tests
pytest -q

# Specific test
pytest tests/test_validate_schema.py -v

# With coverage
pytest --cov=scripts tests/
```

### Working with Git

```bash
# Create feature branch
git checkout -b feature/your-feature

# Stage changes
git add .

# Commit
git commit -m "feat: your feature description"

# Create PR (using gh CLI)
gh pr create --title "Your PR Title" --body "Description"
```

---

## Using Autonomous Agents

### Compile GH-AW Workflows

```bash
gh aw compile
```

### Run Agent Locally

```bash
gh aw run .github/agentic/pr-reviewer.md
```

### View Agent Logs

```bash
gh run list --workflow=agent_cycle.yml
gh run view <run-id> --log
```

---

## Troubleshooting

### Python Import Errors

```bash
# Reinstall dependencies
pip install --force-reinstall -r <(pip freeze)
```

### Validation Failures

1. Check output for specific errors
2. Review data in `data/processed/`
3. Check `data/reports/` for diagnostics
4. Run individual validation scripts

### Git Issues

```bash
# Update local from remote
git fetch origin
git rebase origin/main

# Check status
git status --short --branch
```

### Container Issues

```bash
# Rebuild container
# In VS Code: Click ">" → "Dev Containers: Rebuild Container"
```

---

## Next Steps

1. **Understand the project**
   - Read `README.md`
   - Review `MVP_SIGMA-INDEX.md`
   - Check `docs/PROJECT_KNOWLEDGE_GRAPH.md`

2. **Run existing workflows**
   - Try `make validate`
   - Try `pytest tests/test_*.py -v`

3. **Make a change**
   - Create feature branch
   - Make changes
   - Run validation
   - Create PR

4. **Learn about agents**
   - Read `.github/agentic/AGENTS.md`
   - Review governance framework

---

## Support

- 📖 Documentation: `docs/`
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 🔒 Security: See `docs/SECURITY_POLICY.md`
