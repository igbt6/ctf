# absolutely relative

__PROBLEM__

In a filesystem, everything is relative ¯\_(ツ)_/¯. Can you find a way to get a flag from this [program](https://2018shell.picoctf.com/static/725b533a89a0e70b85b37ce2965da003/absolutely-relative)? You can find it in /problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee on the shell server. [Source](https://2018shell.picoctf.com/static/725b533a89a0e70b85b37ce2965da003/absolutely-relative.c).

__HINT__

Do you have to run the program in the same directory? (⊙.☉)7
Ever used a text editor? Check out the program 'nano'

__SOLUTION__

```
wget https://2018shell.picoctf.com/static/725b533a89a0e70b85b37ce2965da003/absolutely-relative --no-check-certificate
wget https://2018shell.picoctf.com/static/725b533a89a0e70b85b37ce2965da003/absolutely-relative.c --no-check-certificate

sshpass -p <PASS> ssh luk6xff@2018shell4.picoctf.com


luk6xff@pico-2018-shell:~$ cd /problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee
luk6xff@pico-2018-shell:/problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee$ ls
absolutely-relative  absolutely-relative.c  flag.txt
luk6xff@pico-2018-shell:/problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee$ cat flag.txt
cat: flag.txt: Permission denied
luk6xff@pico-2018-shell:/problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee$ ls -la
total 76
drwxr-xr-x   2 root       root                   4096 Mar 25  2019 .
drwxr-x--x 556 root       root                  53248 Mar 25  2019 ..
-rwxr-sr-x   1 hacksports absolutely-relative_2  8984 Mar 25  2019 absolutely-relative
-rw-rw-r--   1 hacksports hacksports              796 Mar 25  2019 absolutely-relative.c
-r--r-----   1 hacksports absolutely-relative_2    37 Mar 25  2019 flag.txt


luk6xff@pico-2018-shell:/$ cd ~ && touch permission.txt && echo yes > permission.txt
luk6xff@pico-2018-shell:~$ /problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee/absolutely-relative
You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_372b3859}

```

FLAG - `picoCTF{3v3r1ng_1$_r3l3t1v3_372b3859}`
