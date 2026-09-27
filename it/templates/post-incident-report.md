# Modello: report post-incidente

Va scritto per ogni incidente SEV1 e SEV2, e per quelli minori che hanno fatto emergere qualcosa di nuovo. Tieni la riunione di revisione finché i ricordi sono freschi, idealmente entro due settimane dalla chiusura, con tutte le persone coinvolte, anche quelle esterne all'IT.

La revisione è **senza colpevoli** (blameless): l'obiettivo è capire perché il sistema (persone, processi, tecnologia) ha permesso l'incidente e rallentato la risposta, non trovare qualcuno da incolpare. Chi teme di essere incolpato nasconde proprio i dettagli che contano.

---

```text
Report incidente – {ID} – {titolo breve}

Versione: {n}      Data: {data}      Autore: {nome}      Classificazione: {interno / riservato}
Severità: {SEV finale}      IR lead: {nome}      Playbook usati: {PB-xx}
```

## 1. Sintesi

Da cinque a dieci righe per chi non leggerà altro: cosa è successo, impatto, come è stato risolto, le due o tre azioni più importanti.

## 2. Impatto

| Aspetto | Dettagli |
|---|---|
| Servizi colpiti e tempo di fermo | {servizio – dalle – alle – ore totali} |
| Utenti / clienti coinvolti | {numero, chi} |
| Dati coinvolti | {categorie, numero di persone e registrazioni, oppure "nessuno confermato"} |
| Impatto economico (stima) | {costi diretti, mancati ricavi, costi di ripristino} |
| Notifiche effettuate | {Garante {data}, CSIRT Italia {date}, interessati {data}, Polizia Postale {data}} |

## 3. Timeline (UTC)

Costruita dal registro dell'incidente. Includi quando ha agito l'attaccante, non solo quando te ne sei accorto.

| Ora | Evento | Fonte |
|---|---|---|
| {AAAA-MM-GG hh:mm} | {Accesso iniziale tramite ...} | {EDR / log / risultato forense} |
| | {Primo alert} | |
| | {Incidente dichiarato, SEV assegnato} | |
| | {Contenimento completato} | |
| | {Eradicazione completata} | |
| | {Servizi ripristinati} | |
| | {Incidente chiuso} | |

## 4. Metriche

| Metrica | Valore | Definizione |
|---|---|---|
| Dwell time | | Prima attività dell'attaccante → primo rilevamento |
| Tempo di triage | | Primo alert → incidente dichiarato |
| Tempo di contenimento | | Incidente dichiarato → contenimento confermato |
| Tempo di ripristino | | Incidente dichiarato → servizi ripristinati |
| Tempestività delle notifiche | | Conoscenza → ogni notifica, rispetto alla scadenza di legge |

## 5. Causa principale e fattori concorrenti

- **Causa principale**: {la debolezza tecnica o di processo senza la quale l'incidente non sarebbe avvenuto}
- **Fattori concorrenti**: {ciò che l'ha reso più grave o più lento: log mancanti, responsabilità poco chiare, alert non gestito, backup mai testato}

Chiedersi "perché?" più volte di seguito aiuta a passare dal sintomo ("l'utente ha cliccato") alla causa ("il gateway email non riscrive i link dei domini registrati da poco e l'MFA in uso si può aggirare con il phishing").

## 6. Cosa ha funzionato

{Annotalo: la revisione serve anche a proteggere ciò che funziona.}

## 7. Cosa non ha funzionato

{Fatti, non persone. "L'amministratore dei backup è stato irraggiungibile per tre ore" diventa "nella lista di reperibilità non c'è un sostituto per il sistema di backup".}

## 8. Azioni correttive

Ogni azione ha un solo responsabile e una data. Seguile fino alla chiusura nel sistema di ticketing e rivedi quelle aperte nella riunione mensile sulla sicurezza.

| # | Azione | Tipo | Responsabile | Scadenza | Stato |
|---|---|---|---|---|---|
| 1 | {es. imporre l'MFA resistente al phishing ad amministrazione e amministratori IT} | Prevenzione | {nome} | {data} | Aperta |
| 2 | {es. alert nel SIEM sulla cancellazione delle shadow copy} | Rilevamento | {nome} | {data} | Aperta |
| 3 | {es. aggiungere un sostituto dell'amministratore dei backup alla reperibilità} | Risposta | {nome} | {data} | Aperta |
| 4 | {es. aggiornare PB-01 con i passaggi di isolamento degli hypervisor} | Playbook | {nome} | {data} | Aperta |

## 9. Aggiornamenti a playbook e rilevamenti

- Modifiche ai playbook: {quale PB, quale sezione}
- Rilevamenti nuovi o affinati: {nome della regola, tecnica ATT&CK}
- Formazione o esercitazioni: {es. tabletop sul BEC per l'amministrazione nel trimestre {n}}

## 10. Allegati

- Registro dell'incidente
- Inventario delle evidenze e registrazioni della catena di custodia
- Copie delle notifiche e delle ricevute
