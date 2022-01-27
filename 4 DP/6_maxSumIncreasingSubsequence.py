def getSequence(array, sequences, idx):

    sequence = []
    while idx is not None:
        sequence.append(array[idx])
        idx = sequences[idx]
    return sequence[::-1]


def maxSumIncreasingSubsequence(array):
    if len(array) == 1:
        return array[0]

    sums = array[:]
    sequences = [None] * len(array)
    maxSumIdx = 0

    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i] and array[i] + sums[j] >= sums[i]:
                sums[i] = array[i] + sums[j]
                sequences[i] = j

        if sums[i] > sums[maxSumIdx]:
            maxSumIdx = i

    return [sums[maxSumIdx], getSequence(array, sequences, maxSumIdx)]


maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])
