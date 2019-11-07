https://godbolt.org/z/R6Rztm
https://godbolt.org/z/RSRKzk

```sh
g++ memset.cpp -std=c++14 -Wall -Wextra -Wpedantic -O0 -o memsetcpp
./memsetcpp

g++ memset.cpp -std=c++14 -Wall -Wextra -Wpedantic -O3 -o memsetcpp
./memsetcpp

g++ memset.cpp -std=c++14 -Wall -Wextra -Wpedantic -fno-builtin-memset -O3 -o memsetcpp
./memsetcpp

gcc memset.c -std=c11 -Wall -Wextra -Wpedantic -O0 -o memsetc
./memsetc

gcc memset.c -std=c11 -Wall -Wextra -Wpedantic -O3 -o memsetc
./memsetc

gdb -batch -ex "disas main" memsetc
```