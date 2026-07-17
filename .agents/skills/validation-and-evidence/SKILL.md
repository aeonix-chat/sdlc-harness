---
name: validation-and-evidence
description: Turns project-provided checks, reviews, observations, and measurements into bounded, traceable claims and decision evidence. Use when selecting validation for a change or lifecycle gate, defining assurance levels or evidence matrices, running checks, assessing whether evidence is sufficient, reporting verification or validation results, or aggregating evidence for a candidate, release, operational, support, or retirement decision.
---

# Validation and Evidence

## Overview

Establish what must be proven, discover the project's real validation surface,
run the applicable checks, and report only the claims supported by retained
evidence. Read [`../../../docs/validation-and-evidence.md`](../../../docs/validation-and-evidence.md)
before applying this workflow; that document is normative for claim semantics,
assurance profiles, findings, and completion criteria.

## Workflow

### 1. Frame the requested decision

- Identify the lifecycle stage, decision, authority, candidate or operating
  baseline, requirements, risks, and information needs.
- Write falsifiable claims. State the subject, included and excluded boundaries,
  assumptions, limitations, and conditions that would invalidate evidence.
- If the project names an assurance level, locate its versioned local definition.
  Never infer meaning from `L0`, `L1`, or another label alone.

### 2. Discover the project validation surface

- Read repository guidance and the applicable lifecycle-stage document.
- Inspect existing build files, CI configuration, scripts, package metadata,
  test configuration, operational documentation, and validation registry.
- Prefer documented project commands and environments. Do not invent a task
  runner or assume language, provider, credentials, topology, or evidence store.
- Classify each available check by actual boundary and evidence class. Identify
  external systems, secrets, special data, hardware, privileges, and human review.

If no authoritative command or prerequisite can be discovered, report the gap
and continue with other independent evidence. Ask for input only when the
missing choice materially changes the decision.

### 3. Select sufficient evidence

- Map every claim to methods, objects, criteria, depth, coverage, and evidence
  classes. Avoid treating several instances of one check as independent proof.
- Scale rigor to consequence, uncertainty, reversibility, exposure, and policy.
- Include negative, degraded, recovery, compatibility, and boundary cases when
  those affect the claim.
- Distinguish verification of specified requirements from validation for
  intended use. Do not substitute one silently for the other.
- Declare expected outputs and invalidation conditions before execution.

### 4. Execute and preserve evidence

- Run the discovered project commands in their required environments.
- Preserve real exit status, exact subject identity, inputs, tool versions,
  environment, time, and safe actor or automation identity.
- Capture large output once in the approved location and inspect that retained
  record. Do not rerun solely because a display truncated the result.
- Protect secrets and sensitive data. Use safe references for identities and scopes.
- Mark missing prerequisites or inaccessible external boundaries as `blocked`.
  A mock may support a narrower claim, never the original external claim.

When a check fails unexpectedly, invoke `debugging-and-error-recovery`. A repair
changes the subject or environment and requires affected evidence to be rerun.

### 5. Interpret the results

- Compare evidence to criteria and record exactly one finding for each claim:
  `satisfied`, `not_satisfied`, `inconclusive`, `blocked`, or `not_applicable`.
- Keep command execution status separate from the finding.
- State the supported claim, limitations, exclusions, invalidation conditions,
  residual uncertainty, and the decisions the finding may inform.
- Bind the result to the exact candidate, artifact, configuration, provider,
  environment, or active baseline assessed.

### 6. Support the decision

- Aggregate only compatible and current findings bound to the same decision subject.
- Apply local decision policy; do not authorize a lifecycle transition unless
  the user or project has assigned that authority to the agent.
- Record exceptions, compensating controls, risk owner, expiry, and follow-up.
- Update the authoritative validation registry when the task includes changing
  the framework. Do not create a competing inventory.
- Before commit, pull request, release, or other publication, run the project's
  publication-safety validation. Treat absolute local paths, PII, credentials,
  and secret-material findings as blocking until resolved.

## Report contract

Report the outcome before the command transcript. Include:

- decision or information need;
- exact subject and relevant environment;
- claims and evidence classes exercised;
- project commands or assessment methods used;
- findings and retained evidence references;
- blocked, inconclusive, skipped, and not-applicable work separately;
- limitations, invalidation conditions, and residual risk;
- decision supported, decision not supported, or additional evidence required.

Do not say "validated" without naming the bounded claim and boundary. Do not
say "all checks passed" when required work was blocked, inconclusive, or omitted.

## Completion checklist

- [ ] Claims, subject, boundaries, criteria, and assumptions are explicit.
- [ ] Project-provided commands and prerequisites were discovered.
- [ ] Required methods, evidence classes, depth, and coverage are accounted for.
- [ ] Results preserve real status and evidence references.
- [ ] Every claim has an unambiguous finding.
- [ ] Evidence is bound to the exact assessed baseline.
- [ ] Limitations, invalidation conditions, and residual risks are visible.
- [ ] The supported decision and accountable authority are clear.
