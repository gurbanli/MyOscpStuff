# Nmap Cheatsheet


## NMAP
##### Network Scan

> ###### Arguments

```
-sn - ping scan (disable port scan, assumes all hosts up)
-sP - ping scan (skip host discovery, only shows hosts that respond) 
-sL - scan list
```

> ###### Examples

```
Kali> nmap -sn 192.168.1.0/24
Kali> nmap -sP 192.168.1.0/24
Kali> for ip in $(cat targets.txt);do nmap -A -T4 -oN scans/nmap.$ip.txt $ip;done
```

##### Host Scan

> ###### Arguments

```
-p {1-65535} - ports
-6 - ipv6
-O - OS Detection
--osscan-limit - light os scan
--osscan-guess - aggressive os scan
-sV - version detection
--version-intensity {0-9} - light to aggressive
-sT - connect scan
-sU - UDP scan
-sS - stealth syn scan
-sN - tcp null scan
-A - OS detection + nmap scripts + traceroute + version
--script {script.nse} - load specific nmap script
--script-args={args} - pass arguments to script
```

> ###### Examples

```
Kali> nmap -p 1-65535 -sV -sS -T4 $TARGET
Kali> nmap -v -sS -A -T4 $TARGET
Kali> nmap -v -sV -O -sS -T4 $TARGET
```

##### Timing

> ###### Arguments

```
-n - never resolve dns
-R - always resolve dns
-T{0-5} - scan timing slow to fast
-F - fast scan
-r - scan ports consecutively
--version-intensity {0-9} - light to aggressive
--host-timeout {number}
--min-rate {number} --max-rate {number}
--max_retries {number}
```

##### Evasion

> ###### Arguments

```
-f [--mtu {number}] - fragment packets optionally with mtu
-D {decoy1,decoy2} - cloak with decoys
-S {ip} - spoof ip address
-g {port} - use given port number for scan
--proxies {url,url2} - use proxy through http/socks4
--data-length {number} - append random data to packets
--ip-options {options} - send packets with ip options
--ttl {number} - set ip ttl
--spoof-mac {mac} - spoof mac for scan
--bad-sum - send packets with bogus checksums
```

##### Output

> ###### Arguments

```
-v - verbose output
-oX - output xml
-oG - output greppable
--open - only show potentially open ports
--packet-trace - show all packets sent/recv
--append-output - noclobber
```
