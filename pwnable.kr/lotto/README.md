# lotto

1. Login into server with passwd: `guest`:
```
$ ssh lotto@pwnable.kr -p2222
$ scp -P2222 lotto@pwnable.kr:~/* .
```

2. First thing after looking at code which attracts my attention was the following fragment:
```
	// calculate lotto score
	int match = 0, j = 0;
	for(i=0; i<6; i++){
		for(j=0; j<6; j++){
			if(lotto[i] == submit[j]){
				match++;
			}
		}
	}
```
The problem here is if only one value matches between `lotto` and `submit` arrays, we get the correct result.

3. Input data in `lotto` array are always cropped to the range: 1-45. For `submit` array as we read data into `unsigned char` datatype buffer the only valid chars will be from range 33-45:
```
33	21	00100001	&#33;	!	Exclamation mark
34	22	00100010	&#34;	"	Double quote
35	23	00100011	&#35;	#	Number
36	24	00100100	&#36;	$	Dollar sign
37	25	00100101	&#37;	%	Percent
38	26	00100110	&#38;	&	Ampersand
39	27	00100111	&#39;	'	Single quote
40	28	00101000	&#40;	(	Left parenthesis
41	29	00101001	&#41;	)	Right parenthesis
42	2A	00101010	&#42;	*	Asterisk
43	2B	00101011	&#43;	+	Plus
44	2C	00101100	&#44;	,	Comma
45	2D	00101101	&#45;	-	Minus
```
All smaller values are not characters and you cannot easily write them down into `stdin` fd.


4. Lets create then an input string containing data from ASCII table within range (33-45) eg.
```
!!!!!!
```
It's good to have all the signs the same in the input buffer, it will give you a bigger chance to get 6 matches if only one char in `lotto` buffer will be the same as in our `submit`.



After running a few times my `lotto-solver.py` i got the flag:

```
FLAG: {sorry mom... I FORGOT to check duplicate numbers... :(}
```