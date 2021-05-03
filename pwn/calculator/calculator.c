#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>
#include <string.h>

int instruction_count = 0;
char** instructions;

void jit() {

	char skip_buf[8];
	printf("How many instructions would you like to skip?\n");
	fgets(skip_buf, 8, stdin);
	int skip = (float) 13 * atof(skip_buf);
	int len = instruction_count * 13 + 4;
	char* exec = (char*) mmap((void*) 0x100000,len, 0, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
	mprotect(exec, len, PROT_READ | PROT_WRITE | PROT_EXEC);
	exec[len-4] = 0x48;
	exec[len-3] = 0x89;
	exec[len-2] = 0xc8;
	exec[len-1] = 0xc3;
	for(int i = 0; i < instruction_count; i++) {
		char* instr = instructions[i];
		exec[0] = '\x48';
		exec[1] = '\xb8';
		char* ptr;
		unsigned long long parsed = strtoull(instr+4, &ptr, 10);
		memcpy(exec+2,&parsed, sizeof(unsigned long long));
		exec += 10;
		exec[0] = '\x48';
		exec[2] = '\xc1';
		if(strncmp(instr,"add",3) == 0) {
			exec[1] = '\x01';
		} else if(strncmp(instr,"sub",3) == 0) {
			exec[1] = '\x29';
		} else if(strncmp(instr,"xor",3) == 0) {
			exec[1] = '\x31';		
		}
		exec += 3;
	}
	asm("push %rbp;xor %rcx, %rcx;");
	unsigned long long val = ((unsigned long long (*)())(0x100000 + skip))();
	printf("result = %llu\n", val);
	munmap(0x100000, len);

}

void add_instruction() {
	char* instruction = malloc(30);
	memset(instruction,'\x00',30);
	fgets(instruction, 30, stdin);
	instructions[instruction_count] = instruction;
	instruction_count += 1;

	char** new_instructions = malloc((instruction_count + 1) * sizeof(char*));
	memcpy(new_instructions, instructions,(instruction_count) * sizeof(char*));
	free(instructions);
	instructions = new_instructions;
}

void print_instructions() {
	for(int i = 0; i < instruction_count; i++) {
		printf("%s",instructions[i]);
	}
}

void main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	instructions = malloc((instruction_count + 1) * sizeof(char*));

	while(1) {
		printf("1. Add instruction\n2. Print instructions\n3. Evaluate\nAction: ");
		char action_buf[8];
		fgets(action_buf, 8, stdin);
		if(strcmp(action_buf,"1\n") == 0) {
			add_instruction();
		} else if(strcmp(action_buf,"2\n") == 0) {
			print_instructions();
		} else if (strcmp(action_buf,"3\n") == 0) {
			jit();
		} else {
			printf("You didn't enter a valid command, try again! \n");
		}
	}
}
