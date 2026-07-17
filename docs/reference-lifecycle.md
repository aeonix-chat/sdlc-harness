# SDLC Reference Model

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

## 1. Purpose

This document establishes a common lifecycle vocabulary for SDLC Harness. It
defines:

- the top-level lifecycle stages;
- the purpose and minimum verifiable outcome of each stage;
- cross-cutting processes that cannot be isolated within a single stage;
- rules for tailoring the model to a specific product or service.

The executable workflow mapping for this model is defined in the
[SDLC process and skill map](process.md).
The cross-cutting rules for converting checks into decision-grade claims are
defined in [Validation and Evidence](validation-and-evidence.md).

The model applies to software products, platforms, and services regardless of
whether they use agile, continuous delivery, iterative, incremental, or
predictive development approaches.

## 2. Standards perspective

The current [ISO/IEC/IEEE 12207:2026][iso-12207] establishes a common framework
of processes, activities, and tasks covering the full software lifecycle, from
conception through retirement. It does not prescribe a particular lifecycle
model or development methodology. Its processes may be applied concurrently,
iteratively, and recursively.

[ISO/IEC/IEEE 24748-1:2024][iso-24748] complements ISO/IEC/IEEE 12207 with
guidance on lifecycle models, stages, decision points, and tailoring. This
reference model adopts its representative six-stage lifecycle, also explicitly
listed in [ISO/IEC/IEEE 15288:2023][iso-15288]: **Concept, Development,
Production, Utilization, Support, and Retirement**.

A stage and a process are therefore separate dimensions:

- a **stage** describes the state and maturity of a product over time;
- a **process** describes work that may be performed across multiple stages.

Requirements, architecture, risk management, configuration management,
quality, and information management are not one-time phases. They continue
wherever they are required to achieve a stage outcome.

## 3. Reference lifecycle stages

```text
Concept → Development → Production → Utilization → Retirement
              ↑              │             │
              └──────────────┴── Support ──┘
```

The diagram shows the primary decision flow, not a mandatory linear sequence.
Feedback loops, concurrent work, and repeated decision points are expected.

### 3.1 [Concept](stages/concept.md)

**Purpose:** establish the need, context, and viability of the investment.

Minimum outcome:

- the problem, stakeholders, and intended outcomes are identified;
- system boundaries and primary usage scenarios are described;
- key constraints, assumptions, dependencies, and risks are identified;
- applicable security, privacy, safety, and compliance requirements are known;
- alternatives, including not building the solution, have been considered;
- an accountable owner and criteria for continuing or stopping are established.

**Decision point:** there is a justified decision to proceed with realization.

See the [Concept stage standard mapping and evidence contract](stages/concept.md).

### 3.2 [Development](stages/development.md)

**Purpose:** define, implement, and demonstrate the fitness of the solution.

The following activities are performed iteratively within this stage:

1. refine stakeholder needs and requirements;
2. design the architecture and interfaces;
3. implement and integrate the solution;
4. verify conformance to specified requirements;
5. validate fitness for intended use;
6. prepare operational and user readiness.

Minimum outcome:

- requirements and acceptance criteria are traceable to changes and checks;
- architectural decisions and significant trade-offs are recorded;
- source code, dependencies, builds, and configuration are controlled;
- quality and security checks proportional to risk have been completed;
- known defects and residual risks have been accepted by accountable owners;
- the solution is ready for reproducible release and operation.

**Decision point:** the candidate is shown to satisfy its release criteria.

See the [Development stage standard mapping and evidence contract](stages/development.md).

### 3.3 [Production](stages/production.md)

For a software-only product, this stage does not imply physical mass
production. It covers creating, packaging, signing, publishing, and deploying a
reproducible release.

**Purpose:** turn a verified change into an identifiable and controlled delivery.

Minimum outcome:

- the release artifact is unambiguously linked to its source and check results;
- build and deployment processes are reproducible and protected;
- release contents and third-party components are known;
- release checks are complete and the release decision is recorded;
- migration, rollback, communication, and release notes are prepared.

**Decision point:** the release is authorized for use in its target environment.

See the [Production stage standard mapping and evidence contract](stages/production.md).

### 3.4 [Utilization](stages/utilization.md)

**Purpose:** operate the solution safely and realize its intended outcomes.

Minimum outcome:

- service indicators, objectives, and operational owners are defined;
- observability, incident response, backup, and recovery are in place;
- access, configuration, capacity, and service continuity are controlled;
- actual value, reliability, and user experience are measured;
- operational feedback flows into requirements and the backlog.

**Decision point:** the solution remains fit, controlled, and valuable in use.

See the [Utilization stage standard mapping and evidence contract](stages/utilization.md).

### 3.5 [Support](stages/support.md)

Support is a cross-cutting stage that overlaps Production and Utilization and
may initiate new Development cycles.

**Purpose:** sustain the required fitness of the solution as its context changes.

Minimum outcome:

- defects, vulnerabilities, and change requests are received and prioritized;
- corrective, adaptive, perfective, and preventive changes are performed;
- dependencies and platforms remain in a supportable state;
- compatibility is preserved or its controlled breakage is managed;
- root causes of significant failures are addressed and lessons feed back into
  the lifecycle.

**Decision point:** the solution can be sustained at acceptable risk and cost,
or it should be retired.

Maintenance terminology and its relationship to disposal are detailed in
[ISO/IEC/IEEE 14764:2022][iso-14764].

See the [Support stage standard mapping and evidence contract](stages/support.md).

### 3.6 [Retirement](stages/retirement.md)

**Purpose:** end use of the solution without unacceptable impact on users,
data, the business, or the environment.

Minimum outcome:

- the end-of-support or end-of-operation decision is made and communicated;
- consumers, integrations, data, and contractual obligations are identified;
- data is migrated, archived, transferred, or destroyed as required;
- access, secrets, certificates, and infrastructure resources are revoked;
- catalogs, documentation, monitoring, and continuity plans are updated;
- unmanaged dependencies are eliminated and lessons learned are recorded.

**Decision point:** obligations are closed, data is handled according to policy,
and residual risk is accepted.

See the [Retirement stage standard mapping and evidence contract](stages/retirement.md).

## 4. Stage handoffs and feedback

A handoff transfers accountable state and evidence; it does not transfer an
unbounded task list or erase the sending stage's obligations. The receiver must
identify the input baseline, acknowledge acceptance or record an exception, and
preserve traceability to the sending decision.

| From | To | Trigger | Minimum transferred state |
| --- | --- | --- | --- |
| Concept | Development | `proceed` | Approved need and outcome, boundaries, stakeholders, constraints, risks, success criteria, assumptions, and open questions |
| Development | Production | `candidate` | Exact candidate identity, requirements and change trace, verification and validation evidence, configuration, dependencies, deviations, residual risks, and transition needs |
| Production | Utilization and Support | `release` | Authorized artifact and active configuration identity, provenance and composition, deployment result, rollout and rollback state, operating information, known limitations, risks, and support scope |
| Utilization | Support | `change` or accountable problem/vulnerability disposition | Operational evidence, affected active baseline and context, impact, mitigation, reproduction information, urgency, and effectiveness need |
| Support | Development | `resolve` or approved maintenance change | Affected supported baselines, diagnosis, treatment scope, compatibility and risk constraints, acceptance criteria, and required release/disclosure timing |
| Support or Utilization | Retirement | `retire` | Rationale, affected consumers and baselines, supportability and operating evidence, known obligations, initial inventory, risks, and decision authority |
| Retirement | Governance or successor lifecycle | `close` or explicit transfer | Retained records and custodian, transferred obligations, final exceptions, residual-risk acceptance, closure evidence, and lessons |

Feedback may move to any earlier stage without pretending the whole product has
returned to an earlier chronological phase. A changed need returns to Concept;
an approved product change enters Development; a new candidate passes through
Production; an operational event remains in Utilization while its corrective
change flows through Support and Development.

## 5. Cross-cutting processes

The following process areas apply across all relevant stages:

| Area | What the harness should provide |
| --- | --- |
| Governance | Owners, policies, authority, and verifiable decisions |
| Planning and tracking | Objectives, plans, dependencies, status, and forecasts |
| Requirements | Versioning, quality controls, and end-to-end traceability |
| Architecture | Significant decisions, constraints, and system property evaluation |
| Risk | Identification, assessment, treatment, and explicit residual-risk acceptance |
| Security and privacy | Secure-by-design controls and evidence throughout the SDLC |
| Quality and V&V | Quality criteria, verification, validation, independence where required, and bounded claims under the [validation and evidence model](validation-and-evidence.md) |
| Configuration and change | Version identification, baselines, and controlled changes |
| Supply chain | Component provenance, integrity, licensing, and risk |
| Release control | Immutable artifact promotion, environment transitions, release authorization, rollout, rollback, and active-state reconciliation |
| Operational acceptance | Target-bound operability, observability, recovery, supportability, and acceptance evidence |
| Information management | Record availability, integrity, retention, and disposal |
| Measurement | Outcome, flow, quality, reliability, and risk metrics |
| Improvement | Feedback, root-cause analysis, and evolution of the process itself |

Security is not a final-stage gate. [NIST SP 800-218 SSDF 1.1][nist-ssdf]
defines secure development practices to be integrated into each SDLC
implementation. As of the source review date, SSDF 1.2 is only an initial public
draft, so the final version 1.1 remains the normative basis for this baseline.

## 6. Stage contract for the harness

Each tailored stage should be represented by a machine-readable or otherwise
unambiguously verifiable contract:

| Field | Meaning |
| --- | --- |
| `purpose` | Why the stage exists |
| `owner` | Who is accountable for its outcome and decision |
| `entry_criteria` | Minimum conditions for starting the stage |
| `activities` | Applicable processes and controls |
| `evidence` | References to immutable or versioned evidence |
| `exit_criteria` | Measurable conditions for completing the stage |
| `decision` | Stage-specific decision value, authority, timestamp, rationale, evidence, conditions, and next review or handoff |
| `exceptions` | Deviation, expiry, compensating controls, and risk owner |

A decision point does not have to be a manual meeting. It is a verifiable
decision that may be automated fully or partially according to risk.

Decision vocabularies are deliberately stage-specific because they cause
different transitions:

| Stage | Decision vocabulary |
| --- | --- |
| Concept | `proceed`, `hold`, `redirect`, `stop` |
| Development | `candidate`, `rework`, `hold`, `stop` |
| Production | `release`, `hold`, `rebuild`, `rollback`, `stop` |
| Utilization | `continue`, `constrain`, `recover`, `change`, `retire` |
| Support item | `resolve`, `mitigate`, `defer`, `reject`, `duplicate`, `transfer`, `retire` |
| Support portfolio | `continue`, `constrain`, `invest`, `transfer`, `retire` |
| Retirement | `proceed`, `pause`, `rework`, `abort`, `close` |

Do not normalize these values into one generic status without preserving the
original decision semantics and transition.

## 7. Tailoring rules

A project may merge, split, rename, or repeat stages, provided that it:

1. preserves full lifecycle coverage from Concept through Retirement;
2. maps its local stages to this reference model;
3. assigns accountable outcome and risk owners;
4. defines entry criteria, exit criteria, and required evidence;
5. documents exceptions and the rationale for weakened controls;
6. accounts for criticality, regulatory context, scale, and delivery model;
7. does not use agile or continuous delivery as a reason to remove governance,
   security, validation, operation, or retirement activities.

Alignment with this model does not imply certification or full conformance with
ISO/IEC/IEEE 12207. Any conformance claim requires a separately scoped gap
assessment against the licensed text of the applicable standard.

## 8. Normative and supporting references

Normative basis for this baseline:

- [ISO/IEC/IEEE 12207:2026 — Software life cycle processes][iso-12207] — the
  current common process framework for the full software lifecycle;
- [ISO/IEC/IEEE 24748-1:2024 — Guidelines for life cycle management][iso-24748]
  — lifecycle models, stages, decision points, and tailoring;
- [NIST SP 800-218, SSDF 1.1][nist-ssdf] — cross-cutting secure software
  development practices;
- [ISO/IEC/IEEE 14764:2022 — Maintenance][iso-14764] — software maintenance and
  its relationship to retirement.

Supporting references for future iterations:

- [ISO/IEC/IEEE 15288:2023][iso-15288] — system lifecycle processes when
  software is part of a broader system;
- [ISO/IEC/IEEE 15289:2019][iso-15289] — lifecycle information-item content;
- ISO/IEC/IEEE 29148:2018 — requirements engineering;
- ISO/IEC 25010:2023 — product quality model;
- ISO/IEC 27001:2022 — information security management systems.

[iso-12207]: https://www.iso.org/standard/90219.html
[iso-24748]: https://www.iso.org/standard/84709.html
[iso-14764]: https://www.iso.org/standard/80710.html
[iso-15288]: https://www.iso.org/standard/81702.html
[iso-15289]: https://www.iso.org/standard/74909.html
[nist-ssdf]: https://csrc.nist.gov/pubs/sp/800/218/final
