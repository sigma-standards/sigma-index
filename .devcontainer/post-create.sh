#!/bin/bash
set -e

echo "🔧 Setting up SIGMA Global Standards Index development environment..."

# Update package list
apt-get update -qq

# Install required system tools
apt-get install -y --no-install-recommends \
  make \
  curl \
  wget \
  jq \
  zip \
  unzip \
  git-extras \
  build-essential

# Python setup
python3 -m venv /home/vscode/.venv
source /home/vscode/.venv/bin/activate

# Install Python dependencies
pip install --upgrade pip setuptools wheel
if [ -f "pyproject.toml" ]; then
  pip install -e .
fi
pip install -q pytest pytest-cov black flake8 pylint

# GitHub CLI extensions (if gh is available)
if command -v gh &> /dev/null; then
  echo "📦 Installing GitHub CLI extensions..."
  gh extension install github/gh-aw || true
fi

# Create local git hooks for safety
mkdir -p .git/hooks
cat > .git/hooks/pre-commit << 'HOOK'
#!/bin/bash
# Prevent committing secrets
if git diff --cached | grep -iE 'token|secret|key|password|api_key'; then
  echo "⚠️  ERROR: Possible secret detected in staged changes!"
  echo "   Check your changes before committing."
  exit 1
fi
exit 0
HOOK
chmod +x .git/hooks/pre-commit

# Print summary
echo ""
echo "✅ Development environment ready!"
echo ""
echo "Quick start:"
echo "  source ~/.venv/bin/activate        # Activate Python virtual environment"
echo "  make validate                      # Run validation checks"
echo "  make help                          # See available Makefile targets"
echo ""
echo "Important files:"
echo "  AGENTS.md                          # Agent guidelines"
echo "  MVP_SIGMA-INDEX.md                 # Agent execution blueprint"
echo "  CONTRIBUTING.md                    # Contribution guide"
echo "  docs/GITHUB_AGENTIC_SETUP_GUIDE.md # GH-AW configuration"
echo ""
