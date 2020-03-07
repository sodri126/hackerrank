#!/bin/python3

import sys

def solve(grades):
    gradesList = list()
    for x in grades:
        getModule = 5 - (x % 5)
        getResult = x + getModule
        if getResult < 40 or getModule == 3 or getModule > 3:
            gradesList.append(x)
        else:
            gradesList.append(getResult)
    return gradesList

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
