#!/bin/sh

banner="-------------------------------"

###########################
ip="192.168.10.12"
port=9999
###########################

for spkFiles in $(ls *.spk); do
        echo -n "\n\n\n$banner\n$ip\n$port\n\n$spkFiles\n$banner\n\n\n\n\n\n"
        generic_send_tcp $ip $port $spkFiles 0 0
        echo -n "\n\n\n\n\n\n$spkFiles Completed!\n\n\n\n"
done
