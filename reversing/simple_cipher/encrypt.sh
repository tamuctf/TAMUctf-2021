gcc simple_cipher.c -o simple_cipher;
./simple_cipher $(cat flag.txt) > flag.enc;