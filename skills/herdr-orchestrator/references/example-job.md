# Example job j42 · stabilize CSV exports

This fictional example uses short commit labels for readability. Real job records and reports use full Git object IDs.

## Approved plan

- **parser** makes the CSV parser preserve trailing empty fields. It owns parser code and its unit tests.
- **docs** documents the CSV escaping rules using the already agreed behavior. It owns the export guide. It has no dependency on parser code.
- **roundtrip** adds an export/import regression fixture. It owns the integration test and waits for **parser** to be integrated.
- Job-level acceptance requires parser unit tests and the CSV round-trip suite to pass on the integrated commit. The planner starts `job/j42` at `B0`.

## Dispatch and review history

| Dispatch | Work and handoff | Planner transition |
| --- | --- | --- |
| `j42-parser-i1` | Implementer A starts from `B0` and reports candidate `P1` with unit tests. | Parser enters review. |
| `j42-docs-i1` | Implementer B starts from `B0` in a separate worktree while A is running and reports candidate `D1`. | Docs enters review. |
| `j42-parser-r1` | A fresh reviewer inspects `B0..P1` and requests a change. A quoted field followed by a trailing delimiter still loses the last empty value. | Parser enters `changes_requested`. |
| `j42-docs-r1` | The planner reviews `B0..D1` against the agreed rules and records approval. | Docs is accepted and integrated at `I1`. |
| `j42-parser-i2` | A starts at `P1`, fixes the quoted-field case, and reports `B0..P2` with the new regression test. | Parser enters review of `P2`. |
| `j42-parser-r2` | The reviewer inspects `B0..P2`, confirms the regression test and reports approval. | Parser is accepted and integrated on top of `I1` at `I2`. |
| `j42-roundtrip-i1` | A worker starts at `I2`, adds the fixture, and reports `I2..R1`. | Roundtrip enters review. |
| `j42-roundtrip-r1` | The planner reviews `I2..R1` and approves. | Roundtrip is accepted and integrated at `I3`. |

For the second parser review, the worker saves `reports/j42-parser-r2.json` in the job directory, then uses the reporting route from the selected Herdr skill if available, with this payload:

```text
JOB_UPDATE j42 parser j42-parser-r2
```

If the same callback arrives twice, the planner sees that the dispatch was already consumed. If a delayed first-round result arrives while the second round is active, its ID and head identify it as stale. If delivery of the second callback is uncertain, it finds the report at the active dispatch's expected path during reconciliation.

The planner runs the job-level checks at `I3` and records them against that commit before marking the job `ready_for_merge`. It gives the user `I3`, the check outcomes, and the resolved review finding.
