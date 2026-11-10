# Example job j42 · stabilize CSV exports

The parser and docs are independent. The round-trip regression test depends on the parser being integrated. Each item has an implementer and reviewer address in their startup messages. One integrator owns the job branch. The commit labels below stand in for full Git object IDs.

| Event | Sender → receiver | Result |
| --- | --- | --- |
| `parser.r1.start`, `docs.r1.start` | Planner → each implementer | Both start from `B0` in separate worktrees. The planner returns to the user. |
| `parser.r1.candidate` | Parser implementer → parser reviewer | Review `B0..P1`. |
| `docs.r1.candidate` | Docs implementer → docs reviewer | Review `B0..D1` while parser review is underway. |
| `parser.r1.review` | Parser reviewer → parser implementer | Request a fix because a quoted field followed by a trailing delimiter loses the final empty value. |
| `docs.r1.review` | Docs reviewer → integrator | Approve `D1`. The integrator applies it at `I1`. |
| `parser.r2.candidate` | Parser implementer → parser reviewer | Review `B0..P2`, including the new regression test. |
| `parser.r2.review` | Parser reviewer → integrator | Approve `P2`. The integrator applies it at `I2`. |
| `roundtrip.r1.start` | Integrator → round-trip implementer | The parser dependency is satisfied. Start at `I2`. |
| `roundtrip.r1.candidate` | Round-trip implementer → round-trip reviewer | Review `I2..R1`. |
| `roundtrip.r1.review` | Round-trip reviewer → integrator | Approve `R1`. Integrate at `I3` and run the final checks. |
| `job.ready` | Integrator → planner | The final commit is `I3` and the required checks passed. |

After the second parser review, the reviewer sends the approval itself directly to the integrator:

```text
Job j42 | parser.r2.review | APPROVED
Candidate parser.r2.candidate: B0..P2 (use full SHAs in actual messages).
Trailing-empty-field regression fixed; parser regression checks passed.
Integrate P2 and unblock roundtrip after integration.
```

No handoff file is needed. If the message arrives twice, the integrator checks its handled messages and Git state before acting. A delayed request about P1 cannot restart the first review round. Large test output may be linked separately, while the outcome and next action stay in the message.
