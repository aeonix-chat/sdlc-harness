---
name: release-notes
description: Drafts, revises, or reviews evidence-backed audience-facing release notes. Use when translating an initial or incremental release boundary, change history, public contracts, compatibility impact, validation evidence, and known limitations into approved product communication. Do not use it to build, tag, promote, publish, or deploy a release.
---

# Release Notes

Read [`../../../docs/release-notes.md`](../../../docs/release-notes.md) and
[`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md).
Use the project's versioning, canonical note location, release unit, change
system, publication mechanism, and approval authority.

## Workflow

1. Establish exact candidate, release identity, release unit, audiences,
   initial/incremental mode, and previous public baseline.
2. Inventory all controlled changes in the boundary plus public contracts,
   migration information, validation findings, deviations, and limitations.
3. Create a working claim ledger linking each audience outcome to exact release
   identity, evidence, availability, compatibility, limitations, and sources.
4. Exclude unshipped work and unsupported claims; collapse implementation
   changes that produce one audience capability.
5. Draft in audience language, leading with actions and outcomes. Make upgrade,
   migration, deprecation, removal, security, and known limitations explicit.
6. Review completeness, evidence, compatibility, disclosure safety, identity,
   terminology, and editorial quality.
7. Hand approved notes and their claim/range disposition to the project's
   release workflow without performing release mutations.

## Guardrails

- Change history is an inventory boundary, not publishable prose.
- Generated release notes are a completeness aid, not claim authority.
- Do not expose secrets, personal data, private payloads, local paths, or
  unsafe vulnerability detail.
- Do not overstate security, privacy, compatibility, availability, or validation.
- Keep notes bound to one exact release and its controlled release unit.

## Completion

Require complete inventory disposition, evidence-backed audience claims,
actionable compatibility and limitations, disclosure-safe content, approval
where required, and an exact handoff to the release workflow.
