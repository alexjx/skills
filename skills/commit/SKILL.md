---
name: commit
description: Guide for creating atomic commits with conventional commit format. Use when user wants to commit changes.
---

# Commit Changes

## Process

### 1. Review Changes

Run:
```bash
git status
git diff HEAD
git diff --stat HEAD
```

Check for new untracked files:
```bash
git ls-files --others --exclude-standard
```

### 2. Stage Files

Add only the untracked and changed files that belong in the current commit.

Prefer explicit paths over broad staging. Use `git add <paths>` for the files that
actually belong to the change.

**Do NOT stage:**
- `.env` or credential files
- Large binary files
- Files unrelated to the current task
- Task-tracking, planning, or research files under `tasks/`, `.agents/tasks/`,
  `.agents/plans/`, or `.agents/research/` unless the user explicitly asks to
  commit them

If the only remaining changes are workflow files, stop and confirm before
committing. Do not pull them in automatically.

### 3. Create Commit

Write an atomic commit message with a conventional commit tag:

- `feat:` — New capability or feature
- `fix:` — Bug fix
- `refactor:` — Code restructure without behavior change
- `docs:` — Documentation only
- `test:` — Test additions or fixes
- `chore:` — Build, CI, tooling changes
- `perf:` — Performance improvement

**For monorepo changes spanning multiple packages**, note the primary package in the scope:
```
feat(workflows): add DAG condition evaluator
fix(web): resolve SSE reconnection on navigation
refactor(isolation): simplify worktree resolution order
```

**Commit message format:**
```
tag(scope): concise description of what changed

[Optional body explaining WHY this change was made,
not just what changed. Include context that isn't
obvious from the diff.]

[Optional: Fixes #123, Closes #456]
```
