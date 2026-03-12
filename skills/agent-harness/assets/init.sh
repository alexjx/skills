#!/bin/bash
#
# Initialization script for long-running agent sessions.
# Run this at the start of every session to ensure the environment
# is properly configured and the dev server is running.
#

set -e

echo "=== Environment Setup ==="

# 1. Verify we're in the correct directory
echo "Working directory: $(pwd)"

# 2. Check for required files
echo "Checking required files..."
if [ ! -f "feature_list.json" ]; then
    echo "ERROR: feature_list.json not found"
    exit 1
fi

if [ ! -f "claude-progress.txt" ]; then
    echo "WARNING: claude-progress.txt not found, creating..."
    touch claude-progress.txt
fi

# 3. Check git status
echo "Git status:"
git status --short 2>/dev/null || echo "Not a git repository"

# 4. Install dependencies if needed
# (Customize this section for your project)
# if [ -f "package.json" ] && [ ! -d "node_modules" ]; then
#     echo "Installing npm dependencies..."
#     npm install
# fi

# if [ -f "requirements.txt" ]; then
#     echo "Installing Python dependencies..."
#     pip install -r requirements.txt
# fi

# 5. Start development server
# (Customize this section for your project)
# echo "Starting dev server..."
# npm run dev &
# DEV_SERVER_PID=$!
# echo "Dev server PID: $DEV_SERVER_PID"

# 6. Wait for server to be ready
# sleep 3
# curl -s http://localhost:3000/health || echo "WARNING: Health check failed"

echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Read feature_list.json to see current progress"
echo "2. Read claude-progress.txt for context"
echo "3. Pick one incomplete feature to work on"
echo "4. Implement and test thoroughly"
echo "5. Update feature_list.json and claude-progress.txt"
echo "6. Commit your changes"
