"""
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date, timedelta

def countingSundays(start_year, end_year):
    start_date = date(start_year, 1, 1) #set start date to beginning of first year
    end_date = date(end_year, 12, 31) #set end date to end of last year
    number_of_days = (end_date - start_date).days #extract the number of days spanned from start to end
    count_sundays = 0 #start a count of sundays that were the first of the month

    while (start_date <= end_date):
        if (start_date.weekday() == 6) and (str(start_date.strftime("%d")) == '01'):
            count_sundays += 1
        start_date += timedelta(days=1)
    return count_sundays
print(countingSundays(1901, 2000))
