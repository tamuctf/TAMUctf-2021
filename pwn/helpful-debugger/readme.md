# Helpful Debugger

## description

Hey, go ahead and send that binary you were looking at over me and wait for the functions to come back. You should be able to use my gdb; I configured the build for gdb to better handle go binaries.

## solution

Debug builds in Go embed a GDB extension in the binary to add features for working with Go programs, but debugging
binaries isn't something you generally want to execute arbitrary code on load so GDB restricts this a little bit. You
can list the configure args of GDB by executing `show configuration`.  If you do this, you'll notice
"--with-auto-load-safe-path=/".  If the path is the "/" GDB will disable the security protection, allowing programs to
execute arbitrary python on loading. Our initial exploit is provided in [exploit.c](exploit.c), but we found that the
thought process that [CyberErudites followed was much more enlightening](https://ctftime.org/writeup/27769). Check it
out!

