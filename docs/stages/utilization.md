# Utilization Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

Navigation: Previous: [Production](production.md) ·
[Lifecycle](../reference-lifecycle.md) · [Process map](../process.md) · Next:
[Support](support.md)

## Purpose and boundary

The Utilization stage operates an authorized release in its intended context
and determines whether it remains safe, controlled, useful, and supportable.
It starts when Production authorizes a release for use and establishes the
identity of the active release and configuration. It continues until use ends
or a Retirement decision transfers the product into controlled
decommissioning.

Utilization is not a one-time acceptance gate. It is a recurring control loop:
operate, observe, respond, recover, measure, learn, and decide. It overlaps
Support continuously and can trigger new Concept, Development, Production, or
Retirement work.

## Operation is not support

- **Utilization** runs the current service, protects users, handles operational
  events, and measures outcomes in the real context of use.
- **Support** changes or sustains the product so that it can continue to meet
  its requirements as defects, dependencies, threats, and needs evolve.
- **Production** creates and authorizes the controlled release that Utilization
  operates.

An incident may start in Utilization, require a Support fix and a Development
change, pass through Production, and return as a new active baseline. Preserve
the trace across that whole loop.

## Standards model

The standards form complementary layers. This repository uses their public
descriptions and does not reproduce licensed requirements or claim conformity.

| Source | Application in this stage | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Software lifecycle operation processes and their links to maintenance and other lifecycle processes | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | System utilization and the wider system lifecycle | Published |
| [ISO/IEC 20000-1:2018][20000-1] | Requirements for a service management system covering planning, transition, delivery, assurance, and improvement | Published and confirmed; amended 2024 |
| [ISO/IEC 20000-2:2019][20000-2] | Guidance for applying the service management system requirements | Published and confirmed |
| [ISO/IEC 20000-10:2018][20000-10] | Service management concepts and vocabulary | Published and confirmed |
| [ISO/IEC 25019:2023][25019] | Quality-in-use model tied to specified users, goals, resources, and context of use | Published |
| [ISO/IEC 25022:2016][25022] | Candidate quality-in-use measures; values and rating levels remain context-specific | Published; revision in progress |
| [ISO/IEC/IEEE 15939:2017][15939] | Measurement process driven by information needs and validity of results | Published and confirmed |
| [ISO/IEC 27001:2022][27001] | Risk-based information security management during operation | Published; amended 2024 |
| [NIST SP 800-61 Rev. 3][800-61] | Cybersecurity incident response integrated with risk management | Final, 2025 |
| [ISO/IEC 27031:2025][27031] | ICT readiness and recovery capability for business continuity | Published |

ISO/IEC 25022 remains published but is marked for revision. Its measures may be
used as candidates, not as timeless universal targets. Recheck its status and
fit before adopting it in a regulated or long-lived measurement system.

## How the standards fit together

1. ISO/IEC/IEEE 12207 and 15288 establish operation or utilization as lifecycle
   work connected to maintenance, transition, risk, configuration,
   measurement, and information management.
2. ISO/IEC 20000-1 supplies the service-management control system: ownership,
   planning, controlled delivery, monitoring, review, and continual
   improvement. ISO/IEC 20000-2 explains application, while 20000-10 supplies
   vocabulary.
3. ISO/IEC 25019 describes what quality in use means for a specified context.
   ISO/IEC 25022 offers measurement candidates, and ISO/IEC/IEEE 15939 defines
   how to select and validate measures from actual information needs.
4. ISO/IEC 27001 keeps information-security risk under management. NIST SP
   800-61 Rev. 3 supplies an incident-response risk-management profile, and
   ISO/IEC 27031 addresses ICT readiness and recovery for continuity.

These sources do not require one observability product, ticket system, on-call
model, or reliability framework. SLI/SLO practices, error budgets, incident
command systems, and blameless reviews are useful implementation patterns when
tailored to the service. Do not present them as universal ISO requirements.

## Roles and decision rights

One person may hold several roles, but accountability must remain explicit.

| Role | Accountable for |
| --- | --- |
| Service or product owner | Intended outcomes, service commitments, funding, and the recurring continue/change/retire decision |
| Operations owner | Active baseline, operating procedures, telemetry, capacity, recovery, and day-to-day control |
| Incident lead | Coordination, priorities, safety, communication, and recovery during a significant incident |
| Security or privacy owner | Security monitoring, incident obligations, control effectiveness, and residual-risk decisions |
| Support owner | Disposition of defects, problems, vulnerabilities, and change requests leaving Utilization |
| Measurement owner | Information needs, measure definitions, data quality, analysis validity, and review cadence |
| Change or release authority | Authorization of operational changes and new releases at the required independence level |
| Business continuity owner | Continuity objectives, dependencies, exercises, and recovery acceptance |

Automation may detect, classify, notify, collect evidence, and execute bounded
remediation. It must not silently accept residual risk, alter commitments, or
make an irreversible stop/retire decision unless that authority is explicitly
delegated and auditable.

## Entry criteria

Utilization may accept a release only when the handoff from Production identifies:

- the authorized release, artifact digest, deployment, and configuration
  baseline;
- target users, service consumers, environments, dependencies, and owners;
- service and risk objectives, thresholds, and escalation paths;
- deployment verification, rollback, backup, restoration, and continuity
  procedures appropriate to impact;
- telemetry required to establish health and detect material failure;
- known defects, limitations, accepted risks, expiry conditions, and support
  arrangements;
- user, operator, security, privacy, compliance, and communication information;
- the decision record authorizing use.

Missing evidence does not become valid merely because deployment succeeded.
Reject the handoff, constrain use, or record a time-bounded exception with an
owner and compensating controls.

## Operating workflow

### 1. Accept and identify the active baseline

Verify the deployed system against the Production decision and record what is
actually in use. Include release and configuration identity, environment,
feature state, migrations, dependencies, locations, and authorized deviations.
Detect configuration drift and retain enough history to reconstruct the state
at any material event.

Outputs:

- active-release and configuration record;
- verified ownership and support roster;
- accepted handoff or explicit exception;
- link to the Production authorization and deployment evidence.

### 2. Establish the service and control model

Translate stakeholder needs, obligations, and risks into operational controls.
Define service scope, consumers, critical journeys, dependencies, hours of
operation, support model, objectives, thresholds, review cadence, escalation,
and decision authority. Resolve conflicts between business outcomes, user
safety, reliability, security, privacy, cost, and sustainability explicitly.

SLIs, SLOs, and error budgets may encode some objectives. If used, define their
population, calculation, window, data source, exclusions, missing-data
treatment, and decision consequence. A metric without an owner or a linked
decision is telemetry, not a control.

Outputs:

- service model and ownership map;
- objectives, indicators, thresholds, and consequences;
- dependency and obligation register;
- risk treatments and authorized operating envelope.

### 3. Operate the controlled service

Run the service within approved configuration, access, data-handling, and
change boundaries. Control privileged access, secrets, scheduled work,
configuration, jobs, certificates, dependencies, suppliers, storage, capacity,
and cost. Record material operator and automated actions. Route changes through
the applicable change and release controls rather than editing the active
baseline invisibly.

Outputs:

- operational and access records;
- configuration and dependency status;
- capacity, certificate, supplier, and lifecycle forecasts;
- approved changes and detected drift.

### 4. Observe the service and validate the evidence

Collect signals that can reveal user impact, service health, security events,
dependency failure, resource exhaustion, data-quality loss, and control
failure. Test the observability path itself: coverage, freshness, clocks,
cardinality, retention, access, integrity, and alert delivery.

Prefer actionable detection linked to an owner and response. Avoid using the
absence of alerts as proof of health. Correlate technical telemetry with user
journeys and outcomes, and make blind spots and sampling limitations visible.

Outputs:

- telemetry inventory and coverage assessment;
- data-quality and alert-delivery checks;
- current service and risk views;
- owned observability gaps.

### 5. Manage events, requests, incidents, and problems

Use the organization's approved vocabulary and classification scheme. At a
minimum, distinguish:

- an **event** or signal requiring evaluation;
- a **service request** handled through a defined fulfilment path;
- an **incident** requiring restoration of acceptable service or risk state;
- a **problem** or underlying cause requiring investigation and recurrence
  treatment;
- a **change** that modifies a controlled baseline.

Classification determines urgency, authority, evidence, communication, and
handoff; it must not delay protection of users. Link related records without
assuming every incident needs a code change or every alert is an incident.

Outputs:

- classified and deduplicated records;
- impact, urgency, owner, and response target;
- trace links among events, incidents, problems, changes, and releases;
- accountable disposition.

### 6. Respond, recover, and communicate

For a significant incident, establish command, scope, chronology, decision
authority, communication channels, and evidence preservation. Contain impact,
restore the safest acceptable service, verify recovery from the user's
perspective, and continue observation for recurrence. Security incidents must
follow the applicable legal, contractual, privacy, and evidence-handling paths.

Recovery takes precedence over speculative root-cause work when continued
investigation would prolong harm. Emergency changes remain controlled changes:
record the authority, exact action, verification, residual risk, and follow-up.

Outputs:

- incident chronology and decision log;
- impact and affected-scope assessment;
- containment, recovery, and verification evidence;
- timely stakeholder communications;
- follow-up problems, risks, and changes.

### 7. Maintain recovery and continuity capability

Keep backups, restoration, failover, fallback, and continuity procedures
aligned with the active architecture, data, dependencies, and agreed recovery
needs. Test restoration and continuity through proportionate exercises. A
successful backup job is not proof that data, service, or business operations
can be restored within the required conditions.

Track single points of failure, dependency and supplier assumptions, capacity
headroom, credential availability, operator access, and recovery-environment
drift. Record exercise findings and retest corrective actions.

Outputs:

- recovery objectives and dependency assumptions;
- backup integrity and restoration results;
- continuity and failover exercise evidence;
- gaps, treatments, owners, and retest dates.

### 8. Measure quality in use and intended outcomes

Start from a decision-relevant information need, not an available dashboard.
Specify the users and stakeholders, goals, tasks, environment, resources, and
other conditions that define the context of use. Select measures, data sources,
analysis methods, validity checks, ownership, cadence, and thresholds.

Separate service behavior from quality in use and business or mission outcome:
a service may meet availability targets while users cannot complete their work,
or usage may rise without producing the intended benefit. Segment results to
expose material differences and protect privacy. Re-specify the context and
measures when users, goals, environment, or operating assumptions change.

Outputs:

- information needs and measurement definitions;
- specified context of use;
- data provenance, quality, and validity assessment;
- service, quality-in-use, risk, cost, and outcome analysis;
- uncertainty, bias, and limitations.

### 9. Learn and route lifecycle feedback

Review significant incidents, repeated failure, near misses, control weakness,
user friction, changed threats, dependency risk, cost, and outcome evidence.
Focus on system conditions and effective prevention rather than individual
blame. Turn findings into owned, prioritized work with a due date and a link to
the lifecycle decision it may affect.

Route:

- immediate restoration and operational-control work within Utilization;
- defects, vulnerabilities, dependency updates, and sustainment to Support;
- product changes through specification, Development, and Production;
- changed needs, context, or viability questions to Concept;
- obsolete or unsustainable capability toward Retirement.

Outputs:

- review findings and contributing conditions;
- corrective, preventive, adaptive, or improvement actions;
- traceable handoffs and verified closure;
- updated runbooks, controls, requirements, and risks.

### 10. Review and make the recurring use decision

At a risk-based cadence and after material events, assemble current evidence
and record one of the following:

- `continue`: remain within the approved operating envelope;
- `constrain`: limit users, features, traffic, data, geography, or integrations;
- `recover`: execute the approved restoration or continuity path;
- `change`: initiate accountable Support, Concept, Development, or Production work;
- `retire`: initiate controlled Retirement.

The decision records owner, time, evidence, conditions, exceptions, expiry, and
next review. Several decisions may coexist for different service components or
user populations.

## Utilization control loop

```text
Production authorization
          |
          v
active release + configuration --> operate --> observe
          ^                                |        |
          |                                v        v
    new controlled release <--- change <-- respond/recover
                                              |
                                              v
context + information needs --> measure --> learn
                                      \\        |
                                       \\       v
                                        recurring decision
                                      /    |      |       \
                              continue constrain change retire
```

The loop is intentionally non-linear. An urgent recovery can occur before full
measurement or diagnosis, while every material action still produces evidence
for later review.

## Evidence and traceability contract

Maintain at least these links:

```text
Production decision -> active release/configuration
stakeholder need + obligation + risk -> service objective/threshold
objective/threshold -> indicator -> telemetry source -> validity check
event -> incident -> action -> recovery verification
incident/problem -> finding -> risk/requirement/change -> release
context of use -> quality-in-use measure -> analysis -> outcome decision
continuity need -> recovery capability -> exercise -> finding -> retest
all material evidence -> recurring utilization decision
```

Evidence must be attributable, timestamped, protected from inappropriate
change, retained according to policy, and linked to the active baseline. A
dashboard screenshot without its query, time range, population, release, and
data-quality context is weak evidence. A closed ticket without recovery or
effectiveness verification is not proof of completion.

## Decision and exit criteria

Continued use requires evidence that:

- the active release and material configuration are known and controlled;
- owners, escalation, and decision authority are current;
- service, security, privacy, continuity, and outcome thresholds remain
  acceptable or have authorized treatment;
- observability can detect material user, service, dependency, and control
  failure, with blind spots made explicit;
- incident response, restoration, and continuity capabilities remain credible;
- operational risks and exceptions have owners, expiry, and compensating controls;
- quality in use and intended outcomes are measured in the current context;
- feedback and follow-up actions have accountable disposition.

Failure of a criterion requires a `constrain`, `recover`, `change`, or `retire`
decision, not an undocumented continuation. Utilization exits only when use has
ended and the Retirement stage owns the controlled closure.

## Skill routing

The source skill set contains useful supporting workflows but no complete
steady-state operations workflow.

| Need | Use | Boundary in Utilization |
| --- | --- | --- |
| Accept a release in a target context or reassess after material target change | [`operational-acceptance`](../../.agents/skills/operational-acceptance/SKILL.md) | Establishes target-bound operability, recovery, and support readiness; it does not implement the recurring operational control loop |
| Observe a newly released change and decide whether to continue or roll back | [`shipping-and-launch`](../../.agents/skills/shipping-and-launch/SKILL.md) | Covers rollout and immediate post-release observation, not ongoing service management |
| Diagnose a technical operational failure after immediate safety and coordination are established | [`debugging-and-error-recovery`](../../.agents/skills/debugging-and-error-recovery/SKILL.md) | Supplies root-cause discipline; it is not incident command, stakeholder communication, or continuity management |
| Diagnose and improve a measured performance gap | [`performance-optimization`](../../.agents/skills/performance-optimization/SKILL.md) | Requires a context-specific objective and representative operational baseline; example thresholds in the skill are not policy |
| Assess or improve software security controls | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Supports product hardening; it does not replace an ISMS, security operations, or incident-response process |
| Preserve operational decisions, runbooks, and learned knowledge | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Documentation supports evidence but does not prove live control effectiveness |
| Plan migration or removal after an operational `change` or `retire` decision | [`deprecation-and-migration`](../../.agents/skills/deprecation-and-migration/SKILL.md) | Begins downstream migration work; formal closure remains in Retirement |

Do not invoke all related skills for routine operation. Select the workflow
matching the event and preserve the resulting evidence in the Utilization loop.

## Recommended skill sequences

- **New release observation:** `operational-acceptance` ->
  `shipping-and-launch` -> verify active baseline -> observe against release
  thresholds -> continue, constrain, or roll back.
- **Service incident:** establish incident control and protect users -> recover
  -> `debugging-and-error-recovery` for diagnosis -> Support/Development change
  -> Production -> verify recurrence guard in Utilization.
- **Performance degradation:** verify user impact and data quality ->
  `performance-optimization` -> controlled change -> measure the same objective
  after release.
- **Security weakness:** apply the incident path when exploitation or exposure
  is suspected -> `security-and-hardening` for product controls -> verify
  operational detection and residual risk separately.
- **Loss of viability or supportability:** record the operational evidence ->
  Concept/Support decision -> `deprecation-and-migration` when migration is
  approved -> Retirement closure.

## Current automation gaps

No additional skill from the reviewed source repository was copied for this
stage: its launch, debugging, performance, security, and documentation skills
support parts of Utilization but do not implement its operational control loop.
Native harness skills are still needed for:

- recurring active-baseline drift detection and reconciliation;
- service objectives, indicator definitions, telemetry quality, and review;
- incident command, impact assessment, communication, and evidence preservation;
- backup restoration and continuity exercises;
- capacity, dependency, supplier, certificate, and lifecycle forecasting;
- quality-in-use and outcome measurement;
- operational review and machine-readable recurring decisions.

Each future skill should implement one repeatable workflow and refer to this
document for lifecycle policy rather than duplicating the policy in the skill.

## Tailoring

Tailor service objectives, on-call coverage, response times, recovery targets,
telemetry, retention, review cadence, exercise frequency, and independence to
impact, obligations, and operating context. Document:

- what was reduced, increased, or automated;
- the risk and evidence supporting the choice;
- who approved it and when it expires;
- the trigger for reassessment.

Low criticality justifies proportionate controls, not absent ownership,
unknown configuration, unusable recovery, or unmeasured outcomes. Higher
criticality may require independent authorization, redundant control paths,
formal exercises, regulated notification, or human approval for automated
remediation.

[12207]: https://www.iso.org/standard/90219.html
[15288]: https://www.iso.org/standard/81702.html
[20000-1]: https://www.iso.org/standard/70636.html
[20000-2]: https://www.iso.org/standard/72120.html
[20000-10]: https://www.iso.org/standard/74316.html
[25019]: https://www.iso.org/standard/78177.html
[25022]: https://www.iso.org/standard/35746.html
[15939]: https://www.iso.org/standard/71197.html
[27001]: https://www.iso.org/standard/27001.html
[800-61]: https://csrc.nist.gov/pubs/sp/800/61/r3/final
[27031]: https://www.iso.org/standard/27031
