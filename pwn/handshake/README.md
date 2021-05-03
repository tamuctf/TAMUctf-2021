# handshake

## Description

Attack this binary and get the flag!

## Solution

All we need to do is invoke "win", which we'll do using the all-too-simple `vuln` function and getting a [ROP](https://en.wikipedia.org/wiki/Return-oriented_programming).

Ghidra tells us that the position of the buffer is -0x2c, so we use that for our length calculation. Then struct.pack up
a return address for win.

Solution script is provided in solution.py.
