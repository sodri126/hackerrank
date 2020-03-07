#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    getEquallyCandle = m - 1
    getResult = (getEquallyCandle + s) % n
    return getResult if getResult != 0 else n


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
