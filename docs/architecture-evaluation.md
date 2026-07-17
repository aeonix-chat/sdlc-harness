# Architecture Evaluation

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Development](stages/development.md) ·
[Requirements and Traceability](requirements-and-traceability.md)

## Purpose

This document defines how to decide whether an architecture description and
its decisions are sufficient for the concerns, requirements, risks, and change
under consideration. It does not prescribe a diagram notation, methodology, or
central architecture board.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 42010:2022][42010] | Architecture-description concepts, stakeholders, concerns, viewpoints, views, models, decisions, and rationale | Published |
| [ISO/IEC/IEEE 12207:2026][12207] | Architecture definition, design definition, analysis, decision, risk, and V&V context | Published |
| [ISO/IEC 25010:2023][25010] | Product quality characteristics for scenarios and evaluation | Published |
| [ISO/IEC 20246:2017][20246] | Generic work-product review process and evidence | Published; confirmed 2022 |

ISO/IEC/IEEE 42010 specifies architecture-description structure; it does not
mandate one architecting or evaluation method. The harness therefore selects
techniques according to the decision and risk.

## Evaluation record

Preserve:

- entity and architecture-description version being evaluated;
- stakeholders, concerns, context, boundaries, assumptions, and applicable requirements;
- viewpoints, views, models, correspondence rules, and known inconsistencies;
- scenarios and criteria for quality, failure, change, security, privacy,
  safety, operation, support, deployment, migration, and retirement as applicable;
- alternatives, analyses, prototypes, experiments, measurements, and trade-offs;
- decisions, rationale, rejected alternatives, consequences, debt, risks, and owners;
- findings, limitations, required actions, reviewer independence, and verdict.

## Workflow

1. Frame the decision: identify what must be decided, why now, authority,
   reversibility, affected baselines, and evidence needed.
2. Identify stakeholders and concerns. Select only viewpoints and models needed
   to address them; do not produce diagrams without a question they answer.
3. Verify description coherence: boundaries, responsibilities, interfaces,
   data flows, trust zones, deployment, failure behavior, dependencies, and
   requirement allocations must be mutually consistent.
4. Define concrete scenarios with stimulus, context, affected element,
   expected response, and measurable criterion.
5. Evaluate alternatives with appropriate analysis, review, model, prototype,
   experiment, threat analysis, performance measurement, or failure exercise.
6. Identify sensitivity points, trade-offs, coupling, irreversible choices,
   operational burden, migration cost, and uncertainty.
7. Record decisions and rejected alternatives in the project's durable format.
8. Issue `sufficient`, `sufficient-with-actions`, `rework`, or `blocked` for the
   stated scope. Link actions to plan tasks and requirements.

## Guardrails

- Code existence is evidence about the implemented architecture, not proof that
  the architecture satisfies stakeholder concerns.
- An ADR records a decision; it does not replace evaluation evidence.
- A diagram is neither a complete architecture description nor an evaluation.
- Review the actual cross-boundary behavior and failure semantics, not only module names.
- Re-evaluate when material requirements, context, topology, dependencies,
  trust boundaries, data ownership, or assumptions change.

Use `sufficient` only when material concerns have applicable views and evidence,
trade-offs and residual risks have owners, contradictions are resolved, and
implementation can proceed without hidden architectural decisions.

[42010]: https://www.iso.org/standard/74393.html
[12207]: https://www.iso.org/standard/90219.html
[25010]: https://www.iso.org/standard/78176.html
[20246]: https://www.iso.org/standard/67407.html
