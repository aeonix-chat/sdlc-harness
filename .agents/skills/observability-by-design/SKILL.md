---
name: observability-by-design
description: Defines privacy-safe, bounded, testable diagnostic signals for runtime changes. Use when handlers, clients, streams, queues, dependencies, retries, timeouts, lifecycle states, health behavior, or incidents create new observability needs during specification, implementation, review, or validation.
---

# Observability by Design

Read [`../../../docs/observability-by-design.md`](../../../docs/observability-by-design.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use project-provided telemetry libraries, naming, deployment wiring, and checks.

## Workflow

1. State the runtime change or symptom and map its critical path.
2. Assign one owner to each latency, failure, queueing, dependency, resource,
   degradation, and lifecycle phase.
3. Inventory existing application and platform signals. Separate repository
   configuration from observed environment state.
4. Apply the documented impact trigger. Record a concrete not-applicable
   rationale when no new diagnostic distinction is needed.
5. Define signal names, types, units, bounded labels, state accounting,
   correlation, privacy, exposure, failure isolation, and evidence before implementation.
6. Route expensive-to-reverse listener, propagation, ownership, and trust-boundary
   changes through architecture decision work.
7. Verify schema, allowed values, state coverage, management exposure, and
   telemetry failure isolation under deterministic conditions.
8. Hand objectives, thresholds, dashboards, alerts, and production data-quality
   decisions to `service-objectives-and-telemetry`.

## Guardrails

- Never use unbounded identifiers, raw URLs, exception text, credentials, or
  content as metric labels.
- Keep telemetry and exporter failure off the product failure path.
- Do not profile an arbitrary process before evidence attributes the delay.
- Do not present repository instrumentation checks as production SLO evidence.

## Completion

Require a dispositioned impact, owned phases, a bounded and privacy-safe signal
contract, verification evidence, environment handoff, and explicit blind spots.
