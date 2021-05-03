# pwgen

We're trying to figure out the current password of \<REDACTED\>.  We have reason to believe that they generated a set of passwords at the same time using a custom password generation program and that their previous password was `ElxFr9)F`.  Can you figure out their current password?  

`nc challenges.tamuctf.com 4662`

[zipped source of pwgen]  


## solution
`gigem{cryp706r4ph1c4lly_1n53cur3_prn65_DC6F9B}`

Looking at the rand function from the source, we can see that this is a [linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) which is trivially reversible when we have access to the raw outputs:
```rust
impl Random {
    fn rand(&mut self) -> i32 {
        let a = 1103515245;
        let c = 12345;
        self.seed = self.seed.wrapping_mul(a) + c;
        (self.seed >> 16) & 0x7fff
    }
}
```

Unfortunately, we don't have the raw outputs; the outputs are instead passed through a modulo or two to get it into a nice format for a password:
```rust
fn generate_password(rand: &mut Random, n: i32) -> String {
    (0..n)
        .map(|_| (rand.rand() % (0x7f - 0x21) + 0x21) as u8 as char)
        .collect::<String>()
}
```

Because I don't want to work this out by hand or write a solving script, we'll use z3:
```python
from z3 import *

password = 'ElxFr9)F'

s = Solver()

a = BitVecVal(1103515245, 32)
c = BitVecVal(12345, 32)

base_seed = BitVec('s0', 32)
seed = base_seed

def rand():  # see the rand definition above
  global seed
  seed = (seed * a) + c
  res = (seed >> BitVecVal(16, 32)) & BitVecVal(0x7fff, 32)
  return res

# we know the values for the first password, so we can assert them to be equal to characters in password
for i in range(0, len(password)):  # see the generate_password function above
  res = rand()
  pc = BitVec('c' + str(i), 8)
  s.add(pc == Extract(7, 0, res % (0x7f - 0x21) + 0x21), pc == BitVecVal(ord(password[i]), 8))

generated = []

# we don't know the values in the generated password, but we can store these for later extraction
for i in range(len(password), len(password) * 2):
  res = rand()
  pc = BitVec('c' + str(i), 8)
  generated.append(pc)
  s.add(pc == Extract(7, 0, res % (0x7f - 0x21) + 0x21))

s.check()
model = s.model()

# extract the characters from the z3 model
generated = [chr(model[c].as_long()) for c in generated]
print(''.join(generated))
```

After 10 seconds on my clunky laptop, this outputs: `xV!;28vj`

Logging in with `nc 104.155.170.123 4662`:
```
$ nc 104.155.170.123 4662
What's the password?
xV!;28vj
gigem{cryp706r4ph1c4lly_1n53cur3_prn65_DC6F9B}
```

z3 is really so satisfying ;)
