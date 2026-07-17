# Concept Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

Navigation: [Lifecycle](../reference-lifecycle.md) · [Process map](../process.md)
· Next: [Development](development.md)

## Purpose and boundary

The Concept stage decides whether an observed problem, opportunity, obligation,
or risk justifies further investment. It defines the mission or business
problem, explores solution classes, establishes lifecycle concepts and
stakeholder needs, and records an explicit investment decision.

Concept begins with a trigger and an accountable sponsor. It ends with
`proceed`, `hold`, `redirect`, or `stop`. A `proceed` decision transfers an
agreed problem-and-needs baseline into Development; it does not authorize an
unexamined preferred implementation.

Detailed system/software requirements, architecture, technology selection, and
implementation planning belong primarily to Development. They may be explored
in Concept only far enough to evaluate feasibility, risk, and alternatives.

## Standards model

No single standard prescribes a complete product-discovery playbook. The stage
is assembled from complementary standards:

| Source | Role in Concept | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 24748-1:2024][24748] | Defines lifecycle-stage and decision-point concepts and tailoring | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | Supplies the core Business or Mission Analysis and Stakeholder Needs and Requirements Definition processes | Published |
| [ISO/IEC/IEEE 12207:2026][12207] | Aligns the software lifecycle with the system process framework and covers conception through retirement | Published |
| [ISO/IEC/IEEE 29148:2018][29148] | Defines requirements-engineering processes and information items across the lifecycle | Published; revision in development |
| [ISO 9241-210:2019][9241-210] | Adds human-centred design and understanding of the context of use for interactive systems | Published and confirmed |
| [ISO/IEC 25030:2019][25030] | Adds elicitation, definition, use, and governance of measurable quality requirements | Published and confirmed |
| [ISO 31000:2018][31000] | Provides the general risk-management overlay | Published; revision in development |
| [ISO/IEC 27005:2022][27005] | Specializes risk management for information security | Published |
| [NIST SP 800-160 Vol. 1 Rev. 1][800-160] | Integrates stakeholder protection needs and trustworthiness into systems engineering | Final, 2022 |
| [ISO 31700-1:2023][31700] | Adds lifecycle privacy-by-design requirements for consumer products and services | Published; conditional scope |

The public catalog descriptions establish the standards' scope. Clause-level
conformance requires access to the licensed standards and a separately scoped
assessment.

## How the standards fit together

The core Concept flow comes from ISO/IEC/IEEE 15288:

1. **Business or Mission Analysis** defines the strategic problem or
   opportunity, desired mission outcomes, constraints, and viable solution
   classes. A solution class may be a new system, a change to an existing
   system, acquisition, reuse, an operational or process change, or no action.
2. **Stakeholder Needs and Requirements Definition** identifies lifecycle
   stakeholders, develops operational and other lifecycle concepts, and turns
   their needs into an integrated stakeholder-oriented baseline used later for
   validation.

These processes are iterative, not sequential gates. Discovering a stakeholder
need can change the mission framing; comparing solution classes can expose new
stakeholders or constraints.

ISO/IEC/IEEE 29148 makes the resulting needs and requirements explicit,
well-formed, managed, and traceable. ISO 9241-210 adds users, tasks,
environments, and context of use. ISO/IEC 25030 prevents quality from remaining
as vague adjectives. ISO 31000, ISO/IEC 27005, NIST SP 800-160, and ISO 31700-1
apply risk, protection, trustworthiness, and privacy considerations before a
solution is committed.

## Roles and decision rights

| Role | Accountability |
| --- | --- |
| Sponsor / mission owner | Own the problem, value hypothesis, funding boundary, and final Concept decision |
| Concept lead / analyst | Run discovery, maintain evidence and traceability, and keep problem and solution spaces distinct |
| Stakeholder representatives | Own and validate their needs, constraints, scenarios, and acceptance intent |
| Risk and specialty owners | Identify material security, privacy, safety, legal, operational, support, and supplier concerns |
| Decision authority | Issue `proceed`, `hold`, `redirect`, or `stop` and accept conditions and residual uncertainty |

One person may hold several roles for a small change, but accountability and the
decision must remain explicit.

## Entry criteria

- a recorded trigger: problem, opportunity, obligation, or unacceptable risk;
- a sponsor or accountable problem owner;
- enough initial context to identify materially affected stakeholder classes;
- known time, policy, regulatory, contractual, and organizational constraints;
- a preliminary decision scope and authority.

If there is no accountable owner or no decision that the work can influence,
do not manufacture a Concept process; record the blocker or stop.

## Operating workflow

### 1. Frame the trigger and decision

- Record what was observed, by whom, and with what supporting evidence.
- State the decision to be made, decision authority, deadline, and reversibility.
- Separate the observed problem from the initially proposed solution.
- Define the system of interest and what is outside the present decision.

Output: **concept brief** and initial scope.

### 2. Analyze the business or mission problem

- Describe the current state, desired outcomes, drivers, constraints, and
  consequences of no action.
- Define outcome measures and leading indicators before selecting a design.
- Identify assumptions and the evidence needed to validate them.
- Develop credible solution classes, including reuse, acquisition, operational
  change, and no-build/no-action alternatives.

Output: **mission/problem analysis**, outcome model, and solution-class set.

### 3. Identify stakeholders and lifecycle concepts

- Identify acquirers, users, operators, maintainers, support teams, suppliers,
  regulators, affected non-users, and retirement/data-disposition owners.
- Describe operational scenarios and context of use: users, goals, tasks,
  environments, external systems, and abnormal conditions.
- Describe lifecycle concepts for acquisition, development, production,
  deployment, utilization, support, and retirement where material.
- Capture conflicts between stakeholder needs rather than silently resolving them.

Output: **stakeholder map**, context-of-use description, operational concept,
and lifecycle-concept set.

### 4. Define and analyze integrated needs

- Capture stakeholder needs in stakeholder language before translating them
  into solution or software requirements.
- Add measurable quality needs for performance, reliability, usability,
  accessibility, security, privacy, maintainability, portability, and other
  applicable characteristics.
- Identify protection needs, assets, loss consequences, threats, and security
  risk at the level necessary to compare concepts.
- Trace every material need to its stakeholder, source, scenario, or obligation.
- Check needs for conflicts, omissions, feasibility, verifiability, and ability
  to support later validation.

Output: **integrated stakeholder-needs baseline**, quality needs, protection
needs, and traceability.

### 5. Evaluate alternatives and feasibility

- Evaluate each credible solution class against outcomes, needs, lifecycle
  cost, schedule, organizational capability, risks, dependencies,
  supportability, and retirement impact.
- Use prototypes, experiments, research, or supplier discovery only to reduce a
  named uncertainty.
- Record what evidence would falsify the preferred direction.
- Avoid false precision: estimates must expose assumptions and ranges.

Output: **alternatives and feasibility assessment** with a recommended
direction, rejected alternatives, and unresolved uncertainty.

### 6. Validate the concept

- Review the problem framing and integrated needs with representative stakeholders.
- Confirm that proposed outcome measures would demonstrate actual value, not
  just delivery activity.
- Test the highest-impact assumptions and failure modes proportionally to risk.
- Confirm that downstream validation can trace back to stakeholder needs and
  operational/lifecycle concepts.

Output: **concept validation record** and updated evidence.

### 7. Decide and baseline

- Assemble the decision package without hiding dissent, exceptions, or weak evidence.
- Apply the exit criteria below.
- Record `proceed`, `hold`, `redirect`, or `stop`, including conditions, owner,
  timestamp, expiry/review date, and accepted residual uncertainty.
- Version and baseline the evidence passed to Development.

Output: **Concept decision record** and, for `proceed`, a controlled handoff.

## Evidence and traceability contract

The harness should preserve this minimum graph rather than require one large
document:

```text
trigger / source
  → concept brief
  → mission outcomes and measures
  → stakeholders + operational/lifecycle concepts
  → stakeholder, quality, and protection needs
  → alternatives + assumptions + risks
  → validation evidence
  → Concept decision
  → Development baseline
```

Minimum evidence:

- concept brief and decision scope;
- problem or opportunity evidence;
- stakeholder and affected-party map;
- operational concept, context of use, and relevant lifecycle concepts;
- intended outcomes and measurable success and stop indicators;
- integrated stakeholder, quality, protection, and compliance needs;
- assumptions, constraints, dependencies, and trace links;
- risk register with owners and treatment intent;
- alternatives and feasibility assessment, including no action;
- validation results and unresolved disagreements;
- signed or attributable Concept decision.

## Decision and exit criteria

`Proceed` only when:

- the problem, desired outcomes, and consequences of no action are evidence-backed;
- the decision authority and accountable sponsor are known;
- representative lifecycle stakeholders and affected parties were considered;
- operational and lifecycle concepts are sufficient to understand use,
  operation, support, and retirement implications;
- stakeholder, quality, and protection needs are explicit and traceable;
- credible alternatives were compared using declared criteria;
- material assumptions, dependencies, and risks have owners and treatment intent;
- success, failure, validation, and stop criteria can be evaluated;
- the recommended direction is feasible enough to justify the next investment;
- the Development handoff is versioned and approved.

Use `hold` when a time-bounded evidence gap can change the decision, `redirect`
when the framing or solution class must change, and `stop` when value,
feasibility, authority, or acceptable risk is absent.

## Skill routing

| Concept activity | Skill | How to use it | Limitation |
| --- | --- | --- | --- |
| Clarify an underspecified trigger or sponsor intent | [`interview-me`](../../.agents/skills/interview-me/SKILL.md) | Run interactively until outcome, user, why now, success, constraint, and non-goals are explicitly confirmed | Sponsor intent is only one source; it does not replace broader stakeholder discovery |
| Explore solution classes and challenge the initial proposal | [`idea-refine`](../../.agents/skills/idea-refine/SKILL.md) | Diverge, compare distinct directions, expose assumptions, then converge on a concept one-pager | Its one-pager is not the full standards evidence package |
| Formalize the approved handoff | [`spec-driven-development`](../../.agents/skills/spec-driven-development/SKILL.md) | Use at the Concept/Development boundary to capture objective, boundaries, success criteria, and open questions | Do not force tech stack, commands, code style, or implementation planning into early Concept work |
| Record consequential choices | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Preserve the context, alternatives, decision, and consequences | Its ADR template is technical; adapt it for investment and concept decisions |
| Screen obvious security concerns | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Use its boundary and data concerns as a supplemental checklist | It is code-focused and does not implement protection-needs analysis, threat modeling, or ISO 27005 risk assessment |

Do not invoke `planning-and-task-breakdown` during Concept merely to create an
implementation backlog. Use it after a `proceed` decision and an approved
Development specification. Small research tasks inside Concept may still have
owners, deadlines, and evidence criteria without becoming an implementation plan.

## Recommended skill sequence

For an underspecified new initiative:

```text
interview-me
  → idea-refine
  → standards-driven stakeholder / lifecycle / risk analysis
  → concept validation
  → documentation-and-adrs (Concept decision)
  → spec-driven-development (Development handoff only)
```

For a well-evidenced obligation or narrowly scoped change, skip interactive
steps whose outputs already exist, but verify the evidence and retain the same
decision contract.

## Current automation gaps

The repository still lacks native skills for:

- orchestrating Business or Mission Analysis and producing its evidence graph;
- discovering lifecycle stakeholders and defining operational/lifecycle concepts;
- defining and checking stakeholder-needs traceability;
- running general and security risk assessment against explicit decision criteria;
- assessing Concept evidence and issuing a machine-readable decision record.

These are higher-priority Concept additions than another implementation-planning
skill. A future Concept orchestrator should compose focused skills and verify
their evidence; it should not duplicate their detailed workflows.

## Tailoring

A small reversible change may use one concise concept-and-decision record. A
new product, regulated or safety-critical system, new sensitive-data use,
high-impact supplier dependency, or irreversible investment requires broader
stakeholder representation, independent challenge, stronger risk analysis, and
formal authorization. Tailoring may reduce ceremony, not omit the outcome,
traceability, alternatives, risk, or decision evidence.

[12207]: https://www.iso.org/standard/90219.html
[24748]: https://www.iso.org/standard/84709.html
[15288]: https://www.iso.org/standard/81702.html
[29148]: https://www.iso.org/standard/72089.html
[9241-210]: https://www.iso.org/standard/77520.html
[25030]: https://www.iso.org/standard/72116.html
[31000]: https://www.iso.org/standard/65694.html
[27005]: https://www.iso.org/standard/80585.html
[800-160]: https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final
[31700]: https://www.iso.org/standard/84977.html
