import os
import subprocess
import time

while True:
    p = subprocess.Popen(['./lotto'],
                        cwd=os.getcwd(),
                        shell=False,
                        stdin=subprocess.PIPE,
                        #stdout=subprocess.PIPE,
                        #stderr=subprocess.STDOUT,
                        )
    #print(p.communicate(os.linesep.join(["1", "!!!!!!"]))[0])
    #print(p.communicate(input=os.linesep.join(["1", "!!!!!!"]))[0].decode())
    print(p.communicate(["1\n"])[0])
    time.sleep(1)
