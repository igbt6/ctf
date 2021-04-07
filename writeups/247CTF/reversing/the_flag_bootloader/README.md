# CTF Name – the flag bootloader


## Description
https://247ctf.com/dashboard#collapse-c53


## Solution

We got the `flag.com` file
```
luk6xff@pc:~/Projects/ctf/writeups/247CTF/reversing/the_flag_bootloader$ file flag.com
flag.com: DOS/MBR boot sector
```

Let's run it under QEMU:
```
qemu-system-x86_64 -s -drive format=raw,file=flag.com
```
-s option opens tcp port 1234 for gdb connection.

We get this:
[qemu](qemu.png)


Run it under qemu
```
qemu-system-x86_64 -s -S -m 512 -fda flag.com
```

Now let's attach to the process
```
gdb
(gdb) target remote localhost:1234
or
(gef) gef-remote -q localhost:1234 # Doesn't work properly
```

## Flag
```
247CTF{YOUR_FLAG}
```

### Authors
* **Lukasz** - [luk6xff](https://github.com/luk6xff)

### License
[MIT](https://choosealicense.com/licenses/mit/)