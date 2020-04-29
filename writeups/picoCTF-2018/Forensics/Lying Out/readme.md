# Ext Super Magic

__PROBLEM__

Some odd [traffic](https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/traffic.png) has been detected on the network, can you identify it? More [info](https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/info.txt) here. Connect with `nc 2018shell.picoctf.com 27108` to help us answer some questions.

__HINT__


__SOLUTION__

```
wget  https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/traffic.png --no-check-certificate
wget  https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/info.txt --no-check-certificate

```

```
nc 2018shell.picoctf.com 27108
```



FLAG - `picoCTF{ab0CD63BC762514ea2f4fc9eDEC8cb1E}`
