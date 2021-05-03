#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    volatile int modified;
    char buffer[64];

    modified = 0;

    fgets(buffer, 80, stdin);

    if(modified == 0x08406688) {
        FILE* flag = fopen("flag.txt", "r");
        char buf[64];
        if(flag == NULL) {
            strcpy(buf,"Flag file is missing, run that exploit again on the server!");
        } else {
            fgets(buf, 64, flag);
        }
        printf("flag: %s\n",buf);
    } else {
        printf("Try again, you got 0x%08x\n", modified);
    }
    return 0;
}

