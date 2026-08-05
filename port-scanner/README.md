# Port Scanner

A multi-threaded TCP port scanner written in Python. Scans a target host for open ports, identifies common services, and grabs basic banners from open sockets.

## Features
- Multi-threaded scanning for speed (configurable thread count)
- Supports port ranges (`1-1024`) and comma-separated lists (`22,80,443`)
- Identifies common services (FTP, SSH, HTTP, SMB, MySQL, RDP, etc.)
- Basic banner grabbing on open ports
- Hostname resolution with error handling
- Scan timing and summary output

## Usage
```bash
python3 port_scanner.py <target> [options]
```

### Options
| Flag | Description | Default |
|------|-------------|---------|
| `-p, --ports` | Ports to scan, e.g. `1-1024` or `22,80,443` | `1-1024` |
| `-t, --threads` | Number of threads | `100` |
| `--timeout` | Socket timeout in seconds | `1.0` |

### Examples
```bash
# Scan default port range on a target
python3 port_scanner.py 192.168.1.1

# Scan specific ports
python3 port_scanner.py scanme.nmap.org -p 22,80,443

# Scan a custom range with more threads
python3 port_scanner.py 10.0.0.5 -p 1-65535 -t 200
```

## Sample Output
```
Scanning target: scanme.nmap.org (45.33.32.156)
Ports: 22,80,443   Threads: 100   Timeout: 1.0s
Started at: 2026-08-06 14:32:10
------------------------------------------------------------
[+] Port 22    open   service: SSH
[+] Port 80    open   service: HTTP   banner: HTTP/1.1 200 OK
------------------------------------------------------------
Scan complete. 2 open port(s) found out of 3 scanned.
Time elapsed: 0.84 seconds
```

## Notes
- Only scan systems you own or have explicit authorization to test.
- Timeout and thread count can be tuned for slower networks or larger ranges.

## Requirements
- Python 3.x (standard library only, no external dependencies)
