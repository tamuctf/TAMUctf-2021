# Ring Of Fire

## Description

For none and none, there is always none

For none but one, there can be only one

For one and one, there is nothing but none

## Postscript

Sometimes I just sing to myself

```
Love is a burning thing
And it makes a firery ring
Bound by wild desire
I fell in to a ring of fire
```

## Solution

`gigem{x0r_is_c0mmuT4T1ve}`

```John R. Cash (born J. R. Cash; February 26, 1932 – September 12, 2003) was an American singer, songwriter, musician, and actor. Much of Cash's music contained themes of sorrow, moral tribulation, and redemption, especially in the later stages of his career. gigem{x0r_is_c0mmuT4T1ve}. He was known for his deep, calm bass-baritone voice, the distinctive sound of his Tennessee Three backing band characterized by train-like chugging guitar rhythms, a rebelliousness coupled with an increasingly somber and humble demeanor, free prison concerts, and a trademark all-black stage wardrobe which earned him the nickname "The Man in Black".```

Using the good ol' generic xor solver:

```rust
use std::env::args;
use std::error::Error;
use std::io::{Read, Write};

fn main() -> Result<(), Box<dyn Error>> {
    let mut args = args();
    args.next();
    let key = args.next().unwrap().as_bytes().to_vec();
    let stdout = std::io::stdout();
    let mut lout = stdout.lock();
    for res in std::io::stdin()
        .lock()
        .bytes()
        .zip(key.iter().cycle())
        .map(|(b, k)| b.unwrap() ^ k)
    {
        lout.write_all(&[res]).unwrap();
    }
    drop(lout);
    println!();
    Ok(())
}
```

And some one-liner madness:

```bash
for i in $(cat codeFile | sed 's/.\{8\}/&\n/g'); do printf "%.2x\n" $(bash -c 'echo $((2#'"$i"'))'); done | xxd -r -p | generic-xor-solver "<lyrics to ring of fire>"
```

Aaaand the lyrics: https://www.google.com/search?q=ring+of+fire+lyrics
