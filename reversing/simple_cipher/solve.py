from ctypes import *
from string import printable 

libc = libc = CDLL("libc.so.6")

libc.srand(0x1337)

encrypted = open("flag.enc","rb").read()

flag = ['' for x in range(34)]


for i in range(34):
	idx = (i + 15) % 34
	r1 = libc.rand()
	r2 = libc.rand()
	for j in printable:
		if (ord(j) ^ r1 ^ r2) % 256 == encrypted[i]:
			flag[idx] = j

print("".join(flag))
