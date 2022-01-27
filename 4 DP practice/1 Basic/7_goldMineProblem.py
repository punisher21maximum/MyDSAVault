def func(goldTable):
    """
    Problem: Given a matrix representing gold mine.
    Maxismise total gold. You start at first column.
    And can move by 1 to diag up, right or diag down.

    Approach:
    We start from last col and move towards other
    column on left.
    For each column, at each row we find the max
    value, from previous column (on left).
    When we reach first column, we keep track of max
    value.
    """
    m, n = len(goldTable), len(goldTable)
    maxValue = None
    for col in range(1, len(goldTable[0])):
        for row in range(0, len(goldTable)):
            currMax = goldTable[row][col - 1]
            if row - 1 >= 0:
                currMax = max(currMax, goldTable[row - 1][col - 1])
            if row + 1 <= len(goldTable) - 1:
                currMax = max(currMax, goldTable[row + 1][col - 1])

            goldTable[row][col] += currMax

            if col == len(goldTable[0]) - 1:
                if maxValue is None:
                    maxValue = goldTable[col][row]
                else:
                    maxValue = max(maxValue, goldTable[row][col])

    print(maxValue)
    for r in goldTable:
        print(r)
    return maxValue


func([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]])
