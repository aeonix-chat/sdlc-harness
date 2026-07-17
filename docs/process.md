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
| [Concept](stages/concept.md) | Clarify the actual need and decision | [`interview-me`](../.agents/skills/interview-me/SKILL.md) | Confirmed intent, outcome, users, constraints, and non-goals |
| [Concept](stages/concept.md) | Explore and compare solution classes | [`idea-refine`](../.agents/skills/idea-refine/SKILL.md) | Concept one-pager, alternatives, assumptions, MVP boundary, and open questions |
| [Concept](stages/concept.md) / [Development](stages/development.md) | Formalize an approved direction | [`spec-driven-development`](../.agents/skills/spec-driven-development/SKILL.md) | Approved specification and success criteria; technical sections mature in Development |
| [Development](stages/development.md) | Decompose an approved change | [`planning-and-task-breakdown`](../.agents/skills/planning-and-task-breakdown/SKILL.md) | Ordered tasks, dependencies, checkpoints, and acceptance criteria |
| [Development](stages/development.md) | Ground technology decisions in current primary sources | [`source-driven-development`](../.agents/skills/source-driven-development/SKILL.md) | Verified source references, applicable constraints, and explicitly unverified assumptions |
| [Development](stages/development.md) | Design APIs, module boundaries, and public contracts | [`api-and-interface-design`](../.agents/skills/api-and-interface-design/SKILL.md) | Versioned contract, compatibility decisions, validation, and error semantics |
| [Development](stages/development.md) | Deliver safe vertical increments | [`incremental-implementation`](../.agents/skills/incremental-implementation/SKILL.md) | Small working increment and verification results |
| [Development](stages/development.md) | Drive behavior changes with tests | [`test-driven-development`](../.agents/skills/test-driven-development/SKILL.md) | Failing test, passing implementation, and regression coverage |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) / [Support](stages/support.md) | Diagnose unexpected behavior after immediate operational safety and recovery are controlled | [`debugging-and-error-recovery`](../.agents/skills/debugging-and-error-recovery/SKILL.md) | Reproduction, root cause, fix, and recurrence guard linked to the operational event when applicable |
| [Development](stages/development.md) / [Production](stages/production.md) | Assess integration readiness | [`code-review-and-quality`](../.agents/skills/code-review-and-quality/SKILL.md) | Findings by severity, verification assessment, and verdict |
| [Development](stages/development.md) | Reduce implementation complexity without changing behavior | [`code-simplification`](../.agents/skills/code-simplification/SKILL.md) | Behavior-preserving simplification and passing regression evidence |
| [Development](stages/development.md) / [Utilization](stages/utilization.md) | Diagnose and improve performance against requirements | [`performance-optimization`](../.agents/skills/performance-optimization/SKILL.md) | Baseline, profile, change, and measured comparison |
| All stages | Identify and reduce software security risk | [`security-and-hardening`](../.agents/skills/security-and-hardening/SKILL.md) | Threats, controls, security checks, and accepted residual risk |
| [Production](stages/production.md) | Build delivery automation and quality gates | [`ci-cd-and-automation`](../.agents/skills/ci-cd-and-automation/SKILL.md) | Reproducible pipeline, protected gates, and rollback path |
| [Production](stages/production.md) | Establish artifact identity, composition, provenance, authenticity, and custody | [`artifact-integrity-and-provenance`](../.agents/skills/artifact-integrity-and-provenance/SKILL.md) | Immutable coordinates and digests, composition scope, verified provenance, authenticity policy, and retained evidence |
| [Production](stages/production.md) | Promote an immutable candidate and control release state | [`release-and-promotion`](../.agents/skills/release-and-promotion/SKILL.md) | Boundary digest checks, promotion and deployment records, authorized release decision, rollback state, and active-baseline reconciliation |
| [Production](stages/production.md) / [Utilization](stages/utilization.md) | Accept an exact release in an exact operating context | [`operational-acceptance`](../.agents/skills/operational-acceptance/SKILL.md) | Target baseline, exercised operability/recovery evidence, operations and support acknowledgement, conditions, and acceptance decision |
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

- **New capability:** specification → planning → incremental implementation →
  TDD → security → review → validation and evidence → CI/CD → artifact integrity
  and provenance → operational acceptance → release and promotion → launch → documentation.
- **Bug fix:** debugging → TDD → incremental implementation → review → launch
  controls proportional to impact.
- **Security-sensitive change:** specification → threat-focused security
  assessment → planning → implementation and TDD → security verification →
  review → controlled launch.
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
- requirements traceability across all lifecycle artifacts;
- architecture evaluation as a standalone workflow;
- service objectives, indicator definitions, telemetry quality, incident
  command, continuity exercises, quality-in-use measurement, and recurring
  operational decisions;
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
under the MIT License. Local changes should be limited to integration fixes or
deliberate SDLC Harness adaptations, and material divergence should be recorded.
See [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).
