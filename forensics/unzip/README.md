# Unzip

## Description

Hey, can you unzip this for me?

## Solution

`gigem{d0esnt_looK_lik3_5t4rs_t0_M3}` yes it seems

zip2john can be used to convert a password locked zip file into a hash but it gives too much data for hashcat so I use `cut` to grab the second field delimited by colons. 

`zip2john chall.zip | cut -d ':' -f2 > zip.hash`

```text
❯ hashcat --help | grep -i pkzip
  17200 | PKZIP (Compressed)                               | Archives
  17220 | PKZIP (Compressed Multi-File)                    | Archives
  17225 | PKZIP (Mixed Multi-File)                         | Archives
  17230 | PKZIP (Mixed Multi-File Checksum-Only)           | Archives
  17210 | PKZIP (Uncompressed)                             | Archives
  20500 | PKZIP Master Key                                 | Archives
  20510 | PKZIP Master Key (6 byte optimization)           | Archives
```
At this point it depends a little bit on what sort of zip file it is, I was lazy so i just went down the line and tried until it worked.  I operated under the assumption that it'd probably be in rockyou and I was right.  
```text
❯ hashcat -a0 -m17210 zip.hash ~/Downloads/rockyou.txt
...
❯ hashcat -a0 -m17210 zip.hash ~/Downloads/rockyou.txt --show
$pkzip2$1*2*2*0*30*24*75c0f8c7*0*42*0*30*75c0*b004*e980ad8b1ffd804291d329b24794613bf3484fa6292fd97a57836440dfce9ce753a89d0ad9a8b16b042ecee459ed1274*$/pkzip2$:hunter2```
