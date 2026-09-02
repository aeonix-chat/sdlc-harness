# Subagent Orchestration

Status: **baseline 0.1**

## Purpose and boundary

Subagent orchestration provides transparent delegation of bounded work to
parallel or specialized agents. Its outcome is an approved run definition,
inspectable execution record, and complete disposition of every delegated task.

This process governs agent configuration, scope allocation, coordination, and
evidence. It does not decide whether the underlying engineering work is correct;
the applicable requirements, implementation, review, security, and validation
workflows remain responsible for that decision.

Codex supplies the agent runtime. SDLC Harness supplies the control contract
around it. Repository instructions and skills can require disclosure and
recordkeeping, but they cannot intercept a host-provided spawn tool or prove
configuration fields the runtime does not expose. A system requiring trusted
enforcement must place orchestration in a host or SDK layer that owns agent
creation and emits verifiable execution metadata.

## Control objectives

- The user sees the complete requested configuration before any agent starts.
- Delegation begins only after explicit approval of a versioned run manifest.
- Every subagent has one bounded objective, explicit configuration, and clear
  acceptance criteria.
- Parallel writers have exclusive, non-overlapping ownership.
- Requested configuration is kept separate from runtime-observed configuration.
- Missing model, reasoning, usage, permission, or timing telemetry remains an
  explicit limitation rather than an inferred fact.
- Every planned agent receives a terminal disposition and integration decision.
- Prompts, ledgers, and summaries contain no secrets or unnecessary personal data.

## Run lifecycle

```text
draft -> disclosed -> approved -> spawned -> working -> terminal -> integrated
             |           |                      |
             +-- revise <-+                      +-> completed | failed | interrupted
```

1. **Draft:** identify the exact baseline, objective, integration owner,
   concurrency ceiling, and bounded agent tasks.
2. **Disclose:** show the model, reasoning effort, context fork, permissions,
   write scope, exclusions, timeout, retries, nested-delegation policy, prompt,
   and acceptance criteria for every agent.
3. **Approve:** obtain explicit user approval. A changed task, model, reasoning
   effort, permission, ownership boundary, retry count, or agent count invalidates
   prior approval.
4. **Spawn:** start only approved agents and record returned runtime identities.
5. **Observe:** record meaningful state changes, steering, failures, and
   interruptions without noisy unchanged polling.
6. **Terminate:** preserve `completed`, `failed`, or `interrupted` for every task.
7. **Integrate:** the primary agent reviews candidate work, resolves conflicts,
   runs the real project checks, and records acceptance or rejection.

## Configuration truth model

Use three distinct configuration views:

| View | Meaning |
| --- | --- |
| Requested | Values approved in the manifest and passed to the spawn request. |
| Declared | Values present in project or personal custom-agent configuration. |
| Runtime-observed | Values returned or otherwise evidenced by the execution host. |

Never report requested or declared values as effective runtime facts. Use
`not_exposed` when the host does not return the effective value.

## Concurrency and ownership

Read-only exploration is the safest initial parallel workload. Write-capable
agents may run concurrently only when their owned path roots do not overlap and
their tasks do not mutate shared generated state, dependency caches, build
directories, settings, services, or external systems. The primary agent owns
integration and final validation.

A shared filesystem is not isolation. Path ownership is a coordination control;
runtime sandboxing remains a separate host control.

## Evidence contract

The run record should contain:

- run ID, objective, repository identity, branch, commit, and dirty state;
- approval state, approver reference, and timestamp;
- exact per-agent prompt and requested configuration;
- returned runtime agent identity and observed configuration fields;
- sanitized lifecycle events, steering, retries, and interruptions;
- terminal result, changed paths or findings, checks, and limitations;
- integration disposition and integrated validation evidence.

Raw tool logs are not required. Retain bounded references and conclusions, and
follow repository policy for storage, publication, retention, and disposal.

## Executable workflow

Use the
[`subagent-orchestration`](../.agents/skills/subagent-orchestration/SKILL.md)
skill whenever one or more subagents will be created. Its run-contract reference
defines the machine-readable manifest and event ledger.

## Residual limitations

- A model-followed skill is a policy control, not a host-level interlock.
- Some Codex clients expose subagent threads without exposing resolved model,
  reasoning, token usage, cost, or effective permission metadata.
- Local ledgers can demonstrate what was requested and reported, but they are
  not trusted attestations of provider-side execution.
- Host updates can change tool schemas, inheritance behavior, and observable
  metadata; re-evaluate this baseline when the runtime changes.
