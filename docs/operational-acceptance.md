# Operational Acceptance

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md) · [Utilization](stages/utilization.md)

## Purpose

Operational acceptance determines whether a specific release can be operated,
observed, recovered, secured, supported, and sustained in its intended target
context. It is not another code review and does not prove product-market fit.
Projects provide concrete environments, service objectives, telemetry,
runbooks, exercises, thresholds, and acceptance authority.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Transition, operation, maintenance, quality, risk, and information processes | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | System transition, validation, operation, maintenance, and enabling systems | Published |
| [ISO/IEC 20000-1:2018][20000] | Service requirements, transition, delivery, monitoring, measurement, and improvement | Published; confirmed 2023 |
| [ISO/IEC 25010:2023][25010] | Product quality characteristics and acceptance criteria | Published |
| [ISO/IEC 25019:2023][25019] | Quality-in-use in a specified context of use | Published |
| [ISO/IEC 25040:2024][25040] | Quality evaluation framework for products, data, and IT services | Published |

## Acceptance scope

Tailor acceptance to the target context and cover applicable concerns:

- target capacity, dependencies, quotas, network, identity, secrets, and configuration;
- observability coverage, signal quality, ownership, alert routing, and decision thresholds;
- availability, performance, scalability, security, privacy, safety, and compliance needs;
- deployment, migration, rollback, restore, failover, continuity, and disaster recovery;
- runbooks, automation, on-call access, escalation, communications, and incident command;
- support scope, diagnostics, known limitations, vulnerability intake, and supplier obligations;
- data integrity, backup currency, retention, reconciliation, and irreversible-change controls;
- cost, licensing, external-provider limits, and operational sustainability.

Documents alone are evidence of preparation, not evidence that a procedure
works. Exercise critical recovery and response paths at depth proportional to risk.

## Workflow

### 1. Define context and authority

- Identify release, targets, consumers, operating model, service requirements,
  risk tolerance, change window, and acceptance authority.
- Define measurable criteria, observation windows, and non-negotiable constraints.
- Record which criteria require production, production-like, external-provider,
  exercise, document-review, or human-readiness evidence.

### 2. Establish the target baseline

- Resolve target infrastructure, configuration, policies, dependencies,
  credentials, data state, and currently active release by immutable identity.
- Check for drift, conflicting changes, capacity constraints, and expiring dependencies.
- Confirm access and segregation needed to deploy, observe, recover, and support.

### 3. Assess operability and observability

- Verify health semantics, telemetry paths, dashboards, logs, traces, metrics,
  alert delivery, ownership, and diagnostic correlation.
- Test that signals detect meaningful failure rather than only process startup.
- Confirm service objectives and thresholds connect to release/rollback decisions.
- Verify telemetry protection, retention, clock/time assumptions, and blind spots.

### 4. Exercise deployment and recovery

- Rehearse or execute deployment, migration, smoke checks, rollback, restore,
  failover, and recovery at the selected depth and coverage.
- Measure recovery results against declared objectives and data-loss constraints.
- Test degraded and dependency-failure behavior where material.
- Record blocked exercises and untested destructive paths as residual risk.

### 5. Confirm people and support readiness

- Verify current runbooks against the actual release and target.
- Confirm on-call coverage, access, escalation, communications, support scope,
  diagnostic tooling, supplier contacts, and vulnerability intake.
- Ensure known limitations and customer/operator impacts are communicated.
- Obtain acknowledgements from accountable operations and support owners.

### 6. Decide and hand off

- Aggregate candidate-bound technical evidence with target-bound operational evidence.
- Record `accept`, `accept-with-conditions`, `hold`, or `reject`; translate an
  accepted result into the Production release vocabulary only through the release authority.
- For conditions, name owner, compensating control, expiry, review trigger, and rollback threshold.
- Transfer the verified active baseline, operating context, limitations, and
  evidence to Utilization and Support after release.

## Operational handoff contract

When another team or system will deploy, operate, support, or recover the
release, provide a self-contained handoff bound to the exact candidate and
target. It should identify:

- immutable artifact and source identities and where their verified
  coordinates come from;
- target-owned prerequisites and unresolved placeholders without inventing values;
- ordered deployment, configuration, migration, and synchronization actions;
- secret document and consumer identities without plaintext;
- observability, readiness, acceptance, rollback, restore, and escalation checks;
- known limitations, residual risks, conditions, owners, and decision authority;
- what has been verified, what remains operator action, and what would
  invalidate the handoff.

Do not mix independently built release components when the release-unit
contract requires a coherent set. Do not use moving aliases when immutable
identity is required. Preserve stable environment identity and credentials
across ordinary upgrades unless an authorized migration or rotation says
otherwise. Unknown environment-owned values remain explicit inputs.

A handoff is information and acknowledgement, not evidence that its commands
were executed. After execution, reconcile the actual active state and record
acceptance findings separately.

## Decision rules

Use `accept` only when mandatory criteria are satisfied and accountable owners
can operate and recover the exact release in the exact target context. Use
`accept-with-conditions` only within explicit authority and risk tolerance. Use
`hold` for remediable readiness or evidence gaps and `reject` when the target
cannot safely sustain the release.

Acceptance expires when the release, material configuration, target topology,
provider, operating assumptions, or required evidence freshness changes.

[12207]: https://www.iso.org/standard/90219.html
[15288]: https://www.iso.org/standard/81702.html
[20000]: https://www.iso.org/standard/70636.html
[25010]: https://www.iso.org/standard/78176.html
[25019]: https://www.iso.org/standard/78177.html
[25040]: https://www.iso.org/standard/83467.html
