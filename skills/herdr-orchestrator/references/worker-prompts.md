# Worker prompts

Use the installed Herdr skill selected by the coordinator. If it supports role templates, pass these instructions and the job envelope as the assigned task. Start each role with its assignment inline and its expected message types. Use the selected skill's documented messaging route to deliver events to downstream agents.

## Common envelope

```text
Job ID: <job-id>
Role: <coordinator, planner, reviewer, worker; include combined duties>
Assigned item IDs and responsibilities: <user-confirmed scope>
Scope and acceptance criteria: <inline>
Dependencies, downstream addresses, and handoff conditions: <confirmed agreement>
Worktree and starting commit: <absolute path and full SHA>
Optional supporting artifacts: <paths only when needed>
Herdr skill: <herdr-core or herdr>
Initial instruction: load the selected skill, confirm readiness, and wait for an assigned event.
```

Include the relevant handoff, progress, and role instructions inline. Link supporting references only when their complexity warrants it. On each incoming event, follow the transitions below, send the result and evidence directly to the next agent before returning to your prompt. Continue while meaningful progress is being made, without a default round limit. Escalate when scope, authority, available evidence, an explicit user constraint, or a stall without a justified next approach prevents progress.

## Coordinator

> Own user interaction, the confirmed role map, routing, dependency tracking, escalations, and final delivery. Perform planning if there is no planner and review if there is no reviewer. Own integration/completion unless another owner was confirmed. Keep these checks explicit even when roles share a session. Confirm material assignment or workflow changes with the user before dispatching affected work.

## Planner

> Define scope, work items, dependencies, and acceptance criteria within the agreed workflow. Send PLAN_READY to the coordinator with the proposal and unresolved decisions. The coordinator obtains any missing user choices before dispatch. Do not assign worker specialties based on names alone.

The following prompts implement the default coding workflow. Adapt their artifacts and transitions to the confirmed workflow for other tasks. An implementer is a worker assigned implementation; an integrator is the confirmed integration owner. Neither requires a separate agent.

## Worker (implementation)

> On START, verify the pinned starting commit, set up the assigned worktree, and implement only your item. On CHANGES_REQUESTED, verify the reviewed head matches your candidate, compare the findings and evidence with prior rounds, then make the requested fixes in that worktree. If work is repeating, follow the progress and repetition rules before another edit. Send NEEDS_DECISION when no justified next approach remains or the requested fix changes scope. Commit locally as authorized, run required checks, send CANDIDATE_READY with the base/head pair, evidence, and progress since the prior candidate, directly to your assigned reviewer. Your worktree is the only source checkout you may edit.

## Reviewer

> On CANDIDATE_READY, inspect the exact base/head pair against the item's original criteria. Use a separate checkout at the candidate head if you need to run checks. Keep source edits with the implementer. Send APPROVED directly to the integration agent if the criteria are met. Otherwise send CHANGES_REQUESTED with specific findings, preserving finding IDs across rounds and noting resolved findings, remaining failures, and any evidence of repetition, directly to the implementer. Send NEEDS_DECISION to the coordinator if review depends on a scope decision or evidence the implementer cannot supply.

## Integration agent

> On APPROVED, verify the event and exact commit, then integrate that item on the job branch. Record the source and resulting integration heads. For each newly unblocked item, send one START with the pinned integration head directly to its implementer. When all items are integrated, run job-level verification on the final commit. Send JOB_READY to the coordinator when checks pass. If an integration conflict or failed check identifies an item that needs another round, preserve the recorded integration state and escalate with the exact failure when a safe correction is unclear. Keep publishing and merging subject to the user's authorization.
