#include <cstring>
#include <cstdint>
#include <cstdio>

static void readPasswd(char* buf, size_t len)
{
    //std::cin.getline(buf, len);
    memcpy(buf, "ABCDDCBA", strlen("ABCDDCBA"));
}


struct UserData
{
    char passwd[64];
    UserData()
    {
        memset(passwd, 0, sizeof(passwd));
        readPasswd(passwd, sizeof(passwd));
    }

    ~UserData()
    {
        printf("memsetting from destructor...\n");
        memset(passwd, 0, sizeof(passwd));
    }
};

int main() {
    uint8_t *addr = NULL;
    {
        UserData ud;
        printf("%s\n", ud.passwd);
        addr = (uint8_t*)ud.passwd;
    }
    printf("%s\n", addr);
    printf("Bye!\n");
}
