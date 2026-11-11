# Example: CSV export fix

After confirmed planning and personally authored designer documents, coordinator dispatches parser coding. A round-trip test depends on parser integration. Addresses and outcome routes are pinned in assignments; below, labels stand for full SHAs.

Coordinator specifies reviewer and completion action in each coding assignment; orchestrator supplies review context. A reviewer missing context requests it before judging. Unknown routes or unresolved context return to coordinator.

| Event | Sender → receiver | Action |
| --- | --- | --- |
| TASK | Coordinator → coder | Implement parser from B0. |
| RESULT | Coder → reviewer | Review B0..P1 with test evidence. |
| RESULT | Reviewer → coder | Fix trailing-empty-field regression. |
| RESULT | Coder → reviewer | Review B0..P2; report resolved finding and checks. |
| RESULT | Reviewer → integrator | Integrate exact P2. |
| RESULT | Integrator → coordinator | Report integration head I1; unblock round-trip job. |
| TASK | Coordinator → coder | Implement round-trip test from I1. |
| RESULT | Coder → reviewer | Review I1..R1. |
| RESULT | Reviewer → integrator | Integrate R1; run final checks. |
| RESULT | Integrator → coordinator | Report final I2, accepted heads, and checks. |

Each completed phase notifies its next owner. Do not copy phase results to dispatcher. Carry the pending-work query through the chain; coordinator checks it when integration results return. No receipt acknowledgements or status-only acceptance messages follow.

In two-agent mode, dispatcher may also review: coder sends RESULT back to dispatcher/reviewer, which performs its next local duty or sends the required handoff. Never self-message. A lone agent uses the existing workspace; separate writable worktrees apply only to concurrent agents.

Duplicate delivery never repeats work: reconcile event IDs and Git state. Design-document corrections belong to designer, code/tests to coder. See [message rules](job-schema.md) for recovery and repetition.
