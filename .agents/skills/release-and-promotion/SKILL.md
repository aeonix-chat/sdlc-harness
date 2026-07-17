---
name: release-and-promotion
description: Promotes immutable release candidates through repositories, environments, deployment states, release authorization, rollout, rollback, and active-state reconciliation. Use when designing or executing a promotion path, moving a candidate between environments, publishing or deploying a release, deciding release readiness, handling emergency release flow, or proving what version is active.
---

# Release and Promotion

Read [`../../../docs/release-and-promotion.md`](../../../docs/release-and-promotion.md),
[`../../../docs/artifact-integrity-and-provenance.md`](../../../docs/artifact-integrity-and-provenance.md),
and the applicable stage guidance. Use project-provided pipeline, deployment,
approval, environment, and rollback mechanisms.

## Workflow

1. Map repositories, environments, consumer channels, exposure steps,
   authorities, entry criteria, failure states, and rollback paths.
2. Accept the candidate by immutable artifact identity. Verify required
   provenance, composition, signatures, validation findings, exceptions, and
   operational acceptance. Freeze the release set.
3. Promote the same bytes through authorized channels. Recompute digests at
   trust boundaries and preserve evidence associations. Quarantine mismatches.
4. Bind deployment to target configuration, infrastructure, policies, data
   migration, feature state, and rollback target. Preserve partial and failed state.
5. Evaluate current evidence and record `release`, `hold`, `rebuild`,
   `rollback`, or `stop` with authority, rationale, conditions, and risk.
6. Roll out only within approved exposure, thresholds, and observation windows.
   Apply pre-authorized stop or rollback triggers without broadening authority.
7. Reconcile desired, promoted, deployed, released, and exposed state. Verify
   the exact artifact/configuration active in each target and hand it to
   Utilization and Support.

## Guardrails

- Promotion never means rebuilding or modifying the artifact.
- Keep publish, deploy, release, and rollout events distinct in evidence.
- Never use mutable tags as the sole release identity.
- Do not label a successful pipeline step as a successful release decision.
- Emergency flow may shorten lead time, not remove identity, audit, rollback,
  risk ownership, or retrospective review.
- Do not authorize a transition unless project policy grants that authority.

## Completion

Require identical artifact verification across boundaries, current evidence,
authorized decision, explicit configuration and migration state, target
reconciliation, rollback readiness, and a traceable active-baseline handoff.
