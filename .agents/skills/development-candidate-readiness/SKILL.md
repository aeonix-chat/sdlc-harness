---
name: development-candidate-readiness
description: Assembles and reviews the exact integrated Development candidate, requirements coverage, architecture coherence, verification and validation evidence, findings, deviations, residual risks, and transition prerequisites. Use before handing work to Production, declaring a feature or change complete, freezing a candidate, or deciding candidate, rework, hold, or stop.
---

# Development Candidate Readiness

Read [`../../../docs/development-candidate-readiness.md`](../../../docs/development-candidate-readiness.md),
[`../../../docs/stages/development.md`](../../../docs/stages/development.md), and
[`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md)
before making the readiness assessment.

## Workflow

1. Resolve the exact integrated source, dependency, configuration, migration,
   build-definition, tool, and candidate identities without mutable aliases.
2. Freeze or control scope. Reconcile requested, planned, implemented,
   integrated, documented, and excluded work.
3. Reconcile requirements and acceptance coverage, orphan scope, changed
   assumptions, stale evidence, deviations, and superseded findings.
4. Confirm architecture/interface coherence and disposition blocking work-product reviews.
5. Aggregate candidate-bound verification and validation. Separate `satisfied`,
   `not_satisfied`, `blocked`, `inconclusive`, `not_applicable`, and waived work.
6. Review security and specialty findings, defects, debt, limitations,
   exceptions, residual risks, owners, authority, and expiry.
7. Confirm Production and transition prerequisites: reproducible inputs,
   dependencies, configuration, migrations, rollback, recovery, observability,
   support, documentation, training, and consumer information as applicable.
8. Apply appropriate reviewer independence and issue `candidate`, `rework`,
   `hold`, or `stop` with rationale, evidence, conditions, and authority.
9. Transfer the exact candidate and evidence package to Production; any
   material candidate change invalidates affected evidence and the decision.

## Guardrails

- A merge, green PR, mutable branch, or passed unit suite is not a candidate decision.
- Never aggregate evidence from different candidate identities as one result.
- Never convert failed, blocked, inconclusive, or omitted work into success.
- Use `rework` when candidate content or evidence must change, `hold` for a
  time-bounded external gap, and `stop` when authority, feasibility, need, or
  acceptable risk is absent.
- Do not authorize Production release; this workflow owns only Development readiness.

## Completion

Require exact identity, scope reconciliation, current traceability, coherent
architecture, candidate-bound evidence, owned risks, transition feasibility,
authorized decision, and acknowledged Production handoff.
