# Secret Publication and Rotation

Status: **baseline 0.1**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md) · [Validation and evidence](validation-and-evidence.md)

## Purpose

This document governs publication, update, rotation, verification, and handoff
of secret material to an authorized secret-management system without exposing
plaintext or inventing storage, consumer, or authority contracts.

Projects provide the secret inventory, owner, manager and version, paths or
object identities, consumer mappings, credential source, authentication method,
rotation policy, commands or APIs, and environment authority. The harness does
not prescribe a vendor or authorize a live write.

## Authority and modes

Distinguish:

- **design or command preparation**, which produces reviewed instructions with
  placeholders and no live mutation;
- **read-only preflight**, which inspects identity, policy, metadata, versions,
  and capabilities without reading secret values;
- **execute**, which performs an explicitly authorized write or rotation in an
  exact environment.

Authorization to prepare commands or inspect metadata is not authorization to
publish, rotate, revoke, or synchronize secrets. Rotation is not an ordinary
deployment side effect.

## Controlled inventory and change

Every secret field or document needs a stable logical identity, owner,
environment, purpose, source/custodian, target manager identity, consumer set,
classification, rotation rule, and verification method. Treat the controlled
inventory as authoritative. Do not infer paths, field names, mount points,
namespaces, consumer objects, or merge semantics from examples.

Before mutation, establish current metadata/version, write semantics
(create/replace/merge), concurrency or compare-and-set behavior, expected
consumer transition, rollback/recovery, and the effect of partial completion.
Preserve unrelated fields when the approved change is partial; do not use an
unsafe read-modify-write flow that exposes plaintext.

## Secret-handling boundary

- Never place secret values in chat, command history, process arguments, logs,
  screenshots, plans, issues, commits, PRs, temporary repository files, or
  validation output.
- Prefer protected local input, standard input, file descriptors, manager-native
  import, or another project-approved non-echoing mechanism.
- Do not print complete secret documents for verification. Verify through
  version, digest/HMAC where appropriate, status, key-name inventory, consumer
  readiness, or a bounded behavior check that cannot reveal the value.
- If plaintext reaches an unauthorized surface, treat the credential as
  compromised, preserve only sanitized incident evidence, and route revocation
  and replacement through incident/rotation authority.
- Do not generate credentials unless the user and project contract explicitly
  authorize generation and define ownership, entropy, format, custody, and recovery.

## Workflow

1. Identify exact environment, inventory revision, secret identities, owners,
   consumers, requested operation, and decision authority.
2. Select preparation, preflight, or execute mode and state its mutation boundary.
3. Validate authenticated principal, scoped capabilities, manager/version,
   target metadata, concurrency controls, and required consumer prerequisites
   without reading plaintext.
4. Prepare the smallest safe operation using placeholders or protected local
   inputs; review replacement/merge and partial-failure behavior.
5. Immediately before execute mode, confirm that the exact live mutation is
   authorized. Perform only the approved targets.
6. Verify metadata/version and intended consumer behavior without exposing the
   secret. Record partial, blocked, or uncertain outcomes truthfully.
7. For rotation, transition all intended consumers, verify use of the new
   version, revoke or retire the old credential under policy, and preserve an
   emergency recovery path.
8. Hand non-secret identities, versions, consumer status, evidence, residual
   risk, and follow-up to operations and support.

## Completion criteria

Completion requires controlled inventory and authority, no plaintext exposure,
concurrency-safe target updates, metadata and consumer verification, truthful
partial-state handling, rotation closure where applicable, and a sanitized
auditable record. A successful manager command alone is not proof that every
consumer received or can use the secret.
