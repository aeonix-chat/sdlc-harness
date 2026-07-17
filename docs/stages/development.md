# Development Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

Navigation: Previous: [Concept](concept.md) ·
[Lifecycle](../reference-lifecycle.md) · [Process map](../process.md) · Next:
[Production](production.md)

## Purpose and boundary

The Development stage transforms the approved Concept baseline into an
integrated release candidate whose conformance to requirements and fitness for
intended use are supported by evidence.

It begins with an authorized Concept decision, stakeholder-needs baseline, and
development authority. It ends with `candidate`, `rework`, `hold`, or `stop`.
A `candidate` decision identifies a controlled configuration and transfers it,
with its evidence and known risks, to Production.

Development includes requirements definition, architecture and design,
implementation, integration, verification, validation, and transition
readiness. These are interacting processes, not mandatory waterfall phases.
They may execute concurrently, iteratively, recursively for system elements,
and incrementally for product slices.

Production owns creation and authorization of a releasable delivery. Development
owns proving that the candidate is sufficiently defined, integrated, verified,
validated, and ready to be produced and transitioned.

## Standards model

| Source | Role in Development | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Primary software lifecycle process framework from definition through transition, operation, support, and retirement | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | Aligned system processes when software is part of a larger system | Published |
| [ISO/IEC/IEEE 24748-5:2017][24748-5] | Planning and control of software development and its information items | Published and confirmed |
| [ISO/IEC/IEEE 29148:2018][29148] | Stakeholder, system, and software requirements engineering and requirements information | Published; revision in development |
| [ISO/IEC/IEEE 42010:2022][42010] | Required structure and expression of architecture descriptions | Published |
| [ISO/IEC 25010:2023][25010] | Product quality model for requirements and evaluation | Published |
| [ISO/IEC 25030:2019][25030] | Elicitation, definition, use, and governance of quality requirements | Published and confirmed |
| [ISO/IEC/IEEE 29119-2:2021][29119-2] | Governance, management, and implementation of software testing | Published |
| [ISO/IEC/IEEE 29119-3:2021][29119-3] | Test documentation produced by the test processes | Published |
| [ISO/IEC 20246:2017][20246] | Generic process and evidence for reviewing any work product | Published and confirmed |
| [ISO/IEC/IEEE 15939:2017][15939] | Selection, definition, use, and improvement of engineering measures | Published and confirmed |
| [ISO/IEC/IEEE 15289:2019][15289] | Content of lifecycle information items | Published; revision in development |
| [NIST SP 800-218, SSDF 1.1][ssdf] | Secure software development practices integrated into the SDLC | Final; 1.2 remains draft |

Use application-specific standards in addition to this baseline for regulated,
safety-critical, privacy-sensitive, AI, embedded, medical, financial, or other
specialized systems. Public catalog descriptions establish scope; clause-level
conformance requires licensed standards and a scoped assessment.

## How the standards fit together

ISO/IEC/IEEE 12207 supplies the main process framework and is fully aligned at
the process-purpose and outcome level with ISO/IEC/IEEE 15288. A software-only
product primarily uses 12207; a software element within a broader system selects
appropriate activities from both.

The stage can be understood as interacting process groups:

1. **Define:** stakeholder and system/software requirements establish the
   verifiable technical view derived from Concept needs.
2. **Structure:** architecture and design allocate requirements, define
   boundaries and interfaces, and make significant trade-offs explicit.
3. **Realize:** implementation creates configured system elements.
4. **Assemble:** integration combines elements and verifies their interfaces.
5. **Demonstrate:** verification asks whether specified requirements were met;
   validation asks whether the integrated solution is fit for intended use in
   representative contexts.
6. **Prepare transition:** confirm that Production, operation, support,
   migration, rollback, training, and information needs can be satisfied.

ISO/IEC/IEEE 29148, ISO/IEC/IEEE 42010, and the SQuaRE standards deepen
requirements, architecture-description, quality, and measurement work.
ISO/IEC/IEEE 29119-2/-3 deepen test processes and evidence. ISO/IEC 20246 covers
reviews beyond source code. NIST SSDF overlays secure practices across all six
groups rather than creating a final security gate.

## Roles and decision rights

| Role | Accountability |
| --- | --- |
| Product / requirements owner | Own the approved needs, scope, acceptance intent, prioritization, and requirement decisions |
| Technical lead / architect | Own technical coherence, architecture decisions, interfaces, and significant trade-offs |
| Development team | Implement controlled increments and produce truthful engineering evidence |
| Verification and validation owners | Define and execute adequate verification and validation; preserve required independence |
| Security, privacy, safety, operations, support, and other specialty owners | Define and assess applicable constraints, risks, and readiness evidence |
| Configuration / release-candidate owner | Identify the exact candidate and bind it to its baselines and evidence |
| Development decision authority | Issue `candidate`, `rework`, `hold`, or `stop` and accept residual risk within authority |

Roles may be combined for low-risk work, but authorship, review, approval, and
risk acceptance must remain distinguishable where independence matters.

## Entry criteria

- an authorized Concept `proceed` decision and accountable owner;
- versioned stakeholder needs, lifecycle concepts, constraints, risks, outcome
  measures, and acceptance intent;
- defined scope and change authority;
- a tailored development and assurance approach proportionate to risk;
- available people, tools, environments, suppliers, and other enabling systems;
- identified decision points and evidence expectations.

If the Concept baseline cannot explain the problem, users, outcomes, and
material constraints, return it to Concept rather than inventing requirements.

## Operating workflow

### 1. Tailor and plan the development

- Select applicable lifecycle processes, specialty standards, roles,
  independence, environments, methods, and information items.
- Define increments, technical and assurance checkpoints, baselines, change
  control, measures, and candidate criteria.
- Plan requirements, architecture, integration, verification, validation,
  transition, security, supplier, and configuration work together.
- Put high uncertainty and high consequence work early enough to change course.

Output: **development and assurance plan**, decision schedule, and evidence plan.

### 2. Define and baseline requirements

- Transform stakeholder needs into functional, interface, data, quality,
  security, privacy, safety, operational, support, and retirement requirements.
- Make requirements necessary, unambiguous, feasible, singular where practical,
  verifiable, and traceable to their source and validation intent.
- Define acceptance criteria and verification method at the same time as each
  material requirement.
- Resolve conflicts explicitly and control requirement changes and baselines.

Output: **system/software requirements baseline**, acceptance criteria,
verification methods, and bidirectional traceability.

### 3. Define architecture and design

- Identify stakeholder concerns and select architecture viewpoints that address them.
- Define boundaries, responsibilities, interfaces, data flows, deployment and
  trust boundaries, failure behavior, and enabling systems.
- Allocate requirements and quality attributes to elements and interfaces.
- Evaluate alternatives and trade-offs using scenarios, analysis, models,
  prototypes, or experiments proportional to risk.
- Record decisions, rationale, rejected alternatives, consequences, and known debt.

Output: **architecture description**, interface contracts, design baseline,
analysis results, and decision records.

### 4. Implement controlled increments

- Implement the smallest coherent vertical or risk-reducing increment.
- Use version-controlled source, dependencies, build definitions,
  configuration, generated assets, and migrations.
- Apply secure coding, review, static analysis, and unit/component verification.
- Keep incomplete behavior isolated through safe defaults or controlled flags.
- Record deviations and technical debt rather than hiding them in code.

Output: **configured implemented elements** and increment-level evidence.

### 5. Integrate progressively

- Define integration order from architecture, dependencies, interfaces, and risk.
- Integrate frequently in representative environments rather than at stage end.
- Verify interface contracts, data semantics, error handling, compatibility,
  resource behavior, and observability at each boundary.
- Diagnose failures to root cause and update requirements, design, code, tests,
  or assumptions as evidence requires.

Output: **integrated baselines**, interface evidence, defect records, and updated traceability.

### 6. Verify the specified solution

- Verify each applicable requirement with an identified method: analysis,
  review, inspection, demonstration, test, or other justified technique.
- Use reviews for requirements, architecture, design, code, tests, plans, and
  operational information—not only for pull-request diffs.
- Maintain test conditions, expected results, environment, data, execution,
  anomalies, and results at the fidelity required for repeatability.
- Confirm measurement validity and distinguish passing checks from adequate coverage.

Output: **verification record** and requirement-to-evidence coverage.

### 7. Validate fitness for intended use

- Validate against stakeholder needs, operational concepts, quality-in-use
  goals, and real user outcomes rather than only technical requirements.
- Use representative users, scenarios, data, workloads, environments, failures,
  and lifecycle conditions.
- Confirm accessibility, usability, operability, supportability, recoverability,
  and other relevant outcomes.
- Treat a requirement-compliant solution that fails stakeholder use as not validated.

Output: **validation record**, unresolved fitness gaps, and stakeholder disposition.

### 8. Prepare transition and candidate evidence

- Confirm reproducible build inputs, configuration identity, dependency
  inventory, migrations, rollback, recovery, and deployment feasibility.
- Prepare operational, support, user, training, monitoring, and known-limitation information.
- Reconcile defects, deviations, security findings, debt, and residual risks
  with owners, expiry, and acceptance authority.
- Identify the exact release candidate and freeze or control changes during decision.

Output: **candidate configuration**, readiness package, and known-risk baseline.

### 9. Decide and baseline

- Review the evidence graph against the exit criteria below.
- Record `candidate`, `rework`, `hold`, or `stop` with authority, timestamp,
  scope, conditions, exceptions, and residual-risk acceptance.
- Transfer a versioned candidate and evidence package to Production.

Output: **Development decision record** and controlled Production handoff.

## Increment control loop

The nine activities above describe stage coverage, not a one-pass sequence.
Agents should work in short evidence-producing loops:

```text
select requirement / risk / uncertainty
  → refine requirement and acceptance evidence
  → update architecture or design
  → implement smallest coherent increment
  → integrate
  → verify
  → validate when user or context evidence is needed
  → review findings and update traceability
  → baseline or rework
```

No increment is complete merely because code was written or tests passed.

## Evidence and traceability contract

The harness should preserve a graph such as:

```text
Concept need / risk / decision
  → system/software requirement + acceptance criterion
  → architecture concern / decision / interface
  → planned increment and change set
  → configured implementation + dependencies + build
  → integration result
  → verification evidence
  → validation evidence
  → defect / deviation / residual risk disposition
  → identified release candidate
  → Development decision
```

Minimum evidence:

- tailored development and assurance plan;
- controlled requirements and acceptance baseline;
- bidirectional traceability and change history;
- architecture description, interface contracts, and significant decisions;
- threat, privacy, safety, reliability, and other applicable analyses;
- controlled source, dependencies, configuration, build, data, and environments;
- reviews, analyses, tests, verification, validation, and measurement results;
- integration baselines and anomaly/defect disposition;
- operational, support, migration, rollback, recovery, and user readiness;
- candidate identity, accepted deviations and risks, and Development decision.

Evidence may be distributed across repository history, issue tracking, CI,
artifact systems, test systems, and documents. The harness must retain stable
identifiers and relationships rather than force duplication into one report.

## Verification is not validation

| Question | Primary basis | Typical evidence |
| --- | --- | --- |
| **Verification:** Did we build the specified solution correctly? | System/software requirements, architecture, design, interface contracts | Reviews, analysis, static checks, tests, inspections, demonstrations |
| **Validation:** Did we build a solution fit for stakeholder use? | Stakeholder needs, operational/lifecycle concepts, context of use, intended outcomes | Representative scenarios, user evaluation, operational trials, quality-in-use and outcome evidence |

TDD is an implementation technique and a useful source of verification evidence.
It is neither the complete verification process nor validation.

## Decision and exit criteria

Issue `candidate` only when:

- the candidate and every applicable baseline are uniquely identified;
- requirements and acceptance criteria are approved, controlled, and traceable;
- architecture and interfaces address material concerns and risks;
- planned implementation and integration work for the candidate is complete;
- verification covers applicable requirements with reviewable results;
- validation provides adequate evidence of fitness for intended use;
- critical defects and findings are closed, and all other deviations have disposition;
- security, privacy, safety, supplier, licensing, and compliance obligations are addressed;
- build, deployment, migration, rollback, recovery, operation, support, and
  user-readiness evidence is sufficient for Production;
- residual risks and technical debt have accountable owners and authorized acceptance;
- the Production handoff is versioned, complete, and reproducible enough for its purpose.

Use `rework` for a failed criterion within the approved direction, `hold` for a
time-bounded dependency or evidence gap, and `stop` when feasibility, value,
authority, or acceptable risk no longer exists. Return to Concept when evidence
invalidates stakeholder needs, intended outcomes, or the selected solution class.

## Skill routing

| Development activity | Skill | How to use it | Limitation |
| --- | --- | --- | --- |
| Complete the specification handoff | [`spec-driven-development`](../../.agents/skills/spec-driven-development/SKILL.md) | Mature objectives, boundaries, success criteria, commands, structure, style, and testing approach before implementation | Its template is not a full ISO 29148 requirements baseline or traceability system |
| Decompose controlled scope | [`planning-and-task-breakdown`](../../.agents/skills/planning-and-task-breakdown/SKILL.md) | Produce dependency-ordered, risk-aware increments with acceptance and verification | File-count limits are heuristics, not stage exit criteria |
| Ground framework/library decisions | [`source-driven-development`](../../.agents/skills/source-driven-development/SKILL.md) | Verify current official sources before choosing or using technology | Source citation does not prove architecture fitness |
| Design public boundaries and contracts | [`api-and-interface-design`](../../.agents/skills/api-and-interface-design/SKILL.md) | Apply contract-first design to APIs, modules, and service boundaries | Does not create a complete architecture description or evaluate all quality attributes |
| Implement coherent increments | [`incremental-implementation`](../../.agents/skills/incremental-implementation/SKILL.md) | Deliver one safe, compilable, rollback-friendly vertical or risk slice | Must consume controlled requirements and update traceability |
| Develop behavior with tests | [`test-driven-development`](../../.agents/skills/test-driven-development/SKILL.md) | Use red-green-refactor and regression tests for logic and bug fixes | TDD is not full verification, validation, or proof of test adequacy |
| Diagnose failures | [`debugging-and-error-recovery`](../../.agents/skills/debugging-and-error-recovery/SKILL.md) | Reproduce, localize, reduce, fix root cause, guard, and verify | A fix still requires requirement and evidence updates |
| Assess work products and integration readiness | [`code-review-and-quality`](../../.agents/skills/code-review-and-quality/SKILL.md) | Review correctness, readability, architecture, security, performance, and verification | It is code/change focused; ISO 20246 also applies to non-code work products |
| Reduce unnecessary complexity | [`code-simplification`](../../.agents/skills/code-simplification/SKILL.md) | Simplify after behavior is controlled and preserve exact behavior | Do not use it to change requirements or architecture implicitly |
| Address code-level security | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Apply secure boundary, input, authentication, data, and dependency practices | Does not replace threat modeling, security requirements, assurance, or risk acceptance |
| Measure and improve performance | [`performance-optimization`](../../.agents/skills/performance-optimization/SKILL.md) | Profile against explicit performance requirements before optimizing | Web targets are contextual examples, not universal acceptance thresholds |
| Preserve technical decisions and knowledge | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Record significant architecture and interface decisions and update public/operational docs | ADRs do not replace requirements, test, configuration, or readiness records |

## Recommended skill sequences

For a normal new capability:

```text
spec-driven-development
  → planning-and-task-breakdown
  → source-driven-development (when technology facts matter)
  → api-and-interface-design (when boundaries change)
  → incremental-implementation + test-driven-development
  → security-and-hardening (throughout applicable work)
  → debugging-and-error-recovery (on failures)
  → code-review-and-quality
  → documentation-and-adrs
  → broader verification + validation + candidate decision
```

For a bug fix:

```text
debugging-and-error-recovery
  → test-driven-development (reproduction first)
  → incremental-implementation
  → security / performance checks as affected
  → code-review-and-quality
  → regression verification and candidate evidence
```

For an architecture- or interface-heavy change, define and evaluate concerns,
quality attributes, alternatives, and contracts before decomposing
implementation. `api-and-interface-design` supplements this work; it does not
replace an architecture workflow.

## Current automation gaps

The repository still lacks native skills for:

- ISO 29148-aligned requirements definition, quality checks, baselining, and traceability;
- ISO 42010-aligned architecture description and scenario-based evaluation;
- integration strategy and interface-evidence management across components;
- risk-based verification planning and requirement-to-evidence coverage analysis;
- stakeholder and quality-in-use validation in representative contexts;
- candidate evidence aggregation and machine-readable Development decisions;
- risk-based tailoring and independence decisions for regulated or critical work.

These gaps should be filled with focused skills before creating a broad
Development orchestrator. An orchestrator should route and check evidence, not
repeat requirements, architecture, implementation, and V&V instructions.

## Tailoring

Tailoring must consider consequence of failure, uncertainty, reversibility,
novelty, regulatory obligations, supplier dependence, data sensitivity, and
system complexity. It may change review independence, evidence fidelity,
environment realism, automation, documentation depth, and decision frequency.
It may not silently remove requirements control, configuration identity,
verification, validation, risk disposition, or the candidate decision.

[12207]: https://www.iso.org/standard/90219.html
[15288]: https://www.iso.org/standard/81702.html
[24748-5]: https://www.iso.org/standard/60062.html
[29148]: https://www.iso.org/standard/72089.html
[42010]: https://www.iso.org/standard/74393.html
[25010]: https://www.iso.org/standard/78176.html
[25030]: https://www.iso.org/standard/72116.html
[29119-2]: https://www.iso.org/standard/79428.html
[29119-3]: https://www.iso.org/standard/79429.html
[20246]: https://www.iso.org/standard/67407.html
[15939]: https://www.iso.org/standard/71197.html
[15289]: https://www.iso.org/standard/74909.html
[ssdf]: https://csrc.nist.gov/pubs/sp/800/218/final
