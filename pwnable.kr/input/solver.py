import subprocess
import os
import sys
import socket
import time

RUN_ON_SERVER = True

# argv
argv = ['A'] * 99
argv[ord('A')-1] = ''
argv[ord('B')-1] = '\x20\x0a\x0d'

# port
port = 12345
argv[ord('C')-1] = str(port)

# stdio
stdin_b  = b'\x00\x0a\x00\xff'
stderr_b = b'\x00\x0a\x02\xff'
stdin_read, stdin_write   = os.pipe()
stderr_read, stderr_write = os.pipe()
os.write(stdin_write, stdin_b)
os.write(stderr_write, stderr_b)

# env
envs = {b'\xde\xad\xbe\xef' : b'\xca\xfe\xba\xbe'}

# file
with open(b'\x0a', "wb") as f:
    f.write(b'\x00\x00\x00\x00')

# network
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# run process
if RUN_ON_SERVER:
    # on pwnable.kr server you have to run the script from /tmp/ and create ln -s /home/input/flag flag 
    p = subprocess.Popen(["/home/input2/input"]+argv, stdin=stdin_read, stderr=stderr_read, env=envs)
    os.system("ln -s /home/input2/flag")
else:
    p = subprocess.Popen(["input"]+argv, stdin=stdin_read, stderr=stderr_read, env=envs)

# network cont.
time.sleep(3) # wait for server start
s.connect(('127.0.0.1', port))
s.send(b'\xde\xad\xbe\xef')
s.close()