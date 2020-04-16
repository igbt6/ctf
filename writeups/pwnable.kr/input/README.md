# input

1. Login into with pass `guest`:
```
ssh input2@pwnable.kr -p2222
scp -P 2222 input2@pwnable.kr:~/* .
```

2. Quick look at the source code of input.c
The task seems to be easy. I have to create an input of size 100 bytes which contains valid data to pass all the checks.

Script ```solver.py``` created.
```scp -P2222 solver.py input2@pwnable.kr:~/```


After running the script uned /tmp/luk6xff/ I got the flag:
```
FLAG: {Mommy! I learned how to pass various input in Linux :)}
```