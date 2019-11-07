#include <string.h>
#include <stdint.h>
#include <stdio.h>

int main() {
    char passwd[64];
    uint8_t *addr = (uint8_t*)passwd;
    memset(passwd, 0, sizeof(passwd));
    memcpy(passwd, "ABCDDCBA", strlen("ABCDDCBA"));
    printf("%s\n", passwd);
    printf("memsetting from destructor...\n");
    memset(passwd, 0, sizeof(passwd));
    printf("%s\n", addr);
    printf("Bye!\n");
}