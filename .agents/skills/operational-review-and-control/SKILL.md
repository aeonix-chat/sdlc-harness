---
name: operational-review-and-control
description: Reconciles the active release and configuration with current service, user, security, continuity, supportability, dependency, cost, and outcome evidence to make recurring operating decisions. Use for periodic service reviews, post-release or post-incident reassessment, drift review, risk/exception expiry, operational health decisions, or deciding continue, constrain, recover, change, or retire.
---

# Operational Review and Control

Read [`../../../docs/operational-review-and-control.md`](../../../docs/operational-review-and-control.md)
and the Utilization stage guidance. Use project-provided catalog, inventory,
telemetry, risk, review, evidence, and decision systems.

## Workflow

1. Trigger review at the required cadence or after material release, incident,
   drift, dependency, threat, obligation, or context change.
2. Reconcile desired, authorized, deployed, active, and exposed release and
   configuration state. Record drift and unknown populations.
3. Validate evidence identity, freshness, quality, coverage, and limitations.
4. Review service/user outcomes, reliability, security, privacy, continuity,
   supportability, capacity, cost, suppliers/dependencies, and obligations.
5. Compare with operating envelope, thresholds, accepted risks, exception
   expiry, previous conditions, and overdue actions.
6. Dispose gaps and route accountable work to Support, Concept, Development,
   Production, or Retirement.
7. Record `continue`, `constrain`, `recover`, `change`, or `retire` for the
   affected scope with authority, rationale, evidence, conditions, expiry, and next review.
8. Verify execution and effectiveness of resulting controls and handoffs.

## Guardrails

- Do not use `continue` with unknown active state or invalid material evidence.
- Scope decisions to affected components and populations; do not overgeneralize.
- A recorded decision without executed controls does not reduce risk.
- Automation may execute pre-authorized reversible controls, but must not
  silently accept residual risk or make irreversible retirement decisions.

## Completion

Require reconciled active state, credible current evidence, disposed gaps and
exceptions, authorized decision, owned actions, expiry/next review, and later
effectiveness verification.
