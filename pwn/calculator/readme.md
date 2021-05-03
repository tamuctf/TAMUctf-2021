# calculator

Hey, I made this JIT compiled calculator!  Could you take a look at it and see if it's vulnerable?  I left a flag on the server as a reward.  

`nc challenges.tamuctf.com 6319`

## brief dev notes

It's a JIT spray.  The idea is that you can jump into the middle of an instruction so you can encode shellcode as a
parameter to some instruction and then jump into that.  

## solution

An internal writeup was never written properly (reviewer just left dev notes, as seen above). As such, we asked the
competitor `volticks` for permission to link [their writeup](https://github.com/volticks/CTF-Writeups/blob/main/TamuCTF%202021/Calculator/Calculator.md)
instead, as it was far better than what we could drum up during finals week!
