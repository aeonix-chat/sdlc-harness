# Development Candidate Readiness

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Development](stages/development.md) · [Production](stages/production.md)

## Purpose

This document defines the Development decision that identifies an exact
integrated candidate and transfers it, with bounded evidence and known risk, to
Production. A merged change, green pull request, passing unit suite, or mutable
branch is not by itself a Development candidate.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Integration, V&V, transition, configuration, quality, risk, and decision processes | Published |
| [ISO/IEC/IEEE 24748-5:2017][24748-5] | Development planning, control, assessment, and information | Published; confirmed |
| [ISO/IEC/IEEE 29119-2:2021][29119-2] | Test planning, monitoring, control, completion, and reporting | Published |
| [ISO/IEC/IEEE 29119-3:2021][29119-3] | Test documentation and result information | Published |
| [ISO/IEC 20246:2017][20246] | Review of requirements, architecture, plans, code, tests, and other work products | Published; confirmed |
| [ISO 10007:2017][10007] | Configuration-management guidance and baseline control | Published |

## Candidate package

Preserve the following semantics, using project-defined storage:

- immutable or otherwise unambiguous source, dependency, configuration,
  migration, build-definition, tool, and integrated-candidate identities;
- approved requirements and acceptance baseline with traceability and change history;
- architecture/design decisions, interface contracts, and evaluation findings;
- implementation and integration scope, review results, and unresolved anomalies;
- verification and validation claims, boundaries, environments, findings, and evidence;
- security, privacy, safety, performance, accessibility, operability, support,
  migration, rollback, recovery, documentation, and training evidence as applicable;
- defects, deviations, debt, exceptions, limitations, residual risks, owners, and expiry;
- Production, operations, and support prerequisites and handoff acknowledgement;
- decision, authority, timestamp, rationale, conditions, and evidence references.

## Workflow

1. Freeze or control the candidate scope and resolve it independently of mutable aliases.
2. Reconcile planned, implemented, integrated, documented, and excluded scope.
3. Verify requirements coverage and dispose orphan implementation, stale links,
   changed assumptions, and superseded evidence.
4. Confirm architecture/interface coherence and close blocking review findings.
5. Aggregate candidate-bound verification and validation; separate passed,
   failed, blocked, inconclusive, not-applicable, and waived work.
6. Review security and specialty findings, defects, deviations, debt, and
   residual risks with accountable owners and authority.
7. Confirm transition feasibility: build inputs, dependencies, configuration,
   migrations, rollback, recovery, observability, support, and consumer information.
8. Perform an independent or appropriately separated evidence review where risk requires it.
9. Record `candidate`, `rework`, `hold`, or `stop` and transfer the exact
   candidate plus evidence package to Production.

## Decision rules

Issue `candidate` only when:

- the exact integrated baseline is identifiable and controlled;
- applicable requirements and acceptance criteria have current disposition;
- architecture, interfaces, implementation, and evidence describe the same system;
- required integration, verification, validation, reviews, and specialty checks are complete;
- failures and gaps are not represented as success;
- deviations and residual risks are accepted within explicit authority;
- Production can reproduce or consume the candidate inputs without hidden knowledge;
- operations and support readiness prerequisites have accountable disposition.

Use `rework` when the candidate or its evidence must change; `hold` for a
time-bounded external prerequisite, approval, or environment gap; and `stop`
when authority, feasibility, justified need, or acceptable risk is absent. Any
material candidate change invalidates affected evidence and the decision.

[12207]: https://www.iso.org/standard/90219.html
[24748-5]: https://www.iso.org/standard/60062.html
[29119-2]: https://www.iso.org/standard/79428.html
[29119-3]: https://www.iso.org/standard/79429.html
[20246]: https://www.iso.org/standard/67407.html
[10007]: https://www.iso.org/standard/70400.html
