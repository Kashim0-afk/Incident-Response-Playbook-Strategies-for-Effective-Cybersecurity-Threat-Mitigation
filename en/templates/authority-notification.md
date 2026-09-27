# Template: notification to CSIRT Italia and the Garante

> **Not legal advice.** This template helps the response team collect the facts that notifications require, in the order the laws list them. The official submissions go through the CSIRT Italia portal and the Garante's online data breach service, which have their own forms and fields; copy the content from here into them. The decision to notify, and the final text, are approved by management with the DPO and legal counsel.

Keep one working document per incident with all three parts below. Update it as facts change; every version is useful for the final report.

## Part A: common facts

```text
Incident ID:                         {ID}
Organisation, legal entity:          {name, VAT number}
NIS status:                          {essential / important / not in scope}
Contact for this incident:           {name, role, phone, email}
DPO contact:                         {name, phone, email}

Time of detection (UTC):             {first alert}
Time of awareness (UTC):             {when the incident was confirmed/declared}
Current status:                      {ongoing / contained / resolved}

Short description (facts only):      {what happened, in 3-5 sentences}
Systems and services affected:       {list}
Suspected cause:                     {e.g. phishing, exploited VPN vulnerability; "unknown" is allowed}
Malicious or unlawful act suspected: {yes / no / unknown}
Cross-border impact possible:        {yes / no / unknown; which countries}
Indicators of compromise:            {IPs, domains, hashes; defanged}
Measures taken so far:               {containment, eradication steps}
```

## Part B: NIS2 notifications to CSIRT Italia

Legislative Decree 138/2024, art. 25(5). Deadlines run from awareness of the significant incident.

**B1. Early warning (*pre-notifica*) – within 24 hours**

```text
- Reference to Part A facts known so far
- Whether the incident may be the result of unlawful or malicious acts
- Whether it may have a cross-border impact
- Initial request for support from CSIRT Italia, if needed: {yes/no, what}
```

**B2. Incident notification – within 72 hours**

```text
- Updates to the early warning
- Initial assessment: severity and impact
  (services and users affected, duration so far, financial impact estimate)
- Indicators of compromise available
- Measures taken and planned
```

**B3. Intermediate report – when CSIRT Italia asks for one**

```text
- Status updates since the notification
```

**B4. Final report – within one month of the notification**

```text
1. Detailed description of the incident, including severity and impact
2. Type of threat or root cause that probably triggered the incident
3. Mitigation measures applied and ongoing
4. Cross-border impact, where known
```

If the incident is still ongoing at the time of the final report: a progress report at that date, monthly progress reports, and the final report within one month of the end of incident handling.

## Part C: GDPR notification to the Garante (art. 33)

Within 72 hours of awareness, unless the breach is unlikely to result in a risk to individuals. If some information is not yet available, send what you have and complete it in phases (art. 33(4)). If you notify after 72 hours, state the reasons for the delay.

```text
1. Nature of the breach
   - Type: {confidentiality / integrity / availability}
   - How it happened: {short description}
   - Categories of data subjects: {customers, employees, minors, ...}
   - Approximate number of data subjects: {range}
   - Categories of personal data: {identifiers, contact data, financial, health, credentials, ...}
   - Approximate number of records: {range}
2. DPO or other contact point: {name, contact details}
3. Likely consequences for data subjects: {e.g. phishing, fraud, identity theft, discrimination}
4. Measures taken or proposed: {to address the breach and to mitigate adverse effects}
5. Reasons for delay, if after 72 hours: {text}
```

## Part D: communication to data subjects (art. 34)

Only if the breach is likely to result in a high risk and no art. 34(3) exception applies. Clear and plain language.

```text
Subject: Important information about your personal data

What happened
On {date} we discovered that {plain description}. {When it happened, if known.}

What information was involved
{List the categories that concern the reader. Do not minimise.}

What we have done
{Containment, reset of credentials, reports to authorities.}

What you can do
- {e.g. change your password for our service and anywhere you reused it}
- {e.g. be wary of emails or calls that mention this incident and ask for payment or credentials}
- {e.g. check your bank statements}

Contact
{DPO or dedicated contact point, phone and email, opening hours}
```

## Before sending

- [ ] Facts match the incident log; times are in the same time zone
- [ ] Uncertain points are marked as such, not presented as facts
- [ ] No unnecessary personal data in the notification itself
- [ ] Approved by management; DPO and legal counsel consulted
- [ ] Submission receipt or protocol number saved in the incident record
