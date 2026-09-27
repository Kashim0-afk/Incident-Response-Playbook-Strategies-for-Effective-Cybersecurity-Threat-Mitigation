# Incident Response Playbooks

Blue team incident response playbooks aligned with **NIST SP 800-61 Rev. 3 / CSF 2.0** and **MITRE ATT&CK**, with notes on EU and Italian notification duties (**GDPR art. 33-34, NIS2, Legislative Decree 138/2024**). English and Italian.

Playbook di risposta agli incidenti per il blue team, allineati a **NIST SP 800-61 Rev. 3 / CSF 2.0** e **MITRE ATT&CK**, con note sugli obblighi di notifica europei e italiani (**GDPR artt. 33-34, NIS2, D.Lgs. 138/2024**). In inglese e in italiano.

**Website / Sito:** <https://kashim0-afk.github.io/Incident-Response-Playbook-Strategies-for-Effective-Cybersecurity-Threat-Mitigation/>

| | English | Italiano |
|---|---|---|
| Start here / Inizia qui | [Introduction](en/README.md) | [Introduzione](it/README.md) |
| Life cycle / Ciclo di vita | [NIST 800-61r3, CSF 2.0, PICERL](en/lifecycle.md) | [NIST 800-61r3, CSF 2.0, PICERL](it/lifecycle.md) |
| Severity / Severità | [Levels and escalation](en/severity-escalation.md) | [Livelli ed escalation](it/severity-escalation.md) |
| Roles / Ruoli | [RACI matrix](en/roles-raci.md) | [Matrice RACI](it/roles-raci.md) |
| Evidence / Evidenze | [Evidence handling](en/evidence-handling.md) | [Gestione delle evidenze](it/evidence-handling.md) |
| Regulation / Normativa | [GDPR, NIS2 (not legal advice)](en/regulatory.md) | [GDPR, NIS2 (non è consulenza legale)](it/regulatory.md) |
| **Playbooks** | | |
| PB-01 | [Ransomware](en/playbooks/ransomware.md) | [Ransomware](it/playbooks/ransomware.md) |
| PB-02 | [Phishing](en/playbooks/phishing.md) | [Phishing](it/playbooks/phishing.md) |
| PB-03 | [Business email compromise](en/playbooks/bec.md) | [Business email compromise](it/playbooks/bec.md) |
| PB-04 | [Compromised account](en/playbooks/compromised-account.md) | [Account compromesso](it/playbooks/compromised-account.md) |
| PB-05 | [Endpoint malware](en/playbooks/endpoint-malware.md) | [Malware su endpoint](it/playbooks/endpoint-malware.md) |
| PB-06 | [DDoS](en/playbooks/ddos.md) | [DDoS](it/playbooks/ddos.md) |
| PB-07 | [Data breach and exfiltration](en/playbooks/data-breach.md) | [Data breach ed esfiltrazione](it/playbooks/data-breach.md) |
| **Templates / Modelli** | | |
| | [Internal communication](en/templates/internal-communication.md) | [Comunicazione interna](it/templates/internal-communication.md) |
| | [Notification to CSIRT / authorities](en/templates/authority-notification.md) | [Notifica al CSIRT e alle autorità](it/templates/authority-notification.md) |
| | [Post-incident report](en/templates/post-incident-report.md) | [Report post-incidente](it/templates/post-incident-report.md) |
| Sources / Fonti | [References](en/references.md) | [Riferimenti](it/references.md) |

## What each playbook contains

Trigger and detection · triage · decision diagram (Mermaid) · containment · evidence to collect · eradication · recovery · notifications · lessons learned · mistakes to avoid · ATT&CK techniques (IDs checked against ATT&CK Enterprise v19.2) · checklist.

## Repository layout

```text
en/                 English pages
it/                 Italian pages (same file names)
  playbooks/        PB-01 … PB-07
  templates/        communication, notification, post-incident report
_config.yml         Jekyll configuration for GitHub Pages (theme: Cayman)
_layouts/, _includes/, assets/
                    page layout, navigation, Mermaid loader
scripts/check_links.py
                    checks internal links and anchors in all Markdown files
```

Diagrams are written in Mermaid: GitHub renders them in the repository view, and the site loads mermaid.js through `_includes/head-custom.html`.

To preview the site locally: `gem install jekyll jekyll-theme-cayman jekyll-relative-links jekyll-optional-front-matter jekyll-titles-from-headings jekyll-default-layout jekyll-readme-index jekyll-seo-tag`, then `jekyll serve`. To check links: `python scripts/check_links.py`.

## Disclaimer

Study and portfolio material written by a junior SOC analyst. It is not a substitute for your organisation's incident response plan, and the regulatory pages are not legal advice. Verify legal texts on the official sources linked in each page.

Materiale di studio e portfolio. Non sostituisce il piano di risposta agli incidenti della tua organizzazione e le pagine normative non sono consulenza legale. Verifica i testi di legge sulle fonti ufficiali indicate in ogni pagina.

## Changelog

- **2.0** (September 2026): complete rewrite. Separate English and Italian pages, CSF 2.0 / 800-61r3 framing, seven playbooks with ATT&CK mapping and decision diagrams, RACI, severity model, evidence handling, regulatory summary, templates, GitHub Pages site.
- **1.0** (January 2025): first draft, single bilingual file.

## License

[MIT](LICENSE) © 2025 Matteo Zordan
