# Artifact Integrity and Provenance

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md) · [Validation and Evidence](validation-and-evidence.md)

## Purpose

This document defines the portable controls that bind a release artifact to
its controlled inputs, build process, composition, producer, and verification
policy. Projects select their build platform, formats, signing system,
registries, commands, and assurance target.

Integrity answers whether an artifact or record changed. Authenticity answers
which trusted identity made a statement. Provenance describes how an artifact
was produced. Composition describes what it contains. None substitutes for the
others or proves that the software is fit for use.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [NIST SP 800-218, SSDF 1.1][ssdf] | Protect releases, provide integrity verification, archive releases, and retain provenance | Final |
| [NIST SP 800-204D][800-204d] | Integrate supply-chain security measures into CI/CD | Final |
| [ISO/IEC 5962:2021][spdx] | Standardized SPDX 2.2.1 package and component metadata | Published; revision underway |
| [SLSA 1.2][slsa] | Optional build/source provenance and build-platform assurance profiles | Approved industry specification |
| [NTIA Minimum Elements for an SBOM][ntia] | Baseline SBOM data fields and operational practices | Final guidance |

SPDX 3.0 remains a draft ISO revision at the review date. SLSA levels apply
only when their exact track, version, and requirements are named; they are not
generic SDLC assurance levels.

## Artifact evidence set

A tailored release set should identify:

- immutable artifact coordinates and cryptographic digest;
- accepted source revision, dependencies, configuration, and external build inputs;
- build-platform identity, workflow, parameters, time, and output relationship;
- component inventory generated from the produced artifact where feasible;
- provenance and other attestations bound to artifact digests;
- signing or authenticity-verification material and trust policy;
- applicable vulnerability, malware, secret, license, and policy findings;
- publication, archival, retention, access, revocation, and verification instructions;
- known omissions, unverifiable inputs, exceptions, and residual risk.

An SBOM and provenance statement may overlap, but must remain distinguishable.
An SBOM optimized for component risk is not automatically complete build
provenance; provenance is not automatically a complete component inventory.

## Workflow

### 1. Define subject and assurance target

- Identify exact candidate, artifact types, consumers, distribution paths, and threats.
- Select applicable composition, provenance, signing, retention, and policy requirements.
- Define the expected producer/build identities and verification policy before building.
- Select a SLSA or other profile only when the project commits to its exact requirements.

### 2. Control inputs and production

- Bind source, dependencies, tools, base images, configuration, and parameters to immutable identities.
- Protect build definitions as reviewed code and separate trusted control-plane
  functions from tenant-controlled build steps where the selected assurance requires it.
- Prevent one build from influencing another at the tailored assurance level.
- Keep signing and attestation credentials inaccessible to untrusted build steps.

### 3. Identify the produced artifact

- Compute approved cryptographic digests for every distributable object.
- Use immutable coordinates; reject mutable aliases as evidence of identity.
- Treat repackaging, mutation, or environment-specific rebuilding as a new artifact.
- Record the relationship among multi-artifact releases without replacing per-artifact identity.

### 4. Produce composition and provenance

- Generate composition evidence from actual produced content and resolved inputs
  where supported, not only declared dependency manifests.
- Include direct, transitive, vendored, generated, base-image, firmware, and
  other relevant components according to declared scope.
- Generate provenance through the trusted build platform at the required assurance level.
- Bind statements to artifact digests and preserve predicate/schema versions.
- Record missing fields and coverage limitations instead of fabricating completeness.

### 5. Sign, publish, and archive evidence

- Apply the project's approved identity and keyless/key-based trust mechanism.
- Publish artifacts and evidence through authorized immutable channels.
- Keep attestations immutable; corrections produce new statements or releases
  according to the chosen format and repository rules.
- Archive release material and verification instructions for the required lifetime.
- Define rotation, expiry, compromise, revocation, and historical-verification behavior.

### 6. Verify as a consumer

- Resolve the artifact by immutable identity and recompute its digest.
- Authenticate provenance/signatures against the current trust policy.
- Compare actual provenance with expected source, builder, workflow, parameters, and dependencies.
- Validate schemas, subject bindings, composition policy, and required findings.
- Fail closed or report `blocked` when required evidence, trust roots, or verification services are unavailable.

## Decision rules

Use `integrity-verified` only for the exact artifact and policy evaluated. Use
`rebuild` when identity, inputs, production integrity, provenance, or packaging
cannot be trusted. Use `hold` for remediable evidence or authority gaps. Never
repair a published payload in place or reattach evidence from another digest.

Completion requires immutable identity, expected-versus-actual provenance
verification, declared composition coverage, trustworthy evidence bindings,
retention and revocation rules, and explicit disposition of every gap.

[ssdf]: https://csrc.nist.gov/pubs/sp/800/218/final
[800-204d]: https://csrc.nist.gov/pubs/sp/800/204/d/final
[spdx]: https://www.iso.org/standard/81870.html
[slsa]: https://slsa.dev/spec/v1.2/
[ntia]: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
