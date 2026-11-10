# Job records

The plan specifies the user outcome, acceptance criteria and job-level checks. The job JSON is the current snapshot. Save it as a complete replacement using a same-directory temporary file and rename. Create the reports directory before dispatch. Use absolute local paths for worktrees and a single coordinating checkout for all job records. This baseline assumes one machine or a shared filesystem accessible from every worker.

## Planner-owned job.json

```json
{
  "schema_version": 1,
  "job_id": "j42",
  "plan_path": ".agents/plans/j42.md",
  "state": "active",
  "integration": {
    "branch": "job/j42",
    "worktree": "/absolute/path/to/j42-integration",
    "base": "<full git SHA>",
    "head": "<full git SHA>",
    "checks": []
  },
  "max_implementation_attempts": 3,
  "items": {
    "parser": {
      "depends_on": [],
      "state": "reviewing",
      "worktree": "/absolute/path/to/j42-parser",
      "implementation_attempts": 2,
      "candidate": {"base": "<full git SHA>", "head": "<full git SHA>"},
      "active_dispatch": {
        "id": "j42-parser-r2",
        "role": "reviewer",
        "terminal_name": "j42-parser-r2",
        "terminal_address": null,
        "base": "<full git SHA>",
        "head": "<full git SHA>",
        "report_path": "reports/j42-parser-r2.json"
      },
      "last_report": "reports/j42-parser-i2.json",
      "accepted_head": null,
      "integrated_head": null
    }
  }
}
```

- Job states are `active`, `blocked`, and `ready_for_merge`. Set `ready_for_merge` only after every item is integrated and job-level checks pass on `integration.head`. If that head changes, clear its check evidence and reverify.
- Item states are `pending`, `implementing`, `reviewing`, `changes_requested`, `blocked`, `accepted`, and `integrated`. Initialize counters to zero and unset fields to null. A dependency is satisfied at `integrated`.
- Persist a globally unique dispatch ID per job/item/attempt and a unique, terminal name compatible with the selected Herdr skill before launching. If needed, shorten the terminal name independently of the ID. Set the returned terminal address after launch. Keep a single active dispatch per item.
- For an implementer, dispatch `base` is the review base and `head` is the starting commit, which equals base on the first attempt. Fix attempts start at the prior candidate head and retain its review base. For a reviewer, the dispatch pins the candidate base and head. Verify commit existence and ancestry in the repo. Require an implementation result to retain the dispatch base and descend from its starting head.
- Count each implementation or fix attempt started. Review attempts have their own unique dispatch IDs. Transport uncertainty is a reason to reconcile, not to launch another writer. Look up the existing terminal by name, check its transcript and report, and establish that the prior worker has stopped writing before replacing it.
- Accept only a report whose IDs and role match the active dispatch. For review, require the exact current base and head. Record the transition, last report, and cleared or replacement dispatch together in the planner snapshot. Keep completed reports as history.
- Record the accepted head before integrating. Check the integration branch and its actual head before applying an accepted item. If an interruption leaves the integration head ahead of the snapshot, inspect its history and reconcile the recorded candidate before applying anything again. Record the resulting commit in both the item and integration state.

## Worker-owned report

```json
{
  "job_id": "j42",
  "item_id": "parser",
  "dispatch_id": "j42-parser-r2",
  "role": "reviewer",
  "outcome": "APPROVE",
  "base": "<full git SHA>",
  "head": "<full git SHA>",
  "checks": [{"command": "npm test -- parser", "result": "passed", "detail": "12 tests"}],
  "findings": [],
  "summary": "The candidate satisfies the parser acceptance criteria."
}
```

Implementer outcomes are `READY_FOR_REVIEW` and `BLOCKED`. Reviewer outcomes are `APPROVE`, `REQUEST_CHANGES`, and `BLOCKED`. For `REQUEST_CHANGES`, include blocking findings with location, violated criterion, and expected behavior. For `BLOCKED`, identify the needed decision or dependency in `summary`. Use null for an unavailable SHA on a blocked report. Check results are `passed`, `failed`, or `not_run`, with a reason or observed output in `detail`. List substantive plan deviations in the implementation summary.
