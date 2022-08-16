"""
Euler discovered the remarkable quadratic formula:
n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values  0≤n≤39 .
However, when  n=40,402+40+41=40(40+1)+41  is divisible by 41, and certainly when  n=41,412+41+41  is clearly divisible by 41.
The incredible formula  n2−79n+1601  was discovered, which produces 80 primes for the consecutive values  0≤n≤79 .
The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n^2+an+b , where  |a|<range  and  |b|≤range
where  |n|  is the modulus/absolute value of  n
e.g.  |11|=11  and  |−4|=4
Find the product of the coefficients,  a  and  b , for the quadratic expression that produces the maximum number of primes for consecutive values of  n , starting with  n=0 .
"""
from math import floor, sqrt
def isprime(n):
    lst_factors = [] #list to be filled with factors of n
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            lst_factors.append(i)
            lst_factors.append(int(n /i))
    #return(lst_factor)
    if (len(lst_factors) == 2) and (lst_factors[0] != lst_factors[1]):
        return True
    else:
        return False


def quadraticPrimes(limit):
    max_count = 0 #variable for the number of consecutive primes for a certain configuration
    max_coeff_prod = 0 #set variable to be replaced with the next biggest coefficient product
    for a in range((-1)*limit, limit): #iterate through a coefficient possibilities
        for b in range(limit): #iterate through b coefficient possibilities
            count = 0 #count of consecutive primes for this configuration of a and b
            coeff_prod = 0
            n = 0 #start with n equals zero each configuration of a and b coefficients
            while (n**2 + a*n + b > 0) and (isprime(n**2 + a*n + b)): #need to account for if the expression evalutes to zero or negative, as this will mess up the isprime running
                count += 1
                n += 1
            if count > max_count:
                max_count = count
                max_coeff_prod = a*b
    return max_coeff_prod
print(quadraticPrimes(1000))
