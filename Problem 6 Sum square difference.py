"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""
def sumSquareDifference(n):
    lst = [i for i in range(1, n + 1)] #start with a list of numbers from 1 to n
    sum_of_squares = 0
    for item in lst:
        sum_of_squares += (item**2)
    square_of_sum = sum(lst)**2

    return square_of_sum - sum_of_squares
print(sumSquareDifference(100))
