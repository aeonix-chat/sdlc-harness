# Release and Promotion

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md) ·
[Artifact Integrity and Provenance](artifact-integrity-and-provenance.md)

## Purpose

This document defines how an immutable candidate moves through repositories,
environments, deployment states, and authorization points without losing
identity or evidence. Projects provide the concrete pipeline, environments,
approval system, deployment mechanism, and release topology.

Promotion changes the authorized state or location of the same artifact.
Rebuilding or modifying it creates a new candidate. Publishing, deploying,
releasing, and rolling out remain distinct events.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Software lifecycle, configuration, transition, information, and decision processes | Published |
| [ISO/IEC/IEEE 24748-1:2024][24748] | Lifecycle decision points, stage transitions, and tailoring | Published |
| [ISO/IEC 20000-1:2018][20000] | Controlled service planning, transition, delivery, measurement, and improvement | Published; confirmed 2023 |
| [NIST SP 800-204D][800-204d] | Supply-chain controls across build, test, package, and deployment pipelines | Final |

## Promotion record

Every material transition should preserve:

- release and artifact immutable identities;
- source and destination repositories, environments, or exposure states;
- exact configuration, policy, migration, and feature-state identities;
- entry criteria, required evidence, findings, exceptions, and risk acceptance;
- requester, automation identity, approver/authority, timestamps, and segregation of duties;
- deployment result, active-state verification, rollout scope, and observations;
- rollback target, trigger, authority, execution result, and resulting active state;
- links to superseded, quarantined, revoked, or withdrawn releases.

## Workflow

### 1. Model the release path

- Define repositories, environments, consumer channels, exposure steps, and authorities.
- Name each transition and its entry, hold, rejection, rollback, and completion states.
- Separate artifact promotion from configuration change, deployment, release,
  rollout, and migration even when one pipeline performs them together.
- Define concurrency, supersession, emergency, and partial-failure behavior.

### 2. Accept the candidate

- Resolve candidate and artifacts by immutable identity.
- Verify required provenance, composition, signatures, validation findings, and exceptions.
- Freeze the release set and record permitted metadata-only changes.
- Reject evidence that refers to a different digest or mutable alias.

### 3. Promote without rebuilding

- Copy or grant access to the same verified bytes through authorized channels.
- Recompute and compare digests at trust-boundary crossings.
- Preserve evidence associations and audit identity across repositories.
- Quarantine on mismatch, unauthorized substitution, or missing policy evidence.

### 4. Deploy and migrate under control

- Bind deployment to target configuration, infrastructure, secrets policy,
  data migration, feature state, and rollback target.
- Apply least privilege and separation of duties proportional to risk.
- Prevent concurrent or out-of-order changes from invalidating the baseline.
- Preserve the real deployment result and partial state; do not label a failed
  deployment as a successful promotion.

### 5. Authorize release and rollout

- Evaluate current validation and operational-acceptance evidence.
- Record `release`, `hold`, `rebuild`, `rollback`, or `stop` with authority,
  rationale, conditions, expiry, evidence, and residual risk.
- Expand exposure only within defined thresholds and observation windows.
- Stop or roll back automatically where pre-authorized triggers apply; otherwise escalate.

### 6. Reconcile active state

- Verify the artifact and configuration actually active in every target.
- Compare desired, deployed, released, and exposed states.
- Record drift, partial rollout, supersession, rollback, and consumer/channel status.
- Hand the active baseline and operating context to Utilization and Support.

## Decision rules

Promotion succeeds only when the same artifact crosses the boundary, required
evidence remains valid, authority is established, and destination state is
reconciled. Use `rebuild` for payload or provenance failure, `hold` for a
time-bounded prerequisite or approval gap, `rollback` for unacceptable active
state, and `stop` when safe authorization is unavailable.

Emergency paths may reduce lead time, not identity, auditability, risk ownership,
rollback capability, or retrospective review.

[12207]: https://www.iso.org/standard/90219.html
[24748]: https://www.iso.org/standard/84709.html
[20000]: https://www.iso.org/standard/70636.html
[800-204d]: https://csrc.nist.gov/pubs/sp/800/204/d/final
