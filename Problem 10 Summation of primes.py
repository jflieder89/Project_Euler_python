"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below n.
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

def primeSummation(n):
    sum = 0 #starting usm
    for i in range(n): #iterate through numbers up to n
        if isprime(i):
            sum += i
    return sum

print(primeSummation(140759))
