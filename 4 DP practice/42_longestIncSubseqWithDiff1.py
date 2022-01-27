def func(array):
    '''
    Time Complexity: O(n2) 
    Auxiliary Space: O(n)
    '''

    lenOfLongestSubseq = [1 for _ in array]
    maxLenSeqIdx = 0

    sequences = [None for _ in array]

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if abs(currVal - prevVal) == 1:
                lenOfLongestSubseq[i] = max(lenOfLongestSubseq[i],
                                            lenOfLongestSubseq[j] + 1)
                sequences[i] = j

        if lenOfLongestSubseq[i] >= lenOfLongestSubseq[maxLenSeqIdx]:
            maxLenSeqIdx = i

    print(buildSequence(array, sequences, maxLenSeqIdx),
          lenOfLongestSubseq[maxLenSeqIdx])


def buildSequence(array, sequences, idx):
    sequence = []

    while idx is not None:
        sequence.append(array[idx])
        idx = sequences[idx]

    return sequence[::-1]


func([2, 5, 6, 3, 7, 6, 5, 8])
