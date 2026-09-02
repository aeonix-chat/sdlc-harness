---
name: subagent-orchestration
description: Plans, discloses, executes, and audits Codex subagent runs. Use whenever work will be delegated to one or more subagents, especially parallel or write-capable agents; do not use for ordinary single-agent work.
---

# Subagent Orchestration

Make delegation inspectable before it starts and traceable after it finishes.
This skill governs use of the runtime's existing subagent tools; it does not
claim to intercept or technically constrain tools supplied by the host.

## Required protocol

1. Confirm that the user explicitly requested subagents, or that applicable
   project or skill instructions explicitly require delegation. Do not infer
   authorization merely because parallel work might be faster.
2. Read [the run contract](references/run-contract.md). Prepare a bounded run
   manifest before the first spawn. Every agent entry must explicitly state its
   model, reasoning effort, context fork, permission expectation, owned paths,
   forbidden paths, task prompt, acceptance criteria, timeout, and retry limit.
   Do not use implicit model or reasoning inheritance in a controlled run.
3. Show the complete pre-spawn table to the user. Distinguish requested values
   from values the runtime can actually verify. Wait for explicit approval of
   the manifest before spawning any agent.
4. Initialize the local run ledger with `scripts/orchestration_ledger.py` when
   the repository permits local evidence files. Otherwise retain the same
   fields in the conversation and report that no on-disk ledger was created.
   Never put credentials, tokens, personal data, or raw sensitive logs in it.
5. Spawn only the approved agents. Pass `model`, `reasoning_effort`, and
   `fork_turns` explicitly. Use exclusive write ownership: parallel writers
   must not edit overlapping paths, and the primary agent owns integration.
6. Immediately disclose each returned agent name or ID together with the
   requested configuration. If the runtime does not return effective model,
   reasoning, token usage, or another field, record `not_exposed`; never infer
   it from a successful result.
7. Report state transitions that matter: spawned, working, needs attention,
   completed, failed, or interrupted. Do not produce noisy unchanged polling
   updates. Record every steer, retry, scope change, and interruption.
8. Wait for all approved agents unless the manifest defines an earlier stop
   condition. A timeout or slow compile is not permission to silently replace,
   retry, or interrupt an agent. Follow the manifest and disclose the action.
9. Review and integrate centrally. A subagent result is candidate work, not
   accepted evidence. Validate the integrated state with the repository's real
   checks.
10. Return a final result matrix covering every planned agent: requested
    configuration, runtime-observed configuration, status, files or findings,
    checks, integration disposition, limitations, and unavailable telemetry.

## Locked defaults

- Approval mode: explicit user confirmation before spawning.
- Maximum retries: zero unless approved in the manifest.
- Nested delegation: forbidden in the version 1 contract.
- Write concurrency: allowed only for disjoint owned paths.
- Integration ownership: primary agent only.
- Scope changes: require a revised manifest and renewed approval.
- Secrets: references only; never values.
- Missing runtime telemetry: `not_exposed`, never guessed.

The runtime may impose a lower concurrency limit or override permissions. Treat
the manifest as requested configuration, not proof of effective configuration.
Subagents commonly share a filesystem with the primary agent, so path ownership
is a coordination contract rather than isolation.

## Ledger helper

Use the helper through the repository's required Python runner, for example:

```sh
uv run python .agents/skills/subagent-orchestration/scripts/orchestration_ledger.py \
  validate --manifest .agents/runs/<run-id>/manifest.json
```

The helper validates and records orchestration evidence; it never launches an
agent. Read its `--help` output for `init`, `approve`, `event`, and `validate`.

## Completion

A run is complete only when every manifest entry has a terminal disposition,
the integrated result has been assessed, unavailable telemetry is explicit,
and the user receives the final matrix. Preserve durable evidence only when
repository policy permits it; otherwise remove local run artifacts after the
summary is delivered.
