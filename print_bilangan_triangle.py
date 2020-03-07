import sys

if __name__ == "__main__":
    n = int(input()) + 1
    for i in range(0, n):
        cal = n - i
        for j in range(0, cal):
            print(end=' ')

        for k in range(0, i):
            print(k+1, end=' ')

        print()

# create triangle numer