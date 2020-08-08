
# Buffer OverFlow
[![python](https://img.shields.io/badge/python-2-blue.svg)](https://www.python.org/downloads/)  [![python](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)

**some quick scripts I prepared while stuyding for the OSCP.**

## Summarized steps
- Crash the application (spiking)
- Fuzzing (find aprox number of bytes where the crash took place)
- Find offset
- EIP control
- Check for enough space on buffer
- Badchars counting
- Find return address (JMP ESP)
- Create payload

```sh

├── ( 1 ) spiking
│   ├── (1)spikeTemplateGenerator.py
│   ├── (2)autoSpiking.sh
│   └── varList
├── ( 2 ) fuzzing
│   ├── (1)fuzzing.py
│   ├── (2)OffsetFinder.py
│   └── (3)pattern_offset.sh
├── ( 3 ) EIP_controlling
│   ├── (1)EIP-RW.py
│   ├── (2)badchar.py
│   └── (3)return_Address.py
└── ( 4 ) shellcode_generate
    ├── (1)shellcode_generator.sh
    └── (2)exploit.py
    
```
## Requirments

>apt-get update
>apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
>python3 -m pip install --upgrade pip
>python3 -m pip install --upgrade pwntools

## Credits
_Thanks to these individuals for their contribution via code_ :)
#### [Anon-Exploiter](https://github.com/Anon-Exploiter/BOF)
