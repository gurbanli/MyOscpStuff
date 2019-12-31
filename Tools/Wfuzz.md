# WFUZZ Tool Cheatsheet

>##### Common paths
```
$ wfuzz -w wordlist/general/common.txt http://testphp.vulnweb.com/FUZZ
```

>##### Fuzzing Parameters In URLs
```
$ wfuzz -z range,0-10 --hl 97 http://testphp.vulnweb.com/listproducts.php?cat=FUZZ
```

>##### Hiding
```
--hc/hl/hw/hh N[,N]+        : Hide responses with the specified code/lines/words/chars (Use BBB for taking values from baseline)
```

>##### POST Data
```
wfuzz -z file,wordlist/others/common_pass.txt -d "uname=FUZZ&pass=FUZZ"  --hc 302 http://testphp.vulnweb.com/userinfo.php
```

>##### Cookies
```
$ wfuzz -z file,wordlist/general/common.txt -b cookie=value1 -b cookie2=value2 http://testphp.vulnweb.com/FUZZ
```

>##### Fuzzing Custom Headers
```
$ wfuzz -z file,wordlist/general/common.txt -H "myheader: headervalue" -H "myheader2: headervalue2" http://testphp.vulnweb.com/FUZZ
```
>##### User Agent
```
$ wfuzz -z file,wordlist/general/common.txt -H "myheader: headervalue" -H "User-Agent: Googlebot-News" http://testphp.vulnweb.com/FUZZ
```
>##### Fuzzing HTTP Verbs
```
wfuzz -z list,GET-HEAD-POST-TRACE-OPTIONS -X FUZZ http://testphp.vulnweb.com/
```

>##### HTTP PROXY
```
$ wfuzz -z file,wordlist/general/common.txt -p localhost:8080 http://testphp.vulnweb.com/FUZZ
```

>##### Basic Authentication
```
wfuzz -z list,nonvalid-httpwatch --basic FUZZ:FUZZ https://www.httpwatch.com/httpgallery/authentication/authenticatedimage/default.aspx
```

>##### Range Payload
```
wfuzz -c -z range,1-65365 --hl=2 http://10.10.10.55:60000/url.php?path=http://localhost:FUZZ
```
