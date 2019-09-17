from pwn import *
import re


def create_line(start, end):
    if start == end:
        return str(start)
    return ' '.join([str(n) for n in range(start, end)])

r = remote('pwnable.kr', 9007)
r.recvuntil("- Ready? starting in 3 sec... -")

for _ in range(100):
    r.recvuntil("N=")
    line = r.recvline()
    N, C = [int(d) for d in re.findall(r'\d+', line)]
    print N, C

    start = 0
    end = N
    for i in range(C):
        mid = (end+start)//2
        r.sendline(create_line(start, mid))
        #print create_line(start, mid)
        weight = int(r.recvline())
        #print "start: ",start, " mid: ",mid, " end: ",end, " weight: ", weight
        #if weight == 9:
        #    break
        if start >= end:
            break
        if weight%10 != 0:
            end = mid
        else:
            start = mid
    r.sendline(str(start))
    r.recv(256)
    #print r.recv(1024)
    #r.recvuntil("Correct!")
  
r.interactive()