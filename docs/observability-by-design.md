# Observability by Design

Status: **baseline 0.1**
Sources reviewed: **2026-08-24**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Validation and evidence](validation-and-evidence.md) ·
[Service objectives and telemetry](service-objectives-and-telemetry.md)

## Purpose

This document defines how runtime changes acquire privacy-safe, bounded, and
testable diagnostic signals. It covers instrumentation and diagnostic
attribution during Development. Operational objectives, production thresholds,
alerting, dashboards, and recurring health decisions remain governed by
[Service Objectives and Telemetry](service-objectives-and-telemetry.md).

Projects provide their telemetry backend, naming namespace, deployment wiring,
queries, and evidence commands. The harness provides portable signal-design and
evidence semantics.

## Standards and source basis

Use the protocol, telemetry library, and semantic-convention versions selected
by the project. Relevant primary sources include:

- [OpenTelemetry semantic conventions 1.44.0](https://opentelemetry.io/docs/specs/semconv/);
- [W3C Trace Context](https://www.w3.org/TR/trace-context/);
- [OpenMetrics](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md);
- [Prometheus instrumentation practices](https://prometheus.io/docs/practices/instrumentation/).

Experimental conventions must be revision-pinned before they become a project
contract. A later upstream rename must not silently change a released signal.

## Trigger

For each runtime-facing change, ask:

```text
Does this create or alter a latency, failure, queueing, dependency, resource,
degradation, or lifecycle state that an operator could not otherwise
distinguish safely?
```

If not, record a bounded `observability impact: none` rationale when the work is
material enough to have a specification, plan, or review record. Do not add
ceremonial telemetry.

The full workflow normally applies to request handlers, external clients,
streams, queues, workers, caches, database hot paths, retries, timeouts,
cancellation, health/readiness behavior, deployment topology, resource limits,
and reported latency or availability problems.

## Signal contract

For every required signal, define:

- the user or operator information need and owning boundary;
- signal type, stable name, unit, aggregation semantics, and lifecycle;
- finite labels or fields and their allowed value sets;
- success, error, timeout, cancellation, partial, and degradation accounting;
- correlation propagation, trust boundaries, and allowed sinks;
- collection/exposition wiring and isolation from product behavior;
- verification method, expected evidence, limitations, and invalidation rules;
- environment-owner handoff and residual blind spots.

Assign one owner to each measured phase. Duplicate measurement at several
layers creates contradictory latency and failure attribution.

## Signal responsibilities

| Signal | Appropriate use | Not sufficient for |
| --- | --- | --- |
| Metrics | Aggregate rates, errors, durations, concurrency, queueing, saturation | Per-request audit or user analytics |
| Structured events/logs | Classified lifecycle and failure context with bounded correlation | An unstructured content archive |
| Traces/context | Causal flow across boundaries | Authentication, authorization, or basic metric availability |
| Profiles | Hotspots inside an already identified process | Initial localization of distributed latency |
| Platform signals | Resource, restart, and capacity state | Application phase semantics |

Use base units and distributions appropriate to the expected range. Compute
quantiles in the analysis system, not inside the application. Streaming signals
should distinguish admission, establishment or first event, active delivery,
inactivity, completion, cancellation, and failure after partial output when
those states affect decisions.

## Privacy, cardinality, and failure isolation

- Use route templates and bounded operation, result, and error classes.
- Do not put request, account, principal, trace, operation-instance, email, or
  other unbounded identifiers in metric labels.
- Do not emit credentials, prompts, payloads, arbitrary headers, raw URLs, raw
  exception text, or local filesystem paths through telemetry.
- Keep correlation identifiers in privacy-reviewed logs, traces, or exemplars.
- Treat incoming trace context as diagnostic metadata, never authority.
- Keep exporter, exposition, and correlation failures off the product failure
  path and bound any telemetry-related wait.
- Preserve management-plane access boundaries; current network topology is not
  a substitute for an explicit exposure policy.

## Workflow and evidence

1. State the symptom or runtime change and map the critical path.
2. Inventory existing application, dependency, and platform signals without
   inferring live state from repository templates.
3. Apply the trigger and define the signal contract before implementation.
4. Require an architecture decision when changing expensive-to-reverse signal
   ownership, context propagation, management listeners, or trust boundaries.
5. Implement behavior and instrumentation together.
6. Verify schemas, allowed labels, state accounting, exposure, and failure
   isolation under deterministic conditions.
7. Observe packaged or live behavior only within an explicitly identified
   environment boundary.
8. Hand operational indicators, objectives, thresholds, dashboards, and alerts
   to `service-objectives-and-telemetry`.

Repository-controlled checks may prove that documented signals are emitted and
exposed safely. They do not by themselves prove production capacity, an SLO, a
live collector, dashboard, or alert path. Report those as separate claims under
[Validation and Evidence](validation-and-evidence.md).

## Completion criteria

The workflow is complete when impact is dispositioned, phase ownership is
clear, signal and privacy contracts are controlled, deterministic evidence
supports the bounded claims, deployment responsibilities and blind spots are
explicit, and material decisions are recorded.
