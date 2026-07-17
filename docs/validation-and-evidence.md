# Validation and Evidence

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md)

## Purpose

This document defines how SDLC Harness turns checks, observations, reviews,
and measurements into bounded claims that can support lifecycle decisions. It
applies across every stage. Projects provide their own commands, environments,
evidence stores, thresholds, and approval systems; the harness defines the
portable contract between them.

A successful command is an observation, not a conclusion. A validation result
is useful only when it states what was checked, what the evidence supports,
where the claim stops, and which decision the claim may inform.

## Standards basis

| Source | Contribution to this model | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Lifecycle verification, validation, quality assurance, measurement, information, and decision-management context | Published |
| [ISO/IEC/IEEE 1012:2016][1012] | Risk-tailored verification and validation processes and integrity considerations | Published; confirmed 2022 |
| [ISO/IEC/IEEE 15939:2017][15939] | Measures derived from information needs and evaluation of analysis-result validity | Published; confirmed 2022 |
| [ISO/IEC/IEEE 29119-2:2021][29119-2] | Organizational and project test processes, test monitoring, control, and completion | Published |
| [ISO/IEC 15026-2:2011][15026-2] | Useful assurance-case structure connecting claims, arguments, evidence, and explicit assumptions | Withdrawn; used only as an informative structural source |
| [NIST SP 800-53A Rev. 5][800-53a] | Tailorable assessment objectives, methods, objects, depth, coverage, findings, and risk-informed assessment plans | Final; Release 5.2.0 published 2025 |

This repository does not reproduce the licensed standards or claim conformity
to them. The withdrawn ISO/IEC 15026-2 source is not a normative basis; its
claim-and-evidence structure remains a useful, non-exclusive design pattern.

## Core model

Every material validation should preserve this chain:

```text
information need or requirement
  -> bounded claim
  -> subject + boundary + assumptions
  -> assessment method and procedure
  -> observed evidence
  -> finding
  -> permitted decision use
  -> limitations and residual risk
```

The harness distinguishes these terms:

| Term | Meaning |
| --- | --- |
| **Check** | An executable or human assessment procedure |
| **Evidence** | A retained observation or record produced or examined by a check |
| **Finding** | An interpretation of evidence against stated criteria |
| **Claim** | A bounded statement that the findings support |
| **Decision** | An accountable lifecycle action informed by one or more claims and risks |

Verification asks whether specified requirements were met. Validation asks
whether the result is fit for its intended use in its actual context. A project
may need both; passing one must not be reported as passing the other.

## Validation record

The storage format is project-defined, but a material record must carry the
following semantics. References may point to other controlled records rather
than duplicate them.

| Field | Required meaning |
| --- | --- |
| `id` | Stable validation-record identity |
| `claim` | Precise statement and the requirement, risk, or information need it addresses |
| `subject` | Exact code, configuration, artifact, service, process, or control assessed |
| `boundary` | Included and excluded systems, interfaces, dependencies, users, data, and environments |
| `assumptions` | Provider, credential, runtime, operator, data, time, and other validity assumptions |
| `method` | Examine, test, interview, analysis, observation, or a justified combination |
| `procedure` | Project-provided command, workflow, review protocol, or measurement definition |
| `criteria` | Expected outcome, threshold, oracle, or comparison baseline defined before interpretation |
| `execution` | Time, actor or automation identity, environment, input and tool versions, and real result status |
| `evidence` | Immutable or versioned output references, digests where warranted, and retention/access rules |
| `finding` | `satisfied`, `not_satisfied`, `inconclusive`, `blocked`, or `not_applicable`, with rationale |
| `decision_use` | Decisions this finding may inform and authority required for them |
| `limitations` | What the procedure and evidence do not establish |
| `residual_risk` | Remaining uncertainty, owner, treatment or acceptance, and expiry/review condition |

Do not collapse `blocked`, `inconclusive`, or `not_applicable` into success.
The command exit status and the resulting finding are separate facts: a tool
may execute successfully while reporting failed criteria, and infrastructure
may fail before the subject is assessed.

## Evidence classes and assurance profiles

Projects should classify evidence by the boundary it actually crosses, for
example:

- source or package checks in a controlled development environment;
- artifact construction and inspection;
- deterministic runtime or smoke behavior;
- packaged or composed-stack behavior;
- external service or provider compatibility;
- end-to-end intended-user workflow;
- production or production-like operational observation;
- document, configuration, process, or human-practice examination.

These classes are not a universal ladder. One does not automatically subsume
another: an end-to-end check may provide weak artifact-provenance evidence,
while a signed artifact may provide no evidence of fitness for use.

A project may define named levels such as `L0` through `Ln`, but each level
must be a local, versioned assurance profile that specifies:

- the information needs and claims it covers;
- required evidence classes and independent methods;
- assessment depth and coverage;
- required environment fidelity and external boundaries;
- freshness, retention, integrity, and reviewer requirements;
- permitted decisions and explicit non-claims.

Never infer the meaning of a level from its number or compare levels across
projects without comparing their definitions. Changing a profile creates a
new profile version; historical records retain the definition used at execution.

## Workflow

### 1. Frame the decision and claims

- Identify the lifecycle decision, authority, requirements, risks, and
  information needs.
- Write claims narrowly enough to be falsifiable.
- Identify subject identity, boundaries, assumptions, and material exclusions.
- Select an existing local assurance profile when one matches; otherwise tailor
  the required evidence explicitly.

### 2. Discover the project validation surface

- Inspect repository guidance, build metadata, CI configuration, scripts,
  package definitions, and operating documentation.
- Use project-provided commands and environments. Do not assume a task runner,
  language, cloud, credential mechanism, or deployment topology.
- Identify which checks require external systems, secrets, privileged access,
  special data, hardware, or human review.
- Find the authoritative registry or matrix when the project has one. Avoid
  competing command inventories.

### 3. Design sufficient assessment

- Map each claim to one or more methods, objects, criteria, depth, and coverage.
- Prefer independent and differently shaped evidence for high-consequence
  claims; many copies of the same check do not create independent assurance.
- Include negative, degraded, recovery, compatibility, and boundary behavior
  where relevant.
- Define invalidation conditions before execution: source, dependency,
  artifact, configuration, provider, credential scope, environment, data,
  toolchain, or time changes that make evidence stale.

### 4. Execute without corrupting evidence

- Run checks in the declared environment and preserve the actual exit status.
- Capture high-volume output once in an approved evidence location; inspect the
  retained result instead of rerunning only because a user interface truncated it.
- Record missing prerequisites as `blocked`, not passed. Do not silently replace
  a real external boundary with a mock and preserve the original claim.
- Do not expose secrets or sensitive data in logs. Record identities and scopes
  through safe references.

### 5. Interpret and report

- Compare observations with the predeclared criteria.
- State the finding, supported claim, limitations, invalidation conditions, and
  residual uncertainty.
- Link evidence rather than pasting an unbounded transcript.
- Make clear whether the result is verification, validation, monitoring, or
  another assessment type.

### 6. Make or support the decision

- Aggregate only compatible, current records bound to the same candidate or
  operating baseline.
- Apply the project's decision policy and accountable authority.
- Record exceptions, compensating controls, risk owner, expiry, and follow-up.
- Preserve machine-readable records where automation consumes the decision,
  while keeping a human-readable explanation for consequential outcomes.

## Evidence quality rules

Evidence is decision-grade when it is:

- **relevant** to the exact claim and decision;
- **traceable** to requirements, subject identity, procedure, criteria, and finding;
- **authentic and integral** enough for the consequence of a false claim;
- **repeatable or independently reviewable** where practicable;
- **complete within its declared coverage**, with exclusions visible;
- **current**, with freshness and invalidation rules;
- **proportionate**, so cost and rigor follow consequence and uncertainty;
- **protected**, retained, accessible, and disposed according to policy.

Quantity does not compensate for weak relevance or a missing boundary. A
service process merely starting is not evidence of behavior beyond startup. A
mocked provider is not evidence of real-provider compatibility. A passed unit
suite is not evidence that the packaged release or active deployment is the
tested subject.

## Completion criteria

Validation work is complete only when:

- claims, subjects, boundaries, criteria, and assumptions are explicit;
- required methods, depth, coverage, and evidence classes were satisfied or
  explicitly reported as gaps;
- every check has an unambiguous finding and retained evidence reference;
- evidence is bound to the exact candidate or operating baseline;
- limitations, invalidation conditions, and residual risks are recorded;
- the resulting decision or handoff names its authority and evidence basis;
- failures and blocked checks have not been presented as success.

[12207]: https://www.iso.org/standard/90219.html
[1012]: https://www.iso.org/standard/61337.html
[15939]: https://www.iso.org/standard/71197.html
[29119-2]: https://www.iso.org/standard/79428.html
[15026-2]: https://www.iso.org/standard/52926.html
[800-53a]: https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
