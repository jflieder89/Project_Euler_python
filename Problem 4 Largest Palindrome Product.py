"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two n-digit numbers.
"""
def ispal(number):
    string = str(number) #turn it into a string
    reverse_lst = [] #create empty list to be filled in with pieces of string in reverse
    for i in range(len(string)):
        reverse_lst.append(string[len(string)-i-1]) #add in the mirrored character
    reverse_number= int(''.join(reverse_lst)) #turn the list of reversed digits back into a number
    return number == reverse_number



def largestPalindromeProduct(n):
    max = 10**n #set the max digit that can be used for the multiplication searching. The range functions will reduce this by 1.
    largest_palindrome_product = 0
    for i in range(max): #iterate first number up to max
        for j in range(max): #iterate second number up to max
            product = i*j
            if (ispal(product)) and (product > largest_palindrome_product): #if the product is a palindrome and the biggest one yet
                largest_palindrome_product = product #reset the high score, so to speak
    return largest_palindrome_product

print(largestPalindromeProduct(3))
