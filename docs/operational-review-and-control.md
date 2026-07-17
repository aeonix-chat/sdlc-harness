# Operational Review and Control

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Utilization](stages/utilization.md) ·
[Service Objectives and Telemetry](service-objectives-and-telemetry.md)

## Purpose

This document defines the recurring evidence review that determines whether an
active service should continue, be constrained, recover, change, or retire.
Projects provide the service catalog, configuration inventory, risk register,
review cadence, decision system, dashboards, and automation.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC 20000-1:2018][20000] | Service monitoring, measurement, review, reporting, control, and improvement | Published; confirmed 2023 |
| [ISO/IEC/IEEE 12207:2026][12207] | Operation, configuration, measurement, risk, decision, maintenance, and retirement relationships | Published |
| [ISO/IEC/IEEE 15939:2017][15939] | Valid decision-oriented measurement | Published; confirmed 2022 |
| [ISO/IEC 25019:2023][25019] | Quality-in-use evaluation in the current context | Published |

## Review package

Preserve active release/configuration identity, drift, consumers, service
objectives, telemetry validity, incidents/problems, security/privacy state,
capacity/cost, dependencies/suppliers, continuity evidence, quality in use,
outcomes, obligations, exceptions, risks, previous actions, and decision authority.

## Workflow

1. Trigger review at the risk-based cadence and after material incident,
   release, drift, dependency, threat, obligation, or context change.
2. Reconcile desired, authorized, deployed, active, and exposed release and
   configuration state. Record unexplained drift and unknown populations.
3. Validate evidence freshness and quality before interpreting objectives.
4. Review service/user outcomes, reliability, security, privacy, continuity,
   supportability, capacity, cost, supplier/dependency health, and obligations.
5. Compare current state with operating envelope, thresholds, accepted risks,
   exception expiry, and previous decision conditions.
6. Dispose incidents, problems, vulnerabilities, gaps, debt, and overdue
   actions; route work to Support, Concept, Development, Production, or Retirement.
7. Record `continue`, `constrain`, `recover`, `change`, or `retire`, scoped to
   the affected component/population, with authority, rationale, evidence,
   conditions, expiry, and next review.
8. Verify action ownership and later effectiveness; a recorded decision without
   executed controls does not change operational risk.

## Decision rules

Use `continue` only inside the approved operating envelope with current credible
evidence. Use `constrain` for bounded exposure reduction, `recover` for the
approved restoration path, `change` for accountable lifecycle work, and
`retire` to initiate controlled closure. Automation may recommend or execute
pre-authorized reversible controls; it must not silently accept risk or make an
irreversible retirement decision without delegated authority.

[20000]: https://www.iso.org/standard/70636.html
[12207]: https://www.iso.org/standard/90219.html
[15939]: https://www.iso.org/standard/71197.html
[25019]: https://www.iso.org/standard/78177.html
