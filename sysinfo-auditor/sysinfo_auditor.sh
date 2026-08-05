#!/bin/bash
REPORT_DIR="./reports"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_FILE="$REPORT_DIR/sysinfo_report_$TIMESTAMP.txt"
mkdir -p "$REPORT_DIR"

log() {
    echo "$1" | tee -a "$REPORT_FILE"
}

section() {
    log ""
    log "===== $1 ====="
}

# Basic OS and kernel details
section "SYSTEM INFO"
log "Hostname       : $(hostname)"
log "OS             : $(grep PRETTY_NAME /etc/os-release 2>/dev/null | cut -d= -f2 | tr -d '\"')"
log "Kernel         : $(uname -r)"
log "Architecture   : $(uname -m)"
log "Uptime         : $(uptime -p)"

# CPU details
section "CPU INFO"
log "Model          : $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | sed 's/^ //')"
log "Cores          : $(nproc)"
log "Load Average   : $(uptime | awk -F'load average:' '{print $2}')"

# Memory usage
section "MEMORY INFO"
free -h | tee -a "$REPORT_FILE"

# Disk usage
section "DISK USAGE"
df -h --output=source,size,used,avail,pcent,target | grep -Ev 'tmpfs|udev' | tee -a "$REPORT_FILE"

# Logged-in and last logged-in users
section "USER SESSIONS"
log "Currently logged in:"
who | tee -a "$REPORT_FILE"
log ""
log "Last 5 logins:"
last -n 5 | tee -a "$REPORT_FILE"

# Listening network ports
section "LISTENING PORTS"
if command -v ss &>/dev/null; then
    ss -tulnp 2>/dev/null | tee -a "$REPORT_FILE"
else
    netstat -tulnp 2>/dev/null | tee -a "$REPORT_FILE"
fi

# Running processes sorted by CPU usage
section "TOP PROCESSES (by CPU)"
ps aux --sort=-%cpu | head -n 11 | tee -a "$REPORT_FILE"

# Installed package count
section "PACKAGE COUNT"
if command -v dpkg &>/dev/null; then
    log "Installed packages (dpkg): $(dpkg -l | grep -c '^ii')"
elif command -v rpm &>/dev/null; then
    log "Installed packages (rpm): $(rpm -qa | wc -l)"
fi

# Users with UID 0 or shell access (basic hardening check)
section "PRIVILEGED / SHELL USERS"
log "UID 0 accounts:"
awk -F: '$3 == 0 {print $1}' /etc/passwd | tee -a "$REPORT_FILE"
log ""
log "Accounts with login shells:"
grep -E '/bin/bash|/bin/sh' /etc/passwd | cut -d: -f1 | tee -a "$REPORT_FILE"

section "REPORT SAVED"
log "Full report written to: $REPORT_FILE"
