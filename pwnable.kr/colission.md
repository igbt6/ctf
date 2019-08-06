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
To cheat the check_password function we cannot apply `\xEC \x09 \xDD \x21 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00`  as an input argument because there is used `strlen` function which will stop counting at null(0x00) value.  
So the goal was to subtract 0x01010104 from 0x21DD09EC and divide the result by 4.
```
0x21DD09EC - 0x01010104 = 0x20DC08E8
0x20DC08E8 / 4 = 0x0837023A
So:  
0x21DD09EC = 0x01010104 + 4 * 0x0837023A
```
The fianl input string will be:  
`\x3A \x02 \x37 \x08 \x3A \x02 \x37 \x08 \x3A \x02 \x37 \x08 \x3A \x02 \x37 \x08 \x04 \x01 \x01 \x01`


3. Run:
```
$ ./col `echo -e -n "\x3A\x02\x37\x08\x3A\x02\x37\x08\x3A\x02\x37\x08\x3A\x02\x37\x08\x04\x01\x01\x01"`
```

3. You'll get the flag:  
```
FLAG: {daddy! I just managed to create a hash collision :)}
```
