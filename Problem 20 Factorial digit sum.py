"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits n!
"""
from time import time
from math import factorial
start_time = time()
def sumFactorialDigits(n):
    sum = 0
    str_fact = str(factorial(n))
    for digit in str_fact:
        sum += int(digit)
    return sum
end_time = time()
print(sumFactorialDigits(100))
print('This took', (end_time - start_time) * 1000, 'milliseconds')
