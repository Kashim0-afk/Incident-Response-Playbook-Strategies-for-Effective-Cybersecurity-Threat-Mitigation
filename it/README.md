# Introduzione

Questa è una raccolta di playbook di risposta agli incidenti pensata per un'organizzazione di piccole o medie dimensioni che dispone di un SOC (interno o in outsourcing), di un EDR, di un SIEM e di un tenant Microsoft 365 o Google Workspace. È scritta dal punto di vista di chi difende: cosa controllare per primo, cosa contenere, quali evidenze conservare, chi avvisare ed entro quando.

[English version](../en/README.md)

## Come usarla

1. Leggi il materiale comune prima di averne bisogno: il [ciclo di vita](lifecycle.md), i [livelli di severità e i criteri di escalation](severity-escalation.md), i [ruoli e la matrice RACI](roles-raci.md) e la [gestione delle evidenze](evidence-handling.md).
2. Quando un alert diventa un incidente, apri il playbook corrispondente. Ognuno parte da un breve blocco di triage e da un diagramma decisionale, poi passa a contenimento, eradicazione, ripristino e lezioni apprese.
3. Tieni un registro dell'incidente fin dal primo minuto (orari in UTC, chi ha fatto cosa). Il [report post-incidente](templates/post-incident-report.md) si costruisce da lì.
4. Se possono essere coinvolti dati personali o un servizio essenziale, guarda subito gli [obblighi normativi](regulatory.md): i termini del GDPR e della NIS2 decorrono da quando si viene a conoscenza dell'incidente, non da quando finisce l'indagine.

Strumenti e comandi sono citati solo come esempi. Adattali a ciò che usi davvero e compila rubrica e soglie prima di un incidente, non durante.

## Contenuti

**Fondamenti**

| Pagina | Di cosa tratta |
|---|---|
| [Ciclo di vita della risposta agli incidenti](lifecycle.md) | NIST SP 800-61r3 e CSF 2.0, con il modello classico PICERL a confronto |
| [Severità ed escalation](severity-escalation.md) | Quattro livelli di severità, tempi di risposta di esempio, criteri di escalation |
| [Ruoli e RACI](roles-raci.md) | Chi fa cosa durante un incidente |
| [Gestione delle evidenze](evidence-handling.md) | Ordine di volatilità, catena di custodia, cosa non fare |
| [Obblighi normativi](regulatory.md) | GDPR artt. 33-34, NIS2 e D.Lgs. 138/2024 (non è consulenza legale) |

**Playbook**

| Playbook | Severità predefinita |
|---|---|
| [Ransomware](playbooks/ransomware.md) | SEV1 |
| [Phishing](playbooks/phishing.md) | SEV3, più alta se sono state inserite credenziali |
| [Business email compromise (BEC)](playbooks/bec.md) | SEV2 |
| [Account o credenziali compromessi](playbooks/compromised-account.md) | SEV2, SEV1 per account privilegiati |
| [Malware su un endpoint](playbooks/endpoint-malware.md) | SEV3 |
| [DDoS](playbooks/ddos.md) | SEV2 |
| [Data breach ed esfiltrazione](playbooks/data-breach.md) | SEV1 o SEV2 |

**Modelli**

| Modello | Uso |
|---|---|
| [Comunicazione interna](templates/internal-communication.md) | Avviso al personale e briefing per la direzione |
| [Notifica al CSIRT e alle autorità](templates/authority-notification.md) | Struttura per le notifiche a CSIRT Italia e al Garante |
| [Report post-incidente](templates/post-incident-report.md) | Revisione senza colpevoli, timeline, azioni correttive |

[Fonti e riferimenti](references.md)

## Perimetro e limiti

- I playbook presuppongono che l'organizzazione abbia già svolto il lavoro di preparazione che il NIST colloca sotto Govern, Identify e Protect: inventario degli asset, log, backup, una policy di risposta agli incidenti approvata. Quando un passaggio dipende da qualcosa predisposto in anticipo (un contratto di protezione DDoS, backup offline, una chat fuori banda), il playbook lo dice.
- Non coprono OT/ICS, indagini su minacce interne con il coinvolgimento delle risorse umane, né la compromissione della supply chain di un fornitore software. Servono playbook dedicati.
- La sezione normativa riassume i testi e li cita. Non è consulenza legale: la decisione di notificare spetta all'organizzazione, al suo DPO e ai suoi legali.
