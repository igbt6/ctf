# fd

1. Take a look into col.c
```c
#include <stdio.h>
#include <string.h>

unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
    int* ip = (int*)p;
    int i;
    int res=0;
    for(i=0; i<5; i++){
            res += ip[i];
    }
    return res;
}

int main(int argc, char* argv[])
{
    if(argc<2){
        printf("usage : %s [passcode]\n", argv[0]);
        return 0;
    }
    if(strlen(argv[1]) != 20){
        printf("passcode length should be 20 bytes\n");
        return 0;
    }

    if(hashcode == check_password( argv[1] )){
        system("/bin/cat flag");
        return 0;
    }
    else
        printf("wrong passcode.\n");
    return 0;
}
```

2. Password mus be equal to ```hashcode = 0x21DD09EC = 568134124```.  
To cheat the check_password function we can apply EC09DD21000000000000 as an input argument. Ý!000000000000
```
$ ./col EC09DD21000000000000
```

2. Type LETMEWIN  

3. You'll get the flag:  
```
FLAG: {}
```
