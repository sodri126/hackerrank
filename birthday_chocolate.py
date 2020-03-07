#!/bin/python3

import sys

def solve(n, s, d, m):
    count = 0
    for x in range(0, n):
        count += sum(s[x:m+x]) == d and 1 or 0    
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
