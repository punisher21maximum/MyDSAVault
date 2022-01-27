def maxSumIncSubseq(array):

    sumOfMaxSumSubseq = array[:]
    sequences = [None for _ in array]
    maxSumIdx = 0

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and sumOfMaxSumSubseq[j] + currVal > sumOfMaxSumSubseq[i]:
                sumOfMaxSumSubseq[i] = sumOfMaxSumSubseq[j] + currVal
                sequences[i] = j

        if sumOfMaxSumSubseq[i] >= sumOfMaxSumSubseq[maxSumIdx]:
            maxSumIdx = i

    print(sumOfMaxSumSubseq[maxSumIdx],
          buildSequence(array, sequences, maxSumIdx), sequences)


def buildSequence(array, sequences, idx):
    sequence = []

    while idx is not None:
        sequence.append(array[idx])
        idx = sequences[idx]

    return sequence[::-1]


maxSumIncSubseq([1, 101, 2, 3, 100, 4, 5])
