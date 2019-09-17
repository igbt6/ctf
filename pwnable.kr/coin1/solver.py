from pwn import *
import re


def create_line(start, end):
    if start == end:
        return str(start)
    return ' '.join([str(n) for n in range(start, end+1)])

print create_line(1, 3)

r = remote('pwnable.kr', 9007)

r.recvuntil("- Ready? starting in 3 sec... -")

for _ in range(100):
    r.recvuntil("N=")
    line = r.recvline()
    N, C = [int(d) for d in re.findall(r'\d+', line)]
    print N, C

    start = 0
    end = N-1
    for i in range(C):
        mid = start + (end-start)//2
        r.sendline(create_line(start, mid))
        line = r.recvline()
        #print line
        weight = int(line)
        print " start: ",start, " mid: ",mid, " end: ",end, " weight: ", weight
        if weight == 9:
            break
        if start >= end:
            break
        if weight%10 != 0:
            end = mid
        else:
            start = mid

    r.sendline(str(mid))
    #r.recvline()
  
r.interactive()

