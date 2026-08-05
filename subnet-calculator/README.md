# Subnet Calculator

A command-line IPv4/IPv6 subnet calculator built on Python's `ipaddress` module. Computes network details from a CIDR notation input and can split a network into smaller subnets.

## Features
- Accepts input as a CLI argument or interactive prompt
- Computes network address, broadcast address, netmask, wildcard mask, prefix length, total addresses, and usable host range
- Flags whether the network is private
- Optional interactive subnetting: split a network into smaller subnets of a chosen prefix length

## Usage
```bash
# Pass CIDR directly
python3 subnet_calculator.py 192.168.1.0/24

# Or run interactively
python3 subnet_calculator.py
```

## Sample Output
```
Enter IP/CIDR (e.g. 192.168.1.0/24): 192.168.1.0/24

--- Subnet Info ---
Network Address : 192.168.1.0
Broadcast Address: 192.168.1.255
Netmask          : 255.255.255.0
Wildcard Mask    : 0.0.0.255
Prefix Length    : /24
Total Addresses  : 256
Usable Host Range: 192.168.1.1 - 192.168.1.254
Usable Hosts     : 254
Is Private       : True

Split this network into smaller subnets? (y/n): y
Enter new prefix length (> /24): 26

--- Split into /26 (4 subnets) ---
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

## Requirements
- Python 3.x (standard library only, no external dependencies)
