#!/usr/bin/env python3
import ipaddress
import sys

def get_input():
    if len(sys.argv) == 2:
        return sys.argv[1]
    return input("Enter IP/CIDR (e.g. 192.168.1.0/24): ").strip()

def calculate(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    return network

def get_host_range(network):
    hosts = list(network.hosts())
    if not hosts:
        return None, None
    return hosts[0], hosts[-1]

def print_results(network):
    first_host, last_host = get_host_range(network)
    print("\n--- Subnet Info ---")
    print(f"Network Address : {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Netmask          : {network.netmask}")
    print(f"Wildcard Mask    : {network.hostmask}")
    print(f"Prefix Length    : /{network.prefixlen}")
    print(f"Total Addresses  : {network.num_addresses}")
    if first_host and last_host:
        print(f"Usable Host Range: {first_host} - {last_host}")
        print(f"Usable Hosts     : {network.num_addresses - 2}")
    else:
        print("Usable Host Range: N/A (network too small)")
    print(f"Is Private       : {network.is_private}")

def subnet_into(network, new_prefix):
    try:
        subnets = list(network.subnets(new_prefix=new_prefix))
    except ValueError as e:
        print(f"Cannot subnet: {e}")
        return
    print(f"\n--- Split into /{new_prefix} ({len(subnets)} subnets) ---")
    for sub in subnets:
        print(sub)

def main():
    cidr = get_input()
    network = calculate(cidr)
    print_results(network)
    choice = input("\nSplit this network into smaller subnets? (y/n): ").strip().lower()
    if choice == "y":
        new_prefix = int(input(f"Enter new prefix length (> /{network.prefixlen}): "))
        subnet_into(network, new_prefix)

if __name__ == "__main__":
    main()
