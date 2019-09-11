

import subprocess
import os
import sys
import socket
import time

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
p = subprocess.Popen(["input2"]+argv, stdin=stdin_read, stderr=stderr_read, env=envs)

# network cont.
time.sleep(1) # wait for server start
s.connect(('localhost', port))
s.send(b'\xde\xad\xbe\xef')
s.close()