from pwn import *
import re

r = remote('f3d6bdbf164a0d48.247ctf.com', 50211)
context.log_level = 'debug'

# Skip first 2 lines
r.recvline()
r.recvline()

for _ in range(500):
    splitted = r.recvline().decode("utf-8").split()
    res = int(splitted[5]) + int(splitted[7].strip('?'))
    r.sendline(str(res)+'\r\n')
    # Skip the b'Yes, correct!\r\n'
    r.recvline()
r.interactive()
