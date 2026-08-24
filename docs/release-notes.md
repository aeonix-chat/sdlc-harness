# Release Notes

Status: **baseline 0.1**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Production](stages/production.md) · [Validation and evidence](validation-and-evidence.md)

## Purpose

Release notes are controlled, audience-facing information about an exact
release. They translate verified product capabilities, compatibility changes,
security information, and known limitations into language users, integrators,
operators, and developers can act on.

Release-note authoring does not tag, build, promote, publish, deploy, or
authorize a release. Projects define the canonical location, format, versioning
scheme, source-control host, and publication mechanism.

## Release boundary and inventory

Identify the candidate source revision, release identity, release unit,
audiences, previous public baseline when one exists, and whether the release is
initial or incremental. Use complete version-control and change-management
history within that boundary as an inventory, not as ready-made prose.

Consider commits, reviewed changes, issues, public contracts, migration and
deployment documentation, candidate-bound validation, known deviations, and
artifact/release-unit definitions. Record why inventory items are included,
collapsed into another capability, or excluded.

## Claim ledger

Before drafting, preserve a working ledger for each candidate public claim:

| Field | Meaning |
| --- | --- |
| Capability or change | Stable audience-facing concept |
| Audience and outcome | Who can do what and why it matters |
| Release identity | Exact candidate or release where the claim applies |
| Evidence | Public contract and bounded validation findings |
| Availability | Required platform, provider, configuration, tier, or client |
| Compatibility | Upgrade, migration, deprecation, and removal impact |
| Limitations | Known boundaries and residual uncertainty |
| Sources | Controlled changes establishing completeness and provenance |

Include a claim only when it exists in the candidate, is externally observable
or actionable, has a stable public meaning, and is supported by evidence that
matches the wording. Tests named after a feature, commit types, labels, planned
work, and intermediate implementation are not sufficient claims.

## Audience translation

Collapse implementation work into product capabilities:

```text
capability or change -> audience action -> value -> availability or boundary
```

Lead with meaningful outcomes and organize by audience task or product
capability. Mention internal mechanisms only when they explain a verified
public compatibility, security, privacy, or operational property. Avoid hype,
unsupported safety claims, and implementation-first change dumps.

For an initial public release, describe current capabilities and limitations
without narrating pre-release fixes or using comparative language without a
released baseline. For an incremental release, describe the audience-visible
delta and make deprecation, removal, migration, security, and upgrade actions
explicit where applicable.

## Safety and review

- Do not expose credentials, personal data, local paths, private payloads,
  internal-only vulnerabilities, or unsanitized evidence.
- Scope security and privacy statements to exact verified properties.
- Keep immutable artifact coordinates in the release manifest or equivalent
  controlled record; link rather than manually retype when practical.
- Do not claim compatibility between independently versioned components unless
  the release-unit contract and evidence support it.
- Require accountable product/security approval where local policy assigns it.

Review range completeness, audience relevance, evidence, compatibility,
release identity, disclosure safety, terminology, and editorial clarity.
Generated notes may help inventory changes but do not replace curated and
approved claims.

## Handoff and completion

Hand the release workflow the approved notes, exact target release/candidate,
range-completeness disposition, claim-review result, and any publication
conditions. Completion means every source change was considered, every
published claim is bounded and evidenced, compatibility and limitations are
actionable, sensitive information is absent, and notes are bound to the exact
release they describe.
