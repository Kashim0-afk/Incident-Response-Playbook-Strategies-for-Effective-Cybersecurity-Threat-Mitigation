# Introduction

This is a set of incident response playbooks for a small or mid-sized organisation that has a SOC (in-house or outsourced), an EDR, a SIEM and a Microsoft 365 or Google Workspace tenant. It is written from the defender's side: what to check first, what to contain, which evidence to keep, who has to be told and by when.

[Versione italiana](../it/README.md)

## How to use it

1. Read the shared material once, before you need it: the [life cycle](lifecycle.md), the [severity levels and escalation criteria](severity-escalation.md), the [roles and RACI matrix](roles-raci.md) and [evidence handling](evidence-handling.md).
2. When an alert turns into an incident, open the matching playbook. Each one starts with a short triage block and a decision diagram, then goes through containment, eradication, recovery and lessons learned.
3. Keep an incident log from the first minute (UTC timestamps, who did what). The [post-incident report](templates/post-incident-report.md) is built from it.
4. If personal data or an essential service may be involved, check the [regulatory obligations](regulatory.md) early: the GDPR and NIS2 clocks start when you become aware of the incident, not when the investigation ends.

The playbooks name concrete tools and commands only as examples. Adapt them to what you actually run, and fill in the contact list and thresholds before an incident, not during one.

## Contents

**Foundations**

| Page | What it covers |
|---|---|
| [Incident response life cycle](lifecycle.md) | NIST SP 800-61r3 and CSF 2.0, with the classic PICERL model for comparison |
| [Severity and escalation](severity-escalation.md) | Four severity levels, example response targets, escalation triggers |
| [Roles and RACI](roles-raci.md) | Who does what during an incident |
| [Evidence handling](evidence-handling.md) | Order of volatility, chain of custody, what not to do |
| [Regulatory obligations](regulatory.md) | GDPR art. 33-34, NIS2 and Italian Legislative Decree 138/2024 (not legal advice) |

**Playbooks**

| Playbook | Default severity |
|---|---|
| [Ransomware](playbooks/ransomware.md) | SEV1 |
| [Phishing](playbooks/phishing.md) | SEV3, raised if credentials were entered |
| [Business email compromise (BEC)](playbooks/bec.md) | SEV2 |
| [Compromised account or credentials](playbooks/compromised-account.md) | SEV2, SEV1 for privileged accounts |
| [Malware on an endpoint](playbooks/endpoint-malware.md) | SEV3 |
| [DDoS](playbooks/ddos.md) | SEV2 |
| [Data breach and exfiltration](playbooks/data-breach.md) | SEV1 or SEV2 |

**Templates**

| Template | Use |
|---|---|
| [Internal communication](templates/internal-communication.md) | Staff notice and management briefing |
| [Notification to CSIRT / authorities](templates/authority-notification.md) | Structure for CSIRT Italia and Garante notifications |
| [Post-incident report](templates/post-incident-report.md) | Blameless review, timeline, corrective actions |

[Sources and references](references.md)

## Scope and limits

- The playbooks assume the organisation has already done the preparation work that NIST places under Govern, Identify and Protect: asset inventory, logging, backups, an approved IR policy. Where a step depends on something prepared in advance (a DDoS protection contract, offline backups, an out-of-band chat), the playbook says so.
- They do not cover OT/ICS, insider investigations with HR involvement, or supply chain compromise of a software vendor. Those need their own playbooks.
- The regulatory section summarises the texts and cites them. It is not legal advice: the decision to notify belongs to the organisation, its DPO and its lawyers.
