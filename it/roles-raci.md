# Ruoli e matrice RACI

In un'organizzazione piccola la stessa persona può ricoprire più ruoli. Conta che ogni ruolo abbia un titolare e un sostituto con nome e cognome, messi per iscritto insieme a numeri di telefono che funzionino anche fuori dalla rete aziendale.

## Ruoli

| Ruolo | Responsabilità | Di solito ricoperto da |
|---|---|---|
| **IR lead** (incident manager) | Dichiara l'incidente e la severità, coordina il team, è titolare del registro dell'incidente e delle decisioni, riferisce alla direzione | Responsabile della sicurezza o analista SOC senior |
| **Analista SOC** | Triage, analisi di log ed EDR, definizione del perimetro, ricerca di IOC, raccolta delle evidenze | SOC L1/L2 o MSSP |
| **IT operations** | Isolamento, modifiche ad account e rete, backup, ricostruzione e ripristino | Amministratori di infrastruttura, identità e cloud |
| **Ufficio legale** | Obblighi contrattuali e normativi, rapporti con forze dell'ordine e assicurazione, riservatezza delle comunicazioni | Legale interno o studio esterno |
| **DPO** | Valuta il rischio per gli interessati, fornisce pareri sulla notifica e sulla comunicazione GDPR, tiene il registro delle violazioni | Responsabile della protezione dei dati |
| **Comunicazione** | Avvisi interni, comunicati per clienti e stampa, monitoraggio dei social | Responsabile comunicazione o marketing |
| **Direzione** | Approva le decisioni con impatto sul business (fermare un servizio, pagare o non pagare, dichiarazioni pubbliche), firma le notifiche | Amministratore delegato, direttore operativo o dirigente delegato |
| **Owner del servizio** | Sa cosa fa il sistema colpito, chi ne dipende e cosa significa "ripristinato" | Responsabile del processo aziendale |
| **IR / forense esterno** | Analisi forense approfondita, negoziazione, capacità aggiuntiva | Società a contratto (retainer) o panel dell'assicurazione |

## Matrice RACI

R = responsabile (esegue) · A = accountable (uno per riga, approva e risponde del risultato) · C = consultato · I = informato

| Attività | IR lead | Analista SOC | IT ops | Legale | DPO | Comunicazione | Direzione |
|---|---|---|---|---|---|---|---|
| Triage e assegnazione della severità | A | R | C | – | – | – | I |
| Dichiarazione di un incidente SEV1 | A/R | C | C | I | I | I | I |
| Isolamento di host e disattivazione di account | A | R | R | – | – | – | I |
| Raccolta e conservazione delle evidenze | A | R | C | C | – | – | – |
| Fermo di un servizio critico per il business | R | C | C | C | – | I | A |
| Valutazione del rischio di una violazione di dati personali | C | C | – | C | R | – | A |
| Notifica al Garante (art. 33 GDPR) | C | C | – | C | R | – | A |
| Pre-notifica e notifiche a CSIRT Italia (NIS2) | R | C | – | C | C | – | A |
| Comunicazione agli interessati (art. 34 GDPR) | C | – | – | C | R | R | A |
| Comunicati a clienti, partner e stampa | C | – | – | C | C | R | A |
| Denuncia alle forze dell'ordine | C | C | – | R | – | – | A |
| Decisione sul pagamento del riscatto | C | – | – | C | – | – | A/R |
| Eradicazione e ripristino | A | C | R | – | – | – | I |
| Dichiarazione di fine ripristino | A/R | C | C | – | – | I | I |
| Revisione post-incidente e monitoraggio delle azioni | A/R | R | R | C | C | C | I |

Note sulla matrice:

- L'IR lead non è accountable per le notifiche alle autorità. Le firma la direzione; l'IR lead fornisce i fatti e la timeline. Chi invia in pratica la notifica NIS dipende da chi l'organizzazione ha registrato come punto di contatto.
- Ai fini del GDPR notifica il titolare del trattamento. Se sei responsabile del trattamento (per esempio un MSP che tratta i dati di un cliente), il tuo obbligo è informare il titolare senza ingiustificato ritardo (art. 33, par. 2): tieni in rubrica il contatto del cliente.
- La "decisione sul pagamento del riscatto" compare perché nessuno la improvvisi alle tre di notte. La posizione di questo playbook è evitare il pagamento: vedi [Ransomware](playbooks/ransomware.md).

## Rubrica da preparare in anticipo

Tienila stampata e in un posto che non dipenda dalle identità aziendali (per esempio una copia offline sul telefono dell'IR lead).

- Membri del team IR e sostituti, con numero di cellulare
- Reperibile della direzione
- DPO, legale
- MSSP / fornitore SOC, supporto del vendor EDR, fornitore IR a contratto
- NOC del provider internet e fornitore di protezione DDoS
- Supporto dei servizi cloud e SaaS, con gli ID di account necessari per aprire un caso prioritario
- Ufficio antifrode della banca (per il BEC)
- Numero verde della polizza cyber e numero di polizza
- Portale di notifica di CSIRT Italia (per i soggetti NIS): <https://www.csirt.gov.it/segnalazione>
- Garante per la protezione dei dati personali, servizio data breach: <https://servizi.gpdp.it/databreach/s/>
- Polizia Postale, segnalazioni online: <https://www.commissariatodips.it/>
