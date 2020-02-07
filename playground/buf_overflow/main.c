#include <stdio.h>
#include <string.h>

void win()
{
    printf("You win!");
}


void lose()
{
    printf("You lose!");
}

void foo(char* str)
{
    char buffer[8];
    printf("Filling buffer with: %s", str);
    strcpy(buffer, str);
}

int main (int argc, char* argv[])
{
    foo(argv[1]);
    printf("Bye!");
}