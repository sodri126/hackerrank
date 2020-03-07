#!/bin/python3

import sys

def solve(year):
    addDay = 0
    addDayTransition = 0
    if year < 1918:
        addDay = year % 4 == 0 and 1 or 0
    elif year == 1918:
        addDayTransition = 13
    else:
        addDay = (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and 1 or 0
    
    listMonth = list([31 if x % 2 == 0 else 30 for x in range(0, 8)])
    listMonth[1] = 28 + addDay

    getTotal = sum(listMonth)
    getDays = (255 - getTotal) + addDayTransition
    return "{0:02d}.{1:02d}.{2}".format(getDays, 9, year)


year = int(input().strip())
result = solve(year)
print(result)
