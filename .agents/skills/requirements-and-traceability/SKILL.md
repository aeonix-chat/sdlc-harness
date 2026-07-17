---
name: requirements-and-traceability
description: Defines, baselines, changes, and reconciles requirements and their bidirectional links from stakeholder needs through acceptance criteria, architecture, implementation, verification, validation, deviations, and candidate decisions. Use for new capabilities, behavior changes, public contracts, regulated or risk-sensitive work, requirements changes, coverage audits, or candidate-readiness gaps.
---

# Requirements and Traceability

Read [`../../../docs/requirements-and-traceability.md`](../../../docs/requirements-and-traceability.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md)
before using this workflow. Use project-defined identifiers and storage.

## Workflow

1. Establish needs, contexts, sources, owners, outcomes, conflicts, assumptions,
   constraints, dependencies, risks, and affected baselines.
2. Define applicable functional, interface, data, quality, security, privacy,
   safety, operational, support, migration, and retirement requirements.
3. Give each material requirement a stable identity, rationale, owner, status,
   applicability, measurable acceptance criteria, and planned assessment method.
4. Review necessity, ambiguity, feasibility, consistency, completeness,
   singularity, testability, and conflicts. Resolve or record gaps before baselining.
5. Baseline with version and authority. Link requirements to architecture,
   interfaces, plan tasks, changes, tests, findings, deviations, and risks.
6. Before any change, perform impact analysis across downstream and upstream links.
7. Reconcile forward and backward coverage before candidate readiness: find
   uncovered requirements, orphan implementation, stale evidence, invalidated
   assumptions, and hidden scope.
8. Record approved, superseded, deferred, waived, and not-applicable outcomes
   without deleting them from history.

## Guardrails

- Do not write acceptance criteria after implementation merely to match behavior.
- Do not equate a passing test count with requirements coverage.
- Do not hide gaps by deleting or weakening requirements without authority.
- Treat implementation without a need, risk treatment, or authorized enabling
  rationale as orphan scope requiring disposition.
- Invalidate affected evidence when requirements or assumptions change.

## Completion

Require an approved baseline, explicit conflicts/gaps, current bidirectional
links, no unexplained orphan scope, and candidate-bound findings for applicable criteria.
