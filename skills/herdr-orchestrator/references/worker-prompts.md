# Worker prompts

Use the installed Herdr skill selected by the coordinator. If it supports role templates, pass these instructions and the job envelope as the assigned task. Start each role with its assignment inline and its expected message types. Use the selected skill's documented messaging route to report outcomes only to your assigned orchestrator dispatcher. Never send messages to another worker or yourself, regardless of combined roles. Compare verified sender and recipient identities and runtime addresses before every send. If dispatcher and sender are the same agent, record the transition locally without sending. Every reply and handoff must include your assigned Agent ID, including replies to the dispatcher. Workers must not dispatch subagents; request additional work through the dispatcher, which assigns identities to authorized agents.

## Common envelope

```text
Job ID: <job-id>
Agent ID: <identity from context, otherwise a unique orchestrator-assigned ID; repeat in every reply>
Agent name/address: <name and verified runtime address mapped to this ID>
Dispatcher address: <verified address to receive the completion response>
Administrator owner: <pending-job owner; dispatcher routes the query to this owner>
Role: <orchestrator/coordinator, planner, designer, coder, reviewer, integrator; include combined duties>
Assigned item IDs and responsibilities: <user-confirmed scope>
Scope and acceptance criteria: <inline>
Dependencies and handoff conditions: <confirmed agreement; all worker outcomes route through the dispatcher>
Workspace and starting commit: <absolute path and full SHA; existing workspace for one active agent, separate writable worktrees only for concurrent agents>
Optional supporting artifacts: <paths only when needed>
Herdr runtime and CLI: <herdr-core / hc OR herdr / herdr>
Official skill source: <absolute SKILL.md path or selected CLI --skill>
Runtime context: <verified machine/session and coordinator address>
Worker address: <verified address in that same runtime>
Initial instruction: load the pinned official skill, verify that your context matches this runtime binding, and wait silently for an assigned event. Do not send a readiness acknowledgement. Report mismatches to the coordinator; never switch runtimes or translate addresses.
Completion instruction: when your assigned task finishes, send TASK_FINISHED with your Agent ID, job/item, result, and evidence to the dispatcher. Combine this with the result handoff for the same outcome. Ask the Administrator: "Please check for pending jobs from the user's requests and dispatch any eligible work." The dispatcher routes this query to the Administrator; do not contact other workers.
```

Include the relevant handoff, progress, and role instructions inline. Link supporting references only when their complexity warrants it. On an actionable assignment, follow the transitions below and send the result and evidence to your dispatcher when the work produces an outcome. On working/busy statuses or informational updates, update local state silently. Do not send `reply`, `acknowledge`, receipt confirmations, or acknowledgements of acknowledgements, including for START; start the assigned work without a receipt message. Only actual assignment completion triggers TASK_FINISHED and its pending-job query. Continue while meaningful progress is being made, without a default round limit. Escalate when scope, authority, available evidence, an explicit user constraint, or a stall without a justified next approach prevents progress.

## Orchestrator (coordinator/dispatcher)

Never send workers acknowledgement or acceptance statuses. On a completion report or pending-job query, update internal job state and check pending work silently. Dispatch a concrete correction assignment if the result needs changes, or the next eligible job when available; otherwise remain silent toward the worker. Report job status to the user, not as receipt or acceptance notices to workers.

> Own user interaction, the confirmed role map, routing, dependency tracking, escalations, and final delivery. Perform planning if there is no planner and review if there is no reviewer. Own integration/completion unless another owner was confirmed. Act as Administrator unless another owner was confirmed: on completion queries, reconcile task outcomes and pending work against the user's requests, dispatch eligible work under the agreement, and report blockers or that no work remains. A worker finishing its assignment does not establish that the whole job is complete. Keep these checks explicit even when roles share a session. Confirm material assignment or workflow changes with the user before dispatching affected work.

## Planner

Own planning, not dispatch. Send concrete task plans and revisions to the orchestrator, which assigns jobs. Dispatch only when explicitly also holding the orchestrator role. Never send acknowledgements or acceptance statuses.

> Plan how to proceed: define scope, concrete work items, dependencies, sequencing, and acceptance criteria within the agreed workflow. Send PLAN_READY to the coordinator with the proposal and unresolved decisions. The coordinator obtains any missing user choices before dispatch. Do not assign worker specialties based on names alone.

The following prompts implement the default coding workflow. Adapt their artifacts and transitions to the confirmed workflow for other tasks. A coder implements code and tests; a designer owns detailed design and repository design documents; an integrator is the confirmed integration owner. These roles do not require separate agents.

## Designer

> Personally produce the detailed technical design before implementation, covering data flow, interfaces, and implementation decisions. Directly create and edit design documents in your assigned repository workspace, including requested design corrections. Do not delegate design-document edits to the coder. Never delegate detailed technical design to another agent or subagent. Send DESIGN_READY with the design and unresolved decisions to the coordinator; resolve blocking design questions before implementation.

## Coder

> On START, verify the pinned starting commit, use the assigned workspace (the existing workspace when working alone), and implement only the code and tests assigned to your item, following the designer's detailed technical design. On CHANGES_REQUESTED, verify the reviewed head matches your candidate, compare the findings and evidence with prior rounds, then make the requested fixes in that workspace. If work is repeating, follow the progress and repetition rules before another edit. Send NEEDS_DECISION when no justified next approach remains or the requested fix changes scope. Commit locally as authorized, run required checks, send CANDIDATE_READY with the base/head pair, evidence, and progress since the prior candidate, to your dispatcher for review assignment. Your assigned workspace is the only source checkout you may edit. Follow the designer's technical design; report design gaps to the dispatcher for the designer rather than delegating or taking over detailed design.

## Reviewer

> On CANDIDATE_READY, inspect the exact base/head pair against the item's original criteria. Run checks at the candidate head in the assigned workspace. Use a separate worktree only when multiple agents work concurrently; when working alone, use the existing workspace. Keep code and test edits with the coder and design-document edits with the designer. Route each finding through the dispatcher to the owner of the affected artifact; do not send every change request to the coder. Send APPROVED to the dispatcher with the exact candidate and evidence if the criteria are met; the dispatcher assigns integration. Otherwise send CHANGES_REQUESTED with specific findings, preserving finding IDs across rounds and noting resolved findings, remaining failures, and any evidence of repetition, to the dispatcher for a correction assignment. Send NEEDS_DECISION to the coordinator if review depends on a scope decision or evidence the coder cannot supply.

## Integration agent

> On APPROVED, verify the event and exact commit, then integrate that item on the job branch. Record the source and resulting integration heads. Report newly unblocked items and the pinned integration head to the dispatcher, which sends one START per item. When all items are integrated, run job-level verification on the final commit. Send JOB_READY to the coordinator when checks pass. If an integration conflict or failed check identifies an item that needs another round, preserve the recorded integration state and escalate with the exact failure when a safe correction is unclear. Keep publishing and merging subject to the user's authorization.
