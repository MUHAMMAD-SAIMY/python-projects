#!/usr/bin/env python3
import socket
import sys
import threading
import argparse
from queue import Queue
from datetime import datetime

print_lock = threading.Lock()
open_ports = []

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Proxy"
}

# grabs a basic service banner from an open socket
def grab_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()
        return banner.split("\n")[0] if banner else ""
    except Exception:
        return ""

# attempts a TCP connect to a single port and reports if open
def scan_port(target, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "unknown")
            banner = grab_banner(sock)
            with print_lock:
                open_ports.append(port)
                line = f"[+] Port {port:<5} open   service: {service}"
                if banner:
                    line += f"   banner: {banner}"
                print(line)
    except Exception:
        pass
    finally:
        sock.close()

# thread worker that pulls ports from the shared queue
def worker(target, timeout, queue):
    while not queue.empty():
        port = queue.get()
        scan_port(target, port, timeout)
        queue.task_done()

# resolves hostname to IP, exits cleanly if it fails
def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[-] Could not resolve host: {target}")
        sys.exit(1)

# parses port strings like "22,80,443" or "1-1024" into a sorted list
def parse_ports(port_string):
    ports = set()
    for part in port_string.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded TCP Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports to scan, e.g. 1-1024 or 22,80,443")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--timeout", type=float, default=1.0, help="Socket timeout in seconds")
    args = parser.parse_args()

    ip = resolve_target(args.target)
    ports = parse_ports(args.ports)

    print(f"Scanning target: {args.target} ({ip})")
    print(f"Ports: {args.ports}   Threads: {args.threads}   Timeout: {args.timeout}s")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    start_time = datetime.now()
    queue = Queue()
    for port in ports:
        queue.put(port)

    thread_list = []
    for _ in range(min(args.threads, len(ports))):
        t = threading.Thread(target=worker, args=(ip, args.timeout, queue))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    duration = (datetime.now() - start_time).total_seconds()
    print("-" * 60)
    print(f"Scan complete. {len(open_ports)} open port(s) found out of {len(ports)} scanned.")
    print(f"Time elapsed: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
