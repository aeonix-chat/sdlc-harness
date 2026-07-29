# SDLC Harness

A repository for shared approaches to managing the lifecycle of software
products and services. Its purpose is to define a verifiable SDLC framework:
stages, decision points, expected evidence, and automation rules, without
prescribing a particular development methodology or toolchain.

## Reference lifecycle

The reference model consists of six lifecycle stages:

1. **Concept** — establish the need and viability of the solution.
2. **Development** — define, implement, and verify the solution.
3. **Production** — prepare a reproducible release and delivery process.
4. **Utilization** — operate the product and realize its intended value.
5. **Support** — sustain supported baselines as defects, threats, dependencies,
   and needs change.
6. **Retirement** — decommission the product and close its obligations in a
   controlled manner.

This is not a waterfall sequence. Stages may overlap, and lifecycle processes
may be performed concurrently, iteratively, and recursively for a product and
its constituent elements.

See the [SDLC reference model](docs/reference-lifecycle.md) for the rationale,
stage boundaries, and minimum controls. Use the
[process and skill map](docs/process.md) to route work to an executable agent
workflow. Apply the cross-cutting
[validation and evidence model](docs/validation-and-evidence.md) to turn
project-provided checks into bounded claims and lifecycle decisions.

Stage-specific standards, evidence, and decision criteria are documented in:

- [Concept](docs/stages/concept.md)
- [Development](docs/stages/development.md)
- [Production](docs/stages/production.md)
- [Utilization](docs/stages/utilization.md)
- [Support](docs/stages/support.md)
- [Retirement](docs/stages/retirement.md)

## Harness principles

- Automate controls and evidence collection without prescribing how teams work.
- Trace needs, requirements, changes, verification, releases, and observed behavior.
- Apply security, quality, risk, and compliance throughout the lifecycle.
- Make lifecycle decisions explicit, reproducible, and auditable.
- Tailor control rigor to the product's risk and context.
- Treat operation, support, and retirement as integral parts of the SDLC.

## Repository structure

- [`docs/reference-lifecycle.md`](docs/reference-lifecycle.md) — the normative
  lifecycle model for this repository and its relationship to relevant standards.
- [`docs/process.md`](docs/process.md) — lifecycle-to-workflow routing, expected
  evidence, skill composition, and known coverage gaps.
- [`docs/validation-and-evidence.md`](docs/validation-and-evidence.md) — common
  claim, assessment, evidence, and assurance-profile contract.
- [`docs/work-intake-and-routing.md`](docs/work-intake-and-routing.md) —
  risk- and uncertainty-based routing from incoming work to SDLC workflows.
- [`docs/execution-continuity.md`](docs/execution-continuity.md) — authorized
  delivery boundaries, continuous execution, and the only allowed early-stop
  conditions.
- [`docs/requirements-and-traceability.md`](docs/requirements-and-traceability.md)
  — requirements quality, baselines, change impact, and lifecycle evidence graph.
- [`docs/architecture-evaluation.md`](docs/architecture-evaluation.md) —
  concern-, scenario-, alternative-, and risk-based architecture evaluation.
- [`docs/development-candidate-readiness.md`](docs/development-candidate-readiness.md)
  — exact candidate assembly, evidence reconciliation, and Development decision.
- [`docs/artifact-integrity-and-provenance.md`](docs/artifact-integrity-and-provenance.md)
  — artifact identity, composition, provenance, authenticity, and custody.
- [`docs/release-and-promotion.md`](docs/release-and-promotion.md) — immutable
  promotion, deployment state, release authorization, rollout, and rollback.
- [`docs/operational-acceptance.md`](docs/operational-acceptance.md) — target-bound
  operability, observability, recovery, and support acceptance.
- [`docs/service-objectives-and-telemetry.md`](docs/service-objectives-and-telemetry.md)
  — decision-linked operational objectives, indicators, coverage, and signal validity.
- [`docs/incident-response-and-recovery.md`](docs/incident-response-and-recovery.md)
  — incident command, containment, recovery, communication, and follow-up.
- [`docs/continuity-and-restore-validation.md`](docs/continuity-and-restore-validation.md)
  — backup restoration, failover, recovery objectives, and continuity exercises.
- [`docs/operational-review-and-control.md`](docs/operational-review-and-control.md)
  — active-baseline reconciliation and recurring operating decisions.
- [`docs/stages/`](docs/stages/) — standards-based guidance and evidence
  contracts for each lifecycle stage.
- [`AGENTS.md`](AGENTS.md) — durable repository guidance for agents.
- [`.agents/skills/`](.agents/skills/) — repository-scoped reusable workflows.
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) — attribution and licenses
  for imported material.

## Status

Model version: **0.2 (baseline)**. All six reference stages have a
standards-grounded workflow, evidence contract, decision criteria, tailoring
guidance, and skill routing. Native workflows cover work routing, requirements
traceability, architecture evaluation, candidate readiness, validation evidence,
artifact integrity and provenance, release promotion, and operational acceptance;
service measurement, incident recovery, continuity validation, and operational
review; project-specific machine-readable schemas and implementations remain integration work. See
the [process map](docs/process.md#known-coverage-gaps).

## Validation

Use `uv` for repository validation:

```sh
uv run python scripts/validate_docs.py
uv run python scripts/validate_publication.py
git diff --check
```

The validators check Markdown structure and links plus publication leakage such
as absolute local paths, PII, private keys, and common credential formats.
Publication safety is required before every commit, pull request, release, or
other publication. Skill changes additionally require the Agent Skills
validator documented in [`AGENTS.md`](AGENTS.md#validation).
