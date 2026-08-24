---
name: integration-client-resilience
description: Designs bounded, resource-safe outbound integration clients. Use when adding or changing HTTP, RPC, SDK, provider, webhook, polling, streaming, or messaging clients, or when deciding deadlines, timeouts, retries, backoff, cancellation, pools, concurrency, cleanup, and unknown side-effect outcomes.
---

# Integration Client Resilience

Read [`../../../docs/integration-client-resilience.md`](../../../docs/integration-client-resilience.md),
[`../../../docs/observability-by-design.md`](../../../docs/observability-by-design.md),
and the authoritative documentation for the selected protocol and SDK version.

## Workflow

1. Map the complete logical operation, including admission, transport,
   credentials or discovery, streaming, nested calls, side effects, and cleanup.
2. Assign one owner to every phase and acquired resource.
3. Define finite caller, total-operation, attempt, transport, stream, and
   cleanup budgets. Fit child work inside the remaining parent budget.
4. Assign retry ownership to one layer. Bound attempts, elapsed time, backoff,
   and jitter; retry only classified replay-safe outcomes.
5. Define idempotency and unknown-outcome handling for state-changing, billed,
   or durable operations.
6. Define cancellation, shutdown, pool, queue, concurrency, lease, stream, and
   background-work ownership with bounded release paths.
7. Synchronize typed defaults, deployment configuration, examples, and the real
   client through one controlled contract.
8. Define bounded errors and diagnostic signals, then prove delay,
   cancellation, saturation, retry, cleanup, and configuration behavior deterministically.

## Guardrails

- Do not inherit implicit SDK timeout or retry behavior without versioned review.
- Retries never reset the parent budget or multiply across layers.
- Equal parent and child deadlines are not a valid hierarchy.
- Work that outlives its caller requires explicit durable ownership and reconciliation.
- Do not expose integration content, credentials, raw URLs, or arbitrary errors through telemetry.

## Completion

Require a reviewable operation graph, deadline hierarchy, retry and side-effect
contract, cancellation and resource ownership, synchronized configuration,
bounded observability, authoritative sources, and deterministic evidence.
