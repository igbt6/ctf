# shellshock

1. Login into server with passwd: `guest`:
```
$ ssh shellshock@pwnable.kr -p2222
$ scp -P2222 shellshock@pwnable.kr:~/* .
```
I got the flag:

```
FLAG: {}
```