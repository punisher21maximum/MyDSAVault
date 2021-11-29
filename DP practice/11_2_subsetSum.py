def subsetSum(array, targetSum):
    '''
    DP:

    set[]={3, 4, 5, 2}
    target=6

        0    1    2    3    4    5    6

    0   T    F    F    F    F    F    F

    3   T    F    F    T    F    F    F

    4   T    F    F    T    T    F    F   

    5   T    F    F    T    T    T    F

    2   T    F    T    T    T    T    T
    '''
    result = [[False for _ in range(targetSum + 1)]
              for _ in range(len(array) + 1)]

    for i in range(len(result)):
        # for 0 amt all True
        result[i][0] = True

    for r in range(1, len(array) + 1):
        currValue = array[r-1]
        for c in range(1, targetSum + 1):
            currTargetSum = c
            if currValue > currTargetSum:
                result[r][c] = result[r-1][c]
            else:
                print(r, currTargetSum - currValue)
                result[r][c] = (result[r-1][c] or
                                result[r-1][currTargetSum - currValue])

    result = [['T' if B else 'F' for B in row] for row in result]
    for r in result:
        print(r)


array = [3, 4, 5, 2]  # [3, 34, 4, 12, 5, 2]
targetSum = 6  # 9
subsetSum(array, targetSum)
