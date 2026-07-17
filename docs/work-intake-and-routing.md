# Work Intake and Routing

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Concept](stages/concept.md) · [Development](stages/development.md)

## Purpose

This document defines the decision boundary between an incoming work item and
the SDLC workflow used to handle it. The route is selected from evidence about
intent, uncertainty, consequence, reversibility, scope, and authority—not from
ticket labels or the apparent size of the requested diff.

Projects provide their issue system, branch convention, ownership model, and
artifact locations. The harness provides portable routing semantics.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Lifecycle, decision management, planning, assessment, risk, and technical processes | Published |
| [ISO/IEC/IEEE 24748-1:2024][24748-1] | Lifecycle tailoring, decision points, and stage relationships | Published |
| [ISO/IEC/IEEE 24748-5:2017][24748-5] | Software development planning and management | Published; confirmed |
| [ISO/IEC/IEEE 29148:2018][29148] | Requirements-engineering inputs and information items | Published; revision underway |

## Intake record

Preserve, directly or by controlled references:

- request identity, source, accountable requester, urgency, and desired outcome;
- affected users, systems, interfaces, data, supported baselines, and obligations;
- problem evidence and whether the request states a need, a preferred solution, or both;
- known requirements, acceptance intent, constraints, assumptions, dependencies, and exclusions;
- consequence of error, exposure, reversibility, uncertainty, and required decision authority;
- selected route, rationale, required artifacts, owners, next decision, and unresolved questions.

Intake accepts work for analysis; it does not authorize implementation or make
an unclear request clear by assumption.

## Route vocabulary

| Route | Select when | Required next workflow |
| --- | --- | --- |
| `direct-change` | Intent, boundary, acceptance, and implementation are obvious; risk and blast radius are low | Focused implementation with tests and review |
| `specification` | Desired behavior or acceptance is incomplete, ambiguous, or materially changing | `spec-driven-development` and requirements work |
| `design-dialogue` | Architecture, public contract, security, data ownership, migration, or expensive-to-reverse choices need approval | Options, trade-offs, decision, then specification/plan |
| `investigation` | Cause, feasibility, current behavior, or evidence is unknown | Read-only diagnosis, experiment, or research; no implied implementation |
| `planned-change` | Requirements are adequate but dependencies and execution order need a persistent plan | `planning-and-task-breakdown` |
| `incident-or-support` | Active operational harm, defect, vulnerability, or supported-baseline issue dominates | Utilization/Support control before Development change |
| `production-only` | Candidate is unchanged and the task concerns build, provenance, promotion, acceptance, or rollout | Production workflow |
| `retirement` | The intended outcome is removal, end of support, data disposition, or closure | Retirement/deprecation workflow |
| `hold-or-reject` | Authority, need, feasibility, prerequisite, or acceptable risk is absent | Record rationale and required unblock condition |

Routes may compose. An investigation can produce a specification; an approved
design dialogue can produce a planned change. Record every route transition.

## Workflow

1. Establish repository and work-item state without mutating external systems.
2. Separate the underlying need and evidence from the proposed implementation.
3. Map affected lifecycle stages, baselines, consumers, contracts, and owners.
4. Assess uncertainty, consequence, reversibility, exposure, novelty, coupling,
   data/security impact, migration needs, and external dependencies.
5. Select the smallest route that controls the material risk. Escalate when a
   route discovers a wider boundary; do not silently downgrade required work.
6. Define required artifacts, skills, decisions, evidence, and immediate next action.
7. Record assumptions and blocking questions. Ask only for choices that cannot
   be safely discovered or reasonably deferred.

## Decision rules

Use `direct-change` only when no material requirement, architectural, security,
data, compatibility, migration, or acceptance decision is hidden. A small diff
can require design dialogue; a large mechanical change can be planned without a
new product specification. External issue mutation, branch creation, assignment,
or acceptance requires the authority provided by the user and local project.

[12207]: https://www.iso.org/standard/90219.html
[24748-1]: https://www.iso.org/standard/84709.html
[24748-5]: https://www.iso.org/standard/60062.html
[29148]: https://www.iso.org/standard/72089.html
