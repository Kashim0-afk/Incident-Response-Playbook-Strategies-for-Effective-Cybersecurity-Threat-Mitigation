# Modello: notifica a CSIRT Italia e al Garante

> **Non è consulenza legale.** Questo modello aiuta il team di risposta a raccogliere i fatti richiesti dalle notifiche, nell'ordine in cui li elencano le norme. Gli invii ufficiali passano dal portale di CSIRT Italia e dal servizio online data breach del Garante, che hanno moduli e campi propri: il contenuto va copiato da qui in quei moduli. La decisione di notificare e il testo finale li approva la direzione, sentiti il DPO e l'ufficio legale.

Tieni un unico documento di lavoro per incidente con le tre parti qui sotto. Aggiornalo man mano che i fatti cambiano: ogni versione serve per la relazione finale.

## Parte A: fatti comuni

```text
ID incidente:                          {ID}
Organizzazione, ragione sociale:       {nome, partita IVA}
Stato NIS:                             {essenziale / importante / fuori ambito}
Referente per questo incidente:        {nome, ruolo, telefono, email}
Contatto del DPO:                      {nome, telefono, email}

Ora del rilevamento (UTC):             {primo alert}
Ora della conoscenza (UTC):            {quando l'incidente è stato confermato/dichiarato}
Stato attuale:                         {in corso / contenuto / risolto}

Descrizione sintetica (solo fatti):    {cosa è successo, in 3-5 frasi}
Sistemi e servizi colpiti:             {elenco}
Causa sospetta:                        {es. phishing, vulnerabilità VPN sfruttata; "sconosciuta" è ammesso}
Sospetto di atto illegittimo/malevolo: {sì / no / non noto}
Possibile impatto transfrontaliero:    {sì / no / non noto; quali paesi}
Indicatori di compromissione:          {IP, domini, hash; in forma disinnescata}
Misure adottate finora:                {contenimento, eradicazione}
```

## Parte B: notifiche NIS2 a CSIRT Italia

D.Lgs. 138/2024, art. 25, comma 5. I termini decorrono da quando si è venuti a conoscenza dell'incidente significativo.

**B1. Pre-notifica – entro 24 ore**

```text
- Fatti della Parte A noti finora
- Se l'incidente possa ritenersi il risultato di atti illegittimi o malevoli
- Se possa avere un impatto transfrontaliero
- Eventuale richiesta di supporto a CSIRT Italia: {sì/no, quale}
```

**B2. Notifica dell'incidente – entro 72 ore**

```text
- Aggiornamenti rispetto alla pre-notifica
- Valutazione iniziale: gravità e impatto
  (servizi e utenti coinvolti, durata finora, stima dell'impatto economico)
- Indicatori di compromissione disponibili
- Misure adottate e previste
```

**B3. Relazione intermedia – quando CSIRT Italia la richiede**

```text
- Aggiornamenti sulla situazione dopo la notifica
```

**B4. Relazione finale – entro un mese dalla notifica**

```text
1. Descrizione dettagliata dell'incidente, compresi gravità e impatto
2. Tipo di minaccia o causa originale (root cause) che ha probabilmente innescato l'incidente
3. Misure di attenuazione adottate e in corso
4. Impatto transfrontaliero, ove noto
```

Se l'incidente è ancora in corso al momento della relazione finale: una relazione sui progressi a quella data, relazioni mensili sui progressi e la relazione finale entro un mese dalla conclusione della gestione dell'incidente.

## Parte C: notifica GDPR al Garante (art. 33)

Entro 72 ore da quando se ne è venuti a conoscenza, salvo che sia improbabile che la violazione presenti un rischio per le persone. Se alcune informazioni non sono ancora disponibili, invia quelle che hai e completa per fasi (art. 33, par. 4). Se notifichi oltre le 72 ore, indica i motivi del ritardo.

```text
1. Natura della violazione
   - Tipo: {riservatezza / integrità / disponibilità}
   - Come è avvenuta: {breve descrizione}
   - Categorie di interessati: {clienti, dipendenti, minori, ...}
   - Numero approssimativo di interessati: {intervallo}
   - Categorie di dati personali: {identificativi, di contatto, finanziari, sanitari, credenziali, ...}
   - Numero approssimativo di registrazioni: {intervallo}
2. DPO o altro punto di contatto: {nome, recapiti}
3. Probabili conseguenze per gli interessati: {es. phishing, frode, furto d'identità, discriminazione}
4. Misure adottate o proposte: {per porre rimedio alla violazione e attenuarne gli effetti negativi}
5. Motivi del ritardo, se oltre le 72 ore: {testo}
```

## Parte D: comunicazione agli interessati (art. 34)

Solo se la violazione è suscettibile di presentare un rischio elevato e non si applica un'eccezione dell'art. 34, par. 3. Linguaggio semplice e chiaro.

```text
Oggetto: Informazioni importanti sui tuoi dati personali

Cosa è successo
Il {data} abbiamo scoperto che {descrizione semplice}. {Quando è avvenuto, se noto.}

Quali informazioni sono coinvolte
{Elenca le categorie che riguardano chi legge. Non minimizzare.}

Cosa abbiamo fatto
{Contenimento, reset delle credenziali, segnalazioni alle autorità.}

Cosa puoi fare
- {es. cambia la password del nostro servizio e di ogni altro servizio in cui l'hai riutilizzata}
- {es. diffida di email o telefonate che citano questo incidente e chiedono pagamenti o credenziali}
- {es. controlla gli estratti conto}

Contatti
{DPO o punto di contatto dedicato, telefono ed email, orari}
```

## Prima di inviare

- [ ] I fatti corrispondono al registro dell'incidente; gli orari sono nello stesso fuso
- [ ] I punti incerti sono indicati come tali, non presentati come fatti
- [ ] Nessun dato personale superfluo nella notifica stessa
- [ ] Approvata dalla direzione, sentiti DPO e ufficio legale
- [ ] Ricevuta o numero di protocollo dell'invio salvati nella pratica dell'incidente
