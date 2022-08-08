"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
"""
from math import sqrt

def specialPythagoreanTriplet(n):
    trip_lst = []
    for a in list(range(1, 1000)): #iterate 'a'
        for b in list(range(1, 1000)): #iterate 'b'
            if ( (sqrt(a**2 + b**2) / 1).is_integer() ) and (a not in trip_lst): # if it is a pythagorean triplet that has not yet been found
                trip_lst.append(a) #add the a and b that form the pythogorean triple to the 'already found' list, trip_st
                trip_lst.append(b)
                if (a + b + int(sqrt(a**2 + b**2))) == n:
                    #print(a, b)
                    return "The product is ",  a * b * int(sqrt(a**2 + b**2))

print(specialPythagoreanTriplet(1000))
