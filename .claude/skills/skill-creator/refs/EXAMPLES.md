# Skill Examples

Reference examples of well-structured skills.

**Note**: All skills are created in the **project** `skills/` directory (e.g., `<project-root>/skills/<skill-name>/`).

## Simple Shell Skill

A skill that wraps a shell command:

```
<project-root>/skills/git-summary/
├── SKILL.md
└── scripts/
    └── summary.sh
```

**SKILL.md:**
```yaml
---
name: git-summary
description: Generate git repository summary with recent commits, contributors, and file stats. Use when user asks for repo overview or git statistics.
---

# Git Summary

Generates a summary of a git repository.

## Usage

```bash
skills/git-summary/scripts/summary.sh [path]
```

## Examples

```bash
skills/git-summary/scripts/summary.sh .
skills/git-summary/scripts/summary.sh /path/to/repo
```
```

**scripts/summary.sh:**
```bash
#!/bin/bash
REPO="${1:-.}"
cd "$REPO"
echo "=== Recent Commits ==="
git log --oneline -10
echo ""
echo "=== Contributors ==="
git shortlog -sn --all | head -10
echo ""
echo "=== File Stats ==="
git ls-files | wc -l
```

## Python Skill with Dependencies

A skill that requires Python packages:

```
<project-root>/skills/data-analyzer/
├── SKILL.md
├── pyproject.toml
└── scripts/
    ├── setup.sh
    └── analyze.py
```

**pyproject.toml:**
```toml
[project]
name = "data-analyzer"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "pandas",
    "numpy",
]
```

**scripts/setup.sh:**
```bash
#!/bin/bash
set -e
cd "$(dirname "$0")/.."
uv sync
echo "Setup complete!"
```

**SKILL.md:**
```yaml
---
name: data-analyzer
description: Analyze CSV and JSON data files with pandas. Use when user wants to analyze data, get statistics, or process tabular data.
---

# Data Analyzer

Analyze data files using pandas.

## Requirements

- `uv` package manager

## Setup

```bash
skills/data-analyzer/scripts/setup.sh
```

## Usage

```bash
cd skills/data-analyzer && uv run python scripts/analyze.py <file>
```
```

## Read-Only Skill

A skill restricted to read-only tools:

```yaml
---
name: code-explainer
description: Explain code structure and logic. Use when user asks what code does or how it works.
allowed-tools: Read, Grep, Glob
---

# Code Explainer

Explains code without modifying it.

## Approach

1. Use Glob to find relevant files
2. Use Grep to locate specific patterns
3. Use Read to examine code
4. Explain in plain language
```

## Multi-File Skill with References

A complex skill with progressive disclosure:

```
<project-root>/skills/api-client/
├── SKILL.md
├── refs/
│   ├── AUTH.md
│   ├── ENDPOINTS.md
│   └── ERRORS.md
└── scripts/
    └── client.py
```

**SKILL.md:**
```yaml
---
name: api-client
description: Interact with the FooBar API. Use when user needs to call FooBar endpoints, authenticate, or handle API responses.
---

# FooBar API Client

Interacts with the FooBar API.

## Quick Start

```bash
cd skills/api-client && uv run python scripts/client.py get /users
```

## Authentication

See [AUTH.md](refs/AUTH.md) for authentication setup.

## Available Endpoints

See [ENDPOINTS.md](refs/ENDPOINTS.md) for full API reference.

## Error Handling

See [ERRORS.md](refs/ERRORS.md) for error codes and troubleshooting.
```

This structure keeps SKILL.md lean while providing detailed docs when needed.
