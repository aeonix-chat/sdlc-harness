---
name: secret-publication-and-rotation
description: Prepares, preflights, executes, verifies, or hands off controlled secret publication and rotation without exposing plaintext. Use for secret-manager writes, credential updates, consumer transitions, rotation, revocation, or recovery when exact inventory, authority, concurrency, and custody boundaries matter.
---

# Secret Publication and Rotation

Read [`../../../docs/secret-publication-and-rotation.md`](../../../docs/secret-publication-and-rotation.md)
and [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use the project's controlled inventory, secret manager, input mechanism,
consumer mapping, commands, and authority.

## Workflow

1. Identify environment, inventory revision, secret identities, owners,
   consumers, operation, and authority.
2. Select command-preparation, read-only preflight, or execute mode; do not
   infer write authority from the first two modes.
3. Inspect principal, scoped capabilities, target metadata/version, write
   semantics, concurrency controls, and consumer prerequisites without plaintext.
4. Prepare the smallest operation with protected local input and explicit
   create/replace/merge, partial-failure, rollback, and recovery semantics.
5. Immediately before a live write, confirm exact mutation authorization and
   change only approved targets.
6. Verify manager metadata/version and bounded consumer behavior without
   printing the value or complete document.
7. For rotation, transition and verify all intended consumers before retiring
   the old credential, then record sanitized evidence and residual risk.

## Guardrails

- Never expose secrets through chat, arguments, history, logs, screenshots,
  plans, source control, or validation evidence.
- Do not invent paths, fields, consumers, merge semantics, or credential formats.
- Do not read plaintext merely to verify a write.
- Treat unauthorized exposure as compromise and route revocation through
  incident authority.
- Deployment does not implicitly authorize credential rotation.

## Completion

Require controlled inventory and authority, safe input custody, concurrency-safe
updates, metadata and consumer evidence, truthful partial-state handling,
rotation closure where applicable, and a plaintext-free audit record.
