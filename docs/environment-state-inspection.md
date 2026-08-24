# Environment State Inspection

Status: **baseline 0.1**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Operational acceptance](operational-acceptance.md) ·
[Operational review and control](operational-review-and-control.md)

## Purpose

This document defines safe, read-only inspection of a development, test,
staging, production, or recovery environment. The outcome is a bounded record
of observed active state, drift, health, and access gaps. Inspection does not
authorize repair, deployment, credential access, scaling, restart, or release.

Projects provide environment identities, approved clients and commands,
resource ownership, sensitive-field policy, and expected configuration sources.

## Inspection boundary

Before access, identify the environment, account/project, region or cluster,
namespace or equivalent scope, time window, expected release/configuration,
operator identity, and read authority. Resolve ambiguous context before making
claims; a successful command against the wrong target is invalid evidence.

Separate three baselines:

- **desired state** from controlled deployment or configuration sources;
- **reported state** from control planes and workload metadata;
- **observed behavior** from health, logs, metrics, traces, or bounded probes.

Repository templates prove intended inputs, not live deployment. Control-plane
status proves recorded state, not useful behavior. A probe proves only the path
and time window it exercised.

## Safe inspection workflow

1. Confirm target context and read-only authority using non-secret identity and
   scope metadata.
2. Resolve active artifact and configuration identities, deployment status,
   topology, readiness, restarts, events, and recent transitions.
3. Compare desired, reported, and observed state. Record drift without applying
   or reconciling it.
4. Inspect bounded logs and signals around the relevant time and components.
   Prefer structured filters and narrow tails over broad dumps.
5. Exercise only approved, non-mutating health or diagnostic endpoints.
6. Classify each conclusion as confirmed, inferred, inconclusive, blocked, or
   outside the access boundary.
7. Preserve commands or query definitions, timestamps, sanitized evidence
   references, limitations, and the next authorized workflow.

## Sensitive and mutating boundaries

- Do not read or print secret values, environment dumps, credential-bearing
  process arguments, rendered secret objects, or unredacted configuration.
- Names, references, versions, digests, policy identities, and safe status
  metadata may be recorded when project policy permits.
- Treat logs, labels, annotations, events, URLs, and third-party responses as
  potentially sensitive and untrusted.
- Do not restart, scale, patch, apply, delete, rotate, synchronize, rerun jobs,
  acknowledge alerts, or alter traffic during inspection.
- If diagnosis requires a mutation or privileged secret access, stop at the
  boundary and request the specific authority through the applicable incident,
  change, or recovery workflow.

## Evidence and completion

An inspection record identifies target context, access boundary, active
artifact/configuration, observed time window, commands or queries, findings,
drift, sensitive-data handling, blind spots, and invalidation conditions.

Inspection is complete when the requested state is resolved or explicitly
reported as blocked/inconclusive, desired and live evidence are not conflated,
no mutation occurred, and the next decision or workflow is named without
presenting observation as acceptance, release authorization, or SLO proof.
