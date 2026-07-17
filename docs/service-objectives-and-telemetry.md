# Service Objectives and Telemetry

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Utilization](stages/utilization.md) · [Validation and Evidence](validation-and-evidence.md)

## Purpose

This document defines how service, user, risk, and outcome needs become
decision-linked objectives and trustworthy operational signals. Projects
provide the telemetry platform, queries, collection agents, alerting system,
service catalog, and automation.

A metric is not an objective. An objective is not evidence unless its indicator,
population, calculation, data provenance, validity, threshold, owner, and
decision consequence are explicit.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC 20000-1:2018][20000] | Service requirements, monitoring, measurement, review, reporting, and improvement | Published; confirmed 2023 |
| [ISO/IEC/IEEE 15939:2017][15939] | Measures derived from information needs and analysis-result validity | Published; confirmed 2022 |
| [ISO/IEC 25019:2023][25019] | Quality-in-use in a specified context of use | Published |
| [ISO/IEC 25022:2016][25022] | Quality-in-use measurement candidates | Published; revision underway |

SLIs, SLOs, error budgets, dashboards, and alerts are useful implementation
patterns, not universal requirements of these standards.

## Objective and indicator contract

Preserve:

- information need, stakeholder, service scope, critical journey, context of use, and risk;
- objective statement, target, evaluation window, population, segmentation, exclusions, and owner;
- indicator formula, units, aggregation, data sources, query/version, sampling, and missing-data treatment;
- collection path, clocks, freshness, retention, access, integrity, privacy, and cost constraints;
- warning/decision thresholds, consequence, escalation, review cadence, and expiry;
- baseline, uncertainty, bias, blind spots, validity findings, and change history.

## Workflow

1. Start from a decision and information need; identify users, journeys,
   service boundaries, dependencies, obligations, risks, and desired outcomes.
2. Separate product behavior, service reliability, security/control health,
   quality in use, cost, and business or mission outcomes.
3. Define measurable objectives and indicators with population, window,
   formula, sources, exclusions, uncertainty, and decision consequences.
4. Map telemetry coverage across user, service, dependency, resource, data,
   security, and control-failure paths. Record blind spots.
5. Validate instrumentation, query semantics, clocks, cardinality, sampling,
   freshness, retention, access, integrity, privacy, and alert delivery.
6. Establish baseline and thresholds from requirements and risk, not arbitrary
   round numbers or current performance alone.
7. Exercise alerts and response routing. An alert without an owner and action is noise.
8. Review indicator validity when the release, population, context, dependency,
   query, instrumentation, or decision need changes.

## Decision rules

Use an indicator for control only when it is relevant, reproducible or
reviewable, current, sufficiently complete, and linked to an accountable
decision. Absence of alerts is not proof of health. A dashboard screenshot
without query, time range, population, baseline, and data-quality context is
weak evidence. Report unavailable or invalid telemetry as `blocked` or
`inconclusive`, never as satisfactory performance.

[20000]: https://www.iso.org/standard/70636.html
[15939]: https://www.iso.org/standard/71197.html
[25019]: https://www.iso.org/standard/78177.html
[25022]: https://www.iso.org/standard/35746.html
