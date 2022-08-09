"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**exponent?
"""
def powerDigitSum(exp):
    num = str(2**exp) #obtain the exponent and turn it into a string, which is iterable
    total = 0
    for digit in num: 
        total += int(digit)
    return total

print(powerDigitSum(1000))
