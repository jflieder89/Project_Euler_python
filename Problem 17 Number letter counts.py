"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?
Note: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#first transfer into word from numbers
def to_letters(n):
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + (ones[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + (("and" + to_letters(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return to_letters(n // 1000) + "thousand" + (to_letters(n % 1000) if (n % 1000 != 0) else "")

def numberLetterCounts(n):
    return sum(len(to_letters(i)) for i in range(1, n+1))
print(numberLetterCounts(1000))
