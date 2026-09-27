# Roles and RACI matrix

In a small organisation one person may hold several roles. What matters is that every role has a named owner and a deputy, written down with phone numbers that work outside the corporate network.

## Roles

| Role | Responsibilities | Typically held by |
|---|---|---|
| **IR lead** (incident manager) | Declares the incident and its severity, coordinates the team, owns the incident log and the decisions, reports to management | Security manager or senior SOC analyst |
| **SOC analyst** | Triage, log and EDR analysis, scoping, IOC hunting, evidence collection | SOC L1/L2, or the MSSP |
| **IT operations** | Isolation, account and network changes, backups, rebuild and restore | Infrastructure, identity and cloud admins |
| **Legal** | Contractual and regulatory duties, relations with law enforcement, insurer, privilege of communications | In-house counsel or external firm |
| **DPO** | Assesses the risk to data subjects, advises on GDPR notification and communication, keeps the breach register | Data Protection Officer |
| **Communications** | Internal notices, customer and press statements, social media monitoring | Communications or marketing lead |
| **Management** | Approves business-impacting decisions (shutting down a service, paying or not paying, public statements), signs off notifications | CEO, COO or delegated executive |
| **Service owner** | Knows what the affected system does, who depends on it and what "restored" means | Business process owner |
| **External IR / forensics** | Deep forensics, negotiation, surge capacity | Retainer firm or insurer's panel |

## RACI matrix

R = responsible (does the work) · A = accountable (one per row, signs off) · C = consulted · I = informed

| Activity | IR lead | SOC analyst | IT ops | Legal | DPO | Comms | Management |
|---|---|---|---|---|---|---|---|
| Triage and severity assignment | A | R | C | – | – | – | I |
| Declaring a SEV1 incident | A/R | C | C | I | I | I | I |
| Isolating hosts and disabling accounts | A | R | R | – | – | – | I |
| Collecting and preserving evidence | A | R | C | C | – | – | – |
| Shutting down a business-critical service | R | C | C | C | – | I | A |
| Personal data breach risk assessment | C | C | – | C | R | – | A |
| Notification to the Garante (GDPR art. 33) | C | C | – | C | R | – | A |
| Early warning and notifications to CSIRT Italia (NIS2) | R | C | – | C | C | – | A |
| Communication to data subjects (GDPR art. 34) | C | – | – | C | R | R | A |
| Customer, partner and press statements | C | – | – | C | C | R | A |
| Report to law enforcement | C | C | – | R | – | – | A |
| Ransom payment decision | C | – | – | C | – | – | A/R |
| Eradication and restore | A | C | R | – | – | – | I |
| Declaring the end of recovery | A/R | C | C | – | – | I | I |
| Post-incident review and action tracking | A/R | R | R | C | C | C | I |

Notes on the matrix:

- The IR lead is not accountable for notifications to authorities. Management signs them off; the IR lead supplies the facts and the timeline. Who submits a NIS2 notification in practice depends on who the organisation registered as its contact point.
- For the GDPR, the controller notifies. If you are a processor (for example an MSP handling a customer's data), your duty is to inform the controller without undue delay (art. 33(2)); keep the customer's contact in the list.
- "Ransom payment decision" appears so that nobody improvises it at 3 a.m. The playbook's position is to avoid payment; see [Ransomware](playbooks/ransomware.md).

## Contact list to prepare in advance

Keep it printed and in a location that does not depend on corporate identity (for example an offline copy on the IR lead's phone).

- IR team members and deputies, with mobile numbers
- Management on-call
- DPO, legal counsel
- MSSP / SOC provider, EDR vendor support, external IR retainer
- Internet provider NOC and DDoS protection provider
- Cloud and SaaS support with the account IDs needed to open a priority case
- Bank fraud desk (for BEC)
- Cyber insurer hotline and policy number
- CSIRT Italia notification portal (for NIS entities): <https://www.csirt.gov.it/segnalazione>
- Garante per la protezione dei dati personali, data breach service: <https://servizi.gpdp.it/databreach/s/>
- Polizia Postale, online reporting: <https://www.commissariatodips.it/>
