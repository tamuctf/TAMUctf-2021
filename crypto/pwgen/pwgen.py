import z3
from pwn import *
import re
import sys

def guess_next_number(known):
    n_nums = len(known)
    
    states = {f'state_{i}': z3.BitVec(f'state_{i}', 32) for i in range(1, n_nums + 2)}
    next_number = z3.BitVec('next_number', 32)
    
    s = z3.Solver()

    a = 1103515245
    c = 12345
    m = 16
    for i in range(2, n_nums + 2):
        s.add(states[f'state_{i}'] == states[f'state_{i - 1}'] * a + c)

    for i in range(1, n_nums + 1):
        s.add(z3.URem((states[f'state_{i}'] >> m) & 0x7fff, (0x7f - 0x21)) + 0x21 == known[i - 1])
        
    s.add(next_number == z3.URem((states[f'state_{n_nums + 1}'] >> m) & 0x7fff,  (0x7f - 0x21)) + 0x21)
    
    if s.check() == z3.sat:
        return s.model()[next_number]
    else:
        print(f"Couldn't satisfy constraints for {known}")
        sys.exit(1)
    


known = "ElxFr9)F"
correct = "xV!;28vj"


known_nums = [ord(x) for x in known]


password = ""

for i in range(8):

    next_num = guess_next_number(known_nums)
    print(f"guessed {chr(int(str(next_num)))}, actual {correct[i]}")
    if chr(int(str(next_num))) != correct[i]:
        print("failed :(")
        sys.exit(0)
    password += chr(int(str(next_num)))
    known_nums.append(next_num)


print("password = ", password)
p = remote("localhost",4662)
p.sendline(password)
print(re.search("(gigem{.*})", p.recvall().decode()).group(1))
