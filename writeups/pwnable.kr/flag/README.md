# flag

1. Download a file
```
$ wget http://pwnable.kr/bin/flag
```
2. Open the `flag` binary under cutter/ghidra 

3. Looking for strings in the executable I noticed the following strings:
```
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved. $
```
which means that binary has been packed with `upx packer` tool.
Let's try to unpack it:
```
$ ~/Programs/upx-3.95-amd64_linux/upx -d -k -oflag_decompressed flag 
```

4. Open the `flag_decompressed` binary under cutter/ghidra

5. You will notice the instruction:
```
mov rdx, qword obj.flag 
```
which stores in `rdx` our flag from 0x496628
```
0x00496628          .string "UPX...? sounds like a delivery service :)"
```

You'll get the flag:  
```
FLAG: {UPX...? sounds like a delivery service :)}
```