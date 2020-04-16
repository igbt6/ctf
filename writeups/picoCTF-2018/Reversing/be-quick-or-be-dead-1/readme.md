# be-quick-or-be-dead-1

__PROBLEMS__

You find this when searching for some music, which leads you to [be-quick-or-be-dead-1](./be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f.

__HINT__

What will the key finally be?


__SOLUTION__
1. Load `be-quick-or-be-dead-1` into [cutter](www.cutter.re) 
Looking at the function: `calculate_key`

```
|   sym.calculate_key ();
|           ; var uint32_t var_4h @ rbp-0x4
|           0x00400706      push rbp
|           0x00400707      mov  rbp, rsp
|           0x0040070a      mov  dword [var_4h], 0x6ff54b3d
|       .-> 0x00400711      add  dword [var_4h], 1
|       :   0x00400715      cmp  dword [var_4h], 0xdfea967a
|       `=< 0x0040071c      jne  0x400711
|           0x0040071e      mov  eax, dword [var_4h]
|           0x00400721      pop  rbp
\           0x00400722      ret
```

We can see that this function start with `0x6ff54b3d` and decrements it until its equal to `0xdfea967a`. To speed up this function we can change the value to final value minus 1.
Patch the binary line (in cutter click right on the line, then Edit/Bytes):
```
0x00400715      cmp  dword [var_4h], 0xdfea967a
```
into:
```
0x00400715      cmp  dword [var_4h], 0x6ff54b40
```
Patching is done. Now if you'll run the binary again it will give you the flag.
Printing flag:
picoCTF{why_bother_doing_unnecessary_computation_29ff5e84}

2. Using gdb with gef:
Load binary into gdb and run:
```
gdb be-quick-or-be-dead-1
gef➤  run
Starting program: /media/sf_VM_SHARED/be-quick-or-be-dead-1 
Be Quick Or Be Dead 1
=====================

Calculating key...

Program received signal SIGALRM, Alarm clock.
Done calculating key
Printing flag:
picoCTF{why_bother_doing_unnecessary_computation_29ff5e84}
[Inferior 1 (process 31385) exited normally]
```

FLAG - `picoCTF{why_bother_doing_unnecessary_computation_29ff5e84}`
