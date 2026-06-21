import re

file_path = input("Enter file path: ")
with open(file_path, 'r') as file:
    content = file.read()

Ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
Ip_addresses = re.finditer(Ip_pattern, content)

IPs = set()

for match in Ip_addresses:
        if all(0 <= int(o) <= 255 for o in match.group().split('.')):
            IPs.add(match.group())
            
for ip in IPs:
        print(ip)
