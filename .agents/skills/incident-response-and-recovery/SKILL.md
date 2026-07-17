---
name: incident-response-and-recovery
description: Controls operational and security incidents through impact assessment, command, containment, safe recovery, communication, evidence preservation, follow-up, and closure. Use for outages, degradations, data or security events, control failures, emergency changes, major alerts, coordinated recovery, or post-incident review.
---

# Incident Response and Recovery

Read [`../../../docs/incident-response-and-recovery.md`](../../../docs/incident-response-and-recovery.md)
and the Utilization stage guidance. Use project-provided paging, ticketing,
communications, forensics, status, emergency-change, and recovery systems.

## Workflow

1. Validate enough of the signal to act, create the incident identity, bind the
   active baseline, preserve original evidence, and protect sensitive data.
2. Assess actual/potential user, service, data, dependency, safety, security,
   privacy, and obligation impact with uncertainty.
3. Establish one incident lead, authority, roles, chronology, channels, update
   cadence, evidence custodian, and stop/escalation conditions.
4. Protect users and contain expansion with reversible bounded actions. Record
   every material action and emergency change.
5. Restore the safest acceptable state through approved recovery paths; do not
   delay recovery for speculative root-cause work.
6. Verify recovery from user, service, data, dependency, security, and control
   perspectives, then observe for recurrence and partial failure.
7. Communicate authorized facts, impact, uncertainty, action, workaround, and
   next update. Route follow-up to operations, Support, Development, Production,
   Concept, or Retirement.
8. Review contributing conditions and response effectiveness; verify action
   closure and residual-risk disposition before incident closure.

## Guardrails

- Do not wait for perfect classification before protecting users.
- Do not permit competing incident commanders or conflicting recovery actions.
- Do not expose secrets, PII, forensic material, or speculation in broad communications.
- Restart or ticket closure is not recovery evidence.
- Do not make unauthorized security/privacy disclosures.
- Invoke `debugging-and-error-recovery` only after immediate control and recovery are established.

## Completion

Require verified acceptable state, chronology and decisions, preserved evidence,
completed communications, owned follow-up, residual-risk disposition, and closure authority.
