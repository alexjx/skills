---
name: herdr-orchestrator
description: Set up or resume multi-agent coding jobs in Herdr with direct implementer-to-reviewer handoffs, parallel work items, bounded review rounds, and a final integration handoff.
---

# Herdr orchestrator

Stay in the user's planner session. Agree on the outcome and acceptance criteria, choose the work graph, and start a job whose workers can advance it by messaging each other. The planner handles scope decisions and receives the final result.

Load the installed `herdr-core` or `herdr` skill by name and read its `SKILL.md`. If both are available, choose the one for the current session or use the user's choice. Use that skill for terminal addressing, startup readiness, direct messaging, and recovery. If neither is available, or the selected backend cannot deliver a prompt to a downstream agent, surface that setup blocker before starting the job.

## Set up the job

1. Record the approved scope, acceptance criteria, and job-level checks in `.agents/plans/<job-id>.md`. Divide it into independently owned work items with explicit dependencies.
2. Read [the job schema](references/job-schema.md) and [worker prompts](references/worker-prompts.md). Create the job manifest and worktrees. Assign an implementer and a reviewer per active item, plus one integration agent for the job. A reviewer may cover multiple items if its incoming turns can be serialized. Use separate writable worktrees for concurrent changes.
3. Start and confirm the readiness of receivers before sending initial work. Give each role the manifest, its inbound events, and the addresses of its downstream roles. Tell idle workers to return to their prompt after setup. Publish the complete manifest before kicking off dependency-free items.
4. After kickoff, workers save their results and message the next role directly. The integration agent owns the dependency join and final verification. Continue working with the user in the planner session. The integration agent reports the final commit or escalates a decision that exceeds the approved scope.

For a concrete parallel job and review loop, see [the worked example](references/example-job.md). On explicit resume, reconcile durable reports and route records before replaying a missing handoff. Use a replacement worker only after resolving ownership of the prior worker's write access.
