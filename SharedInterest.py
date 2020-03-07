if __name__=="__main__":
    friends_nodes = 5
    friends_from = [1, 1, 2, 2, 2, 3]
    friends_to = [2, 2, 3, 3, 4, 4]
    friends_weight = [1, 2, 1, 3, 3, 2]

    totalLen = len(friends_from)
    twoDimension = []
    for idx in range(totalLen):
        twoDimension.append([friends_from[idx], friends_to[idx], friends_weight[idx]])

    print(twoDimension)

    #for check if the same interest
    temp = twoDimension[0]
    totalDimensionLen = len(twoDimension)

    row = 0
    column = 0
    while row < totalDimensionLen:
        column = row+1
        while column < totalDimensionLen:
            if (twoDimension[row][0] == twoDimension[column][0]) and (twoDimension[row][1] == twoDimension[column][1]):
                twoDimension[row][2] += twoDimension[column][2]
                twoDimension.remove(twoDimension[column])
                totalDimensionLen -= 1
            column += 1
        row += 1
    
    print(twoDimension)

    totalDimensionLen = len(twoDimension)
    listItem = []
    row = 0
    column = 0
    idx = 0
    isStop = False
    listMerged = [i for i in range(i, totalDimensionLen)]
    while row < totalDimensionLen:
        column = row + 1
        while column < totalDimensionLen:
            if (twoDimension[row][1] == twoDimension[column][0]):
                listItem.append([twoDimension[row][0], twoDimension[row][1], twoDimension[column][1], twoDimension[row][2]+twoDimension[column][2]])
            elif(column is not contains):
                listItem.append(twoDimension[column])
            column += 1

        row += 1
    
    print(listItem)

    # high = 0
    # itemHigh = None
    # for item in listItem:
    #     if item[len(item)-1] > high:
    #         high = item[(len(item)-1)]
    #         itemHigh = item
      
    # maximumResult = []
    # for idx in range(0, len(itemHigh)-2):
    #     maximumResult.append(itemHigh[idx]*itemHigh[idx+1])
    
    # print (max(maximumResult))
    # for idx in range(1, totalDimensionLen):
    #     if (temp[0] == twoDimension[idx][0]) and (temp[1] == twoDimension[idx][1]):
    #         twoDimension[idx][2] += temp[2]
    #         twoDimension.remove(temp)
    #         totalDimensionLen -=1