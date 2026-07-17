---
name: continuity-and-restore-validation
description: Validates backup integrity, data and service restoration, failover, degraded operation, recovery objectives, external dependencies, and continuity capability through controlled exercises. Use when reviewing backups, planning or executing restore tests, disaster-recovery exercises, failover validation, RTO/RPO evidence, or continuity readiness after material change.
---

# Continuity and Restore Validation

Read [`../../../docs/continuity-and-restore-validation.md`](../../../docs/continuity-and-restore-validation.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use project-provided backup, recovery, infrastructure, credential, supplier,
exercise, and communication mechanisms.

## Workflow

1. Derive critical services, minimum acceptable capacity, recovery time and
   data-loss objectives, dependencies, obligations, threats, and authority.
2. Inventory required data, state, services, infrastructure, providers,
   credentials, keys, tools, people, communications, and recovery environments.
3. Verify backup/replication scope, integrity, encryption, isolation,
   retention, immutability, access, monitoring, and restoration instructions.
4. Select exercise depth: review, walkthrough, component restore, partial
   failover, full service recovery, or broader continuity simulation.
5. Establish authorization, safe isolation, stop conditions, evidence capture,
   communications, and protection against production or data harm.
6. Execute once and preserve real results. Verify data semantics, application
   behavior, security, dependencies, configuration, observability, user journeys,
   capacity, and reconciliation.
7. Measure elapsed time, data loss, manual steps, bottlenecks, hidden
   dependencies, access failures, and objective compliance.
8. Record `capable`, `capable-with-gaps`, `not-capable`, or `blocked`, with
   risks, owners, corrections, expiry, and retest.

## Guardrails

- Backup success is not restore or continuity proof.
- Do not conduct destructive exercises without explicit authority.
- Do not claim boundaries, dependencies, or capacity that were not exercised.
- Invalidate claims after material data, topology, provider, credential, key,
  architecture, objective, or freshness change.

## Completion

Require scope-bound exercise evidence, measured objectives, verified restored
behavior and data, dependency coverage, explicit gaps, accountable acceptance,
and scheduled retest where needed.
