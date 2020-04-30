# assembly-2

__PROBLEM__

What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell.picoctf.com/static/cc3fee38d52ce2d65e9362de95417d8b/loop_asm_rev.S) located in the directory at /problems/assembly-2_2_39150748a2771e0f5d2cbb14351ba582.

__HINT__

assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

__SOLUTION__


```
wget https://2018shell.picoctf.com/static/cc3fee38d52ce2d65e9362de95417d8b/loop_asm_rev.S --no-check-certificate

sudo apt-get install gcc-multilib

```

asm2(0x4,0x2d)

Let's replace some values:

param1 = *(ebp+0x8) = 0x4
param2 = *(ebp+0xc) = 0x2d

loc_var1 = *(ebp-0x4)
loc_var2 = *(ebp-0x8)

```asm
asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [param2]          ; eax = param2
	mov 	DWORD PTR [loc_var1],eax        ; loc_var1 = param2 (loc_var1 = 0x2d)
	mov    	eax,DWORD PTR [param1]          ; eax = param1
	mov	    DWORD PTR [loc_var2],eax        ; loc_var2 = param1 (loc_var2 = 0x4)
	jmp    	part_b
part_a:
	add    	DWORD PTR [loc_var1],0x1        ; loc_var1 += 1 (loc_var1 = 0x2e)
	add	    DWORD PTR [param1],0x64         ; param1 += 0x64 (param1 = 0x68)
part_b:
	cmp    	DWORD PTR [param1],0x1d89       ; if (param1 <= 0x1d89) jmp to part_a
	jle    	part_a
	mov    	eax,DWORD PTR [loc_var1]        ; eax = *loc_var1 (eax = 0x2e)
	mov	    esp,ebp
	pop	    ebp
	ret
```


* First way to solve the problem with compiling the code:
Run `make`
```
(venv) luk6xff@luk6xff:~/picoCTF-2018/Reversing/assembly-2$ make
gcc -m32 -c loop_asm_rev.S
gcc -m32 -c solver.c
solver.c: In function ‘main’:
solver.c:4:28: warning: implicit declaration of function ‘asm2’ [-Wimplicit-function-declaration]
     printf("Flag: 0x%x\n", asm2(0x4, 0x2d));
                            ^~~~
gcc -m32 -o solver loop_asm_rev.o solver.o
./solver
Flag: 0x79
```

* Second way with python solver
```
python3 solver.py
Flag: 0x79
```

FLAG - `0x79`
