#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

void vuln(char* main_buf) {
	printf("What's the flag? ");
	char buf[32];
	fflush(0);
	gets(buf);
	memcpy(main_buf, buf, 32);
	printf("\n");
}

void main() {
	setvbuf(stdout, 0, 2, 0);
	int lib = open("flag_check.o",O_RDONLY);
	void* lib_flagcheck = mmap(0x10000000, 2048, PROT_EXEC | PROT_READ, MAP_PRIVATE, lib, 0);
	char buf[32];
	vuln(&buf);


	int len = strlen(buf);
	if(buf[len-1] == '\n') {
		buf[len-1] = '\0';
		len = len - 1;
	}
	int (*flag_check)(char*, int) = (0x10000000 + 0x40); 
	if ((*flag_check)(&buf, len) == 1) {
		printf("Correct!\n");
	} else {
		printf("That's wrong :(\n");
	}
}
