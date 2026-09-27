# Modello: comunicazione interna

Durante un incidente i messaggi interni hanno due compiti: dire alle persone cosa fare (e cosa non fare) e fermare le voci di corridoio. Tienili brevi, fattuali e datati. Non inserire indicatori tecnici, nomi di presunti attaccanti o ipotesi sulla causa.

Se la posta o Teams possono essere compromessi, invia l'avviso su un canale che l'attaccante non può leggere: SMS, catena telefonica, un messaggio da un tenant separato, cartelli all'ingresso.

## 1. Primo avviso al personale

```text
Oggetto: [INCIDENTE IT] {Servizio/sistema} non disponibile – aggiornamento n. {n} – {data} {ora}

Cosa sta succedendo
Alle {ora} abbiamo rilevato un incidente di sicurezza che riguarda {sistemi o servizi, in parole semplici}.
I team IT e sicurezza ci stanno lavorando.

Cosa significa per te
- {es. posta e file server non sono disponibili}
- {es. il gestionale funziona normalmente}

Cosa ti chiediamo
- Lascia il computer acceso e non riavviarlo, a meno che non te lo dica l'IT.
- Non collegare chiavette USB o dispositivi personali alla rete.
- Non inoltrare questo messaggio fuori dall'azienda e non commentare sui social.
- Segnala qualunque cosa insolita (messaggi strani, richieste di password o di pagamenti)
  a {numero di telefono / contatto}, non via email.

Cosa non ti chiederemo mai
Non ti chiederemo mai password o codici MFA via email, chat o telefono.

Prossimo aggiornamento
Entro le {ora}, tramite {canale}.

{Nome}, {ruolo} – {numero di telefono}
```

## 2. Aggiornamento

```text
Oggetto: [INCIDENTE IT] {Servizio} – aggiornamento n. {n} – {data} {ora}

Cosa è cambiato dall'ultimo aggiornamento
- {es. la posta è di nuovo disponibile; il file server è ancora offline}

Cosa puoi fare adesso
- {es. puoi accedere di nuovo; ti verrà chiesto di impostare una nuova password}

Cosa non è ancora disponibile, con una stima se l'abbiamo
- {sistema}: {stima oppure "non abbiamo ancora una stima"}

Prossimo aggiornamento entro le {ora}.
```

## 3. Briefing per la direzione

Una pagina, da leggere in due minuti. Inviala a intervalli fissi durante SEV1 e SEV2.

```text
Incidente {ID} – briefing n. {n} – {data} {ora UTC}
Severità: {SEV1–SEV4} (cambiata da {precedente} perché {motivo}) | IR lead: {nome}

1. Situazione
   {Due o tre frasi: cosa è successo, cosa è colpito, se è contenuto.}

2. Impatto sul business
   - Servizi fermi: {elenco} dalle {ora}
   - Clienti coinvolti: {chi, quanti, stima}
   - Dati potenzialmente coinvolti: {categorie, oppure "in corso di verifica"}

3. Azioni dall'ultimo briefing
   - {azione} – {responsabile} – {fatta / in corso}

4. Decisioni richieste alla direzione
   - {es. approvare il fermo del negozio online per un massimo di 4 ore}
   - {es. approvare l'attivazione del fornitore IR a contratto}

5. Scadenze legali e normative
   - GDPR: conoscenza alle {ora}; scadenza 72h {data ora}; valutazione DPO {stato}
   - NIS2: pre-notifica dovuta entro {data ora} / inviata alle {ora} / non applicabile perché {motivo}
   - Assicurazione avvisata: {sì/no, ora}; forze dell'ordine: {sì/no}

6. Prossimo briefing: {ora}
```

## Suggerimenti di scrittura

- Di' cosa sai e cosa non sai ancora. "Non sappiamo ancora se sono stati copiati dati; ne sapremo di più entro le 18:00" è meglio del silenzio o di un'ipotesi.
- Usa gli stessi fatti su tutti i canali. Gli avvisi interni escono dall'azienda: scrivili come se potesse leggerli un cliente.
- Indica un unico punto di contatto, così le domande non arrivano a chi sta facendo il lavoro tecnico.
