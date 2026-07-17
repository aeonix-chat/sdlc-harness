# Requirements and Traceability

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Development](stages/development.md) ·
[Validation and Evidence](validation-and-evidence.md)

## Purpose

This document defines how stakeholder needs become controlled, verifiable
requirements and how their relationships remain visible through architecture,
implementation, verification, validation, deviations, and candidate decisions.
Projects choose storage and identifiers; the semantic graph is portable.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 29148:2018][29148] | Requirements processes, characteristics, attributes, and information items | Published; confirmed 2024, revision underway |
| [ISO/IEC/IEEE 12207:2026][12207] | Stakeholder, system/software requirements, V&V, configuration, and information processes | Published |
| [ISO/IEC 25010:2023][25010] | Product quality model for quality requirements and acceptance | Published |
| [ISO/IEC 25030:2019][25030] | Quality requirements elicitation, definition, and governance | Published; confirmed |
| [ISO/IEC/IEEE 15939:2017][15939] | Measures connected to explicit information needs | Published; confirmed |

## Requirement contract

A material requirement should identify:

- stable identifier, statement, type, source, rationale, owner, priority, and status;
- affected baseline, users, system boundary, interfaces, data, and operating context;
- assumptions, constraints, dependencies, conflicts, risks, and applicability;
- measurable acceptance criteria and planned verification/validation method;
- allocation to architecture elements, interfaces, implementation, and tests;
- change history, approvals, supersession, deviations, and residual risk.

Requirements should be necessary, implementation-neutral where appropriate,
unambiguous, feasible, singular enough to assess, and verifiable. Acceptance
criteria must not be invented after implementation merely to match observed behavior.

## Traceability graph

Maintain bidirectional links across applicable nodes:

```text
need / risk / obligation
  -> requirement + acceptance criterion
  -> architecture concern / decision / interface
  -> plan task / change set / configured implementation
  -> verification finding
  -> validation finding
  -> defect / deviation / residual risk
  -> candidate and Development decision
```

Traceability is a decision aid, not a demand for one database or exhaustive
links to every line. Tailor granularity to consequence and change frequency.

## Workflow

1. Establish stakeholder needs, contexts, sources, owners, conflicts, and outcome measures.
2. Define functional, interface, data, quality, security, privacy, safety,
   operational, support, migration, and retirement requirements as applicable.
3. Define acceptance criteria and assessment methods with each requirement.
4. Review quality, feasibility, consistency, completeness, risks, and testability.
5. Baseline approved requirements and record authority, version, assumptions, and open issues.
6. Allocate requirements to architecture, interfaces, increments, and evidence.
7. Maintain forward and backward links as design and implementation evolve.
8. Perform impact analysis before accepting a requirement or baseline change.
9. Reconcile coverage, orphan implementation, stale evidence, deviations, and
   unresolved risks before candidate readiness.

## Change and coverage rules

- A changed requirement invalidates affected design, implementation, tests,
  evidence, documentation, and decisions until impact is assessed.
- Implementation without a need, requirement, risk treatment, or authorized
  enabling rationale is orphan scope and requires disposition.
- A passed check without a requirement/claim and applicable boundary is not coverage.
- `not_applicable`, waived, deferred, and superseded requirements remain visible
  with authority and rationale; they are not deleted to improve coverage metrics.
- Coverage quantity does not prove requirement quality or fitness for use.

Completion requires an approved baseline, no unexplained contradictions or
orphan scope, current bidirectional links, explicit gaps, and candidate-bound
verification and validation findings for all applicable acceptance criteria.

[29148]: https://www.iso.org/standard/72089.html
[12207]: https://www.iso.org/standard/90219.html
[25010]: https://www.iso.org/standard/78176.html
[25030]: https://www.iso.org/standard/72116.html
[15939]: https://www.iso.org/standard/71197.html
