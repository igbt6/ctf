#include <string.h>
#include <stdint.h>
#include <stdio.h>


#define CPP_STYLE


#ifdef CPP_STYLE

static void readPasswd(char* buf, size_t len)
{
    //std::cin.getline(buf, len);
    memcpy(buf, "ABCDDCBA", strlen("ABCDDCBA"));
}

struct UserData
{
    char passwd[64];
};

void UserDataCtor(struct UserData* ud)
{
    memset(ud->passwd, 0, sizeof(ud->passwd));
    readPasswd(ud->passwd, sizeof(ud->passwd));
}

void UserDataDtor(struct UserData* ud)
{
    printf("memsetting from destructor...\n");
    memset(ud->passwd, 0, sizeof(ud->passwd));
}

int main() {
    uint8_t *addr = NULL;
    {
        struct UserData ud;
        UserDataCtor(&ud);
        printf("%s\n", ud.passwd);
        addr = (uint8_t*)ud.passwd;
        UserDataDtor(&ud);
    }
    printf("%s\n", addr);
    printf("Bye!\n");
}

#else

int main() {
    uint8_t *addr = NULL;
    {
        char passwd[64];
        addr = (uint8_t*)passwd;
        memset(passwd, 0, sizeof(passwd));
        memcpy(passwd, "ABCDDCBA", strlen("ABCDDCBA"));
        printf("%s\n", passwd);
        printf("memsetting from destructor...\n");
        memset(passwd, 0, sizeof(passwd));
    }
    printf("%s\n", addr);
    printf("Bye!\n");
}

#endif