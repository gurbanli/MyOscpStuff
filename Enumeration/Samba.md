# Samba Enumeration
```
# Fingerprint version
Kali> smbclient -L //$TARGET
metasploit (smb_version)

# TODO
Kali> nmblookup -A $TARGET

# null Session
Kali> rpcclient -v "" $TARGET
Kali> smbclient -L //$TARGET
Kali> smbmap -H $TARGET

# Minimal Scan
Kali> enum4linux $TARGET

# Scan Everything
Kali> enum4linux -a $TARGET

# discover windows/samba on subnet find macs and netbios name/domain
Kali> nbtscan 192.168.1.0/24

# Enumerate users
Kali> nmap -sU -sS --script=smb-enum-users -p U:137,T:139 192.168.11.0/24
Kali> python /usr/share/doc/python-impacket-doc/examples/samrdump.py $TARGET
use auxiliary/scanner/smb/smb_lookupsid
impacket/examples/lookupsid.py user:password@$TARGET
ridenum.py $TARGET 500 50000 /path/to/wordlist.txt

# Mount Linux/Windows
Kali> mount $TARGET:/vol/share /mnt/nfs
Kali> Mount -t cifs //<server ip>/<share> <local dir> -o username=”guest”,password=””
C:\>net use Z: \\win-server\share password /user:domain\janedoe /savecred /p:no
```
