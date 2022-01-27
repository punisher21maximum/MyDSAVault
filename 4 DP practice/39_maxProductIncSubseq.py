def maxProdIncSubseq(array):
    '''
    Time Complexity: O(n^2) 
    Auxiliary Space : O(n)
    '''

    prodOfMaxprodSubseq = array[:]
    sequences = [None for _ in array]
    maxProdIdx = 0

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and prodOfMaxprodSubseq[j] * currVal > prodOfMaxprodSubseq[i]:
                prodOfMaxprodSubseq[i] = prodOfMaxprodSubseq[j] * currVal
                sequences[i] = j

        if prodOfMaxprodSubseq[i] >= prodOfMaxprodSubseq[maxProdIdx]:
            maxProdIdx = i

    print(buildSequence(array, sequences, maxProdIdx),
          prodOfMaxprodSubseq[maxProdIdx])


def buildSequence(array, sequences, idx):
    sequence = []

    while idx is not None:
        sequence.append(array[idx])
        idx = sequences[idx]

    return sequence[::-1]


maxProdIncSubseq([10, 22, 9, 33, 21, 50, 41, 60])
