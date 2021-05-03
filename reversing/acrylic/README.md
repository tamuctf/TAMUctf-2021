# Acrylic

## Description
This is an easy challenge.
There is a flag that can be printed out from somewhere in this binary.
Only one problem: There's a lot of fake flags as well.

## solution

The binary has a handy get_flag() function. We could reverse this statically but why bother when you could just use GDB?

```text
gdb acrylic -ex "starti" -ex "call (char*) get_flag()" -ex "q" | grep -Po "gigem{.*}"
```