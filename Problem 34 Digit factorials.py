"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial
def digitFactorial():
    lst = [] #to make a list of applicable numbers
    master_sum = 0 #to be a sum of all applicable numbers
    for i in range(41000): #iterate through numbers
        num_sum = 0 #sum of a numbers digits factorial'ed
        for digit in str(i): #iterate through digits of the number
            num_sum += factorial(int(digit))
        if (num_sum == i) and (len(str(i)) > 1):
            lst.append(i)
            master_sum += i
    dct = {'sum': master_sum, 'numbers': lst}
    return dct

print(digitFactorial())
