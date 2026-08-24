---
name: environment-state-inspection
description: Inspects an exact live environment through a safe read-only boundary. Use when resolving deployed artifact and configuration identity, readiness, restarts, topology, drift, recent errors, diagnostic signals, or access gaps without changing the environment.
---

# Environment State Inspection

Read [`../../../docs/environment-state-inspection.md`](../../../docs/environment-state-inspection.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use only project-approved read-only clients, commands, scopes, and redaction rules.

## Workflow

1. Identify exact environment context, expected baseline, time window, operator
   identity, and read authority.
2. Resolve active artifact/configuration identities, topology, status,
   readiness, restarts, events, and recent transitions.
3. Compare controlled desired state, control-plane reported state, and observed
   behavior without conflating their claims.
4. Inspect narrowly filtered logs, signals, and approved non-mutating probes.
5. Record confirmed, inferred, inconclusive, blocked, and out-of-bound findings
   separately with timestamps and sanitized evidence references.
6. Name drift, blind spots, invalidation conditions, and the next authorized
   incident, change, acceptance, or review workflow.

## Guardrails

- Never read or print secret values, environment dumps, credential-bearing
  arguments, or rendered secret objects.
- Do not restart, scale, patch, apply, delete, rotate, sync, rerun, acknowledge,
  or alter traffic.
- Repository templates are desired-state evidence, not live-state evidence.
- Inspection does not authorize acceptance, release, repair, or risk acceptance.

## Completion

Require exact target and time boundaries, resolved active identities where
accessible, separated desired/reported/observed findings, sanitized evidence,
explicit gaps, and no environment mutation.
