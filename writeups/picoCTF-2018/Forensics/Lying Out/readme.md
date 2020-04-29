# Lying Out

__PROBLEM__

Some odd [traffic](https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/traffic.png) has been detected on the network, can you identify it? More [info](https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/info.txt) here. Connect with `nc 2018shell.picoctf.com 27108` to help us answer some questions.

__HINT__


__SOLUTION__

```
wget  https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/traffic.png --no-check-certificate
wget  https://2018shell.picoctf.com/static/abfdb498b12895694285a032f261c545/info.txt --no-check-certificate

```

```
$ nc 2018shell.picoctf.com 27108

You'll need to consult the file `traffic.png` to answer the following questions.

Which of these logs have significantly higher traffic than is usual for their time of day? You can see usual traffic on the attached plot. There may be multiple logs with higher than usual traffic, so answer all of them! Give your answer as a list of `log_ID` values separated by spaces. For example, if you want to answer that logs 2 and 7 are the ones with higher than usual traffic, type 2 7.

log_ID      time  num_IPs
0        0  01:00:00    10209
1        1  03:30:00    11585
2        2  05:30:00    11616
3        3  08:30:00    13209
4        4  10:45:00    10216
5        5  11:30:00    17024
6        6  12:15:00    12939
7        7  14:00:00     9842
8        8  16:30:00     9918
9        9  18:30:00    15887
10      10  19:15:00    11611
11      11  21:45:00     9788
12      12  23:30:00    10517
13      13  23:30:00    10419

1 2 3 5

Correct!

Great job. You've earned the flag: picoCTF{w4y_0ut_de051415}
```

FLAG - `picoCTF{w4y_0ut_de051415}`
