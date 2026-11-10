# Dispatch and worker prompts

## Use the selected Herdr skill

Follow the installed `herdr-core` or `herdr` skill selected by the planner. Use the recorded worker name and assigned worktree. Use a fitting role template if the selected skill supports one, and supply the envelope below as the task. Follow that skill's recovery guidance if launch or task delivery is uncertain.

Use the selected skill's documented reporting route, such as a native parent reply or a documented prompt to the planner. If the skill provides no suitable callback, have the planner wait for the worker using the selected skill and then read the report. Keep subdelegation with the planner unless the job explicitly assigns it elsewhere.

Write the JSON report to a temporary file beside the assigned report, then rename it into place before reporting back. When a callback route is available, send this payload:

```text
JOB_UPDATE <job-id> <item-id> <dispatch-id>
```

The planner looks up the report path in its own job record. If delivery is uncertain, leave the report available for reconciliation. Use the selected skill's wait mechanism when awaiting results and reconcile expected report files on return or when resuming a job.

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
Reporting: <return route from the selected skill, or planner collects the report>
Prior findings for a fix: <findings or none>
```

Both roles use the report shape in [job-schema.md](job-schema.md). Embed the fields in the dispatched prompt so workers can complete the handoff without discovering the skill. The report location and callback target come from the dispatch. Keep writes inside the assigned scope and report location. Report command failures and skipped checks accurately.

## Implementer prompt

> Work in the assigned worktree. Verify its starting commit and implement the item against the stated criteria. On a fix round, address the supplied findings while preserving accepted behavior. Commit the candidate on the item branch if the job authorizes local commits. Run the required checks and record the review base, actual candidate head, results, and plan deviations. Use READY_FOR_REVIEW when a candidate is available with the required evidence. Use BLOCKED when you need a decision, a dependency, or a check you cannot complete. Save the report, then use the assigned reporting route if one is provided. Leave the job record, integration branch, and publishing actions to the planner.

## Reviewer prompt

> Review the exact supplied base/head pair against the original item criteria. Check the diff and run relevant verification in the assigned checkout. Keep the candidate and job state read-only. Return APPROVE when the criteria and required evidence are met, REQUEST_CHANGES with actionable blocking findings, or BLOCKED when essential evidence is unavailable. Report the actual base and head reviewed. Save the report, then use the assigned reporting route if one is provided. The planner owns the decision to integrate.
