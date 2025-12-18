#!/bin/bash
# Scaffold a new skill directory structure
# Usage: ./scaffold.sh <skill-name>

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <skill-name>"
    echo "Example: $0 my-new-skill"
    exit 1
fi

SKILL_NAME="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Navigate to project root: scripts/ -> skill-creator/ -> skills/ -> .claude/ -> project-root
PROJECT_ROOT="$(dirname "$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")")"
SKILLS_ROOT="$PROJECT_ROOT/skills"
SKILL_DIR="$SKILLS_ROOT/$SKILL_NAME"

# Validate name
if [[ ! "$SKILL_NAME" =~ ^[a-z0-9-]+$ ]]; then
    echo "Error: Skill name must be lowercase letters, numbers, and hyphens only"
    exit 1
fi

if [[ ${#SKILL_NAME} -gt 64 ]]; then
    echo "Error: Skill name must be 64 characters or less"
    exit 1
fi

if [[ "$SKILL_NAME" == *"anthropic"* || "$SKILL_NAME" == *"claude"* ]]; then
    echo "Error: Skill name cannot contain 'anthropic' or 'claude'"
    exit 1
fi

if [ -d "$SKILL_DIR" ]; then
    echo "Error: Skill '$SKILL_NAME' already exists at $SKILL_DIR"
    exit 1
fi

echo "Creating skill: $SKILL_NAME"
mkdir -p "$SKILL_DIR/scripts"
mkdir -p "$SKILL_DIR/refs"

# Create SKILL.md template
cat > "$SKILL_DIR/SKILL.md" << 'EOF'
---
name: SKILL_NAME_PLACEHOLDER
description: TODO - Describe what this skill does AND when to use it. Include trigger words.
---

# SKILL_NAME_PLACEHOLDER

Brief description of what this skill does.

## Requirements

- List required tools/dependencies

## Setup

```bash
# One-time setup commands (if needed)
```

## Usage

```bash
# How to use this skill
```

## Examples

### Example 1

```bash
# Show a concrete example
```
EOF

# Replace placeholder with actual name
sed -i "s/SKILL_NAME_PLACEHOLDER/$SKILL_NAME/g" "$SKILL_DIR/SKILL.md"

echo "Created:"
echo "  $SKILL_DIR/SKILL.md"
echo "  $SKILL_DIR/scripts/"
echo "  $SKILL_DIR/refs/"
echo ""
echo "Next steps:"
echo "  1. Edit $SKILL_DIR/SKILL.md to add description and instructions"
echo "  2. Add scripts to $SKILL_DIR/scripts/"
echo "  3. Add pyproject.toml if using Python dependencies"
