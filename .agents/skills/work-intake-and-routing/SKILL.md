---
name: work-intake-and-routing
description: Classifies incoming engineering work and selects the smallest safe SDLC route from intent, uncertainty, consequence, reversibility, scope, and authority. Use when accepting or triaging a task, issue, bug, feature, investigation, migration, incident follow-up, production change, or retirement request before planning or implementation begins.
---

# Work Intake and Routing

Read [`../../../docs/work-intake-and-routing.md`](../../../docs/work-intake-and-routing.md)
and the affected lifecycle-stage documents before routing work.

## Workflow

1. Inspect repository state, request evidence, affected code/contracts, current
   baseline, and related work without mutating external systems.
2. Separate the underlying need and desired outcome from the proposed solution.
3. Identify affected users, systems, interfaces, data, lifecycle stages,
   obligations, owners, constraints, assumptions, dependencies, and exclusions.
4. Assess uncertainty, consequence, reversibility, exposure, novelty, coupling,
   security/data impact, compatibility, migration, and external dependencies.
5. Select the smallest adequate route: `direct-change`, `specification`,
   `design-dialogue`, `investigation`, `planned-change`, `incident-or-support`,
   `production-only`, `retirement`, or `hold-or-reject`.
6. Name required skills, artifacts, decisions, evidence, owner, immediate next
   action, and unresolved questions. Record why the lighter route is sufficient.
7. Escalate the route when new evidence widens the boundary. Preserve the route
   transition rather than rewriting intake history.

## Guardrails

- Do not infer implementation authority from permission to inspect or classify.
- Do not treat ticket labels, estimated diff size, or urgency as sufficient routing evidence.
- Do not use `direct-change` when a material requirement, architecture,
  security, data, compatibility, migration, or acceptance decision is hidden.
- Route active harm through operational control before ordinary Development work.
- Ask only for decisions that cannot be discovered or safely deferred.

## Report

State: need, affected baseline, selected route, rationale, required artifacts
and skills, decision authority, next action, assumptions, and blockers.
