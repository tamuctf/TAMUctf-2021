# setec astronomy

## Description

After a top NSA scientist was found murdered, we searched his office and found a black box with the output still on the display. We have no idea what the code was, but we were able to find a schematic of the black box in his office and turn it into an HDL file. Figure out what the input was. You are alone on this. Remember: Trust No One.

## Discovered output

`11001010011011101100110001011000111110101010111000001100011101101111100001111010001000100110000011100100100110001110000001111101`

Encryption Scheme: ISO-8859-1

## Solution

`gigem{t0o_M4nY_s3cR3tS}`

This is helpfully a rather simple reversing challenge. Unhelpfully, there's
a lot of really finagle-y bit-level operations, so we'll use bitvectors to
make things less bad.

The only tricky bit about the code ended up being the XORs; we just use the
commutative property of XOR to get the input XOR via known values.

```rust
use bitvec::prelude::*;
use hex_literal::hex;

use encoding::all::ISO_8859_1;
use encoding::{DecoderTrap, Encoding};

static BYTES: [u8; 16] = hex!("ca6ecc58faae0c76f87a2260e498e07d");

fn main() {
    let mut phoenix = bitvec![Msb0, u8; 0; 128];
    for i in (0usize..128).step_by(8) {
        phoenix[i..(i + 8)].store(BYTES[i / 8]);
    }

    println!("phoenix: {:x?}", phoenix);

    // reverse
    phoenix.reverse(); // can only be done in place, unfortunately

    println!("reversed phoenix: {:x?}", phoenix);

    // concat
    let abbott = phoenix[0..32].to_bitvec();
    let cosmo = phoenix[32..64].to_bitvec();
    let mut ayk = phoenix[64..96].to_bitvec();
    ayk.resize(128, false);
    let earl = phoenix[96..128].to_bitvec();

    let mut temp: bool;
    // Xors
    for i in 0..32 {
        temp = ayk[i];
        ayk.set(i + 64, earl[i] ^ temp); // yuck, manual xor
    }
    for i in 0..32 {
        temp = ayk[i + 64];
        ayk.set(i + 96, cosmo[i] ^ temp);
    }
    for i in 0..32 {
        temp = ayk[i + 96];
        ayk.set(i + 32, abbott[i] ^ temp);
    }

    println!("xord ayk: {:x?}", ayk);

    // swaps, ranges are inclusive
    for i in 0..=3 {
        ayk.swap(i + 95, i + 81);
    }
    for i in 0..=7 {
        ayk.swap(i + 63, i + 120);
    }
    for i in 0..=7 {
        ayk.swap(i + 54, i + 32);
    }
    for i in 0..=3 {
        ayk.swap(i + 3, i + 19);
    }

    println!("swapped ayk: {:x?}", ayk);

    // concat 2: beyond cyberspace
    let mut in_v = ayk[0..32].to_bitvec();
    in_v.resize(128, false);
    let dave = ayk[32..64].to_bitvec();
    let red = ayk[64..96].to_bitvec();
    let king = ayk[96..128].to_bitvec();

    // Xors 2: resurrection
    for i in 0..32 {
        temp = in_v[i];
        in_v.set(i + 96, red[i] ^ temp);
    }
    for i in 0..32 {
        temp = in_v[i + 96];
        in_v.set(i + 64, dave[i] ^ temp);
    }
    for i in 0..32 {
        temp = in_v[i + 64];
        in_v.set(i + 32, king[i] ^ temp);
    }

    println!("xord in_v: {:x?}", ayk);

    let res: Vec<u8> = in_v.into();
    println!(
        "{}",
        ISO_8859_1
            .decode(&res, DecoderTrap::Strict)
            .unwrap()
            .as_str()
    );
}
```
