---
name: herdr-orchestrator
description: Set up or resume multi-agent coding jobs in Herdr with direct implementer-to-reviewer handoffs, parallel work items, progress-aware review loops, and a final integration handoff.
---

# Herdr orchestrator

Stay in the user's planner session. Agree on the outcome and acceptance criteria, choose the work graph, and start a job whose workers can advance it by messaging each other. The planner handles scope decisions and receives the final result.

Load the installed `herdr-core` or `herdr` skill by name and read its `SKILL.md`. If both are available, choose the one for the current session or use the user's choice. Use that skill for terminal addressing, startup readiness, direct messaging, and recovery. If neither is available, or the selected backend cannot deliver a prompt to a downstream agent, surface that setup blocker before starting the job.

## Set up the job

1. Establish the approved scope, acceptance criteria, job-level checks, and independently owned work items with explicit dependencies. Keep this inline for simple jobs; use `.agents/plans/<job-id>.md` when the plan is complex or needs to survive sessions.
2. Read [handoff guidance](references/job-schema.md) and [worker prompts](references/worker-prompts.md). Assign an implementer and reviewer per active item, plus one integration agent. A reviewer may cover multiple items if its incoming turns can be serialized. Use separate writable worktrees for concurrent changes.
3. Start and confirm receivers are ready before sending initial work. Send each role its scope, criteria, worktree, expected messages, and downstream addresses inline. Tell idle workers to return to their prompt after setup, then kick off dependency-free items.
4. Workers send results and evidence directly to the next role. Default to concise plain text, without JSON envelopes or handoff files. Use files only for complex content, large artifacts, or necessary recovery checkpoints, with the actionable summary still inline. The integration agent owns the dependency join and final verification. Continue working with the user in the planner session; the integrator reports the final commit or escalates a decision exceeding scope.

For a concrete parallel job and review loop, see [the worked example](references/example-job.md). On explicit resume, reconcile available messages, any checkpoints, and Git state before replaying a missing handoff. Use a replacement worker only after resolving ownership of the prior worker's write access.

Continue implementation and review until the acceptance criteria pass while meaningful progress is being made; do not impose a default round limit. Use the [progress and repetition rules](references/job-schema.md#progress-and-repetition) to detect stalled or cycling work, change approach, and escalate when a decision is needed.
