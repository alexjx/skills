# Select and bind the Herdr runtime

Resolve before discovery, launch, messaging, or recovery. `herdr-core`/`hc` and legacy `herdr`/TUI are incompatible runtimes; installation order does not select one.

## Selection

Inspect only relevant markers and the existing job agreement; do not dump the environment or launch servers/agents to probe.

| Context | Candidate without an explicit choice |
| --- | --- |
| Nonempty HC_TERMINAL_ID; no HERDR_ENV=1 | Core, CLI `hc` |
| HERDR_ENV=1; empty/unset HC_TERMINAL_ID | TUI, CLI `herdr` |
| Both markers | Resolve nested/stale context before control commands. |
| Neither | Ask which runtime unless already specified. |

Explicit user choice or a resumed job's binding identifies the target, not access permission or reachability. Resolve context conflicts; never silently migrate. For older jobs without a binding, establish one from verified agents/context before replaying work.

## Verify and bind

1. Read the selected official SKILL.md, or its CLI's `--skill` output if uninstalled; verify the runtime identity. Missing skill/CLI/context/messaging is a blocker, never permission to substitute the other backend.
2. Follow current official prerequisites/help: `hc --skill` or `herdr --skill`. Bare `herdr` launches/attaches TUI; do not use it for discovery.
3. TUI requires HERDR_ENV=1 and forbids controlling a focused session from outside Herdr. Core uses HC_TERMINAL_ID and requires a runtime choice outside core. Existing explicit choice satisfies the choice only; never manufacture markers or addresses.
4. Use documented inspection to verify machine/session, caller context, live agents, and target ownership. Resolve conflicting markers through evidence and intended target, not arbitrary precedence.

Record runtime, official skill source, machine/session, and verified addresses in the agreement and every assignment. Addresses are opaque and backend-scoped: never translate pane/terminal IDs, reuse names across servers, or mix runtimes.

Workers load the pinned skill and verify context before acting; report mismatches without executing. On resume/reconnect, revalidate identities and binding before resending. Failed sends do not prove non-delivery; use the selected recovery rules. Runtime changes require an explicit migration decision and fresh discovery.

## Review cases

Check: core-only/TUI-only markers select their runtime despite both CLIs being installed; both/neither remain unresolved absent a choice; explicit TUI outside TUI stops at prerequisites; resumed jobs never auto-migrate; missing dependencies, worker mismatch, and send failure never trigger cross-runtime fallback.
