---
name: handover
description: Consolidate prior multi-step discussions, decisions, and artifacts into one executable handover document for a target agent or external tool agent. Use when work spans multiple design/communication steps and needs clean transfer.
---

# Skill: Context To Handover

## Purpose
Create a complete handover document from existing context, especially when handover is not the first step in the workflow.

This skill is for context synthesis and transfer, not for implementation itself.

## When To Use
Trigger this skill when any of the following is true:
- The current work included multiple design/discussion steps before execution.
- Context is scattered across messages and files.
- The next executor is another agent, tool-integrated agent, or human operator.
- You need a single handover artifact that can be run without reading full chat history.

## Non-Goals
- Do not redesign the whole solution unless there is a clear contradiction.
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
5. Open questions and unresolved risks

For each collected item, capture:
- source path or source type (chat/file/tool output)
- short factual summary
- why it matters for execution

## Handover Document Contract (critical)
The handover document must include all sections below:
1. `Goal`
2. `Target Executor Profile`
3. `Current State`
4. `Decisions Already Made`
5. `Constraints`
6. `Relevant Artifacts`
7. `Execution Plan`
8. `Verification`
9. `Open Questions`
10. `Out of Scope`
11. `Referenced Sources`
12. `Kickoff Command or First Action`

### Section Rules
- `Relevant Artifacts` must list concrete paths and usage notes.
- `Referenced Sources` must only list sources actually used for this handover.
- `Execution Plan` must be actionable, ordered, and free of placeholders.
- `Verification` must include runnable checks when possible.
- `Open Questions` must include owner and expected resolution path when possible.

## Workflow
1. Identify target executor type and its constraints.
2. Gather all relevant upstream context (chat + docs + artifacts).
3. Resolve conflicts by preserving latest explicit decision and recording deltas.
4. Write `handover-<timestamp>.md` from template.
5. Run completeness check against the 12 required sections.
6. Ensure next executor can start from the handover doc alone.

## Quality Bar
- Context complete enough to avoid re-reading full thread.
- No hidden assumptions.
- No agent-type ambiguity.
- No missing artifact paths for required inputs.
- Verification criteria are concrete.

## Final Response Format
Respond with:
1. handover workspace path
2. file paths created/updated
3. what context was synthesized (short)
4. copy-ready line for next executor (for example: `Run .agents/handover/handover-20260402-1030.md`)

## Template
Use `assets/handover-template.md` as the default scaffold.
