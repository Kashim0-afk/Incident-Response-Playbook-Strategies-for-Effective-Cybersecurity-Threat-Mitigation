# Template: post-incident report

Write it for every SEV1 and SEV2 incident, and for smaller ones that revealed something new. Hold the review meeting while memories are fresh, ideally within two weeks of closure, with everyone who took part, including people outside IT.

The review is **blameless**: the goal is to understand why the system (people, processes, technology) allowed the incident and slowed the response, not to find someone to blame. People who fear blame hide the details that matter.

---

```text
Incident report – {ID} – {short title}

Version: {n}      Date: {date}      Author: {name}      Classification: {internal / confidential}
Severity: {final SEV}      IR lead: {name}      Playbook(s) used: {PB-xx}
```

## 1. Summary

Five to ten lines for someone who reads nothing else: what happened, impact, how it was resolved, the two or three most important actions.

## 2. Impact

| Aspect | Details |
|---|---|
| Services affected and downtime | {service – from – to – total hours} |
| Users / customers affected | {number, who} |
| Data involved | {categories, number of people and records, or "none confirmed"} |
| Financial impact (estimate) | {direct costs, lost revenue, recovery costs} |
| Notifications made | {Garante {date}, CSIRT Italia {dates}, data subjects {date}, police {date}} |

## 3. Timeline (UTC)

Built from the incident log. Include when the attacker acted, not only when you noticed.

| Time | Event | Source |
|---|---|---|
| {YYYY-MM-DD hh:mm} | {Initial access via ...} | {EDR / log / forensic finding} |
| | {First alert} | |
| | {Incident declared, SEV assigned} | |
| | {Containment completed} | |
| | {Eradication completed} | |
| | {Services restored} | |
| | {Incident closed} | |

## 4. Metrics

| Metric | Value | Definition |
|---|---|---|
| Dwell time | | First attacker activity → first detection |
| Time to triage | | First alert → incident declared |
| Time to contain | | Incident declared → containment confirmed |
| Time to recover | | Incident declared → services restored |
| Notification timeliness | | Awareness → each notification, compared with the legal deadline |

## 5. Root cause and contributing factors

- **Root cause**: {the technical or process weakness without which the incident would not have happened}
- **Contributing factors**: {things that made it worse or slower: missing logs, unclear ownership, alert not triaged, backup not tested}

Asking "why?" several times in a row helps to move from the symptom ("the user clicked") to the cause ("the email gateway does not rewrite links from newly registered domains, and MFA can be phished").

## 6. What went well

{Keep these; the review is also about protecting what works.}

## 7. What did not go well

{Facts, not people. "The backup admin could not be reached for three hours" becomes "there is no deputy for the backup system on the on-call list".}

## 8. Corrective actions

Every action has one owner and a date. Track them to closure in the ticketing system; review open ones at the monthly security meeting.

| # | Action | Type | Owner | Due date | Status |
|---|---|---|---|---|---|
| 1 | {e.g. enforce phishing-resistant MFA for finance and admins} | Prevent | {name} | {date} | Open |
| 2 | {e.g. alert on shadow copy deletion in the SIEM} | Detect | {name} | {date} | Open |
| 3 | {e.g. add backup admin deputy to on-call list} | Respond | {name} | {date} | Open |
| 4 | {e.g. update PB-01 with the hypervisor isolation steps} | Playbook | {name} | {date} | Open |

## 9. Playbook and detection updates

- Playbook changes: {which PB, which section}
- New or tuned detections: {rule name, ATT&CK technique}
- Training or exercises: {e.g. tabletop exercise on BEC for finance in Q{n}}

## 10. Attachments

- Incident log
- Evidence inventory and chain of custody records
- Copies of notifications and receipts
