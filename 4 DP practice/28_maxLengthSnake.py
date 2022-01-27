def maxLengthSnake(matrix, col=0):
    '''
    Snake can move:
        - 1 right or 1 down
        - next value  =  +-1 current value 
    '''
    maxLenArray = [[1 for col in range(len(matrix[0]))]
                   for row in range(len(matrix))]

    for row in range(len(matrix)):
        rightCol = col + 1
        rightVal = matrix[row][rightCol]
        currVal = maxLenArray[row][col]
        if (rightCol < len(matrix[0])
            and (rightVal + 1 == currVal
                 or rightVal - 1 == currVal)):
            maxLengthSnake(matrix, col + 1)


    return matrix