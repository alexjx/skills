---
name: agent-harness
description: Framework for orchestrating multiple AI agent sessions to complete complex, long-running software projects. Use when the user wants to set up or use the long-running agent harness pattern for managing multi-session projects, breaking work into discrete sessions with persistent state tracking, or implementing incremental progress workflows across multiple Claude Code sessions.
---

# Long-Running Agent Harness

Framework for completing complex projects across multiple Claude Code sessions.

## Overview

The harness solves the **context window limitation** by breaking work into discrete sessions where each agent:

1. Starts with a fresh context
2. Reads the current state from files
3. Makes incremental progress on ONE feature
4. Documents everything for the next agent

This is based on Anthropic's research on effective agent harnesses.

## When to Use This Skill

Use this skill when:
- A project is too large for a single Claude Code session
- You want to work incrementally across multiple sessions
- Multiple agents (or you over multiple days) need to collaborate on one codebase
- You need persistent progress tracking that survives context window limits

## Architecture

```
Initializer Agent (First Session)
       │
       ▼
Creates harness files:
├── init.sh              → Environment setup script
├── feature_list.json    → Requirements (all failing)
├── claude-progress.txt  → Handoff log
└── Git repo
       │
       ▼
Coding Agent Session 1 ──▶ Coding Agent Session 2 ──▶ ... ──▶ Coding Agent Session N
```

## Setup

### Step 1: Initialize the Harness

Copy the harness files to your project:

```bash
cp -r ~/.claude/skills/agent-harness/assets/* ./my-project/
cd my-project
chmod +x init.sh
```

### Step 2: Define Features

Edit `feature_list.json` with your actual requirements:

```json
{
  "project_name": "My Web App",
  "features": [
    {
      "id": "feat-001",
      "category": "infrastructure",
      "description": "Project setup and dev server",
      "steps": ["Create package.json", "Set up dev server", "Verify hot reload"],
      "passes": false
    },
    {
      "id": "feat-002",
      "category": "authentication",
      "description": "User login with email/password",
      "steps": ["Create login form", "Add validation", "Test E2E"],
      "passes": false
    }
  ]
}
```

**CRITICAL**: Set ALL `passes` to `false` initially. This prevents agents from declaring victory too early.

### Step 3: Customize init.sh

Edit `init.sh` for your project:

```bash
# Add your setup commands
npm install
npm run dev &
sleep 3
curl -s http://localhost:3000/health || echo "WARNING: Health check failed"
```

## The Agent Loop

Every session follows this exact pattern:

```bash
# 1. Get bearings
./init.sh                    # Set up environment
read feature_list.json       # See current progress
read claude-progress.txt     # Get context from last session
git log --oneline -20        # Understand recent changes

# 2. Verify state
# - Start dev server
# - Run existing tests
# - Check for regressions

# 3. Select ONE feature
# - Read feature_list.json
# - Pick highest-priority incomplete feature

# 4. Implement
# - Make focused changes
# - Test thoroughly (like a human user)
# - Commit frequently

# 5. Complete and handoff
# - Update feature_list.json (set passes: true)
# - Append to claude-progress.txt
# - Final descriptive commit
```

## Feature Categories (Priority Order)

| Category | Description | Priority |
|----------|-------------|----------|
| `infrastructure` | Setup, config, tooling | 0 - Do first |
| `core` | Essential functionality | 1 |
| `feature` | User-facing features | 2 |
| `polish` | UI/UX improvements | 3 - Do last |

## Rules

1. **Work on ONLY ONE feature at a time**
2. **It is UNACCEPTABLE to remove or edit tests**
3. **Set ALL features to passes: false initially**
4. **Test like a human user** (not just unit tests)
5. **Leave code in a clean, mergeable state**
6. **Use JSON for structured data** (not markdown)
7. **Write descriptive commit messages**

## File Reference

### feature_list.json

Source of truth for requirements and progress:

```json
{
  "id": "feat-001",
  "category": "authentication",
  "description": "User login",
  "steps": ["Step 1", "Step 2"],
  "passes": false,
  "notes": ""
}
```

- `id`: Unique identifier
- `category`: infrastructure | core | feature | polish
- `passes`: Boolean - ONLY set to true after thorough testing
- `notes`: Context for next agent

### claude-progress.txt

Human-readable handoff log. Append at end of each session:

```
Session: 2024-03-05T10:00:00
Worked on: feat-001
Changes: Created LoginForm component
Issues: None
State: Ready for next feature
```

### init.sh

Idempotent setup script. Must be safe to run multiple times.

## Helper Commands

The `harness.py` script provides convenience commands:

```bash
python harness.py init                 # Initialize harness files
python harness.py status               # Show completion progress
python harness.py next                 # Suggest next feature
python harness.py complete ID "notes"  # Mark feature done
python harness.py session              # Run full workflow
```

## Recovery

If something goes wrong:

```bash
# Revert to last known good state
git log --oneline -20
git reset --hard <good-commit>

# Update feature_list.json to reflect current reality
# (set passes: false for features that need rework)
```

## Assets

This skill includes template files in `assets/`:

- `init.sh` - Setup script template
- `feature_list.json` - Feature list template
- `claude-progress.txt` - Progress log template
- `harness.py` - Helper CLI script

Copy these to your project and customize them.
