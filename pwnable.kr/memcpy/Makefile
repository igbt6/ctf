all: obj
	gcc memcpy.o -o memcpy -lm

obj:
	gcc -c -o memcpy.o memcpy.c

.PHONY : clean

clean:
	rm memcpy.o memcpy