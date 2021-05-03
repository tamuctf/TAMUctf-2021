# Basic RSA

## Description
To: Dr. Rivest
CC: Dr. Shamir

We found this code and these numbers.
Mean anything to you?

Sincerely
- Dr. Adleman

## solution

<details>
  <summary>Thinking Process</summary>
  
  Starting from nothing, I see three names with some weird numbers and specific variable names.
I also see the gigem{} flag format with spaced blocks of numbers inside of it.

If I google Rivest, I find information about Ron Rivest, the cryptographer and co-inventor of RSA. 

If I google "N e encryption" I find a page on the RSA algorithm.

From the names of people and variable names, I can assume that the RSA encyption algorithm is involved.

I find a basic guide on generating a key and decryption: https://www.di-mgt.com.au/rsa_alg.html#decryption

I have n but not d, and I need to compute m  = c^d mod n, then get the plaintext using m.

To get d, I need p and q.

I use an online tool, `factorize 15241604814814604814814604814814609737853` 
https://www.wolframalpha.com/input/?i=factorize+15241604814814604814814604814814609737853

Following the given examples, I tried to implement decryption using a guessed d, but didn't make progress (see commented out code). I got blocks of numbers out of range to be converted into UTF or ASCII, so I assumed that my d was incorrect.

I searched more and found that RSA is not "RSA". RSA with no padding or randomness ("Textbook RSA") isn't very good encrpytion, and the actual standard specifies padding and randomness. Since padding and randomness wasn't specified in the message, I looked elsewhere. I found a stackoverflow post which suggested a brute force attack of encrypting all possible values

---

You can run an exhaustive search on the possible plaintexts. No padding means no randomness; encryption is deterministic, so you can "try" plaintexts and see if one matches the encrypted value when encrypted.

https://crypto.stackexchange.com/questions/6770/cracking-an-rsa-with-no-padding-and-very-small-e

---

A more academic source
"Since textbook RSA is deterministic, if the messagemis chosenfrom a small list of possible values, then it is possible to determinemfrom the ciphertextc=[memodN] by trying each value ofm,1mL."
http://cs.wellesley.edu/~cs310/lectures/26_rsa_slides_handouts.pdf

I changed my approach to find the equivalent input to the encryption function that produces the same output as the current cipher block, then add that input to the output.

---

</details>

<details>
  <summary>Python Solution</summary>
  
  ```python
# requires python >= 3.9
import string

N = 2095975199372471
e = 5449
input_string = "gigem{ 875597732337885 1079270043421597 616489707580218 2010079518477891 1620280754358135 616660320758264 86492804386481 171830236437002 1500250422231406 234060757406619 1461569132566245 897825842938043 2010079518477891 234060757406619 1620280754358135 2010079518477891 966944159095310 1669094464917286 1532683993596672 171830236437002 1461569132566245 2010079518477891 221195854354967 1500250422231406 234060757406619 355168739080744 616660320758264 1620280754358135 }"
# provided information

prepend = "gigem{ "
postpend = " }"

# from https://www.wolframalpha.com/input/?i=factorize+15241604814814604814814604814814609737853
p = 123457
q = 123456789123456789123456789123456829

phi = (p-1)*(q-1)
assert (e>1 & e < phi), "e is out of range"

#find rsa D using multiplicative inverse
d = pow(e, -1, phi)

# split input text
input_as_list = input_string.removeprefix(prepend).removesuffix(postpend).split(" ")


#out_num = []
#for string_block in input_as_list: #decrypt each 'block'
#    cipher_block = int(string_block)
#    assert str(cipher_block) == string_block, "String did not become equiv base 10 int"
#    msg_block = pow(cipher_block, d, N) #apply to each block
#    out_num.append(msg_block)

def cipher(n: int, e: int, plaintext: str) -> int:
    # given public key (n,e), cipher the plaintext str into an integer ciphertext
    # https://www.di-mgt.com.au/rsa_alg.html
    # convert plaintext to an int
    assert len(plaintext) == 1
    m = ord(plaintext)
    assert (1 < m) & (m < n)
    ciphertext = pow(m, e) % n
    return ciphertext

out_str = ""
for string_block in input_as_list: # decrypt each 'block'
    cipher_block = int(string_block)
    for char in string.printable:
        if cipher_block == cipher(N,e,char):
            out_str+=char
            break

print(prepend+out_str+postpend)
```
  
</details>
