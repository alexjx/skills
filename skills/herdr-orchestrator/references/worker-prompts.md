# Dispatch and worker prompts

## Herdr Core transport

Run `hc --skill` and confirm the planner runs inside Herdr Core with `HC_TERMINAL_ID` set. Resolve that ID in the planner and put its literal value in the prompt. Check that the selected worker CLI is installed and accepts a startup prompt. Launch each worker from the planner using its recorded terminal name and worktree. For example, with a Codex worker:

```bash
hc run --bg --name "$terminal_name" --cwd "$worker_worktree" codex "$worker_prompt"
```

Use a role-specific launcher or Core template if the worker uses a different CLI. Use an isolated checkout at the pinned head for a reviewer who needs to run checks. The same planner can do routine reviews itself by recording a reviewer dispatch and report locally, then processing it normally.

The worker writes its JSON to a temporary file beside the assigned report and renames it into place once complete. It then sends one short message. Replace each angle-bracket token with the literal value supplied at dispatch.

```bash
hc send --if idle '<planner-terminal>' 'JOB_UPDATE <job-id> <item-id> <dispatch-id>'
```

This is a best-effort wake-up. If Core declines delivery because the planner is busy, blocked, or unavailable, leave the report in place. The planner scans expected report paths whenever it resumes, handles a callback or child lifecycle note, or before it next dispatches work. When unattended progress is required and callbacks may be missed, the planner can use bounded waits and reconcile on each return. An idle planner only reacts automatically when its CLI accepts the incoming prompt. Child exit and report delivery are separate events.

## Common envelope

Supply this information with each role prompt:

```text
Job ID: <job-id>
Item ID: <item-id>
Dispatch ID: <dispatch-id>
Role: <implementer or reviewer>
Approved plan: <absolute path>
Item scope and acceptance criteria: <criteria>
Worktree: <absolute path>
Review base: <full SHA>
Starting or review head: <full SHA>
Required checks: <commands and expected outcomes>
Report path: <absolute path>
Planner callback terminal: <literal terminal ID>
Prior findings for a fix: <findings or none>
```

Both roles use the report shape in [job-schema.md](job-schema.md). Embed the fields in the dispatched prompt so workers can complete the handoff without discovering the skill. The report location and callback target come from the dispatch. Keep writes inside the assigned scope and report location. Report command failures and skipped checks accurately.

## Implementer prompt

> Work in the assigned worktree. Verify its starting commit and implement the item against the stated criteria. On a fix round, address the supplied findings while preserving accepted behavior. Commit the candidate on the item branch if the job authorizes local commits. Run the required checks and record the review base, actual candidate head, results, and plan deviations. Use READY_FOR_REVIEW when a candidate is available with the required evidence. Use BLOCKED when you need a decision, a dependency, or a check you cannot complete. Save the report, then send the callback. Leave the job record, integration branch, and publishing actions to the planner.

## Reviewer prompt

> Review the exact supplied base/head pair against the original item criteria. Check the diff and run relevant verification in the assigned checkout. Keep the candidate and job state read-only. Return APPROVE when the criteria and required evidence are met, REQUEST_CHANGES with actionable blocking findings, or BLOCKED when essential evidence is unavailable. Report the actual base and head reviewed. Save the report, then send the callback. The planner owns the decision to integrate.
