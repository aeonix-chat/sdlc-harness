---
name: architecture-evaluation
description: Evaluates architecture descriptions and decisions against stakeholder concerns, requirements, quality and failure scenarios, alternatives, trade-offs, coupling, migration, and residual risk. Use before expensive-to-reverse design choices, public interface or data-ownership changes, cross-system integration, security-boundary changes, major migrations, or candidate readiness when architectural sufficiency is uncertain.
---

# Architecture Evaluation

Read [`../../../docs/architecture-evaluation.md`](../../../docs/architecture-evaluation.md)
and [`../../../docs/requirements-and-traceability.md`](../../../docs/requirements-and-traceability.md)
before evaluating architecture.

## Workflow

1. Define the decision, entity, architecture-description version, affected
   baseline, authority, urgency, reversibility, and required evidence.
2. Identify stakeholders, concerns, context, boundaries, assumptions, and
   requirements. Select viewpoints and models that answer those concerns.
3. Check coherence across responsibilities, interfaces, data flows, trust
   boundaries, deployment, dependencies, failure behavior, and requirement allocation.
4. Define concrete scenarios with stimulus, context, affected element,
   expected response, and measurable criterion.
5. Compare viable alternatives using review, analysis, model, prototype,
   experiment, threat analysis, measurement, or failure exercise as appropriate.
6. Identify sensitivity points, trade-offs, coupling, operational burden,
   migration cost, irreversible choices, uncertainty, debt, and residual risk.
7. Record decisions, rationale, rejected alternatives, consequences, owners,
   actions, and invalidation conditions in the project's durable format.
8. Issue `sufficient`, `sufficient-with-actions`, `rework`, or `blocked` for the
   explicit scope; link actions to requirements and plan tasks.

## Guardrails

- A diagram is neither a complete architecture description nor evaluation evidence.
- An ADR records a decision but does not replace analysis of alternatives and consequences.
- Existing code describes implemented structure; it does not prove concerns are satisfied.
- Evaluate real boundary and failure behavior, not only module names.
- Re-evaluate after material context, topology, dependency, trust, data, or requirement change.

## Completion

Require coverage of material concerns, coherent views, scenario evidence,
explicit trade-offs, owned residual risks, resolved contradictions, and no
hidden architectural decision blocking implementation.
