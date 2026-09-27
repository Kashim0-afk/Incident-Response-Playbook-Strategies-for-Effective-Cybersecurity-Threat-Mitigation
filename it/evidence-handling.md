# Gestione delle evidenze

Le evidenze servono a tre cose: capire cosa è successo, dimostrarlo a terzi (assicurazione, autorità, un giudice) e verificare che l'eradicazione abbia funzionato. La maggior parte si perde nelle prime ore, tra riavvii, reinstallazioni, rotazione dei log o un amministratore che "fa pulizia" in buona fede.

## Ordine di volatilità

La RFC 3227 (*Guidelines for Evidence Collection and Archiving*, BCP 55) raccomanda di raccogliere dal più volatile al meno volatile:

1. Registri, cache
2. Tabella di routing, cache ARP, tabella dei processi, statistiche del kernel, memoria
3. File system temporanei
4. Disco
5. Dati di logging e monitoraggio remoti relativi al sistema
6. Configurazione fisica, topologia di rete
7. Supporti di archiviazione

In pratica, su un host Windows o Linux sotto indagine:

- **Prima la memoria**, con uno strumento affidabile lanciato da un supporto esterno o tramite l'EDR (per esempio WinPmem, AVML o la funzione di acquisizione della memoria dell'EDR).
- **Poi il triage live**: processi in esecuzione, connessioni di rete, utenti collegati, attività pianificate, servizi. Strumenti come Velociraptor o KAPE li raccolgono in modo coerente.
- **Immagine del disco** o, se non è praticabile, una raccolta mirata di artefatti (event log, hive del registro, dati dei browser, `$MFT`).
- **Log centrali** prima che ruotino: telemetria EDR, SIEM, domain controller, VPN, firewall, proxy, DNS, log di audit cloud (sign-in e audit di Entra ID, unified audit log di Microsoft 365, CloudTrail). Controlla la retention: alcune licenze base conservano certi log cloud solo per pochi giorni.

## Catena di custodia

Per ogni elemento raccolto annota:

| Campo | Esempio |
|---|---|
| ID dell'elemento | `IR-2026-014-E03` |
| Descrizione | Immagine della memoria dell'host `FIN-LT-022` |
| Raccolto da, data e ora (UTC) | G. Rossi, 2026-09-14 09:42Z |
| Metodo e strumento, con versione | Live response EDR, WinPmem (versione annotata) |
| Hash del file (SHA-256) | `9f2c…` |
| Luogo di conservazione | Share cifrato delle evidenze `\\ir-evidence\2026-014\` (accesso limitato al team IR) |
| Ogni passaggio di mano | Data, da chi, a chi, motivo |

Lavora sempre sulle copie, mai sull'originale. Ricalcola l'hash quando consegni un'evidenza.

## Cosa non fare

- **Non spegnere né riavviare le macchine colpite**, a meno che non sia possibile isolarle e stiano propagando attivamente un'infezione. Isolale dalla rete (contenimento di rete dall'EDR, porta dello switch, disattivazione del Wi-Fi). Lo spegnimento distrugge la memoria, che può contenere chiavi di cifratura, codice iniettato e strumenti dell'attaccante. Anche la #StopRansomware Guide della CISA indica di spegnere solo i dispositivi che non si riesce a scollegare dalla rete.
- **Non lanciare "pulizie" antivirus e non reinstallare** prima di aver raccolto ciò che serve. Con il disco cancellato, l'analisi della causa diventa un'ipotesi.
- **Non accedere a un host compromesso con un account domain admin.** Gli accessi interattivi possono lasciare in memoria credenziali che l'attaccante può rubare. Usa la shell remota dell'EDR o un account IR dedicato e con privilegi limitati.
- **Non caricare file interni su sandbox pubbliche o su VirusTotal** se possono contenere dati aziendali o personali. Di solito basta inviare l'hash; il file può rivelare i tuoi dati e far capire all'attaccante che è stato scoperto.
- **Non contattare l'attaccante** da account aziendali e non rispondere alle email di estorsione senza l'approvazione dell'ufficio legale e della direzione.

## Registro dell'incidente

Oltre alle evidenze, tieni un registro continuo: orario (UTC), chi, cosa è stato osservato o fatto, su quale asset. È l'ossatura del report post-incidente e di qualunque notifica alle autorità, che chiedono una timeline. Annota anche le decisioni e le motivazioni, compreso il motivo per cui un passaggio è stato saltato.
