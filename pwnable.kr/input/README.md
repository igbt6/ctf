# input

1. Login into with pass `guest`:
```
ssh input2@pwnable.kr -p2222
scp -P 2222 input2@pwnable.kr:~/* .
```

2. Quick look at the source code of input.c
The task seems to be easy. I have to create an input of size 100 bytes which contains valid data to pass all the checks.

```

$ python -c "print('A '*ord('A') + '\x00' + ' ' + '\x20 \x0a \x0d' + 'A '*(100-4-ord('A')))" > /tmp/payload
$ ./input < /tmp/payload
```



I got get the flag:  
```
FLAG: {}
```