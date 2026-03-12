#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

cd "$SKILL_DIR"

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "Error: 'uv' is not installed."
    echo ""
    echo "Install uv using one of these methods:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "  or: pip install uv"
    echo "  or: brew install uv (macOS)"
    echo ""
    echo "See: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

echo "Installing dependencies with uv..."
uv sync

echo ""
echo "Installing Chromium browser only (playwright)..."
uv run python -m playwright install chromium --with-deps

echo ""
echo "Verifying installation..."
uv run crawl4ai-doctor

echo ""
echo "Setup complete!"
echo ""
echo "To crawl a URL:"
echo "  cd $SKILL_DIR && uv run python scripts/crawl.py \"https://example.com\""
echo "  or: cd $SKILL_DIR && uv run crawl \"https://example.com\""
