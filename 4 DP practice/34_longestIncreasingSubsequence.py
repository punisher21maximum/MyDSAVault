def longestIncreasingSubsequence(array):

    seqLength = [1 for num in array]
    maxSeqIdx = 0

    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and seqLength[j] + 1 > seqLength[i]:
                seqLength[i] = seqLength[j] + 1

        if seqLength[i] >= seqLength[maxSeqIdx]:
            maxSeqIdx = i

    print(seqLength, seqLength[maxSeqIdx])


longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60])
