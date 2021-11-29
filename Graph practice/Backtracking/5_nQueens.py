def getIdx(idx, N):
    rowIdx = idx // N
    colIdx = idx % N
    return rowIdx, colIdx


def placeQ(idx, board, N):
    rowIdx, colIdx = getIdx(idx, N)
    board[rowIdx][colIdx] = 'Q'


def unplaceQ(idx, board, N):
    rowIdx, colIdx = getIdx(idx, N)
    board[rowIdx][colIdx] = ' '


def isSafe(idx, board, N):
    '''
    safe to place Q condition.
    No other queen in same:
        row, col, both diagonals
    '''
    rowIdx, colIdx = getIdx(idx, N)

    for col in range(N):
        # print(rowIdx, col)
        if board[rowIdx][col] == 'Q':
            return False

    for row in range(N):
        if board[row][colIdx] == 'Q':
            return False

    # diag TR:  row- col+
    row = rowIdx
    col = colIdx
    while row != -1 and col != N:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1

    # diag BR:  row+ col+
    row = rowIdx
    col = colIdx
    while row != N and col != N:
        if board[row][col] == 'Q':
            return False
        row += 1
        col += 1

    # diag TL:  row- col-
    row = rowIdx
    col = colIdx
    while row != -1 and col != -1:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    # diag BL:  row+ col-
    row = rowIdx
    col = colIdx
    while row != N and col != -1:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True


def nQUeens(N):
    '''
    Place N Queens on chess board
    Algo:

    '''
    board = [[' ' for _ in range(N)]
             for _ in range(N)]
    Q = 0  # num of placed Qs
    idx = 0
    queenPositions = []

    # while not(idx == (N * N - 1) and Q == 0):
    for _ in range(100):
        print('idx', idx, idx//N, idx % N, Q, board)
        if idx >= (N * N) and Q != N:
            # unplace last Q
            lastQIdx = queenPositions.pop()
            unplaceQ(lastQIdx, board, N)
            idx = lastQIdx
            Q -= 1

        if isSafe(idx, board, N):
            # place Q
            placeQ(idx, board, N)
            Q += 1
            queenPositions.append(idx)

        if Q == N:  # Goal
            # unplace last Q
            lastQIdx = queenPositions.pop()
            unplaceQ(lastQIdx, board, N)
            idx = lastQIdx
            # print
            print(board)
            Q -= 1

        idx += 1


nQUeens(4)
