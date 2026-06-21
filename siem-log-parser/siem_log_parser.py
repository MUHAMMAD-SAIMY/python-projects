import re

file_path = input("Enter file path: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
    exit()

log_pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[(.+?)\] "(\w+) (.+?) HTTP/\d\.\d" (\d{3})'

for match in re.finditer(log_pattern, content):
    ip        = match.group(1)
    timestamp = match.group(2)
    method    = match.group(3)
    path      = match.group(4)
    status    = match.group(5)

    print(f"""
IP        : {ip}
Timestamp : {timestamp}
Method    : {method}
Path      : {path}
Status    : {status}
{'-' * 40}""")
