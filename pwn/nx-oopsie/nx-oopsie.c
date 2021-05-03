#if _FORTIFY_SOURCE > 0
  #undef _FORTIFY_SOURCE
  #define _FORTIFY_SOURCE 0
#endif

#include <stdio.h>
#include <string.h>

void vuln() {
  char buf[64];
  printf("What's your name? ");
  fflush(stdout);
  if (fgets(buf, sizeof(buf) * 2, stdin) != NULL) {
    printf("Hi %s! Pleased to meet you.\n", buf);
  }
}

void leak() {
  printf("Psst! I heard you might need this...: %p\n", __builtin_frame_address(0));
}

int main() {
  leak();
  vuln();
}
