# Support Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

Navigation: Previous: [Utilization](utilization.md) ·
[Lifecycle](../reference-lifecycle.md) · [Process map](../process.md) · Next:
[Retirement](retirement.md)

## Purpose and boundary

The Support stage sustains the required fitness of a software product as
defects, threats, dependencies, platforms, users, and obligations change. It
plans and controls maintenance, routes approved modifications through
Development and Production, preserves supported baselines, and determines
whether continued support remains viable.

Support planning begins before the first release. Active Support overlaps
Utilization and continues until Retirement closes or transfers every support
obligation. It is a lifecycle stage and portfolio capability, not merely a help
desk or an unprioritized defect queue.

## Support is not operation or development

- **Utilization** operates the active release, responds and recovers, and
  measures real-world service and user outcomes.
- **Support** receives product problems and changing conditions, determines
  their disposition, and sustains supported product baselines.
- **Development** specifies, implements, verifies, and validates approved
  product changes.
- **Production** creates and authorizes the controlled maintenance release.

ISO/IEC/IEEE 14764 explicitly excludes operational functions such as backup,
recovery, and system administration. Support may improve those capabilities,
but Utilization performs them. Conversely, restoring service during an incident
does not prove that the underlying defect or vulnerability has been removed.

## Standards model

The sources below form complementary layers. This repository uses their public
descriptions and does not reproduce licensed requirements or claim conformity.

| Source | Application in this stage | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Full lifecycle framework connecting maintenance with development, operation, support, and retirement | Published |
| [ISO/IEC/IEEE 14764:2022][14764] | Software maintenance planning, execution, control, review, evaluation, maintenance types, and related disposal guidance | Published |
| [ISO/IEC 20000-1:2018][20000-1] | Service-management controls for requests, problems, changes, suppliers, service assurance, and improvement | Published and confirmed; amended 2024 |
| [ISO/IEC 20000-2:2019][20000-2] | Guidance for applying the service-management system | Published and confirmed |
| [ISO/IEC 29147:2018][29147] | Receiving vulnerability reports and disclosing remediation information | Published and confirmed; revision in development |
| [ISO/IEC 30111:2019][30111] | Processing and remediating reported potential product or service vulnerabilities | Published and confirmed; revision in development |
| [NIST SP 800-218 SSDF 1.1][800-218] | Secure-development practices, including vulnerability response and root-cause feedback | Final, 2022 |
| [NIST SP 800-216][800-216] | Public guidance for establishing and operating vulnerability disclosure programs | Final, 2023 |

ISO/IEC 29147:2018 and ISO/IEC 30111:2019 remain current published editions,
but replacements are under development. Recheck their status before adopting a
regulated, contractual, or long-lived vulnerability workflow.

## How the standards fit together

1. ISO/IEC/IEEE 12207 establishes maintenance within the complete software
   lifecycle and permits concurrent, iterative, and recursive application.
2. ISO/IEC/IEEE 14764 elaborates software maintenance and distinguishes
   maintenance from operation. It also recognizes maintenance across multiple
   products sharing maintenance resources.
3. ISO/IEC 20000-1 places maintenance work inside a managed service system with
   ownership, controlled changes, supplier coordination, measurement, and
   continual improvement.
4. ISO/IEC 29147 covers vulnerability intake and communication, while ISO/IEC
   30111 covers analysis, remediation, and the handling process between receipt
   and disclosure.
5. NIST SSDF connects vulnerability response to secure Development so root
   causes improve the product and development process. NIST SP 800-216 provides
   additional public guidance for disclosure programs.

Ticket states, severity labels, maintenance windows, semantic versioning, and
specific service-desk tools are implementation choices. Tailor them to product
risk and commitments; do not present a local convention as an ISO requirement.

## Maintenance classification

Classify the intent of maintenance independently from urgency and work type:

| Class | Intent | Example |
| --- | --- | --- |
| Corrective | Correct a discovered fault | Fix an incorrect calculation |
| Adaptive | Preserve fitness in a changed environment | Support a new platform or protocol version |
| Perfective | Improve quality, performance, maintainability, or user value | Reduce latency or simplify a costly subsystem |
| Preventive | Reduce the likelihood or impact of future failure | Replace an unsupported dependency before failure |

A vulnerability fix may be corrective or preventive; an emergency fix may
belong to any class. Classification supports analysis and planning but does not
determine priority by itself.

## Roles and decision rights

One person may hold several roles, but accountability must remain explicit.

| Role | Accountable for |
| --- | --- |
| Product or service owner | Support scope, consumer commitments, investment, priority, and support/retire decisions |
| Support owner | Intake system, classification, response, knowledge, supported baselines, and item disposition |
| Maintainer | Impact analysis, maintenance planning, implementation coordination, and technical closure evidence |
| Development owner | Specification, implementation, verification, validation, and recurrence prevention for approved changes |
| Release authority | Controlled maintenance release and deployment authorization |
| Security response owner | Confidential vulnerability handling, severity and exposure analysis, remediation, coordination, and disclosure |
| Dependency or supplier owner | Component inventory, support status, supplier notices, licenses, and replacement plans |
| Risk or compliance owner | Acceptance of residual risk, exceptions, deadlines, and notification obligations |
| Consumer representative | Validation of impact, compatibility, migration feasibility, and user communication |

Automation may collect, correlate, deduplicate, classify provisionally, propose
priority, open changes, and verify defined checks. It must not silently disclose
a vulnerability, accept residual risk, break compatibility, or end support.

## Entry criteria

Before a product is accepted into support, establish:

- supported products, editions, versions, environments, interfaces, and owners;
- support policy, channels, hours, response expectations, exclusions, and
  escalation paths;
- product, dependency, supplier, license, certificate, and platform inventory;
- source, build, test, configuration, release, and rollback capability;
- maintenance environments and access appropriate to product risk;
- vulnerability reporting, confidential handling, coordination, and disclosure
  paths;
- compatibility, migration, retention, and end-of-support policies;
- known defects, limitations, risks, obligations, and accepted exceptions;
- evidence and knowledge repositories with required access and retention.

Unsupported baselines and best-effort arrangements must be explicit to
consumers. Deployment into use is not a substitute for a support agreement.

## Operating workflow

### 1. Establish and maintain the support model

Define the support portfolio, supported-baseline matrix, consumer commitments,
maintenance classes, prioritization model, change paths, release policy,
vulnerability policy, knowledge model, measures, and review cadence. Forecast
the skills, environments, suppliers, and capacity needed across products.

Outputs:

- versioned maintenance and support plan;
- supported-baseline and compatibility matrix;
- ownership, escalation, and authority map;
- published consumer and vulnerability-reporting information.

### 2. Receive and preserve support inputs

Provide controlled channels for defects, requests, incidents, telemetry,
vulnerabilities, dependency and supplier notices, compliance changes, and
improvement proposals. Acknowledge receipt according to policy, protect
sensitive reports, retain original evidence, and link duplicates without
destroying reporter or affected-context information.

For vulnerability reports, separate the public reporting channel from the
restricted handling record. Do not expose exploit detail, reporter identity, or
unpatched affected populations through ordinary backlog tooling.

Outputs:

- uniquely identified input and source;
- receipt and communication record;
- preserved evidence and confidentiality classification;
- duplicate, related-incident, release, and component links.

### 3. Classify, assess, and prioritize

Determine the affected product and supported baselines, input type, maintenance
class, impact, urgency, exploitability or exposure where applicable, consumer
scope, obligations, safety and security consequences, workarounds, and required
decision date. Distinguish observed impact from hypothesis and confidence.

Priority is a policy decision informed by evidence, not severity alone. Include
active exploitation, reachability, user harm, recurrence, contractual dates,
dependency lifecycle, change risk, remediation availability, and opportunity
cost. Record who can override the normal ordering and why.

Outputs:

- classification and affected-baseline assessment;
- evidence-backed priority and response target;
- immediate mitigation or escalation;
- accountable owner and next decision.

### 4. Reproduce, diagnose, and analyze impact

Preserve operational evidence before changing the system. Reproduce where
possible, localize the failure, determine contributing conditions and root
cause to the depth justified by risk, and identify all affected versions,
components, interfaces, data, consumers, and dependent products.

For vulnerabilities, validate safely in an isolated environment, assess
reachability and exposure, search for variants, coordinate affected suppliers,
and protect embargoed information. Lack of reproduction does not prove absence;
record uncertainty and the monitoring or investigation needed.

Outputs:

- reproduction or documented non-reproduction evidence;
- technical and systemic cause analysis;
- affected and unaffected baseline rationale;
- workaround, mitigation, and candidate treatment options;
- testable recurrence or effectiveness criteria.

### 5. Decide the item disposition

Record one of these dispositions with owner, rationale, evidence, conditions,
due date, and review trigger:

- `resolve`: remove the cause through a controlled change;
- `mitigate`: reduce likelihood or impact without claiming full resolution;
- `defer`: accept time-bounded exposure pending a defined trigger or date;
- `reject`: no product change, with reason and communication;
- `duplicate`: link to the controlling item without losing evidence;
- `transfer`: assign an identified supplier, successor, or lifecycle workflow;
- `retire`: initiate the Retirement decision path.

Residual risk acceptance must come from the authorized risk owner, not from the
maintainer or agent by default. A closed ticket is an administrative state, not
evidence that the problem is resolved.

### 6. Specify and plan the maintenance change

For approved product changes, update the applicable requirement or defect
contract, acceptance criteria, affected interfaces, compatibility expectations,
security and privacy constraints, migration and rollback needs, documentation,
and release scope. Analyze regression surface, dependencies, data changes, and
support consequences before implementation.

Route non-trivial changes through the normal Development stage. Emergency
maintenance may compress timing and approval paths but must retain identity,
authority, focused verification, rollback, residual-risk recording, and
follow-up work.

Outputs:

- approved change or maintenance specification;
- impact, compatibility, regression, and risk analysis;
- implementation and verification plan;
- release, communication, migration, and rollback needs.

### 7. Implement, verify, and validate the change

Use controlled source, dependencies, environments, and incremental changes.
Create a check that demonstrates the reported failure or missing control when
feasible, implement the smallest complete treatment, verify the changed and
affected behavior, and validate the user or operational scenario.

Security fixes require checks for variants and bypasses. Dependency upgrades
require compatibility, license, provenance, and transitive-impact review.
Preserve the link from support item to requirement, change, checks, review,
artifact, and residual risk.

Outputs:

- controlled implementation and review;
- failure-demonstrating and regression checks;
- verification, validation, security, and compatibility evidence;
- updated risk, dependency, and documentation records.

### 8. Produce and transition the maintenance release

Pass the verified candidate through Production. Identify affected and fixed
versions, prerequisites, migration, rollback, known limitations, and the exact
relationship to the support item. Coordinate timing and disclosure when early
release information could increase risk.

Utilization verifies deployment, mitigation removal where appropriate, service
health, and effectiveness in the real context. Do not mark resolution solely
because code merged or an artifact was published.

Outputs:

- authorized, traceable maintenance release;
- release notes, advisory, and consumer instructions;
- deployment and post-release evidence;
- updated supported-baseline matrix.

### 9. Communicate, disclose, and close

Communicate status and action in terms appropriate to consumers and reporters.
For vulnerabilities, coordinate affected parties and disclose remediation
information according to policy, obligations, exploitation risk, fix
availability, and user protection. Preserve revision history and distinguish
confirmed facts from estimates.

Close only after the disposition criteria are met, required consumers can act,
knowledge and records are updated, and follow-up work has owners. Verify that a
mitigation remains effective and that a resolution prevents recurrence in the
defined scope.

Outputs:

- consumer, reporter, supplier, and stakeholder communication;
- vulnerability advisory or justified restricted disclosure;
- closure and effectiveness evidence;
- updated known-error, runbook, support, and migration knowledge.

### 10. Review supportability and improve the system

At a risk-based cadence, analyze demand, aging, recurrence, escape sources,
vulnerability and dependency exposure, response and resolution performance,
change failure, compatibility cost, support capacity, consumer impact, and
maintainer knowledge concentration. Validate measure quality before drawing
conclusions.

Turn trends into product, architecture, process, tooling, supplier, staffing,
or retirement decisions. Reassess support scope when skills, source, build
capability, test environments, dependencies, or economics no longer support
credible maintenance.

Outputs:

- support performance and trend review;
- root-cause and escape-prevention improvements;
- capacity, dependency, and end-of-support forecast;
- `continue`, `constrain`, `invest`, `transfer`, or `retire` portfolio decision.

## Support control loop

```text
Utilization / users / suppliers / security research
                         |
                         v
intake -> classify -> analyze -> disposition
                                  |       \
                                  |        -> mitigate/defer/reject/retire
                                  v
                           specify maintenance
                                  |
                                  v
                   Development -> Production
                                  |
                                  v
                     Utilization verification
                                  |
                                  v
                   communicate -> close -> learn
                                      |        |
                                      +--------+
```

The loop may run concurrently for many supported baselines. Emergency response
can accelerate it, but must not break evidence continuity.

## Vulnerability disclosure is not incident response

- **Vulnerability handling** validates and remediates a potential weakness in a
  product or service.
- **Vulnerability disclosure** receives reports and communicates remediation
  information so affected parties can reduce risk.
- **Incident response** handles suspected or confirmed adverse events and
  restores acceptable risk and service state in Utilization.

One finding may trigger all three workflows. Link them while preserving their
different owners, confidentiality, evidence, urgency, and closure criteria.

## Evidence and traceability contract

Maintain at least these links:

```text
support policy -> supported baseline + commitment
input/report -> preserved evidence -> affected baseline/component
input -> classification + priority -> disposition + authority
problem/vulnerability -> cause/variant analysis -> requirement/change
change -> implementation -> checks/review -> release artifact
release -> deployment -> effectiveness/recurrence verification
vulnerability report -> coordination -> advisory/revision history
dependency/supplier notice -> impact -> update/migration/risk acceptance
support measures -> trend -> improvement/supportability decision
end-of-support decision -> consumer migration -> Retirement
```

Evidence must be attributable, timestamped, access-controlled, retained under
policy, and linked to the exact supported and active baselines. Preserve
confidentiality without making decisions unauditable. Record uncertainty,
contradictory evidence, exceptions, and expiry.

## Item and stage decisions

An item closes only when:

- its affected scope and disposition are recorded;
- the authorized owner accepted residual risk or approved the treatment;
- required changes passed Development and Production controls;
- deployment or consumer action is verified where necessary;
- resolution or mitigation effectiveness is demonstrated;
- required communication, knowledge, and follow-up records are complete.

The Support stage remains viable while:

- supported baselines and commitments are explicit and achievable;
- source, build, test, release, rollback, and diagnostic capabilities remain
  credible;
- critical dependencies, suppliers, environments, and expertise remain
  available or have controlled replacement paths;
- vulnerability intake, handling, remediation, and disclosure remain effective;
- deferred work and residual risks have owners, dates, and review triggers;
- consumers receive usable compatibility, migration, and end-of-support notice.

Support exits only after Retirement closes or transfers outstanding consumers,
data, vulnerabilities, contracts, knowledge, and other obligations.

## Skill routing

| Need | Use | Boundary in Support |
| --- | --- | --- |
| Reproduce, localize, diagnose, and guard against recurrence | [`debugging-and-error-recovery`](../../.agents/skills/debugging-and-error-recovery/SKILL.md) | Technical diagnosis only; it does not set priority, accept risk, coordinate disclosure, or close the support item |
| Inspect the affected active environment without mutation | [`environment-state-inspection`](../../.agents/skills/environment-state-inspection/SKILL.md) | Resolves exact active identity, drift, recent errors, and access gaps as support evidence | It does not repair the environment or close the support item |
| Correct an outbound integration contract | [`integration-client-resilience`](../../.agents/skills/integration-client-resilience/SKILL.md) | Defines bounded deadlines, retries, cancellation, resources, and unknown outcomes for the maintenance change | It does not replace diagnosis, requirements disposition, implementation, or release controls |
| Publish or rotate a support-related secret | [`secret-publication-and-rotation`](../../.agents/skills/secret-publication-and-rotation/SKILL.md) | Controls exact inventory, authority, custody, consumer transition, verification, and rotation closure | Support urgency does not automatically authorize credential mutation or revocation |
| Specify a material corrective, adaptive, perfective, or preventive change | [`spec-driven-development`](../../.agents/skills/spec-driven-development/SKILL.md) | Use for product change contracts, not routine intake administration |
| Break an approved maintenance change into controlled work | [`planning-and-task-breakdown`](../../.agents/skills/planning-and-task-breakdown/SKILL.md) | Requires approved scope and acceptance criteria |
| Demonstrate failure and drive the behavioral fix | [`test-driven-development`](../../.agents/skills/test-driven-development/SKILL.md) | A regression test supports resolution but does not replace impact or effectiveness analysis |
| Deliver a multi-file maintenance change safely | [`incremental-implementation`](../../.agents/skills/incremental-implementation/SKILL.md) | Operates inside Development controls |
| Review a maintenance candidate before integration | [`code-review-and-quality`](../../.agents/skills/code-review-and-quality/SKILL.md) | Review verdict is one part of the release evidence |
| Assess and improve product security controls | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Does not implement confidential intake, coordination, severity authority, or vulnerability disclosure |
| Manage compatibility-breaking replacement and consumer movement | [`deprecation-and-migration`](../../.agents/skills/deprecation-and-migration/SKILL.md) | Must follow an accountable maintain/migrate/retire decision; formal closure belongs to Retirement |
| Produce the controlled maintenance release | [`ci-cd-and-automation`](../../.agents/skills/ci-cd-and-automation/SKILL.md) and [`shipping-and-launch`](../../.agents/skills/shipping-and-launch/SKILL.md) | Production workflows; merge or deployment alone does not close Support |
| Preserve decisions, advisories, runbooks, and support knowledge | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Documentation is necessary evidence but not proof of treatment effectiveness |

## Recommended skill sequences

- **Corrective maintenance:** `debugging-and-error-recovery` ->
  `spec-driven-development` when scope is material ->
  `test-driven-development` -> `incremental-implementation` -> review ->
  Production workflows -> effectiveness verification.
- **Vulnerability remediation:** restricted intake and triage -> safe diagnosis
  and variant search -> `security-and-hardening` plus Development skills ->
  coordinated Production release -> disclosure -> operational verification.
- **Adaptive dependency change:** lifecycle or supplier signal -> affected-scope
  analysis -> specification and plan -> incremental implementation and tests ->
  compatibility review -> controlled release -> baseline update.
- **Compatibility break or end of support:** supportability decision ->
  `deprecation-and-migration` -> controlled releases and consumer verification
  -> Retirement closure.

## Current automation gaps

Existing and newly generalized skills cover debugging, environment inspection,
integration resilience, secret transitions, security, development, launch, and
migration portions of maintenance, but not the complete Support control system.
Native harness skills are still needed for:

- support intake, deduplication, classification, prioritization, and disposition;
- supported-baseline and compatibility-matrix management;
- coordinated vulnerability intake, handling, disclosure, and advisory revision;
- dependency, supplier, license, certificate, platform, and end-of-life monitoring;
- maintenance impact analysis across products and consumers;
- emergency maintenance governance and follow-up;
- effectiveness verification and support-item closure;
- portfolio capacity, supportability, and end-of-support decisions.

Each future skill should implement one repeatable workflow and refer to this
document for lifecycle policy rather than duplicating it.

## Tailoring

Tailor channels, support windows, response targets, maintenance classes,
independence, environments, disclosure coordination, compatibility promises,
release cadence, and evidence depth to risk and commitments. Document:

- what was reduced, increased, or automated;
- the evidence and risk supporting the choice;
- the approver, scope, expiry, and compensating controls;
- the reassessment trigger.

Low criticality may justify simpler queues and release paths. It does not
justify ambiguous supported versions, lost reports, uncontrolled fixes,
unowned vulnerabilities, or silent abandonment. Consumer-visible commitments
and end-of-support changes must be communicated.

[12207]: https://www.iso.org/standard/90219.html
[14764]: https://www.iso.org/standard/80710.html
[20000-1]: https://www.iso.org/standard/70636.html
[20000-2]: https://www.iso.org/standard/72120.html
[29147]: https://www.iso.org/standard/72311.html
[30111]: https://www.iso.org/standard/69725.html
[800-218]: https://csrc.nist.gov/pubs/sp/800/218/final
[800-216]: https://csrc.nist.gov/pubs/sp/800/216/final
