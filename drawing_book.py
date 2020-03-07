import sys
import os

def pageCount(n, p):
    totalFront = 0
    totalBack = 0

    if p > 1:
        for i in range(2, n+1, 2):
            totalFront += 1
            if i == p or i+1 == p:
                break

    if n % 2 == 0:
        n += 1
    while n > 2:
        if n == p or n-1 == p:
            break
        totalBack += 1
        n -= 2
    return min(totalFront, totalBack)

if __name__ == "__main__":
    n = int(input())
    p = int(input())

    result = pageCount(n, p)

    print(result)