"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
from math import floor, sqrt
def isprime(n):
    if n == 1:
        return False
    lst_factors = [] #list to be filled with factors of n
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            lst_factors.append(i)
            lst_factors.append(int(n /i))
    #return(lst_factor)
    if (len(lst_factors) == 2):
        return True
    else:
        return False

def nthprime(n):
    prime_count = 0 #number of primes found so far
    count = 1 # choose where to start looking for primes
    while prime_count < n:
        if isprime(count) == True:
            prime_count += 1
        count += 1 # move onto the next number
    return (count - 1) #return the last, or nth, prime in the list

print(nthprime(1000))
