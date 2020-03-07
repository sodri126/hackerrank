import sys

if __name__=="__main__":
    c = [0, 0, 1, 0, 0, 1, 0]

    totalJump = 0
    totalClouds = len(c)
    idx = 0
    while idx < totalClouds-1:
        if idx+2 <= totalClouds-1 and c[idx+2] == 1:
            idx += 1
            totalJump += 1
        else:
            idx += 2
            totalJump += 1

        print("Index to be: "+ str(idx) + " and total jumps are: "+ str(totalJump))
    
    print(totalJump)
