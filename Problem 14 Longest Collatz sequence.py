"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under the given limit, produces the longest chain?
Note: Once the chain starts the terms are allowed to go above limit.
"""
def longestCollatzSequence(max):
    longest_chain_producer = 0 #to be updated with the number that produces a longer chain
    longest_chain_count = 0 # to be updated with the chain count bigger than was previously the biggest
    for i in range(1, max):
        test_chain_count = 0 #the count for this i. start it over for each i
        test = i #make a copy of i for more clean work
        while test != 1: #so stop when the number changes to 1
            if test % 2 == 0: #if it's even
                test = int(test/2)
                test_chain_count += 1
            elif test % 2 != 0: #if it's odd. Needs to be elif instead of if so that when 2 turns into 1 above, it doesn't go right back up to 4 here.
                test = ( 3 * test ) + 1
                test_chain_count += 1
        test_chain_count += 1 #add one to the count for the final entry, which is 1
        if test_chain_count > longest_chain_count:
            longest_chain_producer = i
            longest_chain_count = test_chain_count
    return "The longest chain produced by a number under ", max, " is ", longest_chain_count, " and is produced by ", longest_chain_producer

print(longestCollatzSequence(1000000))
