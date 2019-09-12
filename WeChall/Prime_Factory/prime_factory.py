# taken from: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


N = 1000000
SIZE = 2

first_two_primes = []

# Find a SIZE number of primaries greater than milion
for i in range(N, 2*N):
    if is_prime(i):
        digit_sum = sum(map(lambda x : int(x), str(i)))
        if is_prime(digit_sum):
            first_two_primes.append(i)
            if len(first_two_primes) >= SIZE:
                break

print("SOLUTION: "+''.join(map(str, first_two_primes)))
