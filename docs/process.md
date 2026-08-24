# SDLC Process and Skill Map

This document connects the [reference lifecycle](reference-lifecycle.md) to
repeatable agent workflows. It is the routing layer between lifecycle guidance
and the skills under [`.agents/skills`](../.agents/skills/).

## How to use the map

1. Identify the lifecycle stage affected by the task.
2. Select the workflow that matches the requested outcome.
3. Invoke the linked skill and follow its exit criteria.
4. Record the resulting evidence and feed material findings into downstream or
   earlier lifecycle work.

Skills are composable. A production change will commonly use specification,
planning, implementation, testing, security, review, and release workflows. Do
not interpret the table as a mandatory waterfall sequence.

## Lifecycle coverage

| Stage | Workflow | Skill | Minimum evidence |
| --- | --- | --- | --- |
| All stages | Turn checks, reviews, observations, and measurements into bounded decision support | [`validation-and-evidence`](../.agents/skills/validation-and-evidence/SKILL.md) | Claim, subject, boundary, procedure, retained evidence, finding, limitations, and residual risk |
| All stages | Classify incoming work and select the smallest safe lifecycle route | [`work-intake-and-routing`](../.agents/skills/work-intake-and-routing/SKILL.md) | Need, affected baseline, uncertainty/risk assessment, selected route, rationale, required artifacts, authority, and next action |
| All stages | Execute an authorized multi-step boundary without artificial pauses | [Execution continuity](execution-continuity.md), then the applicable implementation and validation skills | Completed authorized outcome and verification, or an evidence-backed stop report identifying the blocker, new authority, user intervention, or scope change required |
| [Concept](stages/concept.md) | Clarify the actual need and decision | [`interview-me`](../.agents/skills/interview-me/SKILL.md) | Confirmed intent, outcome, users, constraints, and non-goals |
| [Concept](stages/concept.md) | Explore and compare solution classes | [`idea-refine`](../.agents/skills/idea-refine/SKILL.md) | Concept one-pager, alternatives, assumptions, MVP boundary, and open questions |
| [Concept](stages/concept.md) / [Development](stages/development.md) | Formalize an approved direction | [`spec-driven-development`](../.agents/skills/spec-driven-development/SKILL.md) | Approved specification and success criteria; technical sections mature in Development |
| [Concept](stages/concept.md) / [Development](stages/development.md) / [Support](stages/support.md) | Define requirements and maintain lifecycle traceability | [`requirements-and-traceability`](../.agents/skills/requirements-and-traceability/SKILL.md) | Controlled requirements and acceptance baseline, allocations, bidirectional links, change impact, coverage, deviations, and risks |
| [Development](stages/development.md) | Evaluate architecture against concerns, scenarios, alternatives, and risk | [`architecture-evaluation`](../.agents/skills/architecture-evaluation/SKILL.md) | Scoped architecture description, scenarios, evaluation evidence, trade-offs, findings, actions, and sufficiency verdict |
| [Development](stages/development.md) | Decompose an approved change | [`planning-and-task-breakdown`](../.agents/skills/planning-and-task-breakdown/SKILL.md) | Ordered tasks, dependencies, checkpoints, and acceptance criteria |
| [Development](stages/development.md) | Ground technology decisions in current primary sources | [`source-driven-development`](../.agents/skills/source-driven-development/SKILL.md) | Verified source references, applicable constraints, and explicitly unverified assumptions |
| [Development](stages/development.md) | Design APIs, module boundaries, and public contracts | [`api-and-interface-design`](../.agents/skills/api-and-interface-design/SKILL.md) | Versioned contract, compatibility decisions, validation, and error semantics |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) / [Support](stages/support.md) | Design bounded outbound integration behavior | [`integration-client-resilience`](../.agents/skills/integration-client-resilience/SKILL.md) | Operation graph, deadline hierarchy, retry and side-effect policy, resource ownership, synchronized configuration, and deterministic evidence |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) | Design privacy-safe diagnostic signals for runtime behavior | [`observability-by-design`](../.agents/skills/observability-by-design/SKILL.md) | Impact disposition, phase ownership, bounded signal contract, privacy and failure-isolation decisions, verification, and environment handoff |
| [Development](stages/development.md) | Deliver safe vertical increments | [`incremental-implementation`](../.agents/skills/incremental-implementation/SKILL.md) | Small working increment and verification results |
| [Development](stages/development.md) | Drive behavior changes with tests | [`test-driven-development`](../.agents/skills/test-driven-development/SKILL.md) | Failing test, passing implementation, and regression coverage |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) / [Support](stages/support.md) | Diagnose unexpected behavior after immediate operational safety and recovery are controlled | [`debugging-and-error-recovery`](../.agents/skills/debugging-and-error-recovery/SKILL.md) | Reproduction, root cause, fix, and recurrence guard linked to the operational event when applicable |
| [Development](stages/development.md) / [Production](stages/production.md) | Assess integration readiness | [`code-review-and-quality`](../.agents/skills/code-review-and-quality/SKILL.md) | Findings by severity, verification assessment, and verdict |
| [Development](stages/development.md) | Assemble the exact candidate package and decide Development readiness | [`development-candidate-readiness`](../.agents/skills/development-candidate-readiness/SKILL.md) | Candidate identity, reconciled scope/traceability, architecture and review disposition, candidate-bound V&V, risks, transition prerequisites, and decision |
| [Development](stages/development.md) | Reduce implementation complexity without changing behavior | [`code-simplification`](../.agents/skills/code-simplification/SKILL.md) | Behavior-preserving simplification and passing regression evidence |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) | Diagnose and improve performance against requirements | [`performance-optimization`](../.agents/skills/performance-optimization/SKILL.md) | Baseline, profile, change, and measured comparison |
| All stages | Identify and reduce software security risk | [`security-and-hardening`](../.agents/skills/security-and-hardening/SKILL.md) | Threats, controls, security checks, and accepted residual risk |
| [Production](stages/production.md) | Build delivery automation and quality gates | [`ci-cd-and-automation`](../.agents/skills/ci-cd-and-automation/SKILL.md) | Reproducible pipeline, protected gates, and rollback path |
| [Production](stages/production.md) | Establish artifact identity, composition, provenance, authenticity, and custody | [`artifact-integrity-and-provenance`](../.agents/skills/artifact-integrity-and-provenance/SKILL.md) | Immutable coordinates and digests, composition scope, verified provenance, authenticity policy, and retained evidence |
| [Production](stages/production.md) | Promote an immutable candidate and control release state | [`release-and-promotion`](../.agents/skills/release-and-promotion/SKILL.md) | Boundary digest checks, promotion and deployment records, authorized release decision, rollback state, and active-baseline reconciliation |
| [Production](stages/production.md) | Produce evidence-backed audience-facing release communication | [`release-notes`](../.agents/skills/release-notes/SKILL.md) | Complete change disposition, bounded audience claims, compatibility and limitations, approval, and exact release handoff |
| [Production](stages/production.md) / [Utilization](stages/utilization.md) / [Support](stages/support.md) | Publish or rotate controlled secret material | [`secret-publication-and-rotation`](../.agents/skills/secret-publication-and-rotation/SKILL.md) | Exact inventory and authority, safe custody, concurrency-safe update, metadata and consumer evidence, rotation closure, and plaintext-free record |
| [Production](stages/production.md) / [Utilization](stages/utilization.md) | Accept an exact release in an exact operating context | [`operational-acceptance`](../.agents/skills/operational-acceptance/SKILL.md) | Target baseline, exercised operability/recovery evidence, operations and support acknowledgement, conditions, and acceptance decision |
| [Utilization](stages/utilization.md) | Define service objectives and validate operational telemetry | [`service-objectives-and-telemetry`](../.agents/skills/service-objectives-and-telemetry/SKILL.md) | Decision-linked objectives, reproducible indicators, telemetry coverage, data-quality findings, thresholds, owners, and blind spots |
| [Utilization](stages/utilization.md) | Coordinate incident control, recovery, communication, and follow-up | [`incident-response-and-recovery`](../.agents/skills/incident-response-and-recovery/SKILL.md) | Active-baseline incident record, impact and chronology, decisions/actions, preserved evidence, verified recovery, communications, and owned follow-up |
| [Utilization](stages/utilization.md) | Validate restoration, failover, and continuity capability | [`continuity-and-restore-validation`](../.agents/skills/continuity-and-restore-validation/SKILL.md) | Scope-bound exercise, measured recovery/data-loss results, restored behavior/data evidence, gaps, acceptance, and retest |
| [Utilization](stages/utilization.md) | Review current operating evidence and make the recurring use decision | [`operational-review-and-control`](../.agents/skills/operational-review-and-control/SKILL.md) | Reconciled active baseline, current evidence, disposed risks/exceptions, authorized decision, conditions, actions, and next review |
| [Production](stages/production.md) / [Utilization](stages/utilization.md) / [Support](stages/support.md) | Inspect exact active environment state without mutation | [`environment-state-inspection`](../.agents/skills/environment-state-inspection/SKILL.md) | Target and time boundary, active identities, separated desired/reported/observed findings, drift, sanitized evidence, access gaps, and no mutation |
| [Production](stages/production.md) | Review candidate and release-change evidence | [`code-review-and-quality`](../.agents/skills/code-review-and-quality/SKILL.md) | Review verdict and disposition of blocking findings |
| [Production](stages/production.md) | Diagnose pipeline or deployment failures | [`debugging-and-error-recovery`](../.agents/skills/debugging-and-error-recovery/SKILL.md) | Reproduction, root cause, new controlled candidate or pipeline fix, and recurrence guard |
| [Production](stages/production.md) / [Utilization](stages/utilization.md) | Prepare deployment, authorize rollout, and observe release | [`shipping-and-launch`](../.agents/skills/shipping-and-launch/SKILL.md) | Readiness checks, rollout and rollback plan, thresholds, release decision, and post-release evidence |
| [Support](stages/support.md) | Specify a material maintenance change after diagnosis and disposition | [`spec-driven-development`](../.agents/skills/spec-driven-development/SKILL.md) | Affected baselines, treatment scope, compatibility and risk constraints, and acceptance criteria |
| [Support](stages/support.md) | Drive corrective behavior changes with regression evidence | [`test-driven-development`](../.agents/skills/test-driven-development/SKILL.md) | Failure-demonstrating check, passing treatment, and affected regression coverage |
| [Support](stages/support.md) / [Production](stages/production.md) | Produce and transition a controlled maintenance release | [`ci-cd-and-automation`](../.agents/skills/ci-cd-and-automation/SKILL.md) and [`shipping-and-launch`](../.agents/skills/shipping-and-launch/SKILL.md) | Traceable artifact, release decision, deployment evidence, and post-release effectiveness signal |
| [Utilization](stages/utilization.md) / [Support](stages/support.md) / [Retirement](stages/retirement.md) | Migrate consumers and remove obsolete capabilities after an accountable change or retirement decision | [`deprecation-and-migration`](../.agents/skills/deprecation-and-migration/SKILL.md) | Migration state, consumer communication, removal checks, and closure decision |
| [Retirement](stages/retirement.md) | Decompose an authorized multi-owner retirement around dependencies and irreversible checkpoints | [`planning-and-task-breakdown`](../.agents/skills/planning-and-task-breakdown/SKILL.md) | Ordered retirement plan, owners, dependencies, reversible checkpoints, verification, and closure criteria |
| All stages | Preserve decisions and operating knowledge | [`documentation-and-adrs`](../.agents/skills/documentation-and-adrs/SKILL.md) | Current documentation and decision records linked to the change |

## Cross-cutting composition

Use these combinations as defaults, tailoring them to risk:

- **New capability:** intake/routing → requirements and specification →
  architecture evaluation as needed → planning → incremental implementation →
  TDD → integration resilience and observability when triggered → security →
  review → validation and evidence → Development candidate
  readiness → CI/CD → artifact integrity
  and provenance → operational acceptance → release and promotion → launch → documentation.
- **Bug fix:** intake/routing → debugging → requirements impact → TDD →
  incremental implementation → review → validation and candidate readiness →
  launch controls proportional to impact.
- **Security-sensitive change:** specification → threat-focused security
  assessment → planning → implementation and TDD → security verification →
  review → controlled launch.
- **Release communication:** exact candidate and release boundary → complete
  change inventory → audience claim ledger → evidence and compatibility review
  → approved notes → controlled release workflow.
- **Secret change:** controlled inventory and authority → metadata-only preflight
  → protected-input update or rotation → manager and consumer verification →
  sanitized handoff and rotation closure.
- **Migration or removal:** specification → dependency and consumer discovery →
  migration planning → incremental implementation → verification → staged
  launch → deprecation closure.
- **Operational incident:** establish incident control and protect users →
  recover → root-cause debugging → Support/Development change → controlled
  Production release → verify recurrence guard in Utilization.
- **Product vulnerability:** restricted intake and triage → safe validation and
  affected-scope analysis → remediation through Development → coordinated
  Production release → disclosure → effectiveness verification.
- **Product retirement:** authorize and inventory → plan → notify and freeze →
  migrate consumers → preserve records and dispose data → revoke trust and
  decommission → close obligations → independently review where required.

## Known coverage gaps

The imported source set does not provide complete workflows for:

- business or mission analysis before a software specification;
- project-specific requirements/traceability stores and automated coverage reports;
- project-specific telemetry backends, environment inspection commands,
  incident, continuity, quality-in-use, and recurring operational-decision implementations;
- support intake and disposition, supported-baseline management, coordinated
  vulnerability disclosure, dependency lifecycle monitoring, maintenance
  effectiveness verification, and supportability decisions;
- project-specific protected-build, SBOM/provenance, signing, artifact-custody,
  and release-attestation implementations;
- retirement inventory and reconciliation, records preservation, data
  disposition, trust revocation, infrastructure decommissioning, obligation
  closure, and independently reviewable closure evidence;
- project-specific lifecycle evidence schemas and machine-readable decision records;
- risk-based tailoring of controls.

These gaps are candidates for native SDLC Harness skills. They should be added
only after their inputs, outputs, decision rights, and evidence contracts are
defined in the documentation.

## Source and adaptation policy

The initial skill set was imported from Addy Osmani's `agent-skills` project
under the MIT License. Later native workflows may be generalized from evidence
and operating experience in adopting repositories, but must remove repository,
vendor, command, environment, and authority assumptions. Material divergence
and imported third-party material should remain attributable. See
[`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

The `observability-by-design`, `integration-client-resilience`, `release-notes`,
`environment-state-inspection`, and `secret-publication-and-rotation`
workflows were generalized in August 2026 from reusable engineering and
operating experience in the adopting `amnezia-gpt/amgpt-router` repository.
Their harness contracts deliberately omit that project's services, commands,
deployment topology, vendors, storage paths, and authority assumptions.
