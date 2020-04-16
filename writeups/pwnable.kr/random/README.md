# random

1. Login into with pass `guest`:
```
ssh random@pwnable.kr -p2222  
```

2. Quick look at the source code of random.c
Line: ``` random = rand();	// random value! ``` always gives the same result.
```
gef➤  break *main+21
     0x4005fb <main+7>         adc    BYTE PTR [rax+0x0], bh
     0x400601 <main+13>        call   0x400500 <rand@plt>
     0x400606 <main+18>        mov    DWORD PTR [rbp-0x4], eax
 →   0x400609 <main+21>        mov    DWORD PTR [rbp-0x8], 0x0
     0x400610 <main+28>        mov    eax, 0x400760
     0x400615 <main+33>        lea    rdx, [rbp-0x8]
     0x400619 <main+37>        mov    rsi, rdx
     0x40061c <main+40>        mov    rdi, rax
     0x40061f <main+43>        mov    eax, 0x0

gef➤  x/d $rbp-0x4
0x7ffd70a3b40c: 1804289383
gef➤  x/x $rbp-0x4
0x7ffd70a3b40c: 0x6b8b4567
```

3. How i found the `key`:

I have `random = 0x6b8b4567`

What `key` must be equal to to make `(key ^ random) == 0xdeadbeef` comparison true ?
As the XOR operation is reversible:
```
a = b XOR c
b = a XOR c
```
I did the following

```
$ python -c "print(hex(0xdeadbeef ^ 0x6b8b4567))" > /tmp/payload_hex
$ python -c "print(0xdeadbeef ^ 0x6b8b4567)" > /tmp/payload
CHECK:
$ python -c "print(hex(0xb526fb88 ^ 0x6b8b4567))"

$ ./random < /tmp/payload
```



I got get the flag:  
```
FLAG: {Mommy, I thought libc random is unpredictable...}
```
