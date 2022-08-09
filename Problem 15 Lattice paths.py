"""
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a given gridSize?
"""
#The math for this is (2n)! / (n! + n!) for an n-length square.
from math import factorial
def latticePaths(n):
    return int( ( factorial((2*n)) ) / ( factorial(n) * factorial(n) ) )
print(latticePaths(20))
