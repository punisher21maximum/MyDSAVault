def maxSumIncreasingSubsequence(array):

    sequence = [None for _ in array]
    sums = [num for num in array]
    maxSumIdx = 0

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and sums[j] + currVal >= sums[i]:
                sums[i] = sums[j] + currVal
                sequence[i] = j

        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    print(sums[maxSumIdx], buildSequence(array, sequence, maxSumIdx))


def buildSequence(array, sequence, idx):

    result = []

    while idx is not None:
        result.append(array[idx])
        idx = sequence[idx]

    return result[::-1]


maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])
