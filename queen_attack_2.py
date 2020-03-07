#!/bin/python3

import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    # 0 for the not allowing access way, 1 for the allowing, 2 for the queen
    boardChess = [[0 for i in range(n)] for j in range(n)]
    # create 
    r_q = r_q - 1
    c_q = c_q - 1
    for i in range(n):
        boardChess[r_q][i] = 1
        boardChess[i][c_q] = 1

    # serong kiri
    # contains word "getBegin" getRow
    if r_q <= c_q:
        #row is less than column
        p = c_q - r_q
        getBeginSerongKiri = 0
        for i in range(p, n):
            boardChess[getBeginSerongKiri][i] = 1
            getBeginSerongKiri = getBeginSerongKiri + 1
    else:
        #row is greater than                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               column 
        p = r_q  - c_q + 1
        getBeginSerongKiri = r_q - 1
        for i in range(0, p):
            boardChess[getBeginSerongKiri][i] = 1
            getBeginSerongKiri = getBeginSerongKiri + 1
    
    boardChess[r_q][c_q] = 2                                    
    for i in range(n):
        for j in range(n):
            print(str(boardChess[i][j]), end=' ')
        print()
    
            
    return 0

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)