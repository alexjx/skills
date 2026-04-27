---
name: handover
description: Consolidate prior multi-step discussions, decisions, and artifacts into one executable handover document for a target agent or external tool agent. Use when work spans multiple design/communication steps and needs clean transfer.
---

# Skill: Execution-Ready Handover

## Purpose
Create a complete handover document from existing context after planning and design are already finished in the current agent.

This skill is for execution-ready context synthesis and transfer, not for delegating unfinished design work.

## When To Use
Trigger this skill when any of the following is true:
- The current work already included design/discussion steps and now needs execution handoff.
- Context is scattered across messages and files.
- The next executor is another agent, tool-integrated agent, or human operator.
- You need a single handover artifact that can be executed without reading full chat history.

Use this skill late in the workflow. The invoking agent must finish the task list and design spec before handoff.

## Non-Goals
- Do not hand off unresolved architecture or vague implementation ideas.
- Do not ask the next executor to reconstruct missing design from chat history.
- Do not assume the target is a coding agent.
- Do not produce vague summaries that omit decisions, constraints, or evidence.

## Target Agent Model (critical)
Treat `target agent` as an abstract executor. It may be:
- coding agent
- workflow/tool agent (for example automation, browser, retrieval, or orchestration agent)
- external platform agent
- human operator

Always capture target-specific details explicitly:
- runtime/platform
- available tools and blocked tools
- expected input/output interface
- execution constraints (time, budget, permissions, environment)

## Workspace Policy
- Default handover workspace: `.agents/handover/`
- If user specifies another path, use user path.
- Keep related artifacts in one workspace when possible.

## Preconditions (critical)
Before writing handover, the invoking agent must complete:
1. A concrete task list with ordered execution steps.
2. A design spec that explains the chosen approach, data flow, interfaces, and important tradeoffs.
3. A current-state summary that distinguishes completed work from remaining execution work.

If those are missing, stop and finish them in the current agent before producing handover.

## Required Outputs
Create/update in the selected handover workspace:
1. `handover-<timestamp>.md` (required)
2. Optional supporting docs only if needed (for example `context-index.md`)

## Source Collection Model (critical)
Before writing handover, collect and classify context from:
1. Conversation decisions
2. Existing design docs/specs/plans
3. Research notes and references
4. Existing code/log/test evidence (if implementation already started)
5. Remaining execution tasks, blockers, and unresolved risks

For each collected item, capture:
- source path or source type (chat/file/tool output)
- short factual summary
- why it matters for execution

Also normalize the collected context into two execution-facing outputs before writing the final handover:
- `Design Spec`: stable decisions the next executor should follow
- `Concrete Task List`: discrete tasks the next executor should complete

## Handover Document Contract (critical)
The handover document must include all sections below:
1. `Goal`
2. `Target Executor Profile`
3. `Current State`
4. `Design Spec`
5. `Concrete Task List`
6. `Decisions Already Made`
7. `Constraints`
8. `Relevant Artifacts`
9. `Execution Plan`
10. `Verification`
11. `Open Questions`
12. `Out of Scope`
13. `Referenced Sources`
14. `Kickoff Command or First Action`

### Section Rules
- `Design Spec` must be complete enough that the next executor does not need to redesign core behavior.
- `Concrete Task List` must be a checklist of discrete tasks with clear outputs or completion criteria.
- `Relevant Artifacts` must list concrete paths and usage notes.
- `Referenced Sources` must only list sources actually used for this handover.
- `Execution Plan` must be actionable, ordered, and free of placeholders.
- `Verification` must include runnable checks when possible.
- `Open Questions` should be limited to true blockers or externally owned decisions.

## Workflow
1. Identify target executor type and its constraints.
2. Gather all relevant upstream context (chat + docs + artifacts).
3. Resolve conflicts by preserving latest explicit decision and recording deltas.
4. Finish the design spec in the current agent.
5. Finish the concrete task list in the current agent.
6. Write `handover-<timestamp>.md` from template.
7. Run completeness check against the 14 required sections.
8. Ensure next executor can start executing from the handover doc alone.

## Quality Bar
- Context complete enough to avoid re-reading full thread.
- Design complete enough to avoid re-planning.
- Remaining work expressed as concrete tasks, not themes.
- No hidden assumptions.
- No agent-type ambiguity.
- No missing artifact paths for required inputs.
- Verification criteria are concrete.

## Final Response Format
Respond with:
1. handover workspace path
2. file paths created/updated
3. what design and tasks were finalized (short)
4. copy-ready line for next executor (for example: `Execute .agents/handover/handover-20260402-1030.md`)

## Template
Use `assets/handover-template.md` as the default scaffold.
