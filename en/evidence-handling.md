# Evidence handling

Evidence serves three purposes: understanding what happened, proving it to third parties (insurer, authorities, a court), and checking that eradication worked. Most of it is lost in the first hours, through reboots, reimaging, log rotation or a well-meaning admin "cleaning up".

## Order of volatility

RFC 3227 (*Guidelines for Evidence Collection and Archiving*, BCP 55) recommends collecting from the most volatile to the least volatile:

1. Registers, cache
2. Routing table, ARP cache, process table, kernel statistics, memory
3. Temporary file systems
4. Disk
5. Remote logging and monitoring data relevant to the system
6. Physical configuration, network topology
7. Archival media

In practice, on a Windows or Linux host under investigation:

- **Memory first**, with a trusted tool run from external media or via the EDR (for example WinPmem, AVML, or the EDR's own memory acquisition).
- **Live triage** next: running processes, network connections, logged-on users, scheduled tasks, services. Tools such as Velociraptor or KAPE collect these consistently.
- **Disk image** or, if that is impractical, a targeted collection of artefacts (event logs, registry hives, browser data, `$MFT`).
- **Central logs** before they rotate: EDR telemetry, SIEM, domain controllers, VPN, firewall, proxy, DNS, cloud audit logs (Entra ID sign-in and audit logs, Microsoft 365 unified audit log, CloudTrail). Check retention: some cloud logs are kept for only a few days on basic licences.

## Chain of custody

For each item collected, record:

| Field | Example |
|---|---|
| Item ID | `IR-2026-014-E03` |
| Description | Memory image of host `FIN-LT-022` |
| Collected by, date and time (UTC) | J. Rossi, 2026-09-14 09:42Z |
| Method and tool, with version | EDR live response, WinPmem (exact version noted) |
| Hash of the file (SHA-256) | `9f2c…` |
| Storage location | Encrypted evidence share `\\ir-evidence\2026-014\` (access limited to the IR team) |
| Every transfer | Date, from, to, reason |

Work on copies, never on the original. Recompute the hash when you hand evidence over.

## What not to do

- **Do not switch off or reboot affected machines** unless you cannot isolate them and they are actively spreading an infection. Isolate them from the network instead (EDR network containment, switch port, removing Wi-Fi). Powering off destroys memory, which may hold encryption keys, injected code and attacker tooling. CISA's #StopRansomware Guide gives the same advice: power down only if devices cannot be disconnected.
- **Do not run antivirus "cleanup" or reimage** before collecting what you need. Once the disk is wiped, root cause analysis is guesswork.
- **Do not log in to a compromised host with a domain admin account.** Interactive logons can leave credentials in memory for the attacker to steal. Use the EDR's remote shell or a dedicated, limited IR account.
- **Do not upload internal files to public sandboxes or VirusTotal** if they may contain company or personal data. Submitting a hash is usually enough; the file itself can reveal your data and tell the attacker they have been spotted.
- **Do not contact the attacker** from corporate accounts, and do not reply to extortion emails without legal and management approval.

## Incident log

Separate from the evidence, keep a running log: timestamp (UTC), who, what was observed or done, on which asset. It is the backbone of the post-incident report and of any notification to authorities, which ask for a timeline. Note also decisions and their reasons, including why a step was skipped.
