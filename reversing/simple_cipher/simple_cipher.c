#include <stdlib.h>
#include <stdio.h>
#include <string.h>



int main(int argc, char** argv) {
	if(argc < 2) {
		printf("./simple_cipher <plaintext>\n");
		exit(1);
	}
	int len = strlen(argv[1]);
	char* encrypted = malloc(len);

	srand(0x1337);

	for(int i = 0; i < len; i++) {
		encrypted[i] = (argv[1][(i + 15) % len] ^ rand() ^ rand()) % 256;
	}
	printf("%s", encrypted);
	free(encrypted);
}