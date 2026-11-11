# Select and bind the Herdr runtime

Resolve this before agent discovery, launch, messaging, or recovery. Skill installation and CLI presence indicate availability, not which runtime owns the job. Do not choose the newer runtime merely because it is installed.

## Selection

Read only the relevant environment markers and existing job agreement. Do not dump the environment or start a server to detect a backend.

| Current context | Candidate for a new job without an explicit choice |
| --- | --- |
| Nonempty `HC_TERMINAL_ID`, no `HERDR_ENV=1` | `herdr-core`, CLI `hc` |
| `HERDR_ENV=1`, empty/unset `HC_TERMINAL_ID` | Legacy `herdr`, CLI `herdr` |
| Both markers present | Ambiguous, possibly inherited/nested context; resolve the intended runtime before control commands |
| Neither marker present | No inferred runtime; ask which runtime to use unless already specified |

A user's explicit runtime choice or a resumed job's recorded binding identifies the intended target. It does not prove that this process can access it. If that target conflicts with the current context, explain the mismatch and resolve it before dispatch. Do not silently migrate a resumed job to the runtime detected in a new shell. If an older job has no binding, establish one from verified context and its existing agents before replaying work.

## Verify the selected dependency

1. Locate and read the selected official skill's `SKILL.md`. If it is not installed as a skill, the selected binary's `--skill` output can supply its official instructions; verify the output identifies the expected runtime. If neither source is available, report the missing dependency. Never substitute the other skill.
2. Follow that skill's prerequisites and obtain current CLI documentation. Core uses `hc --skill`; TUI uses `herdr --skill` and its documented help. Do not run bare `herdr` for discovery: it launches or attaches the TUI. Do not probe by launching agents, starting servers, or sending messages.
3. Respect runtime-specific access requirements. The installed TUI skill requires `HERDR_ENV=1` and prohibits controlling a focused session from outside Herdr. The core skill uses `HC_TERMINAL_ID` and asks for a choice when outside core; an existing explicit user choice satisfies that choice, but does not establish a valid target address. Never manufacture environment markers to pass these checks.
4. Use the selected skill's documented inspection commands to verify the intended session/machine and live agents. Check caller context and target ownership; markers can be stale or inherited. Resolve conflicting markers through this evidence and the user's intended target, not an arbitrary precedence rule. An unreachable or missing target is a blocker, not permission to try the other backend.

## Bind and preserve

Include the runtime (`herdr-core` or `herdr`), selected official skill source, machine/session context, and verified coordinator/worker addresses in the job agreement and every worker envelope. Treat addresses as backend-scoped opaque handles. Do not translate TUI pane IDs to core terminal IDs, reuse names across servers, or mix discovery from one runtime with messaging through the other. This workflow does not bridge runtimes.

Workers load the pinned skill and verify their context before acting. A mismatch goes to the coordinator without executing the task through another backend. On resume or reconnect, revalidate the binding and live identities before resending; a failed send does not prove non-delivery. Follow the selected runtime's recovery rules. Changing runtime requires an explicit migration decision and fresh address discovery, not fallback.

## Evidence and review cases

Verified against the installed official `herdr-core` skill, `hc --skill`, and `herdr --skill` on 2026-11-11. The [official Herdr FAQ](https://herdr.dev) confirms the app/core and [legacy TUI](https://herdr.dev/tui) have separate servers and do not share agents. Installed official instructions remain authoritative for operational details.

When editing this routing, review these cases: core-only marker selects core even with both CLIs installed; TUI-only marker selects TUI even with core installed; both/neither markers do not select by installation order; explicit TUI outside TUI stops at its context prerequisite; a recorded core job in a TUI shell does not migrate; a missing selected CLI does not fall back; a worker context mismatch does not dispatch; a send failure does not trigger cross-runtime retry.
