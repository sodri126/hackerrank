import sys

if __name__ == "__main__":
    n = int(input())
    i = 0
    while n > i:
        for j in range(0, n):
            print(j+1, end=' ')
        print()
        n -= 1