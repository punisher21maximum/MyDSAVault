def maxSubsetSumNoAdjacent(array):

    if not array:
        return -1
    elif len(array) == 1:
        return array[0]

    maxSum = [array[0]]
    maxSum.append(max[array[0], array[1]])

    for i in range(len(array)):
        currentMax = max(maxSum[i-1], maxSum[i-2] + array[i])
        maxSum.append(currentMax)

    return maxSum[-1]
