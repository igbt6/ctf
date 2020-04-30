all:
	gcc -m32 -c loop_asm_rev.S
	gcc -m32 -c solver.c
	gcc -m32 -o solver loop_asm_rev.o solver.o
	./solver

clean:
	rm solver *.o
