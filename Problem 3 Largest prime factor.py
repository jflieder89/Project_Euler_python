"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the given number?
"""
from math import floor, sqrt #use this for sqrt and floor functions

lst_factors = [] # a list to be filled up with factors, if there are any
def largestPrimeFactor(n):
    original_number = n # keep a copy of the original number since n could be reduced
    for i in range(2, floor(sqrt(n)) + 1): #to look for factors from 2 to no higher than the square root of the original number
        while (n % i == 0) and (n > 1): #if i is a factor of n and n hasn't been reduced to 1, and keep trying in case it is a multiple factor
            lst_factors.append(i)
            n = int(n / i)
    if n != 1: # if there was no reduction of the original number down to one (AKA it was prime!), add it to the list
        lst_factors.append(n)
    return 'The highest prime factor of '+ str(original_number) + ' is ' + str(max(lst_factors))
print(largestPrimeFactor(600851475143))
