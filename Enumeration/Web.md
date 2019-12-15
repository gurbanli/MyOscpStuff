# Web Enumeration

## Methodology

### General
```
1. Check Website source code and backend technology.
2. Find dirs (Directory Fuzzing)
3. Use nikto
4. Use nmap scripts
5. Use Burp to analyze requests
6. Use application specific techniques and tools ( For ex. wpscan, droopescan etc.)
```

### Directory Fuzzing

> ##### Gobuster
```
gobuster dir -u http://example.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 150 -x php,txt 2> /dev/null

```

> ##### Dirbuster
![Dirbuster Example](..\Images\dirbuster.png)

> ##### Dirb
```
dirb http://$TARGET /usr/share/wordlists/dirb/big.txt 
```

### Scan Tools

> ##### nikto
```
nikto -h http://example.com
```

> ##### wpscan
```
#Enumerate usernames ...
wpscan --url https://target.tld/ --enumerate u

#Do wordlist password brute force on the 'admin' username only with 50 threads ...
wpscan --url www.example.com --wordlist darkc0de.lst --username admin --threads 50

#Enumerate installed plugins ...
wpscan --url www.example.com --enumerate p

#Enumerate installed plugins ...
wpscan --url www.example.com --enumerate p

#Enumerate installed themes ...
wpscan --url www.example.com --enumerate t

```
> ##### Cadaver (WebDav test)
```
cadaver 192.168.1.101/webdav

Then sign in with username and password. The default username and passwords on xamp are:

Username: wampp

Password: xampp

Then use put and get to upload and download. With this you can of course upload a shell that gives you better access.
```

> ##### Davtest
```
davtest -url http://192.168.1.101 -directory demo_dir
```



