"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
"""
def smallestMult(n):
    lst = [i for i in range(1, n + 1)] #start with a list of numbers from 1 to n
    count = 0 #need to set this to zero once before the while loop
    test = 0 #set to zero for now
    while count < len(lst): #so while we do not have all numbers of the list going evenly into the test numbers
        count = 0 #start at zero for each value of the test number. This will be how many numbers of the list go evenly into the tested numbers
        test += n #start with n, then going to increase by n with each failure since it is the biggest jump that can be made safely
        for i in lst: #iterate through the list
            if (test % i) == 0: #if the number in the list goes evenly into test
                count += 1
    return test #we will only break out of the loop if count = len(lst), which means test is the smallest common multiple!

print(smallestMult(20))
