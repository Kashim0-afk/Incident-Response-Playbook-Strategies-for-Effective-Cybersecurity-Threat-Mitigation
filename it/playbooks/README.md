# Playbook

Ogni playbook ha la stessa struttura: trigger e rilevamento, triage, diagramma decisionale, contenimento, evidenze, eradicazione, ripristino, notifiche, lezioni apprese, errori da evitare, tecniche ATT&CK e checklist. I livelli di severità fanno riferimento a [Severità ed escalation](../severity-escalation.md).

| ID | Playbook | Severità predefinita | Prima azione tipica |
|---|---|---|---|
| PB-01 | [Ransomware](ransomware.md) | SEV1 | Isolare gli host senza spegnerli; proteggere i backup |
| PB-02 | [Phishing](phishing.md) | da SEV4 a SEV2 | Trovare tutti i destinatari e rimuovere il messaggio; revocare le sessioni di chi ha inserito le credenziali |
| PB-03 | [Business email compromise](bec.md) | SEV2 | Chiamare la banca se sono partiti soldi; verificare fuori banda |
| PB-04 | [Account compromesso](compromised-account.md) | SEV2, SEV1 se privilegiato | Revocare sessioni e token, poi reimpostare la password |
| PB-05 | [Malware su un endpoint](endpoint-malware.md) | SEV3 | Isolare tramite EDR, acquisire la memoria, reinstallare |
| PB-06 | [DDoS](ddos.md) | SEV2 | Riconoscere il tipo di attacco e attivare la mitigazione del provider |
| PB-07 | [Data breach ed esfiltrazione](data-breach.md) | SEV1 o SEV2 | Fermare la fuga dopo aver salvato i log; coinvolgere il DPO |

Raramente un incidente resta dentro un solo playbook. Un clic su un phishing può diventare un account compromesso, poi un BEC o un data breach; un alert di malware può essere il primo segnale di un ransomware. Ogni playbook rimanda al successivo nei punti in cui i percorsi si incrociano.
