# Integration Client Resilience

Status: **baseline 0.1**
Sources reviewed: **2026-08-24**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Observability by design](observability-by-design.md) ·
[Validation and evidence](validation-and-evidence.md)

## Purpose

This document defines the portable reliability contract for outbound HTTP,
RPC, SDK, provider, webhook, polling, streaming, and messaging clients. A
client is not complete until its total operation, deadlines, retries,
cancellation, side effects, resource ownership, and evidence are explicit.

Projects select protocols, SDKs, dependencies, configuration locations, and
numeric budgets. The harness defines the decisions and evidence required to
prevent hidden unbounded work and retry amplification.

## Source basis

Use the exact protocol and SDK versions selected by the project. General
primary guidance includes:

- [gRPC deadlines](https://grpc.io/docs/guides/deadlines/),
  [cancellation](https://grpc.io/docs/guides/cancellation/), and
  [retry](https://grpc.io/docs/guides/retry/);
- [Google SRE: cascading failures](https://sre.google/sre-book/addressing-cascading-failures/);
- [AWS Builders' Library: timeouts, retries, and backoff](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter).

Protocol and SDK defaults are versioned evidence, not permission to copy a
number or inherit implicit behavior without review.

## Logical operation model

Map the whole operation, including hidden prerequisites and cleanup:

```text
caller budget
  -> queue or concurrency admission
  -> pool acquisition / DNS / connect / security handshake
  -> credential or discovery prerequisite
  -> request write
  -> first authoritative response or event
  -> body or inter-event reads
  -> nested dependency operations
  -> acknowledgement, settlement, release, and cleanup
```

Mark sequential, parallel, retried, streamed, externally billed, and detached
phases. Assign one owner to each phase and acquired resource.

## Deadline hierarchy

Define separately where applicable:

- caller or workflow deadline;
- total logical-operation budget;
- per-dependency and per-attempt deadlines;
- admission, pool, connect, handshake, write, and read bounds;
- stream establishment or first-event budget;
- established-stream inactivity and total lifecycle bounds;
- cleanup, drain, shutdown, lease, and background-work bounds.

Propagate the caller's remaining deadline when the protocol supports it. Every
child attempt must fit inside the remaining parent budget with time for result
mapping and cleanup. Equal parent and child deadlines create a race.

Choose finite values from product requirements, dependency behavior,
representative conditions, measurements, and reviewed upstream experience.
Keep application defaults, typed configuration, deployment values, and
examples synchronized through one controlled contract.

## Retry and side-effect contract

- Retries consume the original operation budget; they do not reset it.
- Retry only classified transient outcomes when replay is safe.
- Assign retry ownership to one layer and bound attempts, elapsed time,
  backoff, and coordinated-client jitter.
- Honor protocol pushback only when it fits the remaining budget.
- Distinguish failure before remote execution from an unknown outcome after a
  side effect may have started.
- Define idempotency, reservation, settlement, reconciliation, and release for
  state-changing, externally billed, or durable operations before retrying.

## Cancellation and resource ownership

For disconnect, deadline, explicit cancellation, exception, and shutdown,
decide what happens to requests, tasks, bodies, streams, sockets, sessions,
pools, semaphores, queue entries, leases, reservations, external jobs, and
partial results.

Propagate cancellation and release resources by default. Work that must outlive
the caller requires explicit durable ownership, persisted identity, bounded
execution, reconciliation, and observable terminal state. A forgotten task is
not a continuation strategy.

Reuse long-lived clients and pools where appropriate. Bound connections,
in-flight work, queues, and cleanup. Do not invent non-standard heartbeat,
progress, or cancellation messages on a standard protocol endpoint.

## Errors and observability

Expose bounded stable classifications that distinguish the material phases,
including admission, transport, prerequisite, first response/event, stream
inactivity, total deadline, cancellation, dependency rejection, and uncertain
cleanup or reconciliation.

Apply [Observability by Design](observability-by-design.md). Do not log raw
URLs, headers, credentials, payloads, arbitrary exception messages, or
integration content. Profile only after evidence assigns delay to a process.

## Verification and completion

Use deterministic fakes or controlled delayed boundaries with shortened test
budgets. Avoid production-duration sleeps in CI. Cover configuration wiring,
each material timeout class, total-budget composition, retry ownership,
cancellation cleanup, saturation, unknown side-effect outcomes, and SDK-default
drift.

Completion requires a controlled client contract containing the logical phase
graph, deadline hierarchy, retry and side-effect rules, cancellation and
resource ownership, typed configuration, observability, authoritative sources,
and bounded verification evidence.
