def getMaxGold(matrix):
    '''
    Ques:
    You can start from any row in 1st col.
    And move to next col, but only, to right or diagonally 1 up or
    diagonally 1 down.
    And get max gold.

    Approach 1:
    We traverse from 2nd last col to 1st col.
    And update the max gold each cell can have.
    By taking max of 3 options, diag up, right, diag down.
    '''
    maxGold = float('-inf')
    for col in reversed(range(0, len(matrix[0]) - 1)):
        for row in range(len(matrix)):
            nextCol = col + 1
            maxInNextCol = matrix[row][nextCol]

            if row - 1 >= 0:
                maxInNextCol = max(maxInNextCol, matrix[row - 1][nextCol])
            if row + 1 <= len(matrix) - 1:
                maxInNextCol = max(maxInNextCol, matrix[row + 1][nextCol])

            matrix[row][col] += maxInNextCol

            maxGold = max(maxGold, matrix[row][col])

    for row in matrix:
        print(row)
    print(maxGold)


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

getMaxGold(gold)
