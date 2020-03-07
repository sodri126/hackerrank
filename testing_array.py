import sys

if __name__ == "__main__":
    arr = ['muhamad', 'shodri', 'ari', 'hari', 'kurniawan']
    arr.append('pengen')
    arr.remove('muhamad')
    arr.pop(0)
    # arr.reverse() # reverse a list
    print(arr)

    test_arr = [[1,2,3], [4,5,6], [7,8,9]]
    for i in test_arr:
        for j in i:
            print(j, end=' ')
        print()

    print("After delete some elements")
    del test_arr[0][2]
    for i in test_arr:
        for j in i:
            print(j, end=' ')
        print()