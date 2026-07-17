---
name: operational-acceptance
description: Assesses whether an exact release is operable, observable, recoverable, secure, supportable, and sustainable in an exact target context. Use before production release or rollout, when defining operational acceptance criteria, verifying environment readiness, exercising rollback or recovery, accepting a service handoff, or reassessing readiness after material target changes.
---

# Operational Acceptance

Read [`../../../docs/operational-acceptance.md`](../../../docs/operational-acceptance.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md)
before using this workflow. Use project-provided environments, service
objectives, telemetry, runbooks, exercises, thresholds, and decision authority.

## Workflow

1. Identify exact release, target, consumers, operating model, service
   requirements, risk tolerance, observation window, and acceptance authority.
2. Define measurable criteria and required evidence classes for capacity,
   dependencies, security, observability, recovery, support, data, continuity,
   cost, licensing, and provider obligations.
3. Resolve and inspect the target baseline: infrastructure, configuration,
   policies, credentials, dependencies, data state, active release, drift, and access.
4. Verify telemetry paths, health semantics, alert delivery, ownership,
   diagnostic correlation, service thresholds, retention, and blind spots.
5. Exercise deployment, migration, smoke behavior, rollback, restore, failover,
   degraded modes, and recovery at the risk-selected depth. Measure results
   against declared criteria.
6. Verify current runbooks, on-call access, escalation, communications, support
   scope, diagnostics, supplier contacts, and vulnerability intake with owners.
7. Record `accept`, `accept-with-conditions`, `hold`, or `reject`. Bind
   conditions to owner, compensating control, expiry, review trigger, and rollback threshold.
8. Transfer accepted active-baseline identity, operating context, limitations,
   and evidence to Utilization and Support.

## Guardrails

- Documents prove preparation, not successful execution of a procedure.
- Process startup is not evidence of useful behavior or observability.
- A production-like environment supports only the boundaries it faithfully represents.
- Record untested destructive paths and blocked exercises as residual risk.
- Acceptance is target-specific and expires after material release,
  configuration, topology, provider, assumption, or freshness changes.
- Operational acceptance informs release authority; it does not replace it.

## Completion

Require candidate-bound and target-bound evidence, exercised critical paths,
accepted observability and recovery, accountable operations/support owners,
explicit gaps and conditions, and a current handoff for the exact active baseline.
