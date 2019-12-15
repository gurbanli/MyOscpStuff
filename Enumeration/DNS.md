# DNS Enumeration

> ##### Zone Transfer
```
Kali> host -l megacorpon.com ns1.megacorpone.com
Kali> dnsrecon -d domain.com -t axfr @ns1.domain.com
Kali> dnsenum domain.com
Kali> nslookup -> set type=any -> ls -d domain.com
```
> ##### Enumerate subdomains
```
Kali> for sub in $(cat subdomains.txt);do host $sub.domain.com|grep "has.address";done
Kali> dnsrecon -d $TARGET -D wordlist.txt -t std --xml output.xml
Kali> gobuster dns -d domain.com -w wordlist.txt -r 10.10.10.169
```
