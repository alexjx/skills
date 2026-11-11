# Example job j42 · stabilize CSV exports

This is the default coding workflow, after the user confirms the following responsibilities and handoffs. Separate reviewers and an integrator are illustrative; the coordinator covers planning, review, and integration when those owners are absent. Agent names suggest scopes but do not select them.

The confirmed designer has personally completed the detailed technical design before dispatch; this responsibility is never delegated. The planner breaks the request into concrete jobs; the coordinator dispatches them. Design-document edits and corrections are assigned to the designer, while code and test changes are assigned to coders. Each dispatched task includes an Agent ID from context or assigned by the orchestrator, mapped to the agent's runtime address. All replies repeat that ID.

The parser and docs are independent. The round-trip regression test depends on the parser being integrated. Each agent receives its dispatcher address in its startup message; workers never contact peers or themselves. The coordinator is the dispatcher in this example. One integrator owns the job branch. The commit labels below stand in for full Git object IDs.

| Event | Sender → receiver | Result |
| --- | --- | --- |
| `parser.r1.start`, `docs.r1.start` | Coordinator → each coder | Both start from `B0` in separate worktrees. The coordinator continues interacting with the user. |
| `parser.r1.candidate` | Parser coder → coordinator → parser reviewer | Review `B0..P1`. |
| `docs.r1.candidate` | Docs coder → coordinator → docs reviewer | Review `B0..D1` while parser review is underway. |
| `parser.r1.review` | Parser reviewer → coordinator → parser coder | Request a fix because a quoted field followed by a trailing delimiter loses the final empty value. |
| `docs.r1.review` | Docs reviewer → coordinator → integrator | Approve `D1`. The integrator applies it at `I1`. |
| `parser.r2.candidate` | Parser coder → coordinator → parser reviewer | Review `B0..P2`, including the new regression test. |
| `parser.r2.review` | Parser reviewer → coordinator → integrator | Approve `P2`. The integrator applies it at `I2`. |
| `roundtrip.r1.start` | Integrator → coordinator → round-trip coder | The parser dependency is satisfied. Start at `I2`. |
| `roundtrip.r1.candidate` | Round-trip coder → coordinator → round-trip reviewer | Review `I2..R1`. |
| `roundtrip.r1.review` | Round-trip reviewer → coordinator → integrator | Approve `R1`. Integrate at `I3` and run the final checks. |
| `job.ready` | Integrator → coordinator | The final commit is `I3` and the required checks passed. |

After the second parser review, the reviewer sends the exact approval and evidence to the coordinator, which assigns integration:

```text
Job j42 | parser.r2.review | APPROVED | From: reviewer-1
Candidate parser.r2.candidate: B0..P2 (use full SHAs in actual messages).
Trailing-empty-field regression fixed; parser regression checks passed.
Dispatcher: assign integration of P2, then dispatch roundtrip once unblocked.
```

If a single agent performs these roles sequentially, it uses the existing workspace and records local role transitions; separate worktrees are used only for concurrent agents.

Each completed assignment reports its outcome and pending-job query to the dispatcher. The dispatcher routes the next actionable assignment without acknowledgement or acceptance statuses. No handoff file is needed. If the message arrives twice, the dispatcher checks handled messages and Git state before dispatching again. A delayed request about P1 cannot restart the first review round. Large test output may be linked separately, while the outcome and next action stay in the message.
