# Incident Response and Recovery

Status: **baseline 0.1**
Sources reviewed: **2026-07-17**

Navigation: [Lifecycle](reference-lifecycle.md) · [Process map](process.md) ·
[Utilization](stages/utilization.md) · [Support](stages/support.md)

## Purpose

This document defines control of operational and security incidents from
detection through safe recovery, communication, evidence preservation, and
accountable follow-up. Projects provide paging, ticketing, communication,
forensics, status, emergency-change, and recovery systems.

Incident command protects users and restores an acceptable risk state.
Root-cause debugging and permanent correction are related but separate work.

## Standards basis

| Source | Contribution | Status at review |
| --- | --- | --- |
| [ISO/IEC 20000-1:2018][20000] | Incident, service request, problem, change, continuity, reporting, and improvement controls | Published; confirmed 2023 |
| [NIST SP 800-61 Rev. 3][800-61] | Cybersecurity incident preparation, detection, response, recovery, and improvement integrated with risk management | Final, 2025 |
| [ISO/IEC 27035-1:2023][27035] | Information-security incident management principles and process | Published |
| [ISO 22301:2019][22301] | Preparedness, response, recovery, and continuity management | Published; revision underway |

## Incident record

Preserve incident identity, detection source, active baseline, chronology,
impact, scope, severity, commander, roles, decisions, evidence, communications,
containment/recovery actions, emergency changes, verification, residual risk,
follow-up, and closure authority. Protect sensitive evidence and identities.

## Workflow

1. Validate the signal enough to act; create the record and preserve original evidence.
2. Assess actual and potential impact, affected users/data/regions/dependencies,
   safety/security/privacy obligations, urgency, and uncertainty.
3. Establish one incident lead, decision authority, roles, chronology,
   communication channels, update cadence, and evidence custodian.
4. Protect users and contain expansion. Prefer reversible, bounded actions and
   record every material operational or emergency change.
5. Restore the safest acceptable service or risk state using approved recovery
   paths. Recovery may precede root-cause certainty.
6. Verify recovery from user, service, data, dependency, security, and control
   perspectives; observe for recurrence and hidden partial failure.
7. Communicate facts, impact, uncertainty, actions, workarounds, and next update
   to authorized audiences without leaking sensitive data or speculation.
8. Classify follow-up as operational control, problem investigation, Support,
   Development, Production, Concept, or Retirement work.
9. Review contributing conditions, response effectiveness, detection gaps, and
   recurrence controls; verify action closure before closing the incident.

## Guardrails and decisions

- Do not delay user protection for perfect severity or root-cause classification.
- Do not let several uncoordinated agents issue conflicting recovery actions.
- Do not destroy forensic evidence or expose secrets/PII in shared logs and updates.
- A service process restarting is not recovery proof.
- A closed ticket is not evidence that impact ended or recurrence controls work.
- Security/privacy notification follows applicable authority and obligations;
  the agent must not make an unauthorized disclosure.

Record `monitor`, `contain`, `recover`, `escalate`, `change`, or `close` with
authority and evidence. Closure requires verified acceptable state, preserved
records, owned follow-up, residual-risk disposition, and communication completion.

[20000]: https://www.iso.org/standard/70636.html
[800-61]: https://csrc.nist.gov/pubs/sp/800/61/r3/final
[27035]: https://www.iso.org/standard/78973.html
[22301]: https://www.iso.org/standard/75106.html
