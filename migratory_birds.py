#!/bin/python3

import sys

def migratoryBirds(n, ar):
    birdList = [0]*5
    for x in ar:
        birdList[x-1] += 1
    getMax = max(birdList)
    return birdList.index(getMax) + 1
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)