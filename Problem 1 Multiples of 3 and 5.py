"""
If we list all the natural numbers below
10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below the provided parameter value number
"""

def multiplesOf3and5(number):
    lst = [] #empty list to be filled in
    for i in range(number): #go from zero to the number below the parameter
        if (i % 3 == 0) or (i % 5 == 0) : #if evenly divisible by 3 or 5 or both
            lst.append(i) #add to the list
    return sum(lst) #return the sum of the list

print(multiplesOf3and5(19564))
