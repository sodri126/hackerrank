import sys

if __name__ == "__main__":
    for i in range(2, 100):
        count = 0
        for j in range(2, i+1):
            if i % j == 0:
                count += 1

        if count == 1:
            print(i, end=' ')