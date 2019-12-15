# SNMP Enumeration
```
# Overview
Default Community Names:
public, private, cisco, manager

Enumerate MIB:
1.3.6.1.2.1.25.1.6.0 System Processes
1.3.6.1.2.1.25.4.2.1.2 Running Programs
1.3.6.1.2.1.25.4.2.1.4 Processes Path
1.3.6.1.2.1.25.2.3.1.4 Storage Units
1.3.6.1.2.1.25.6.3.1.2 Software Name
1.3.6.1.4.1.77.1.2.25 User Accounts
1.3.6.1.2.1.6.13.1.3 TCP Local Ports

# Enmerate users from SNMP
Kali> snmpwalk public -v1 192.168.X.XXX 1 | grep 77.1.2.25 | cut -d” “ -f4
Kali> python /usr/share/doc/python-impacket-doc/examples/samrdump.py SNMP $TARGET

# Search SNMP with nmap
Kali> nmap -sT -p 161 192.168.1.0/24 -oG snmp_results.txt

# Examples
Kali> snmpwalk -c public -v1 $TARGET 1.3.6.1.2.1.25.4.2.1.2
Kali> onesixtyone -c community -I $TARGET
Kali> snmpcheck -t $TARGET
Kali> snmpenum -t $TARGET

# Version3
Kali> nmap -sV -p 161 --script=snmp-info 192.168.1.0/24

# Wordlists
/usr/share/metasploit-framework/data/wordlists/snmp_default_pass.txt
```
