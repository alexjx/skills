---
name: herdr-orchestrator
description: Set up or resume multi-agent jobs in Herdr by confirming agent responsibilities, workflow, and handoff conditions with the user; coordinate execution, review, and completion.
---

# Herdr orchestrator

Keep a coordinator responsible for interacting with the user and coordinating the other agents. Roles are responsibilities, not required separate sessions. Confirm their owners and workflow before dispatching work.

Before discovering agents or issuing control commands, resolve the runtime using [backend selection](references/backend-selection.md). `herdr-core` (`hc`) and legacy `herdr` (TUI) are incompatible runtimes, not alternative command spellings. Load only the selected official skill for operations. Use it for terminal addressing, startup readiness, direct messaging, and recovery. If its required skill, CLI, session context, or downstream messaging capability is unavailable, surface that setup blocker before starting the job; never fall back to the other runtime.

## Agree on the team and workflow

On the first run for a job, inspect available agents and existing user instructions. Use agent names and stated context to propose responsibilities; names are hints, not authorization. Present one concise proposal for the user to confirm or correct before starting agents or dispatching work:

- **Coordinator:** user interaction, routing, dependency tracking, blockers, and final delivery.
- **Planner:** scope, decomposition, dependencies, and acceptance criteria. If absent, the coordinator performs these duties.
- **Reviewer:** evaluate outputs against the agreed criteria and request corrections or approve. If absent, the coordinator performs these duties; review is not skipped.
- **Workers:** one or more agents executing explicitly assigned scopes. Ask the user to choose or confirm each worker's responsibility, using names to suggest likely scopes when helpful. Do not silently assign specialties, divide work, or create extra workers.

Include each agent's name/address, role(s), scope, and expected output. Confirm the workflow alongside the role map: stages, dependencies, who hands off to whom, the evidence and conditions required for each transition, correction routes, escalation conditions, and final acceptance checks. Explain that this initial confirmation establishes responsibilities and handoff rules. Existing explicit choices count as confirmation; ask only about unresolved choices. While awaiting confirmation, discovery and proposal preparation may continue, but dependent execution must wait.

For coding jobs, propose the existing implementation → review → integration workflow as the **default**, not a requirement. It provides a clear quality gate on each exact candidate and a single owner for combining concurrent changes and checking the final result. Planning precedes implementation; review findings return to the worker; blockers and final results go to the coordinator. Integration is a responsibility the coordinator covers unless the user confirms another owner, not a required extra agent. Adapt the stages and evidence to other tasks or the user's preferred workflow.

Record the confirmed agreement inline for simple jobs or in `.agents/plans/<job-id>.md` when it needs to survive sessions. On resume, reuse it and reconcile messages, checkpoints, and current artifacts before replaying work. Confirm material changes to responsibilities or handoff rules rather than repeating the whole setup.

## Run the agreed job

1. Read [handoff guidance](references/job-schema.md) and [role prompts](references/worker-prompts.md). Bind logical roles to the confirmed agents, including coordinator fallbacks. For concurrent code changes, use separate writable worktrees.
2. Start and confirm receivers are ready before sending initial work. Send each agent its confirmed scope, criteria, workspace, expected messages, and downstream addresses inline. Tell idle agents to return to their prompt after setup, then kick off dependency-free items.
3. Send results and evidence directly to the next confirmed owner when the agreed handoff conditions are met. Default to concise plain text, without JSON envelopes or handoff files. Use files for complex content, large artifacts, or necessary recovery checkpoints, with the actionable summary still inline. If consecutive roles belong to the same agent, perform the next responsibility locally and record its outcome instead of messaging itself.
4. The coordinator tracks dependencies and communicates with the user. The confirmed integration/completion owner combines accepted outputs and performs final verification, then reports to the coordinator for user delivery. Keep publishing and merging subject to the user's authorization.

For the default coding workflow, see [the worked example](references/example-job.md). Use a replacement worker only after resolving ownership of the prior worker's write access and confirming changed responsibilities.

Continue execution and review until the acceptance criteria pass while meaningful progress is being made; do not impose a default round limit. Use the [progress and repetition rules](references/job-schema.md#progress-and-repetition) to detect stalled or cycling work, change approach, and escalate when a decision is needed.
