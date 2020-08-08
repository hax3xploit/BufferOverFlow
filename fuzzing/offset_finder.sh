#!/bin/bash

echo Size of bytes to create pattern:

read pattern_size

msf-pattern_create -l $pattern_size

echo EIP data to find exact matches:

read eip_data

msf-pattern_offset -l $pattern_size -q $eip_data
