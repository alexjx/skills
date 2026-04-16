---
name: execute-plan
description: Execute the implementation plan. Use when you have a written plan file to implement.
---

# Execute Plan

## Overview

Load a plan, decompose it into a dependency graph, then execute tasks using parallel subagents where safe to do so. Verify results before declaring completion.

Announce at start: "I'm using the execute-plan skill to implement this plan."

---

## Step 1: Load and Review Plan

1. Read the plan file specified by the user.
2. Review critically — identify ambiguities, missing context, or contradictions.
3. If concerns exist: raise them with the user **before proceeding**.
4. If no concerns: continue to Step 2.

---

## Step 2: Dependency Analysis

Decompose all plan tasks into a dependency tree:

1. List every task from the plan.
2. For each task, identify:
   - **Inputs**: files, modules, or state it requires.
   - **Outputs**: files, modules, or state it produces.
3. Draw edges: task B depends on task A if B requires A's output.
4. Identify **independent groups** — tasks with no shared inputs/outputs and no dependency edges between them.

**Safe to parallelize when:**
- Tasks write to different files/modules with no overlap.
- Tasks don't share mutable state or intermediate outputs.
- Tasks don't depend on each other's outputs.

**Not safe to parallelize when:**
- Any dependency edge exists between the tasks.
- Tasks touch the same file or shared state.
- Ordering is ambiguous or unclear.

If **no safe parallel slice exists**, fall through to sequential execution (Step 4).

---

## Step 3: Parallel Execution (when safe slices exist)

Run at most **2–3 parallel subagents** per wave:

### For each parallel wave:

1. Identify the next group of independent tasks (up to 3).
2. Spawn one subagent per task using whatever subagent mechanism the current environment supports.
3. Prefer a **fast, cost-efficient model** for implementation subagents — check what's available.
4. Each subagent prompt must include:
   - Full task description from the plan.
   - Relevant file paths and context (do not assume subagent has memory).
   - Expected output: specific files changed, functions added, tests written.
   - Any constraints from the original plan.
5. Wait for all agents in the wave to complete before launching the next wave.
6. After each wave: run Step 5 (verify) before continuing.

---

## Step 4: Sequential Execution (fallback)

When no safe parallel slice exists, execute tasks one at a time:

1. Pick the next unblocked task (all dependencies satisfied).
2. Implement it — either directly or via a subagent if available.
3. Verify the result (Step 5) before moving to the next task.
4. Repeat until all tasks complete.

---

## Step 5: Verify Each Wave / Task

After every wave or sequential task, verify before continuing:

```
- Run the project's test suite if available.
- Check that expected output files exist and are non-empty.
- Confirm no regressions in previously passing tests.
- Review subagent output for stated blockers or errors.
```

If verification fails:
- Do **not** continue to the next wave.
- Diagnose the failure.
- Re-run the failing task (or fix it in-context) before proceeding.
- If blocked: stop and ask the user for clarification.

---

## Step 6: Final Verification and Done

After all tasks are complete:

1. Run full test suite / build / lint checks.
2. Confirm every task in the plan is marked complete.
3. Summarize what was done:
   - Number of tasks executed.
   - Which tasks ran in parallel vs. sequential.
   - Any deviations from the plan (with reasons).
4. Only then announce: "Plan execution complete. All tasks verified."

---

## Execution Model Reference

### Subagent Prompt Template

When spawning a subagent, include:

```
## Task
<task description from plan>

## Context
- Files to read: <list>
- Files to create/modify: <list>
- Completed dependencies: <outputs from prior tasks>

## Constraints
<constraints from the plan>

## Expected Output
<deliverables: files, functions, tests>

Implement exactly what is described. Report what changed and any blockers.
```

### Dependency Tree Format (for internal tracking)

Track task state inline:

```
Tasks:
  [A] setup-db-schema         deps=[]          status=done
  [B] implement-user-model    deps=[A]         status=done
  [C] implement-auth-routes   deps=[B]         status=in_progress
  [D] implement-profile-api   deps=[B]         status=in_progress   ← parallel with C
  [E] write-integration-tests deps=[C,D]       status=not_started
```

---

## When to Stop and Ask

Stop immediately and ask the user when:

- A task has a blocker that isn't self-resolvable (missing dependency, broken environment).
- The plan has a critical gap that prevents starting a task.
- Verification fails twice for the same task.
- A subagent reports a conflict or contradiction with the plan.

Do not guess or work around blockers silently.

---

## Constraints

- Maximum **2–3 parallel subagents** per wave. Do not spawn more.
- Prefer **smaller independent tasks** for parallelization over large coupled ones.
- Always verify after each wave — never skip verification to save time.
- Do not parallelize when in doubt — sequential is always safe.
- Never start implementation on `main`/`master` without explicit user consent.
