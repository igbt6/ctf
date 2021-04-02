# CTF Name – the encrypted password


## Description
https://247ctf.com/dashboard#collapse-c36


## Solution

First step is to find an entry point address of the binary as   main` is not visible in the binary (stripped symbols)
```bash
$ gdb encrypted_program
(gef) run
CTRL + C
(gef) info files
```
And you can see the entry point address:
```
Symbols from "/home/luk6xff/Projects/ctf/writeups/247CTF/reversing/the_encrypted_password/c351ac9cd9e85ab7eb921dd362b51b246a401dba/encrypted_password".
Native process:
        Using the running image of child process 39410.
        While running this, GDB does not access memory from...
Local exec file:
        `/home/luk6xff/Projects/ctf/writeups/247CTF/reversing/the_encrypted_password/c351ac9cd9e85ab7eb921dd362b51b246a401dba/encrypted_password', file type elf64-x86-64.
        Entry point: 0x555555554700
        0x0000555555554238 - 0x0000555555554254 is .interp
        0x0000555555554254 - 0x0000555555554274 is .note.ABI-tag
        0x0000555555554274 - 0x0000555555554298 is .note.gnu.build-id
        0x0000555555554298 - 0x00005555555542bc is .gnu.hash
        0x00005555555542c0 - 0x00005555555543f8 is .dynsym
        0x00005555555543f8 - 0x00005555555544b6 is .dynstr
        0x00005555555544b6 - 0x00005555555544d0 is .gnu.version
        0x00005555555544d0 - 0x0000555555554500 is .gnu.version_r
        0x0000555555554500 - 0x00005555555545d8 is .rela.dyn
        0x00005555555545d8 - 0x0000555555554668 is .rela.plt
        0x0000555555554668 - 0x000055555555467f is .init
        0x0000555555554680 - 0x00005555555546f0 is .plt
        0x00005555555546f0 - 0x00005555555546f8 is .plt.got
        0x0000555555554700 - 0x0000555555554a32 is .text
        0x0000555555554a34 - 0x0000555555554a3d is .fini
        0x0000555555554a40 - 0x0000555555554aa9 is .rodata
```
Lets put a breakpoint there:
```
(gef) b *0x555555554700 # the entry point address (.text section)
(gef) layout asm
```



## Flag
```
247CTF{}
```

### Authors
* **Lukasz** - [luk6xff](https://github.com/luk6xff)

### License
[MIT](https://choosealicense.com/licenses/mit/)