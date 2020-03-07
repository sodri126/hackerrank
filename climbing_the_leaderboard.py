#!/bin/python3

import sys

def rank(n,scores,score):
    rankData = 1
    for x in range(0, n):
        
        if x == n-1 and score != scores[x]:
            return rankData+1
        elif x == n-1 and score == scores[x]:
            return rankData
        elif score >= scores[x]:
            return rankData
        elif (score < scores[x] and score > scores[x+1]) and (scores[x] > scores[x+1]):
            m = int(input().strip())
            alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

            scores = sorted(set(scores), reverse=True)
            n = len(scores)

            for x in alice:
                while(n > 0) and (x >= scores[n-1]):
                    n -= 1
                    print(n+1)
                    return rankData+1
        else:      
            rankData += 0 if x < n-1 and scores[x] == scores[x+1] else 1            
            continue

        

def solve(n,scores,m,alice):
    listRank = list()
    for x in alice:
        listRank.append(rank(n,scores,x))
    return listRank

def binarySearch(n,scores,score):
    first = 0
    last = n-1
    while(first <= last):
        midpoint = (first + last)//2
        if scores[midpoint] == score:
            return midpoint
        else:
            if score < scores[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

scores = sorted(set(scores), reverse=True)
n = len(scores)

for x in alice:
    while(n > 0) and (x >= scores[n-1]):
        n -= 1
    print(n+1)
    