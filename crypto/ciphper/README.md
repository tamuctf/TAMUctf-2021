# ciphper

Background story: this code was once used on a REAL site to encrypt REAL data.
Thankfully, this code is no longer being used and has not for a long time.

A long time ago, one of the sites I was building needed to store some some
potentially sensitive data. I did not know how to use any proper encryption
techniques, so I wrote my own symmetric cipher.

The encrypted content in **output.bin** is a well-known, olde English quote in
lowercase ASCII alphabetic characters. No punctuation; just letters and spaces.

The flag is key to understanding this message.

Hint: The first 6 characters of the flag are `gigem{`.

## solution

reverse the encryption function, execute it with the key "gigem{" to get the first 6 chars of the key. from there with the knowledge from readme (old english quote, well known) and 'to\`be\`' it was pretty easy to expand the pattern out to 'to\`be\`or\`not\`to\`be\`that\`is\`the\`question'.

flag: gigem{dont~roll~your~own~crypto} true lol
