# quackme

__PROBLEMS__

Can you deal with the Duck Web? Get us the flag from this [program](./main). You can also find the program in /problems/quackme_2_45804bbb593f90c3b4cefabe60c1c4e2.

__HINT__

Objdump or something similar is probably a good place to start.


__SOLUTION__
1. Load `main` into [cutter](www.cutter.re) and look at the function" `do_magic`

```asm
211: sym.do_magic ();
; var uint32_t var_1dh @ ebp-0x1d
; var uint32_t var_1ch @ ebp-0x1c
; var int32_t var_18h @ ebp-0x18
; var char *s @ ebp-0x14
; var size_t size @ ebp-0x10
; var void *var_ch @ ebp-0xc
0x08048642      push    ebp
0x08048643      mov     ebp, esp
0x08048645      sub     esp, 0x28
0x08048648      call    read_input ; sym.read_input
0x0804864d      mov     dword [s], eax
0x08048650      sub     esp, 0xc
0x08048653      push    dword [s]  ; const char *s
0x08048656      call    strlen     ; sym.imp.strlen ; size_t strlen(const char *s)
0x0804865b      add     esp, 0x10
0x0804865e      mov     dword [size], eax
0x08048661      mov     eax, dword [size]
0x08048664      add     eax, 1
0x08048667      sub     esp, 0xc
0x0804866a      push    eax        ; size_t size
0x0804866b      call    malloc     ; sym.imp.malloc ;  void *malloc(size_t size)
0x08048670      add     esp, 0x10
0x08048673      mov     dword [var_ch], eax
0x08048676      cmp     dword [var_ch], 0
0x0804867a      jne     0x8048696
0x0804867c      sub     esp, 0xc
0x0804867f      push    str.malloc___returned_NULL._Out_of_Memory ; 0x8048884 ; const char *s
0x08048684      call    puts       ; sym.imp.puts ; int puts(const char *s)
0x08048689      add     esp, 0x10
0x0804868c      sub     esp, 0xc
0x0804868f      push    0xffffffffffffffff ; int status
0x08048691      call    exit       ; sym.imp.exit ; void exit(int status)
0x08048696      mov     eax, dword [size]
0x08048699      add     eax, 1
0x0804869c      sub     esp, 4
0x0804869f      push    eax        ; size_t n
0x080486a0      push    0          ; int c
0x080486a2      push    dword [var_ch] ; void *s
0x080486a5      call    memset     ; sym.imp.memset ; void *memset(void *s, int c, size_t n)
0x080486aa      add     esp, 0x10
0x080486ad      mov     dword [var_1ch], 0
0x080486b4      mov     dword [var_18h], 0
0x080486bb      jmp     0x804870b
0x080486bd      mov     eax, dword [var_18h]
0x080486c0      add     eax, sekrutBuffer ; 0x8048858
0x080486c5      movzx   ecx, byte [eax]
0x080486c8      mov     edx, dword [var_18h]
0x080486cb      mov     eax, dword [s]
0x080486ce      add     eax, edx
0x080486d0      movzx   eax, byte [eax]
0x080486d3      xor     eax, ecx
0x080486d5      mov     byte [var_1dh], al
0x080486d8      mov     edx, dword [greetingMessage] ; 0x804a038
0x080486de      mov     eax, dword [var_18h]
0x080486e1      add     eax, edx
0x080486e3      movzx   eax, byte [eax]
0x080486e6      cmp     al, byte [var_1dh]
0x080486e9      jne     0x80486ef
0x080486eb      add     dword [var_1ch], 1
0x080486ef      cmp     dword [var_1ch], 0x19
0x080486f3      jne     0x8048707
0x080486f5      sub     esp, 0xc
0x080486f8      push    str.You_are_winner ; 0x80488ab ; const char *s
0x080486fd      call    puts       ; sym.imp.puts ; int puts(const char *s)
0x08048702      add     esp, 0x10
0x08048705      jmp     0x8048713
0x08048707      add     dword [var_18h], 1
0x0804870b      mov     eax, dword [var_18h]
0x0804870e      cmp     eax, dword [size]
0x08048711      jl      0x80486bd
0x08048713      leave
0x08048714      ret
```

The most interesting part of the function is shown below:
```asm
...
0x080486bd      mov     eax, dword [var_18h]
0x080486c0      add     eax, sekrutBuffer ; 0x8048858
0x080486c5      movzx   ecx, byte [eax]
0x080486c8      mov     edx, dword [var_18h]
0x080486cb      mov     eax, dword [s]
0x080486ce      add     eax, edx
0x080486d0      movzx   eax, byte [eax]
0x080486d3      xor     eax, ecx
0x080486d5      mov     byte [var_1dh], al
0x080486d8      mov     edx, dword [greetingMessage] ; 0x804a038
0x080486de      mov     eax, dword [var_18h]
0x080486e1      add     eax, edx
0x080486e3      movzx   eax, byte [eax]
0x080486e6      cmp     al, byte [var_1dh]
0x080486e9      jne     0x80486ef
0x080486eb      add     dword [var_1ch], 1
0x080486ef      cmp     dword [var_1ch], 0x19
0x080486f3      jne     0x8048707
0x080486f5      sub     esp, 0xc
0x080486f8      push    str.You_are_winner ; 0x80488ab ; const char *s
0x080486fd      call    puts       ; sym.imp.puts ; int puts(const char *s)
0x08048702      add     esp, 0x10
0x08048705      jmp     0x8048713
0x08048707      add     dword [var_18h], 1
0x0804870b      mov     eax, dword [var_18h]
0x0804870e      cmp     eax, dword [size]
0x08048711      jl      0x80486bd
0x08048713      leave
0x08048714      ret
...
```

I have tried to write a bit of pseudo code to shown you how it works:
```c
char *password = read_input_msg[]; // Msg read from input
...
size_t var_18h = 0; // counter
size_t var_1ch = 0; // valid chars counter
while (true)
{
    char var_1dh = sekrutBuffer[var_18h] ^ password[var_18h]
    if (var_1dh == greetingMessage[var_18h])
    {
        var_1ch = var_1ch + 1;
    }

    if (var_1ch >= 25)
    {
        printf("You_are_winner");
        return;
    }

    var_18h++;
    if (var_18h >= strlen(s))
    {
        return;
    }
}
...
```
The simple xor problem, we can easily detect what `password` shall be, by an inversion of `xor` operation: `password = sekrutBuffer ^ greetingMessage`.

I have done it in [solver.py script](./solver.py);
The password input i got is: `picoCTF{qu4ckm3_35246994}` which is as well our final flag.

After applying the flag we get:
```
$ luk6xff@pico-2018-shell:/problems/quackme_2_45804bbb593f90c3b4cefabe60c1c4e2$ ./main
You have now entered the Duck Web, and you're in for a honkin' good time.
Can you figure out my trick?
picoCTF{qu4ckm3_35246994}
You are winner!
That's all folks.
```

FLAG - `picoCTF{qu4ckm3_35246994}`
