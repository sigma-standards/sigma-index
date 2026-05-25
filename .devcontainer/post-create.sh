#!/usr/bin/env bash
set -e

echo "=== SIGMA Sandbox Post-Create Setup ==="

# Update system
apt-get update -qq
apt-get install -y -qq make jq nodejs npm

# Create Python virtual environment
python3 -m venv /workspace/.venv
source /workspace/.venv/bin/activate

# Install Python dependencies
pip install --upgrade pip setuptools wheel
pip install -r pyproject.toml 2>/dev/null || \
  pip install requests beautifulsoup4 SPARQLWrapper pandas openpyxl pyarrow lxml pytest

# Install Node.js dependencies for search
npm install -g pagefind

# Initialize git config if needed
git config user.email "sigma-sandbox@local" || true
git config user.name "SIGMA Sandbox Agent" || true

# Run baseline validation
echo "=== Running baseline validation ==="
make validate || echo "⚠️ Validation warnings noted - proceed to fix"

echo "✅ SIGMA sandbox ready!"
