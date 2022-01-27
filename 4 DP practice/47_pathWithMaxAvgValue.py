def mainFunc(matrix):
    '''
    Problem:
    Given a matrix of N*N, each cell has a cost.
    Travel: from top-left to bottom-right.
    Allowed movement: down or right only.
    Maximise avg cost = total cost / num cells 

    Thoery:
    for N*N matrix, for everypath we travel = (2*N - 1) cells.
    so we have to maximise the travel cost.

    Approach:
    for first col:
        for row in matrix: maxtrix[row][0] = matrix[row-1][0] + cost[row][0]
    for first row:
        for col in matrix: maxtrix[0][col] = matrix[0][col-1] + cost[0][col]
    for rest:
        maxtrix[row][col] = max(matrix[row-1][col], matrix[row][col-1]) + cost[row][col]
    '''
    N = len(matrix)  # N = num of rows/cols

    for row in range(1, N):  # first col
        matrix[row][0] += matrix[row-1][0]

    for col in range(1, N):  # first row
        matrix[0][col] += matrix[0][col-1]

    for row in range(1, N):
        for col in range(1, N):
            matrix[row][col] += max(matrix[row-1][col],
                                    matrix[row][col-1])

    print(matrix[-1][-1], matrix[-1][-1]/(2*N-1))


mainFunc([[1, 2, 3],
          [6, 5, 4],
          [7, 3, 9]])
