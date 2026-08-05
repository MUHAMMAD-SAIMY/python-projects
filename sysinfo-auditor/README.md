# Sysinfo Auditor

A Bash script that audits a Linux system and produces a timestamped report covering system, hardware, network, and basic security-relevant information. Useful as a quick local recon / hardening-check baseline.

## Features
- OS, kernel, and hardware info (CPU model, cores, load average)
- Memory and disk usage
- Currently logged-in users and last 5 login records
- Listening network ports (via `ss` or `netstat`)
- Top processes by CPU usage
- Installed package count (dpkg or rpm)
- Basic privilege audit: UID 0 accounts and accounts with login shells
- Saves a full timestamped report to `./reports/`

## Usage
```bash
chmod +x sysinfo_auditor.sh
./sysinfo_auditor.sh
```

Reports are saved to:
```
./reports/sysinfo_report_<YYYY-MM-DD_HH-MM-SS>.txt
```

## Sample Output (excerpt)
```
===== SYSTEM INFO =====
Hostname       : kali
OS             : Kali GNU/Linux Rolling
Kernel         : 6.6.15-amd64
Architecture   : x86_64
Uptime         : up 2 hours, 14 minutes

===== PRIVILEGED / SHELL USERS =====
UID 0 accounts:
root

Accounts with login shells:
root
saimy
```

## Notes
- Designed for Debian/Kali-based systems but falls back gracefully (e.g. `rpm` for RPM-based distros).
- Only run against systems you own or are authorized to audit.
- Requires standard Linux utilities: `bash`, `ss`/`netstat`, `ps`, `awk`, `grep`.

## Requirements
- Bash
- Standard Linux core utilities (no external dependencies)
