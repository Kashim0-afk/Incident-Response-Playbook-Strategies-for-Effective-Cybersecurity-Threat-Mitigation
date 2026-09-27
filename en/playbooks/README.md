# Playbooks

Each playbook follows the same layout: trigger and detection, triage, a decision diagram, containment, evidence, eradication, recovery, notifications, lessons learned, mistakes to avoid, ATT&CK techniques and a checklist. Severity levels refer to [Severity and escalation](../severity-escalation.md).

| ID | Playbook | Default severity | Typical first action |
|---|---|---|---|
| PB-01 | [Ransomware](ransomware.md) | SEV1 | Isolate hosts without powering them off; protect backups |
| PB-02 | [Phishing](phishing.md) | SEV4 to SEV2 | Find every recipient and purge; revoke sessions for users who entered credentials |
| PB-03 | [Business email compromise](bec.md) | SEV2 | Call the bank if money has left; verify out of band |
| PB-04 | [Compromised account](compromised-account.md) | SEV2, SEV1 if privileged | Revoke sessions and tokens, then reset the password |
| PB-05 | [Malware on an endpoint](endpoint-malware.md) | SEV3 | Isolate through EDR, collect memory, reimage |
| PB-06 | [DDoS](ddos.md) | SEV2 | Identify the attack type and activate provider mitigation |
| PB-07 | [Data breach and exfiltration](data-breach.md) | SEV1 or SEV2 | Stop the leak after capturing logs; involve the DPO |

Incidents rarely stay inside one playbook. A phishing click can become a compromised account, then BEC or a data breach; a malware alert can be the first sign of ransomware. Each playbook links to the next one where the paths cross.
