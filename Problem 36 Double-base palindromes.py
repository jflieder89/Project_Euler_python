"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1,000,000, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from time import time
start_time = time()
def decimal_to_binary(n): #created my own binary converter. I'm sure there is one built in that I could have used but I figured I'd go through exercise
    bin = 0 #binary number to be created
    exponent = 0 #start with zero and then change to get maximum needed exponent
    while n >= 2**(exponent+1): #iterate through 2**exponent to see how high an exponent is needed to cover the number n
        exponent +=1
    while n > 0: #now apply the exponents in descending order and turn into binary
        if n >= 2**exponent: #definitely need the = component of that so that when n is whittled down to 1, it will end properly
            n -= 2**exponent #subtract 2**exponent from the remainding part of n
            bin += 10**exponent #translate that exponent into binary and incorporate into bin
        exponent -= 1 #go to the next lowest 2**power
    return bin

def ispal(number):
    string = str(number) #turn it into a string
    reverse_lst = [] #create empty list to be filled in with pieces of string in reverse
    for i in range(len(string)):
        reverse_lst.append(string[len(string)-i-1]) #add in the mirrored character
    reverse_number= int(''.join(reverse_lst)) #turn the list of reversed digits back into a number
    return number == reverse_number

def doubleBasePalindromes(n):
    master_sum = 0
    for i in range(1, n):
        if (ispal(i)):
            if (ispal(decimal_to_binary(i))):
                #print(i, decimal_to_binary(i))
                master_sum += i
    return master_sum
print(doubleBasePalindromes(1000000))
end_time = time()
print('This took', end_time - start_time, 'seconds')
