#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
int* WINNING_NUMBERS;
int* ENTERED_NUMBERS;


void seed() {
	srand(time(0) ^ 0xc35ac35f);
}

void generate_winning_numbers() {
	int r = 0;
	for(int i = 0; i < 16; i++) {
		r = rand();
		*(WINNING_NUMBERS + i) = r;
	}
}

void print_winning_numbers() {
	for(int i = 0; i < 16; i++) {
		printf("%X ", *(WINNING_NUMBERS + i));
	}
	printf("\n");
}

void print_entered_numbers() {
	for(int i = 0; i < 16; i++) {
		printf("%X ", *(ENTERED_NUMBERS + i));
	}
	printf("\n");
}


void cheat() {
	memcpy(ENTERED_NUMBERS, WINNING_NUMBERS, 64);
}

void __attribute__ ((noinline)) protect(int address) {
	mprotect(address, 64, PROT_READ | PROT_WRITE);
}

void query_numbers() {
	for(int i = 0; i < 16; i++) {
		printf("Enter number %d: ", i+1);
		scanf("%x",ENTERED_NUMBERS + i);
		fgetc(stdin); // consume newline
	}
}

void check_numbers() {
	printf("You entered: ");
	print_entered_numbers();
	printf("Winning numbers: ");
	print_winning_numbers();
	for(int i = 0; i < 16; i++) {
		if(*(ENTERED_NUMBERS + i) != *(WINNING_NUMBERS + i)) {
			printf("You didn't win, feel free to try again!\n");
			exit(1);
		}
	}
	printf("You win!  Congratulations! Winning isn't enough to get you the flag though. \n");
	exit(0);
}

void __attribute__ ((noinline)) ask_name() {
	char name[64];
	gets(name);
	printf("Hi, %s!\n", name);
}

int menu() {
	while(1) {
		printf("1. Enter Numbers\n2. Check Numbers\n3. Enter Name\nAction: ");
		char action_buf[8];
		fgets(action_buf, 7, stdin);
		if(strcmp(action_buf,"1\n") == 0) {
			query_numbers();
		} else if(strcmp(action_buf,"2\n") == 0) {
			check_numbers();
		} else if (strcmp(action_buf,"3\n") == 0) {
			ask_name();
		} else if (strcmp(action_buf,"1337\n") == 0) {
			cheat();
		} else {
			printf("You didn't enter a valid command, try again! \n");
		}
	}

}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	WINNING_NUMBERS = mmap(0x10000000,64, 0, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0); // 16 ints
	ENTERED_NUMBERS = mmap(0x20000000,64, 0, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0); // 16 ints
	protect(WINNING_NUMBERS);
	protect(ENTERED_NUMBERS);
	seed();
	generate_winning_numbers();
	menu();
}