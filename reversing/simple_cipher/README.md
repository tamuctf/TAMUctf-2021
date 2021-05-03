# simple_cipher

## Description

We have a flag encrypted using this program.  Can you figure out what it is?  

## Solution

`gigem{d0n7_wr173_y0ur_0wn_c1ph3r5}`

1. Open in Ghidra.
2. Browse to main using the function search.
3. Retype, rename variables for clarity:

Original:

![figurë](https://media.github.tamu.edu/user/4480/files/29480880-1ff4-11eb-9089-5251fd7dc468)

Post:

![figurë](https://media.github.tamu.edu/user/4480/files/54325c80-1ff4-11eb-94c2-4027a19f16c2)

4. Select > Function, File > Export Program > C/C++ > Selection Only (this tacks in all the types we need to compile)
5. Add stdio.h, stdlib.h, and string.h headers
6. Swap pos offset:

![figurë](https://media.github.tamu.edu/user/4480/files/eaff1900-1ff4-11eb-8bf0-58b8367bf3a9)

7. Compile and run:

![figurë](https://media.github.tamu.edu/user/4480/files/2863a680-1ff5-11eb-8acd-f99b9663e236)

8. Profit
