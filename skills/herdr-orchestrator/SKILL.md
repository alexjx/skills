---
name: herdr-orchestrator
description: Set up or resume multi-agent jobs in Herdr by confirming agent responsibilities, workflow, and handoff conditions with the user; coordinate execution, review, and completion.
---

# Herdr orchestrator

Keep a coordinator responsible for interacting with the user and coordinating the other agents. Roles are responsibilities, not required separate sessions. Confirm their owners and workflow before dispatching work.

Before discovering agents or issuing control commands, resolve the runtime using [backend selection](references/backend-selection.md). `herdr-core` (`hc`) and legacy `herdr` (TUI) are incompatible runtimes, not alternative command spellings. Load only the selected official skill for operations. Use it for terminal addressing, startup readiness, direct messaging, and recovery. If its required skill, CLI, session context, or downstream messaging capability is unavailable, surface that setup blocker before starting the job; never fall back to the other runtime.

## Agree on the team and workflow

On the first run for a job, inspect available agents and existing user instructions. Use agent names and stated context to propose responsibilities; names are hints, not authorization. Present one concise proposal for the user to confirm or correct before starting agents or dispatching work:

- **Orchestrator (coordinator/dispatcher):** user interaction, dispatching concrete jobs to each role, routing results, dependency tracking, blockers, and final delivery. Dispatch is owned by this role.
- **Planner:** plan how to proceed and break the scope into concrete tasks with dependencies and acceptance criteria. Deliver the plan to the orchestrator; do not dispatch jobs unless explicitly also assigned the orchestrator role. If absent, the orchestrator performs planning as a combined responsibility.
- **Designer:** personally produce the detailed technical design, including data flow, interfaces, and implementation decisions. Directly create and edit design documents in the repository, including design corrections; do not send these edits to the coder. Never delegate detailed technical design to other agents. If there is no separate designer, confirm an existing agent as the design owner before implementation.
- **Reviewer:** evaluate outputs against the agreed criteria and request corrections or approve. If absent, the coordinator performs these duties; review is not skipped.
- **Coder:** implement code and tests according to the detailed design. Own code corrections; design-document changes belong to the designer.
- **Workers:** one or more agents executing explicitly assigned scopes. Ask the user to choose or confirm each worker's responsibility, using names to suggest likely scopes when helpful. Do not silently assign specialties, divide work, or create extra workers.

Worker describes a dispatched agent, not a separate specialty: planners, designers, coders, reviewers, and integrators can all be workers. Roles may share an agent, but planning and dispatch remain distinct responsibilities. Route corrections by artifact ownership: design documents to the designer, code and tests to the coder, and task-plan changes to the planner.

Include each agent's name/address, role(s), scope, and expected output. Confirm the workflow alongside the role map: stages, dependencies, who hands off to whom, the evidence and conditions required for each transition, correction routes, escalation conditions, and final acceptance checks. Explain that this initial confirmation establishes responsibilities and handoff rules. Existing explicit choices count as confirmation; ask only about unresolved choices. While awaiting confirmation, discovery and proposal preparation may continue, but dependent execution must wait.

For coding jobs, propose the existing implementation → review → integration workflow as the **default**, not a requirement. It provides a clear quality gate on each exact candidate and a single owner for combining concurrent changes and checking the final result. Planning precedes implementation; review findings reach the responsible owner through the agreed workflow; blockers and final results go to the coordinator. Integration is a responsibility the coordinator covers unless the user confirms another owner, not a required extra agent. Adapt the stages and evidence to other tasks or the user's preferred workflow.

Record the confirmed agreement inline for simple jobs or in `.agents/plans/<job-id>.md` when it needs to survive sessions. On resume, reuse it and reconcile messages, checkpoints, and current artifacts before replaying work. Confirm material changes to responsibilities or handoff rules rather than repeating the whole setup.

## Run the agreed job

1. Read [message rules](references/job-schema.md) and [role prompts](references/worker-prompts.md). The orchestrator owns the full workflow and supplies each assignment's scope, criteria, context, workspace, and completion recipient with verified Agent ID/address. Derive identities from context or assign stable IDs and record address mappings. Use the existing workspace for a lone agent; separate writable worktrees only for concurrent agents.
2. Inspect runtime readiness, then send TASK. Workers begin silently. Planning and required technical design precede coding. The orchestrator supplies reviewers the user goal, criteria, plan/design, artifacts, evidence, and onward route.
3. Each agent sends one RESULT after each assigned task/phase to its named recipient, falling back to the requesting orchestrator. Worker/coder output goes to the assigned reviewer. The result includes evidence and the receiver's next action; it is the completion notification, not a separate status. Every chain returns its outcome to the orchestrator. Do not copy each result to multiple recipients. Missing context, unknown routes, or inability to proceed produce BLOCKED to the orchestrator; defer judgment until resolved.
4. Follow only assigned routes. Workflow handoffs between workers are allowed; unrelated peer messages, worker-dispatched subagents, and self-messages are forbidden. Compare identities and runtime addresses before sending; perform shared-role transitions locally. Only the orchestrator assigns new jobs. Workers request extra work through it.
5. On receiving a result, perform the assigned next phase or route the required outcome; never send receipt, readiness, working, acknowledgement, or acceptance statuses. Review approval is evidence in a RESULT requesting integration, not an acceptance notice to the coder. Corrections are actionable work for the artifact owner, not a status update.
6. The orchestrator checks pending user-requested work when the result chain returns; the orchestrator dispatches eligible tasks or reports blockers to the user. Keep the pending-work query in the result, without a separate query message. The integration/completion owner verifies the final artifact and reports to orchestrator for delivery. Publishing and merging remain subject to user authorization.

See [the example](references/example-job.md). Keep messages inline and concise; use files only for substantial artifacts or recovery. Resolve previous write ownership and confirm changed responsibilities before replacing a worker.

Continue execution and review until the acceptance criteria pass while meaningful progress is being made; do not impose a default round limit. Use the [progress and repetition rules](references/job-schema.md#progress-and-repetition) to detect stalled or cycling work, change approach, and escalate when a decision is needed.
