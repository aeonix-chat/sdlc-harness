# Continuity and Restore Validation

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Utilization](stages/utilization.md) · [Operational Acceptance](operational-acceptance.md)

## Purpose

This document defines evidence that required data, services, dependencies, and
business operations can be restored or continued within declared conditions.
Projects provide backup, replication, failover, disaster-recovery, exercise,
infrastructure, credential, and communication mechanisms.

A successful backup job proves neither restore integrity nor service continuity.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO 22301:2019][22301] | Business continuity management, disruption response, recovery, and predefined operating capacity | Published; revision underway |
| [ISO 22313:2020][22313] | Guidance for applying ISO 22301 | Published; revision underway |
| [ISO/IEC 20000-1:2018][20000] | Service availability, continuity, transition, operation, and improvement | Published; confirmed 2023 |
| [ISO/IEC 27031:2025][27031] | ICT readiness for business continuity, including external service dependencies | Published |

## Capability contract

Define critical products/services, minimum acceptable capacity, recovery time
and data-loss objectives, dependencies, data sets, sites/regions, identities,
keys, suppliers, people, communication, assumptions, exercise scope, and
acceptance authority. Bind all evidence to the active architecture and baseline.

## Workflow

1. Derive continuity needs from business impact, obligations, safety, user
   needs, dependency failure, threat, and active architecture.
2. Inventory data, state, services, dependencies, credentials, keys, tooling,
   people, suppliers, and recovery environments needed for restoration.
3. Define backup/replication scope, integrity, encryption, isolation,
   retention, immutability, access, monitoring, and restore procedure.
4. Select an exercise: document review, walkthrough, component restore,
   partial failover, full service recovery, or broader continuity simulation.
   Match depth to consequence and avoid claiming unexercised boundaries.
5. Establish safe test isolation, authorization, stop conditions, evidence
   capture, communications, and protection against production/data harm.
6. Execute once, preserve real results, and verify restored data semantics,
   application behavior, security, dependencies, configuration, observability,
   user journeys, capacity, and reconciliation.
7. Measure time, data loss, manual steps, bottlenecks, hidden dependencies,
   access failures, and divergence from objectives.
8. Record findings, risks, owners, corrective actions, expiry, and retest.

## Decision rules

Use `capable` only for the exact scope and conditions exercised. Use
`capable-with-gaps`, `not-capable`, or `blocked` when objectives, dependencies,
evidence, or authority are incomplete. Do not conduct destructive tests without
explicit authorization. Invalidate capability claims after material changes to
data, topology, providers, credentials, keys, architecture, objectives, or
exercise freshness.

[22301]: https://www.iso.org/standard/75106.html
[22313]: https://www.iso.org/standard/75107.html
[20000]: https://www.iso.org/standard/70636.html
[27031]: https://www.iso.org/standard/27031
