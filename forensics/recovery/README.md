# Description

I needed to copy a flag from my home computer to the mainframe at work, so I
used a floppy drive. It looks like a few bytes in the file got corrupted, so I
deleted the file thinking it would be fine, but my friend says that's not
enough to prevent hackers from recovering the data.


## solution

1. photorec with the default options will recover a gif
2. upon examination of the gif i noticed that the height/width looked flipped so i swapped them in a hex editor.  
3. `gigem{0u7_0f_516h7_0u7_0f_m1nd}`
