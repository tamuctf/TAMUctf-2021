#include <stdio.h>

#ifdef __aarch64__
char flag[39] = "oops, no flag for you! how unfortunate";
#else
#ifdef __riscv
char flag[39] = "gigem{just_a_touch_of_je_ne_sais_quoi}";
#else
#error Unexpected arch
#endif
#endif

void vuln() {
  char buf[53];
  gets(buf);
}

void taunt() {
  printf("Flag's here: %p\nCome and get it!\n", flag);
  fflush(stdout);
  vuln();
}

void print_flag_debug() {
  printf("Okay, so you really need the flag. Here it is: %s\n", flag);
  fflush(stdout);
}

int main() {
  taunt();
  return 0;
}
