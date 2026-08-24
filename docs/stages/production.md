# Production Stage

Status: **baseline 0.2**
Sources reviewed: **2026-07-17**

Navigation: Previous: [Development](development.md) ·
[Lifecycle](../reference-lifecycle.md) · [Process map](../process.md) · Next:
[Utilization](utilization.md)

## Purpose and boundary

The Production stage turns an approved Development candidate into an
identifiable, protected, reproducible, distributable, and authorized software
release. For software, production means controlled build, package, signing,
publication, deployment, and transition; it does not imply physical mass
production.

Production begins with an exact candidate and its Development evidence package.
It ends with `release`, `hold`, `rebuild`, `rollback`, or `stop`. A `release`
decision transfers a known release baseline and operating context to
Utilization and Support.

Production does not redo Development verification and validation. It verifies
that the candidate was produced without unauthorized change, that its identity,
contents, provenance, and delivery path are controlled, and that the target
environment can accept it safely.

## Deployment is not release

These events may coincide, but the harness must distinguish them:

| Event | Meaning |
| --- | --- |
| **Build** | Transform controlled inputs into candidate artifacts |
| **Publish** | Place immutable artifacts in an authorized repository or distribution channel |
| **Deploy** | Install or activate artifacts in a target environment |
| **Release** | Make capability available to intended consumers under an authorized decision |
| **Rollout** | Change the population or traffic exposed to a released capability |

A feature may be deployed with a flag disabled and not yet released. A packaged
library may be published and released without being deployed by its producer.
Every evidence record must name the event it supports.

## Standards model

| Source | Role in Production | Status at review |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2026][12207] | Primary software lifecycle framework, including supply, configuration, transition, information, quality, and supporting processes | Published |
| [ISO/IEC/IEEE 15288:2023][15288] | Aligned production and transition concerns for software-intensive systems | Published |
| [ISO/IEC/IEEE 24748-1:2024][24748] | Production-stage decision points, enabling systems, and lifecycle tailoring | Published |
| [ISO/IEC/IEEE 15289:2019][15289] | Content and management of lifecycle information items | Published; revision in development |
| [NIST SP 800-218, SSDF 1.1][ssdf] | Protect releases, enable integrity verification, archive releases, and retain component provenance | Final; 1.2 remains draft |
| [ISO/IEC 27036-3:2023][27036] | Security of multi-tier hardware, software, and service supply chains | Published |
| [NIST SP 800-161 Rev. 1 Update 1][800-161] | Cybersecurity supply-chain risk identification, assessment, and mitigation | Final, updated 2024 |
| [ISO/IEC 5962:2021][5962] | Standard SPDX format for software package and component metadata | Published; SPDX 3.0 revision in development |
| [NTIA Minimum Elements for an SBOM][ntia-sbom] | Minimum SBOM data fields, automation support, and practices/processes | Final US government guidance, 2021 |
| [SLSA Build Track 1.2][slsa] | Graduated controls for build provenance, hosted builds, and hardened build platforms | Approved industry specification; informative, not an ISO standard |
| [CISA Secure Software Development Attestation][cisa] | Self-attestation for software supplied in its applicable US federal scope | Current scope-specific program guidance |

ISO/IEC 5962:2021 remains the published ISO SPDX edition at the review date;
SPDX 3.0 is under development and must not be represented as the current ISO
edition. SBOM, provenance, attestation, and signing requirements must be
selected from actual product, customer, regulatory, and risk context rather
than declared universally mandatory.

## How the standards fit together

ISO/IEC/IEEE 12207 and 15288 establish the lifecycle and transition framework;
24748-1 explains stage decisions and tailoring; 15289 governs lifecycle
information. They do not prescribe one CI/CD implementation.

NIST SSDF provides the software-release security overlay. Its relevant
practices require mechanisms for consumers to verify release integrity,
protection and archival of each release, and collection, safeguarding,
maintenance, and sharing of component provenance such as an SBOM.

ISO/IEC 27036-3 and NIST SP 800-161 address supplier and multi-tier supply-chain
risk beyond the producer's own code. ISO/IEC 5962 provides a standardized SPDX
representation for component metadata, while NTIA describes baseline SBOM
content and operating practices. SLSA may be selected as an implementation
profile for build provenance and build-platform integrity. CISA attestation is
only applicable where the relevant acquisition or regulatory scope requires it.

## Roles and decision rights

| Role | Accountability |
| --- | --- |
| Candidate owner | Supplies the exact approved Development baseline and its evidence |
| Build / release engineer | Owns controlled build, packaging, artifact identity, publication, and automation |
| Configuration manager | Maintains source, dependency, environment, artifact, and release baselines |
| Security / supply-chain owner | Owns build integrity, signing, provenance, component and supplier risk, and attestation scope |
| Deployment / platform owner | Owns target-environment readiness, deployment, migration, rollback, and recovery execution |
| Operations and support owners | Accept observability, runbooks, known limitations, vulnerability intake, and support obligations |
| Release authority | Issues `release`, `hold`, `rebuild`, `rollback`, or `stop` and accepts residual risk within authority |

Production credentials, signing keys, and release authorization should not be
controlled solely by the code-producing agent where separation reduces risk.

## Entry criteria

- a uniquely identified Development candidate and `candidate` decision;
- controlled source, dependency, configuration, build, verification, and
  validation baselines;
- accepted Development deviations and residual risks;
- defined target consumers and environments;
- release, migration, deployment, rollback, recovery, and communication intent;
- applicable integrity, provenance, component inventory, signing, retention,
  attestation, and approval requirements;
- named Production, operations, support, security, and release owners.

Reject the handoff when the candidate cannot be identified independently of a
mutable branch, tag, environment, or latest artifact reference.

## Operating workflow

### 1. Accept and freeze the candidate

- Confirm the Development decision, scope, exceptions, and required evidence.
- Bind the candidate to immutable source and configuration identifiers.
- Define permitted changes after acceptance; any material change creates a new
  candidate and requires affected evidence to be regenerated.
- Establish the release identifier and target distribution/deployment scope.

Output: **accepted candidate record** and Production work authorization.

### 2. Prepare and protect the production system

- Use an approved build platform, isolated jobs, controlled identities,
  least-privilege access, ephemeral credentials where feasible, and protected secrets.
- Pin and verify build tools, base images, dependencies, and external inputs.
- Control build definitions as reviewed code and record builder identity and version.
- Protect signing services, repositories, registries, deployment identities,
  and audit records; define key rotation and revocation.
- Select a provenance assurance target proportionate to risk, such as an
  applicable SLSA Build level.

Output: **production-system baseline** and control evidence.

### 3. Produce immutable artifacts

- Build only from the accepted inputs in the controlled production system.
- Avoid rebuilding separately for each environment; promote the same immutable
  artifact and supply environment-specific configuration separately.
- Assign cryptographic digests and immutable artifact coordinates.
- Record build inputs, commands or workflow identity, builder, timestamps, and outputs.
- Compare reproducibility when required; otherwise demonstrate controlled and
  traceable production appropriate to the product.

Output: **immutable release artifacts**, digests, and build record.

### 4. Generate composition and provenance evidence

- Generate a component inventory from the produced artifact and its actual
  inputs, not only from a declared dependency file.
- Include direct, transitive, vendored, generated, container/base-image, and
  other relevant components at the chosen scope.
- Record component versions, suppliers/origins, relationships, licenses, and
  known limitations according to applicable policy.
- Produce machine-readable provenance binding output digests to builder and inputs.
- Protect evidence integrity and define access, sharing, update, and retention rules.

Output: **SBOM/component inventory**, provenance statement, and evidence policy.

### 5. Verify release integrity and policy

- Verify artifact digests, provenance, signatures, and the identity authorized
  to create them.
- Scan the actual release artifacts and components for applicable
  vulnerabilities, malware, secrets, licensing, and policy violations.
- Reconcile findings with Development evidence; do not silently waive newly
  discovered issues.
- Confirm that consumers have a mechanism to verify authenticity and integrity.
- Generate required attestations only from traceable evidence and authorized scope.

Output: **release-integrity and policy-verification record**, findings, and attestations.

### 6. Package, sign, publish, and archive

- Package artifacts without changing the verified payload unexpectedly.
- Sign artifacts, manifests, or provenance according to the selected trust model.
- Publish through controlled, authenticated, and auditable channels using
  immutable versions; prohibit ambiguous production use of mutable `latest` references.
- Archive the release artifacts and supporting integrity/provenance data under
  retention and access policy.
- Test retrieval and consumer verification paths where consequence warrants it.

Output: **published release set**, signatures, distribution record, and archive evidence.

### 7. Verify transition readiness

- Confirm environment configuration, capacity, access, secrets, certificates,
  compatibility, data migration, backup, observability, and support readiness.
- Exercise deployment, migration, health checks, rollback, restore, and recovery
  against the produced artifact in representative conditions.
- Define rollout cohorts, feature-flag states, success thresholds, hold points,
  and automatic/manual rollback triggers.
- Confirm release notes, user/support communication, runbooks, ownership, and escalation.

Output: **transition-readiness record** and executable rollout/rollback plan.

### 8. Deploy and verify the environment

- Deploy only the authorized immutable artifact through controlled automation.
- Record artifact, environment, configuration, actor/service identity, time, and result.
- Run post-deployment integrity, configuration, migration, health, smoke, and
  observability checks before exposure grows.
- Stop or rollback on breached thresholds, uncertain identity, migration
  inconsistency, security failure, or loss of observability.
- Keep deployment state distinct from user release state.

Output: **deployment record**, active baseline, and environment-verification evidence.

### 9. Authorize release and rollout

- Assemble evidence without regenerating or summarizing away important exceptions.
- Confirm release scope, feature state, target consumers, thresholds, and monitoring window.
- Record `release`, `hold`, `rebuild`, `rollback`, or `stop` with authority,
  timestamp, evidence references, conditions, and accepted residual risk.
- Increase exposure only through explicit rollout decisions and retain a fast
  path to previous safe state.

Output: **release decision** and rollout state.

### 10. Transfer and close Production work

- Transfer release identity, active configuration, provenance/SBOM, known risks,
  runbooks, thresholds, support obligations, and recovery information to
  Utilization and Support.
- Confirm vulnerability-response teams can identify affected releases from
  component and provenance records.
- Reconcile temporary permissions, credentials, environments, and flags created
  for Production work.
- Record Production anomalies and improvement actions.

Output: **Utilization/Support handoff** and Production closure record.

## Release control loop

The Production workflow may execute many times per day. Each execution still
preserves the same control relationships:

```text
accepted candidate
  → protected build
  → immutable artifact + digest
  → SBOM + provenance
  → integrity / security / policy verification
  → sign + publish + archive
  → transition verification
  → deploy
  → release / rollout decision
  → observe or rollback
```

Small batches reduce the evidence scope; they do not remove artifact identity,
integrity verification, or decision accountability.

## Evidence and traceability contract

The harness should preserve this minimum graph:

```text
Development decision + candidate baseline
  → controlled source / config / dependency inputs
  → builder + build workflow + production controls
  → artifact digest + immutable coordinates
  → SBOM / component inventory + provenance
  → verification findings + signatures + attestations
  → published and archived release set
  → deployment + environment configuration
  → release / rollout / rollback decision
  → active release observed by Utilization and Support
```

Minimum evidence:

- accepted candidate, Development evidence references, and immutable source identity;
- production-system, builder, workflow, tool, and input baselines;
- release manifest, artifact coordinates, and cryptographic digests;
- component inventory/SBOM and provenance at the selected assurance scope;
- vulnerability, malware, secret, license, integrity, and policy results;
- signatures, verification material, attestations, and key/certificate identity;
- publication, distribution, access, and archival records;
- migration, deployment, rollback, restore, recovery, and smoke-test results;
- target environment, active configuration, flag state, and observability evidence;
- release/rollout decisions, exceptions, residual risks, and handoff acknowledgement.

Evidence may live in CI/CD, artifact stores, registries, transparency systems,
configuration systems, issue tracking, and documents. The harness must bind it
to immutable release identities and preserve verification instructions.

## Decision and exit criteria

Issue `release` only when:

- the exact Development candidate and produced artifacts are unambiguous;
- the production system and its authorized identities satisfy the tailored controls;
- build inputs and outputs are traceable and protected from unauthorized substitution;
- artifact integrity and authenticity can be independently checked;
- contents, component relationships, provenance, and applicable supplier risks are known;
- release-artifact security, license, and policy findings have disposition;
- required signing, attestation, publication, and archival actions are complete;
- deployment, migration, rollback, restore, and recovery paths have adequate evidence;
- target configuration, observability, support, and vulnerability-response readiness are accepted;
- rollout thresholds and stop/rollback triggers are explicit;
- residual risks and exceptions have owners, expiry, and authorized acceptance;
- Utilization and Support can identify and sustain the active release.

Use `hold` for a time-bounded approval, dependency, environment, or evidence
gap. Use `rebuild` whenever inputs, build integrity, provenance, packaging, or
artifact identity are invalid. Use `rollback` when a deployed/released state
breaches safety thresholds or cannot be trusted. Use `stop` when authority,
feasibility, or acceptable risk is absent. Return to Development when the
candidate itself must change.

## Skill routing

| Production activity | Skill | How to use it | Limitation |
| --- | --- | --- | --- |
| Define release claims, select sufficient checks, and aggregate decision evidence | [`validation-and-evidence`](../../.agents/skills/validation-and-evidence/SKILL.md) | Bind project-provided checks and retained outputs to the exact candidate, bounded claims, findings, limitations, and release decision | It does not supply project commands, produce artifacts, or authorize release |
| Establish and verify artifact identity, composition, provenance, authenticity, and custody | [`artifact-integrity-and-provenance`](../../.agents/skills/artifact-integrity-and-provenance/SKILL.md) | Apply the project implementation to controlled inputs and verify the resulting artifact evidence as a consumer | It does not choose the project's build, SBOM, provenance, signing, registry, or trust implementation |
| Promote the immutable candidate, deploy it, authorize release, and reconcile active state | [`release-and-promotion`](../../.agents/skills/release-and-promotion/SKILL.md) | Preserve artifact identity across boundaries and separate promotion, deployment, release, rollout, and rollback decisions | It does not define project environments, approval tooling, deployment topology, or decision authority |
| Accept the exact release in the exact target context | [`operational-acceptance`](../../.agents/skills/operational-acceptance/SKILL.md) | Verify target readiness, observability, recovery, support, and accountable acceptance before release | It does not supply local service objectives, telemetry, runbooks, environments, exercises, or thresholds |
| Design or modify CI/CD and automated gates | [`ci-cd-and-automation`](../../.agents/skills/ci-cd-and-automation/SKILL.md) | Build protected, repeatable feedback and deployment paths with explicit gates | Its examples are GitHub/Node-centric and do not provide provenance, signing, SBOM, or hardened-builder workflow |
| Prepare deployment, rollout, monitoring, and rollback | [`shipping-and-launch`](../../.agents/skills/shipping-and-launch/SKILL.md) | Define readiness checks, staged exposure, thresholds, observability, and rollback | Example thresholds are illustrative; it conflates some deploy/release concerns and does not establish artifact custody |
| Review the candidate and release change | [`code-review-and-quality`](../../.agents/skills/code-review-and-quality/SKILL.md) | Confirm change intent, verification quality, security, architecture, and performance before candidate acceptance | Code review does not authorize production, verify build provenance, or replace release evidence review |
| Check code-level security and dependencies | [`security-and-hardening`](../../.agents/skills/security-and-hardening/SKILL.md) | Use applicable secret, dependency, configuration, and boundary checks | It does not secure build infrastructure, signing identities, artifact stores, provenance, or supplier tiers |
| Record release decisions and consumer information | [`documentation-and-adrs`](../../.agents/skills/documentation-and-adrs/SKILL.md) | Update release notes, operating information, and consequential decisions | ADRs and prose do not replace machine-verifiable release identity and provenance |
| Draft and approve audience-facing release notes | [`release-notes`](../../.agents/skills/release-notes/SKILL.md) | Translate the complete release boundary into bounded product claims, compatibility actions, and limitations | It does not build, tag, promote, publish, deploy, or authorize the release |
| Publish or rotate release-related secrets | [`secret-publication-and-rotation`](../../.agents/skills/secret-publication-and-rotation/SKILL.md) | Preserve controlled inventory, plaintext custody, concurrency, consumer verification, and rotation closure | Deployment does not imply secret-write or rotation authority |
| Inspect target active state without mutation | [`environment-state-inspection`](../../.agents/skills/environment-state-inspection/SKILL.md) | Resolve active artifact/configuration identities and separate desired, reported, and observed state | Read-only inspection does not deploy, repair, accept, or authorize release |
| Diagnose pipeline or deployment failures | [`debugging-and-error-recovery`](../../.agents/skills/debugging-and-error-recovery/SKILL.md) | Reproduce, localize, fix root cause, guard recurrence, and re-run affected controls | Do not patch mutable production artifacts; create a new candidate/release when payload changes |

## Recommended skill sequence

For a standard service release:

```text
code-review-and-quality (candidate evidence review)
  → ci-cd-and-automation
  → artifact-integrity-and-provenance
  → security-and-hardening (applicable checks)
  → validation-and-evidence (candidate-bound findings and limitations)
  → operational-acceptance
  → release-and-promotion
  → shipping-and-launch (rollout observation)
  → Utilization observation or rollback
  → release-notes and documentation-and-adrs (consumer information and durable decisions)
```

Invoke `debugging-and-error-recovery` on failures, but do not repair an artifact
in place. Any payload change must flow back through candidate identification,
build, evidence generation, and authorization.

## Project integration requirements

The Production workflows are toolchain-independent. Each adopting project must
provide and maintain concrete implementations for:

- protected/hardened build profiles and enforcement;
- provenance, SBOM, signing, attestation, and policy formats and commands;
- key/certificate or keyless trust rotation, revocation, and historical verification;
- artifact repositories, promotion paths, archival, retention, and quarantine;
- target environments, deployment, migration, reconciliation, and rollback automation;
- service objectives, telemetry, readiness checks, recovery exercises, and support routing;
- supplier/component risk disposition and VEX or equivalent status where applicable;
- selecting a project-specific machine-readable schema and evidence store for
  Production decisions.

Projects should expose these through documented, deterministic commands or
APIs. Cryptographic operations, schema generation, and artifact mutation must
not be improvised by an agent.

## Tailoring

Tailoring depends on consequence of compromise or failure, distribution reach,
consumer verification needs, supplier depth, regulation, deployment model,
reversibility, and data migration risk. It may select different provenance,
signing, SBOM, attestation, approval, rollout, and retention controls. It may
not silently remove immutable artifact identity, controlled production,
integrity verification, deployment traceability, rollback planning, or release
authorization.

[12207]: https://www.iso.org/standard/90219.html
[15288]: https://www.iso.org/standard/81702.html
[24748]: https://www.iso.org/standard/84709.html
[15289]: https://www.iso.org/standard/74909.html
[ssdf]: https://csrc.nist.gov/pubs/sp/800/218/final
[27036]: https://www.iso.org/standard/82890.html
[800-161]: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
[5962]: https://www.iso.org/standard/81870.html
[ntia-sbom]: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
[slsa]: https://slsa.dev/spec/v1.2/build-track-basics
[cisa]: https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form
