from pwn import *
import re


def create_line(start, end):
    if start == end:
        return str(start)
    return ' '.join(map(str, [n for n in range(start, end)]))

print create_line(1, 1)

r = remote('pwnable.kr', 9007)

r.recvuntil("- Ready? starting in 3 sec... -")

for _ in range(100):
    r.recvuntil("N=")
    line = r.recvline()
    N, C = [int(d) for d in re.findall(r'\d+', line)]
    print N, C

    start = 0
    end = N//2
    for i in range(C):
        r.sendline(create_line(start, end))
        weight = int(r.recvline())
        print weight, start, end
        if start >= end:
            break
        if weight % 10 == 0:
            start = end
            end = end*2
        else:
            start = start
            end = start + (end - start)//2
    #r.sendline(str(start))
    r.recvline()
  
r.interactive()

