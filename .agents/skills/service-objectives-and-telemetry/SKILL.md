---
name: service-objectives-and-telemetry
description: Defines decision-linked service, user, risk, and outcome objectives and validates their indicators, telemetry coverage, queries, alert delivery, data quality, uncertainty, and ownership. Use when establishing or reviewing SLIs/SLOs, dashboards, alerts, service health, quality-in-use measures, operational thresholds, or observability gaps.
---

# Service Objectives and Telemetry

Read [`../../../docs/service-objectives-and-telemetry.md`](../../../docs/service-objectives-and-telemetry.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use project-provided telemetry, query, alert, catalog, and automation systems.

## Workflow

1. Identify the decision, information need, users, critical journeys, service
   boundary, dependencies, obligations, risks, and intended outcomes.
2. Separate product behavior, reliability, control health, quality in use,
   cost, and business/mission outcome claims.
3. Define objectives and indicators with owner, population, segmentation,
   formula, units, window, sources, query/version, exclusions, missing-data
   treatment, uncertainty, threshold, consequence, cadence, and expiry.
4. Map telemetry across user, service, dependency, resource, data, security,
   and control-failure paths; record blind spots.
5. Validate instrumentation, query semantics, clocks, sampling, cardinality,
   freshness, retention, access, integrity, privacy, and alert delivery.
6. Establish evidence-backed baselines and thresholds. Exercise alert routing
   and verify owner action.
7. Report satisfied, failed, blocked, and inconclusive objectives separately;
   revalidate after material context, release, population, query, or instrumentation change.

## Guardrails

- A metric without an owner and decision consequence is not a control.
- Absence of alerts is not proof of health.
- Do not use arbitrary round numbers or current performance as requirements.
- A dashboard screenshot without query, range, population, release, and data-quality context is weak evidence.
- Do not present missing or invalid telemetry as satisfactory performance.

## Completion

Require decision-linked objectives, reproducible indicators, coverage and blind
spots, validated data paths, actionable thresholds, accountable owners, and
explicit uncertainty and invalidation conditions.
