# leg

1. Download files and login into with pass `guest`:
```
$ wget http://pwnable.kr/bin/leg.c
$ wget http://pwnable.kr/bin/leg.asm
$ ssh leg@pwnable.kr -p2222
```

2. After logging into system we see that quemu starts on the machine.
Looking at cpu architecture:
``` 
$ cat /proc/cpuinfo
processor       : 0
model name      : ARM926EJ-S rev 5 (v5l)
BogoMIPS        : 428.44
Features        : swp half thumb fastmult vfp edsp java
CPU implementer : 0x41
CPU architecture: 5TEJ
CPU variant     : 0x0
CPU part        : 0x926
CPU revision    : 5

Hardware        : ARM-Versatile PB
Revision        : 0000
Serial          : 0000000000000000
```
we see that `leg` binary is compiled for ARM926-EJ platform.
Technical reference manual to be found here:
http://infocenter.arm.com/help/topic/com.arm.doc.ddi0198e/DDI0198E_arm926ejs_r0p5_trm.pdf

The goal is to guess a `key` value to make line: ```if ((key1()+key2()+key3()) == key )```
true.

3. Try to guess returned values for following steps:
    * ```key1()``` - returns 0x00008ce4  
    Result of the function is stored in `r0` which contains a value from `r3` which has been earlier assigned to `pc` value from.
    ```
    0x00008cdc <+8>:	mov	r3, pc
    0x00008ce0 <+12>:	mov	r0, r3
    0x00008ce4 <+16>:	sub	sp, r11, #0
    ```
    Effective `pc` stores a current instruction address + 8;
    
    * ```key2()``` - returns 0x00008d08 + 4 = 0x00008d0c
    ```
    0x00008cfc <+12>:	add	r6, pc, #1
    0x00008d00 <+16>:	bx	r6      <-- branch to 0x00008d05 = 0x00008d04
    0x00008d04 <+20>:	mov	r3, pc
    0x00008d06 <+22>:	adds	r3, #4
    0x00008d08 <+24>:	push	{r3}
    0x00008d0a <+26>:	pop	{pc}
    0x00008d0c <+28>:	pop	{r6}		; (ldr r6, [sp], #4)
    0x00008d10 <+32>:	mov	r0, r3
    ```

    * ```key3()``` - returns 0x00008d80
    This function returns just `lr` value which stores return address of the function.
    ```
    0x00008d7c <+64>:	bl	0x8d20 <key3>
    0x00008d80 <+68>:	mov	r3, r0          <-- This is the `lr` address
    0x00008d84 <+72>:	add	r2, r4, r3
    ```

    So the `key` value must equal: 0x00008ce4 + 0x00008d0c + 0x00008d80
    ```
    $ python3 -c "print(int(0x8ce4) + int(0x8d0c) + int(0x8d80))"
    108400
    ```

    * ```key = 108400``` 

4. After running `leg` executable on th server we get the flag:
```
/ $ ./leg
Daddy has very strong arm! : 108400
Congratz!
My daddy has a lot of ARMv5te muscle!
```

```
FLAG: {My daddy has a lot of ARMv5te muscle!}
```