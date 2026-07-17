---
name: artifact-integrity-and-provenance
description: Establishes and verifies immutable artifact identity, composition, provenance, authenticity, custody, and retention. Use when producing or consuming release artifacts, selecting an SBOM or provenance profile, signing or attesting builds, verifying supply-chain evidence, investigating artifact mismatch, or preparing a candidate for promotion.
---

# Artifact Integrity and Provenance

Read [`../../../docs/artifact-integrity-and-provenance.md`](../../../docs/artifact-integrity-and-provenance.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md)
before using this workflow. Use project-provided build, SBOM, provenance,
signing, registry, and verification mechanisms.

## Workflow

1. Identify the exact candidate, artifact set, consumers, distribution path,
   threats, requirements, and assurance profile. Name the exact SLSA track and
   version when applicable.
2. Discover authoritative project commands, build platform, trust policy,
   formats, repositories, retention, and revocation procedures. Do not select a
   vendor or format when the project already defines one.
3. Bind source, dependencies, tools, configuration, parameters, builder, and
   outputs to immutable identities. Reject mutable aliases as artifact identity.
4. Build through the controlled project path. Compute approved digests for all
   outputs; treat any payload mutation or repackaging as a new artifact.
5. Generate composition from produced content and resolved inputs where
   supported. Generate provenance through the trusted platform. Record scope,
   omissions, schema versions, and subject digests.
6. Apply the approved authenticity mechanism without exposing signing material
   to untrusted build steps. Publish and archive immutable artifacts, evidence,
   trust material, and verification instructions.
7. Verify as a consumer: resolve immutable identity, recompute digest,
   authenticate statements, compare actual provenance with expectations,
   validate composition/policy, and preserve findings.
8. Report `integrity-verified`, `hold`, or `rebuild` for the exact subject and
   policy. Record limitations, invalidation conditions, and residual risk.

## Guardrails

- Keep SBOM, provenance, signature, attestation, and validation findings distinct.
- Never attach evidence from another artifact digest.
- Never claim provenance completeness when required inputs are unavailable.
- Fail closed or report `blocked` when required trust roots or verification
  services are unavailable.
- Do not repair a published payload or attestation in place.
- Do not claim fitness for use from integrity or provenance evidence alone.

## Completion

Require immutable artifact identity, controlled input/output traceability,
declared composition coverage, expected-versus-actual provenance verification,
authentic evidence binding, retention/revocation behavior, and disposition of gaps.
