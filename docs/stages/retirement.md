# Retirement Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-16**

Navigation: Previous: [Support](support.md) ·
[Lifecycle](../reference-lifecycle.md) · [Process map](../process.md)

## Purpose and boundary

The Retirement stage ends use and support of a product or defined product
scope without unacceptable impact on people, data, dependent systems,
obligations, or the environment. It converts an authorized retirement decision
into verified migration, information disposition, access revocation, resource
decommissioning, obligation closure, and residual-risk acceptance.

Retirement starts when an accountable authority approves investigation or
execution of retirement. It ends only when intended use has ceased, retained
records and transferred obligations have owners, disposed information and
resources have adequate evidence, and the closure authority accepts the
remaining risk. Turning off a runtime is an activity, not stage completion.

## Deprecation is not retirement

- **Deprecation** discourages new use and signals that a capability or version
  is approaching change or removal.
- **Migration** moves consumers, data, or obligations to a successor state.
- **End of support** ends a defined maintenance commitment.
- **End of operation** ends authorized use of a deployed service or system.
- **Retirement** closes the complete scoped lifecycle, including information,
  identity, infrastructure, suppliers, records, finance, and residual risk.

These milestones may occur at different times. A deprecated interface may
remain supported; a service may stop operating while records must remain
accessible for years; a successor may inherit users without inheriting every
legal or security obligation.

## Standards model

The standards form complementary layers. This repository uses their public
descriptions and does not reproduce licensed requirements or claim conformity.

| Source | Application in this stage | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Software lifecycle retirement and disposal connected to operation, maintenance, configuration, risk, and information management | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | Retirement across complete systems, system elements, and enabling systems | Published |
| [ISO/IEC/IEEE 14764:2022][14764] | Maintenance closure and the related software disposal process | Published |
| [ISO/IEC 20000-1:2018][20000-1] | Controlled service lifecycle, transition, supplier, service, and obligation management | Published and confirmed; amended 2024 |
| [ISO 15489-1:2016][15489] | Creation, capture, control, and management of records over time | Published and confirmed |
| [ISO/IEC 27001:2022][27001] | Risk-based protection and disposition of information assets and access | Published; amended 2024 |
| [ISO/IEC 27040:2024][27040] | Storage security during use and after end of use or end of life | Published |
| [ISO/IEC 27555:2021][27555] | Policies, rules, roles, processes, and documentation for deletion of personally identifiable information | Published; replacement in development |
| [NIST SP 800-88 Rev. 2][800-88] | Enterprise media-sanitization program, validation, and risk-based disposal or reuse | Final, 2025 |

ISO/IEC 27555:2021 remains the published edition but is expected to be replaced
by a revision currently under development. It addresses deletion governance,
not particular legal rules or the suitability of a deletion mechanism. Verify
applicable law, contract, and the current edition before adopting a policy.

## How the standards fit together

1. ISO/IEC/IEEE 12207 and 15288 place retirement inside the complete lifecycle
   and require it to interact with technical and management processes rather
   than occur as an isolated infrastructure task.
2. ISO/IEC/IEEE 14764 links maintenance closure with software disposal.
3. ISO/IEC 20000-1 supplies service-transition and management-system controls
   for changing or ending services and supplier arrangements.
4. ISO 15489-1 governs records that must remain authentic, usable, controlled,
   and attributable after the product that created them is gone.
5. ISO/IEC 27001 and 27040 maintain security through information, storage, and
   access disposition, including end-of-use conditions.
6. ISO/IEC 27555 governs PII deletion policy and evidence. NIST SP 800-88 Rev. 2
   addresses media sanitization and validation at an organizational level.

No standard supplies the organization's exact retention schedule, legal-hold
rules, notice period, cloud-provider deletion guarantee, or acceptable residual
risk. Those must come from applicable authority and be recorded.

## Deletion, sanitization, and decommissioning are different

- **Logical deletion** changes information or system state so data is no longer
  available through the intended interface; it may not remove every copy.
- **PII deletion** follows defined rules, roles, timing, and evidence for
  personally identifiable information.
- **Storage or media sanitization** makes access to target data infeasible for a
  defined level of effort and must be selected and validated for the medium,
  sensitivity, reuse, and disposal path.
- **Cryptographic erase** depends on encryption design and effective key
  sanitization; deleting an application key label is not automatically proof.
- **Decommissioning** removes a system or resource from authorized service. It
  does not by itself prove data deletion or sanitization.
- **Record disposition** may require preservation, transfer, archival, or
  authorized destruction rather than deletion.

Use the precise claim supported by evidence. Do not label account disablement,
database-row deletion, retention expiry, backup rotation, or cloud-resource
termination as equivalent without an approved rationale.

## Roles and decision rights

One person may hold several roles, but accountability must remain explicit.

| Role | Accountable for |
| --- | --- |
| Retirement sponsor | Business rationale, funding, scope, schedule, and proceed/pause/abort decisions |
| Product or service owner | Consumer outcomes, adoption freeze, service milestones, and successor handoff |
| Retirement coordinator | Integrated plan, inventories, dependencies, evidence, exceptions, and closure package |
| Consumer or integration owner | Migration, acknowledgement, reconciliation, and removal of dependency |
| Data or records owner | Retention, legal hold, export, archive, transfer, deletion, and records accessibility |
| Privacy owner | PII obligations, deletion rules, notice, and privacy-risk acceptance |
| Security or identity owner | Access, secrets, keys, certificates, endpoints, evidence protection, and sanitization assurance |
| Infrastructure or operations owner | Traffic cessation, workloads, storage, networks, monitoring, backup, and recovery decommissioning |
| Supplier, finance, or contract owner | Vendor access, licenses, subscriptions, contracts, invoices, and transferred obligations |
| Closure authority | Independent or accountable review of evidence, exceptions, and final residual risk |

Automation may discover resources, block new adoption, notify owners, verify
zero traffic, revoke bounded credentials, and collect evidence when authorized.
It must not destroy information, release legal holds, cancel obligations, or
make irreversible closure decisions without explicit authority and safeguards.

## Entry criteria

Before execution begins, establish:

- the retirement trigger, rationale, sponsor, decision authority, and scope;
- affected products, versions, environments, tenants, regions, interfaces, and
  shared components;
- initial user, consumer, integration, supplier, asset, identity, and data views;
- applicable contracts, laws, regulations, policies, retention schedules,
  privacy duties, and legal holds;
- successor, migration, export, archive, or compensating approach where needed;
- proposed milestones, notice periods, success measures, reversible checkpoints,
  abort conditions, and last responsible rollback point;
- an initial impact, continuity, security, privacy, financial, and residual-risk
  assessment;
- evidence owners and the final closure authority.

An urgent retirement may compress notice or migration time when continued use
creates greater harm. It must still document authority, impact, alternatives,
communications, evidence, and residual obligations.

## Operating workflow

### 1. Authorize and bound retirement

Define exactly what is retiring and what is not: capability, version, service,
deployment, tenant, data set, contract, or complete product. State the reason,
expected outcome, non-goals, milestones, constraints, success and abort
criteria, authority, evidence requirements, and relationship to any successor.

Separate approval to plan from approval to execute irreversible actions. Freeze
unapproved scope expansion and require new evidence when the boundary changes.

Outputs:

- authorized retirement charter and scoped identifiers;
- decision, authority, funding, timeline, and review points;
- impact and risk hypotheses;
- reversible checkpoints and irreversible-action approvals.

### 2. Build and reconcile the retirement inventory

Discover declared and observed consumers, users, integrations, data flows,
domains, endpoints, deployments, jobs, queues, storage, backups, recovery
copies, logs, repositories, artifacts, packages, feature flags, accounts,
roles, secrets, keys, certificates, network rules, suppliers, licenses,
contracts, budgets, dashboards, alerts, runbooks, and support channels.

Use multiple evidence sources because catalogs are often incomplete. Assign an
owner and disposition to every scoped item; reconcile unknown or orphaned items
before irreversible actions.

Outputs:

- versioned retirement inventory and dependency graph;
- declared-versus-observed reconciliation;
- owner and intended disposition for each item;
- gaps, unknowns, shared-resource constraints, and discovery confidence.

### 3. Plan transition, information disposition, and closure

For every inventory item, select retain, migrate, export, archive, transfer,
delete, sanitize, terminate, or explicitly exempt. Define order, prerequisites,
verification, fallback, evidence, owner, due date, and retained obligation.

Plan consumer waves, compatibility windows, data reconciliation, identity
transition, support coverage, communications, continuity, supplier exit,
financial closure, records access, and post-retirement response. Prevent a
successor from becoming an undocumented dumping ground for risk.

Outputs:

- integrated retirement and rollback plan;
- consumer and data transition plan;
- retention, legal-hold, archival, deletion, and sanitization matrix;
- obligation-transfer and closure matrix;
- verification and final acceptance criteria.

### 4. Communicate and stop new adoption

Publish end-of-support and end-of-operation milestones, affected scope,
successor or export paths, required actions, consequences, support channels,
and changes to obligations. Match notice and acknowledgement requirements to
risk, contract, and policy. Track unreachable and non-responsive consumers.

Block new consumers, credentials, contracts, data intake, and dependencies
where appropriate. Constrain feature work to safety, migration, compliance, or
retirement needs, while retaining emergency Support capability.

Outputs:

- notices, audiences, delivery, acknowledgement, and exceptions;
- adoption freeze and enforcement evidence;
- consumer action and escalation status;
- current milestone and support information.

### 5. Migrate consumers, integrations, and required capability

Move consumers in controlled waves. Validate successor readiness, access,
interfaces, data, behavior, capacity, security, privacy, continuity, support,
and rollback before each wave. Reconcile each consumer against both old and new
states and verify removal of the old dependency.

A replacement is not mandatory when the capability is no longer needed, but
the impact must still be accepted. Zero observed traffic is evidence only for
the observation window and visibility available; combine it with ownership,
dependency, and acknowledgement evidence.

Outputs:

- per-consumer disposition and acknowledgement;
- migration, compatibility, and reconciliation results;
- old-dependency removal evidence;
- unresolved consumer risk and escalation.

### 6. Preserve and transfer required records and knowledge

Identify records, source, provenance, decisions, audit evidence, contracts,
user documentation, runbooks, incident and vulnerability history, and other
knowledge that must outlive the system. Preserve authenticity, integrity,
metadata, access controls, searchability, readability, ownership, retention,
and future interpretation.

Test that authorized users can retrieve and understand transferred or archived
records without depending on the retired system, unavailable encryption keys,
obsolete formats, or undocumented expertise.

Outputs:

- retained-record inventory and authority;
- archive or transfer manifest with integrity evidence;
- access, readability, and restoration verification;
- successor custodian, retention, and disposition trigger.

### 7. Execute and verify data disposition

For each data class and copy, apply the authorized retention, hold, return,
transfer, archive, deletion, or sanitization rule. Include primary stores,
replicas, caches, search indexes, analytics, exports, logs, queues, local files,
backups, recovery environments, test data, support attachments, and supplier
copies. Address shared media and immutable retention explicitly.

Verify the claim appropriate to the mechanism and system boundary. Record
method, scope, time, tool or provider, result, validator, exceptions, remaining
copies, and expiry. A provider API success response or missing UI record may be
insufficient for high-assurance deletion.

Outputs:

- per-data-class disposition evidence;
- deletion or sanitization validation appropriate to sensitivity;
- backup, supplier, and derived-data treatment;
- exceptions, remaining exposure, owner, and final trigger.

### 8. Revoke trust and decommission technical resources

Stop traffic, jobs, writes, replication, integrations, and recovery activity in
the approved order. Revoke users, service accounts, roles, tokens, secrets,
keys, certificates, trust relationships, domains, DNS, webhooks, network rules,
and supplier access. Remove workloads, storage, pipelines, artifact publication,
feature flags, monitoring, paging, backups, recovery resources, and environments
only after their evidence and retention needs are satisfied.

Protect names and endpoints from unsafe reuse or takeover. Ensure shared
resources and successor systems are not damaged. Verify both the target's
absence and the absence of unintended residual access or cost.

Outputs:

- traffic and activity cessation evidence;
- identity, credential, key, certificate, and trust revocation records;
- resource and shared-dependency decommissioning evidence;
- domain, endpoint, monitoring, backup, and recovery disposition;
- cost and inventory reconciliation.

### 9. Close service, supplier, financial, and support obligations

Close or transfer contracts, subscriptions, licenses, purchase orders,
invoices, service commitments, warranties, vulnerability channels, support
queues, compliance registrations, continuity plans, insurance dependencies,
asset registers, catalogs, ownership, and reporting. Confirm that retained
records and residual issues still have reachable owners.

Do not remove all contact paths if consumers may still need records, security
reporting, migration help, or legal response. Define the post-retirement contact
and its expiry or successor.

Outputs:

- closed or transferred obligation register;
- supplier-access and financial reconciliation;
- updated catalogs, policies, continuity, and support records;
- post-retirement ownership and contact path.

### 10. Verify closure and learn

Review the complete evidence package against scope and criteria. Search again
for traffic, consumers, resources, identities, data, costs, alerts, contracts,
and references. Resolve contradictions and expired evidence. Obtain independent
review where impact, regulation, irreversibility, or conflict of interest
requires it.

Record `close` only when every item is closed, transferred, or explicitly
accepted as residual risk. Capture lessons about discoverability, data design,
portability, contracts, ownership, supportability, and retirement readiness and
feed them into Concept, Development, Production, Utilization, and Support.

Outputs:

- reconciled closure package and review result;
- final exceptions and residual-risk acceptance;
- closure decision, authority, timestamp, and retained evidence location;
- lessons and lifecycle improvement actions.

## Retirement control flow

```text
retirement trigger
       |
       v
authorize -> discover -> plan -> notify/freeze
                ^                 |
                |                 v
             reconcile <- migrate consumers
                                  |
                                  v
                   preserve records + dispose data
                                  |
                     last reversible checkpoint
                                  |
                                  v
                  revoke trust + decommission
                                  |
                                  v
                 close obligations -> verify
                                         |
                           pause/rework  |  close
```

Reversibility decreases through the flow. Irreversible actions require stronger
authorization and current evidence than planning or notification actions.

## Evidence and traceability contract

Maintain at least these links:

```text
trigger + rationale -> authorized scope + criteria
scope -> inventory item -> owner -> disposition
consumer/dependency -> notice -> migration/acceptance -> old-link removal
data class + authority -> retention/hold -> disposition method -> validation
record -> archive/transfer -> custodian -> access/readability test
identity/secret/key/certificate -> revocation -> verification
resource/contract/license/cost -> termination/transfer -> reconciliation
exception -> compensating control + expiry -> residual-risk owner
all closure evidence -> independent review where required -> close decision
lesson -> earlier lifecycle requirement/control
```

Evidence must be attributable, timestamped, access-controlled, retained for the
required period, and sufficient to identify exact scope and method. Protect
retirement evidence after the systems that produced it disappear. A checklist
tick, ticket closure, empty dashboard, or deletion request without validation
is not independently reviewable proof.

## Decisions and exit criteria

Retirement uses these stage decisions:

- `proceed`: evidence supports the next planned action;
- `pause`: stop before further action while conditions are corrected;
- `rework`: return to discovery, migration, disposition, or verification;
- `abort`: stop retirement and restore the last authorized operating state
  where still possible;
- `close`: accept the completed retirement and retained residual obligations.

Close only when:

- intended use has stopped and no unmanaged consumers or integrations remain;
- every scoped asset, identity, resource, supplier, and obligation is closed,
  transferred, retained, or covered by explicit exception;
- required consumer migration, export, or accepted loss of capability is verified;
- retained records remain authentic, accessible, readable, owned, and scheduled;
- data disposition covers known copies and has evidence appropriate to
  sensitivity, medium, and system boundary;
- access, secrets, keys, certificates, trust, endpoints, and supplier access are
  revoked or transferred;
- runtime, delivery, monitoring, support, backup, recovery, catalog, and cost
  state is reconciled;
- residual risks and unresolved exceptions have authorized owners, controls,
  expiry, and review paths;
- the final closure authority has recorded the evidence-backed decision.

## Skill routing

| Need | Use | Boundary in Retirement |
| --- | --- | --- |
| Decide and plan consumer migration or capability removal | [`deprecation-and-migration`](../../.agents/skills/deprecation-and-migration/SKILL.md) | Covers replacement, notices, migration, and usage removal; it does not close data, identities, infrastructure, contracts, records, or residual risk |
| Decompose an approved multi-owner retirement | [`planning-and-task-breakdown`](../../.agents/skills/planning-and-task-breakdown/SKILL.md) | Requires the retirement charter, inventory, dependencies, irreversible checkpoints, and closure criteria |
| Design or implement migration/export compatibility changes | [`spec-driven-development`](../../.agents/skills/spec-driven-development/SKILL.md), [`api-and-interface-design`](../../.agents/skills/api-and-interface-design/SKILL.md), and Development skills as applicable | These produce successor or transition changes; retirement authority and closure remain separate |
| Review security implications of transition code or retained interfaces | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Product hardening does not perform identity revocation, key sanitization, media sanitization, or privacy deletion governance |
| Preserve retirement decisions, records, runbooks, and lessons | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Documentation supports evidence but does not validate real-world migration, deletion, revocation, or decommissioning |

## Recommended skill sequences

- **Product or service retirement:** authorize and inventory ->
  `planning-and-task-breakdown` -> `deprecation-and-migration` for consumers ->
  preserve records -> data disposition -> trust revocation and decommissioning
  -> obligation reconciliation -> closure review.
- **API or version retirement:** identify consumers ->
  `deprecation-and-migration` -> transition changes through Development and
  Production -> verify zero dependency -> remove interface and credentials ->
  update support/catalog state -> close scoped retirement.
- **Data-bearing retirement:** identify data and authority -> preserve required
  records -> migrate/export and reconcile -> apply deletion or sanitization
  rules -> validate copies and keys -> decommission storage -> close exceptions.
- **Urgent security retirement:** authorize constrained emergency scope ->
  protect users and evidence -> block access/adoption -> migrate or accept
  impact -> revoke trust -> dispose data and resources under explicit authority
  -> complete deferred reconciliation and review.

## Current automation gaps

No additional skill from the reviewed source repository was copied. The
`deprecation-and-migration` skill supports consumer transition but stops far
short of complete retirement. Native harness skills are still needed for:

- retirement chartering, inventory, dependency discovery, and reconciliation;
- consumer notification, acknowledgement, and zero-dependency verification;
- records preservation, archival transfer, accessibility, and disposition;
- data-map-driven retention, legal-hold, deletion, and sanitization evidence;
- identities, secrets, keys, certificates, domains, and trust revocation;
- infrastructure, delivery, monitoring, backup, and recovery decommissioning;
- supplier, license, contract, financial, catalog, and obligation closure;
- closure evidence aggregation, independent review, and residual-risk acceptance.

Each future skill should implement one repeatable workflow and refer to this
document for lifecycle policy rather than duplicating it.

## Tailoring

Tailor discovery depth, notice, migration waves, reversibility, evidence,
independence, retention, deletion assurance, sanitization, and post-retirement
support to data sensitivity, dependency reach, criticality, regulation,
contract, environmental impact, and irreversibility. Document:

- what was reduced, increased, or automated;
- the evidence and risk supporting the choice;
- the authority, scope, compensating controls, and expiry;
- the trigger for reassessment.

An ephemeral non-data-bearing test resource may close with lightweight
evidence. A shared, customer-facing, regulated, safety-relevant, or data-bearing
system requires stronger discovery, notice, reconciliation, validation, and
often independent review. Tailoring cannot turn unknown scope or unverifiable
destruction into acceptable closure.

[12207]: https://www.iso.org/standard/90219.html
[15288]: https://www.iso.org/standard/81702.html
[14764]: https://www.iso.org/standard/80710.html
[20000-1]: https://www.iso.org/standard/70636.html
[15489]: https://www.iso.org/standard/62542.html
[27001]: https://www.iso.org/standard/27001.html
[27040]: https://www.iso.org/standard/80194.html
[27555]: https://www.iso.org/standard/71673.html
[800-88]: https://csrc.nist.gov/pubs/sp/800/88/r2/final
