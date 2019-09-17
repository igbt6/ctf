# coin1

1. Running at:
```
$ nc pwnable.kr 9007
```

2. After connecting to the serrver via netcat I got:
```
---------------------------------------------------
        -              Shall we play a game?              -
        ---------------------------------------------------

        You have given some gold coins in your hand
        however, there is one counterfeit coin among them
        counterfeit coin looks exactly same as real coin
        however, its weight is different from real one
        real coin weighs 10, counterfeit coin weighes 9
        help me to find the counterfeit coin with a scale
        if you find 100 counterfeit coins, you will get reward :)
        FYI, you have 60 seconds.

        - How to play - 
        1. you get a number of coins (N) and number of chances (C)
        2. then you specify a set of index numbers of coins to be weighed
        3. you get the weight information
        4. 2~3 repeats C time, then you give the answer

        - Example -
        [Server] N=4 C=2        # find counterfeit among 4 coins with 2 trial
        [Client] 0 1            # weigh first and second coin
        [Server] 20                     # scale result : 20
        [Client] 3                      # weigh fourth coin
        [Server] 10                     # scale result : 10
        [Client] 2                      # counterfeit coin is third!
        [Server] Correct!

        - Ready? starting in 3 sec... -

N=323 C=9
```

So we have to play the game. The first step i did was using `pwntools` library `https://github.com/Gallopsled/pwntools` and writing a script `coin1.py` which can automatically play with the server.

Firs I started to run the `coin1.py` script with: ```r = remote('pwnable.kr', 9007)``` address from my local machine, but it happened that my network response time is too slow so as was stated I ran it from pwnable.kr server (script modified to ```r = remote('0', 9007)```) and I saw the results:
```
mistake@prowl:/tmp/coin12345$ python c.py
[+] Opening connection to 0 on port 9007: Done
932 10
95 7
284 9
598 10
954 10
15 4
188 8
687 10
348 9
124 7
737 10
489 9
700 10
235 8
78 7
702 10
599 10
338 9
815 10
952 10
892 10
631 10
152 8
33 6
466 9
634 10
302 9
685 10
911 10
208 8
23 5
507 9
288 9
568 10
912 10
878 10
405 9
153 8
130 8
80 7
296 9
411 9
9 4
903 10
599 10
194 8
289 9
377 9
935 10
369 9
871 10
936 10
80 7
605 10
793 10
828 10
909 10
4 2
590 10
433 9
810 10
767 10
677 10
916 10
666 10
49 6
526 10
870 10
694 10
253 8
393 9
585 10
978 10
593 10
228 8
541 10
516 10
74 7
718 10
744 10
910 10
461 9
94 7
420 9
815 10
700 10
439 9
416 9
910 10
686 10
876 10
927 10
885 10
668 10
525 10
983 10
136 8
980 10
969 10
715 10
[*] Switching to interactive mode
Congrats! get your flag
b1NaRy_S34rch1nG_1s_3asy_p3asy
```

And yeah, we got the flag:
```
FLAG: {b1NaRy_S34rch1nG_1s_3asy_p3asy}
```