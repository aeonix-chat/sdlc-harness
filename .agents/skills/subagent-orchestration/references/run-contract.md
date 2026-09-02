# Subagent run contract

Use this contract when preparing a controlled subagent run. JSON is used for
the local ledger so validation requires only the Python standard library.

## Manifest

Required top-level fields:

```json
{
  "schema_version": 1,
  "run_id": "issue-123-tests-001",
  "objective": "Generate characterization tests for three independent modules.",
  "repository": "example/project",
  "baseline": {
    "branch": "feature/issue-123",
    "commit": "0123456789abcdef0123456789abcdef01234567",
    "dirty": false
  },
  "approval": {
    "required": true,
    "status": "pending",
    "approved_by": null,
    "approved_at": null
  },
  "integration_owner": "root",
  "max_concurrency": 3,
  "nested_delegation": false,
  "agents": []
}
```

Each `agents` entry requires:

| Field | Meaning |
| --- | --- |
| `task_name` | Stable, unique task identifier. |
| `objective` | One bounded outcome. |
| `model` | Exact requested model identifier. |
| `reasoning_effort` | Exact requested effort; never `inherit`. |
| `fork_turns` | `none`, `all`, or a positive integer string. |
| `permission_mode` | Requested sandbox/permission expectation. |
| `owned_paths` | Exclusive write scope; use an empty list for read-only agents. |
| `forbidden_paths` | Paths the agent must not edit. |
| `prompt_file` | Relative file containing the exact delegated prompt. |
| `acceptance_criteria` | Observable completion conditions. |
| `timeout_minutes` | Review point, not an automatic destructive action. |
| `max_retries` | Approved retry ceiling. Locked default is zero. |
| `allow_nested_delegation` | Whether this agent may spawn children. |

Example agent entry:

```json
{
  "task_name": "registry-contracts",
  "objective": "Add contract tests for the registry and embedded assets.",
  "model": "gpt-5.6-luna",
  "reasoning_effort": "medium",
  "fork_turns": "3",
  "permission_mode": "workspace-write",
  "owned_paths": ["tests/contracts"],
  "forbidden_paths": ["src"],
  "prompt_file": "agents/registry-contracts/prompt.md",
  "acceptance_criteria": ["The contract target builds", "The suite passes"],
  "timeout_minutes": 20,
  "max_retries": 0,
  "allow_nested_delegation": false
}
```

Paths must be repository-relative and must not contain `..`. Parallel
write-capable agents must have non-overlapping owned path roots. The validator
rejects exact and ancestor/descendant ownership overlaps.

The version 1 locked contract requires both the run-level and every per-agent
nested-delegation field to be `false`. A later schema must define recursive
approval and evidence before nested delegation can be enabled.

## Pre-spawn disclosure

Before approval, show one row per agent with:

- task name and objective;
- model and reasoning effort;
- context fork and permission mode;
- owned and forbidden paths;
- timeout, retry, and nested-delegation policy;
- acceptance criteria.

Also show run ID, baseline, maximum concurrency, integration owner, and which
effective fields the runtime cannot expose.

## Events

`events.ndjson` is append-only. Each line contains:

```json
{
  "schema_version": 1,
  "timestamp": "2026-01-01T00:00:00Z",
  "event": "spawned",
  "task_name": "registry-contracts",
  "details": {
    "runtime_agent_id": "agent:registry-contracts",
    "effective_model": "not_exposed",
    "effective_reasoning_effort": "not_exposed"
  }
}
```

Allowed event types are `planned`, `approved`, `spawned`, `working`,
`steered`, `needs_attention`, `completed`, `failed`, `interrupted`, and
`integrated`.

Event details must be sanitized. Store paths, exit codes, concise findings,
and references to retained output, not raw credentials or unbounded logs.

## Final matrix

The final user-facing report must contain one row per planned agent and must not
drop interrupted or failed agents. Report requested and runtime-observed values
separately. At minimum include:

| Task | Requested model/effort | Effective observation | Status | Output | Checks | Integration |
| --- | --- | --- | --- | --- | --- | --- |

State token usage, cost, timing, effective permissions, or configuration as
`not_exposed` whenever the runtime did not return evidence for them.

## Enforcement boundary

This contract controls agent behavior through repository instructions, skill
instructions, disclosure, and retained evidence. It does not intercept host
tool calls or cryptographically prove runtime configuration. Hard enforcement
requires a host or SDK orchestration layer that owns agent creation and emits
trusted execution metadata.
