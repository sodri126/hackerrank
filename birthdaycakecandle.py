#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    getMax = max(ar)
    return ar.count(getMax)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)