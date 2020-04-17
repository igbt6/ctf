# HEEEEEEERE'S Johnny!

__PROBLEM__

Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell1.picoctf.com 35225. Files can be found here: [passwd](./passwd) [shadow](./shadow).

__HINT__

If at first you don't succeed, try, try again. And again. And again.

If you're not careful these kind of problems can really "rockyou".


__SOLUTION__

This problem can easily be solved by using the very famous tool [John the ripper](https://www.openwall.com/john/).

You only need two commands
`unshadow passwd shadow > crack`
This will unshadow the passwd and the shadow file into crack file and then
`john -show crack`
which gave me:
```
root:hellokitty:0:0:root:/root:/bin/bash
```

The last remained thing was to login onto machine:
```
$  nc 2018shell1.picoctf.com 35225
Username: root
Password: thematrix
picoCTF{J0hn_1$_R1pp3d_99c35524}
```

FLAG - `picoCTF{J0hn_1$_R1pp3d_99c35524}`
