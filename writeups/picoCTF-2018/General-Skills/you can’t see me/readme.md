# you can’t see me

__PROBLEM__

...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2.

__HINT__

What command can see/read files?

What's in the manual page of ls?


__SOLUTION__

Go to the given directory and run `ls -la` which gives us
```
luk6xff@pico-2018-shell:~$ cd /problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2
luk6xff@pico-2018-shell:/problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2$ ls -la
total 60
drwxr-xr-x   2 root       root        4096 Mar 25  2019 .
-rw-rw-r--   1 hacksports hacksports    57 Mar 25  2019 .
drwxr-x--x 556 root       root       53248 Mar 25  2019 ..



```

If you'll use `tab` to auto complete the file name you'll see that there is a file name `.  ` So just use `cat` command to see the content of the file.
```
luk6xff@pico-2018-shell:/problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2$ cat . .\ \
cat: .: Is a directory
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_e3d80588}
```

FLAG - `picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_e3d80588}`
