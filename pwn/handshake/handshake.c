#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void win() {
	FILE* flag = fopen("flag.txt", "r");
	char buf[64];
	if(flag == NULL) {
		strcpy(buf,"Flag file is missing, run that exploit again on the server!");
	} else {
		fgets(buf, 64, flag);
	}
	printf("Correct! %s\n", buf);
	fflush(0);
}

void lose() {
	printf("That isn't correct!  You aren't supposed to be here. \n");
}

void vuln() {
	printf("Whats the secret handshake? ");
	fflush(0);
	char buf[32];
	gets(buf);
	printf("\n");
}

void main() {
	vuln();
	lose();
}