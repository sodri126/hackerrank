#!/bin/python3

import sys

def getRecord(s):
    tmpBest = s[0]
    tmpWorst = s[0]
    countBest = 0
    countWorst = 0
    listBestWorst = list()
    tmp = 0
    for x in s:
        if x > tmpBest:
            tmpBest = x
            countBest += 1
        
        if x < tmpWorst:
            tmpWorst = x
            countWorst += 1
    listBestWorst.append(countBest)
    listBestWorst.append(countWorst)
    return listBestWorst

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))