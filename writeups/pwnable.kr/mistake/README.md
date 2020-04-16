# mistake

1. Login into server with passwd: `guest`:
```
$ ssh mistake@pwnable.kr -p2222
$ scp -P2222 mistake@pwnable.kr:~/* .
```

2. There is a `operators priority` error in the code:
```
	if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){  <-- mistake here :)
		printf("can't open password %d\n", fd);
		return 0;
	}
```
As `<` operator has higher precedence priority than `=`, the result of the `open(..) < 0` will be always 0.
`fd = 0` and as file descriptor 0 is reserved for `stdin`, program will wait for stdin input to be read into `pw_buf`

I chose: `1111111111` for `pw_buf` and `0000000000` for `pw_buf2`.
XORing `0` by `1` will give `1` and the same in the other direction.
Running:
```
mistake@prowl:~$ ./mistake 0000000000
do not bruteforce...
1111111111
input password : 0000000000
Password OK
Mommy, the operator priority always confuses me :(
```
I got the flag:

```
FLAG: {Mommy, the operator priority always confuses me :(}
```