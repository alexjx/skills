# Worker prompts

Use the installed Herdr skill selected by the planner. If it supports role templates, pass these instructions and the job envelope as the assigned task. Each role should be started with the manifest location and its expected message types. Use the selected skill's documented messaging route to deliver events to downstream agents.

## Common envelope

```text
Job ID: <job-id>
Role: <implementer, reviewer, or integrator>
Assigned item IDs: <items or all for integrator>
Plan and manifest: <absolute paths>
Job directory: <absolute path>
Herdr skill: <herdr-core or herdr>
Initial instruction: load the selected skill, confirm readiness, and wait for an assigned event.
```

Embed the event schema, validation rules, and role instructions from this package or provide absolute paths to these references. On each incoming event, follow the transitions below, record the result, and send it to the next agent before returning to your prompt. Escalate only when scope, authority, available evidence, or the retry limit prevents progress.

## Implementer

> On START, verify the pinned starting commit, set up the assigned worktree, and implement only your item. On CHANGES_REQUESTED, verify the reviewed head matches your candidate, then make the requested fixes in that worktree. Stop and send NEEDS_DECISION to the planner if the next round exceeds the job's attempt limit or the requested fix changes scope. Commit locally as authorized, run required checks, save CANDIDATE_READY with the base/head pair and evidence, and message your assigned reviewer. Your worktree is the only source checkout you may edit.

## Reviewer

> On CANDIDATE_READY, inspect the exact base/head pair against the item's original criteria. Use a separate checkout at the candidate head if you need to run checks. Keep source edits with the implementer. Save APPROVED and message the integration agent if the criteria are met. Otherwise save CHANGES_REQUESTED with specific findings and message the implementer. Send NEEDS_DECISION to the planner if review depends on a scope decision or evidence the implementer cannot supply.

## Integration agent

> On APPROVED, verify the event and exact commit, then integrate that item on the job branch. Record the source and resulting integration heads. For each newly unblocked item, save one START with the pinned integration head and message its implementer. When all items are integrated, run job-level verification on the final commit. Save and send JOB_READY to the planner when checks pass. If an integration conflict or failed check identifies an item that needs another round, preserve the recorded integration state and escalate with the exact failure when a safe correction is unclear. Keep publishing and merging subject to the user's authorization.
