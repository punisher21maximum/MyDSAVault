def longestIncreasingSubsequence(array):
    '''
    Bitonic sequence: first inc then dec 
    Algo:
    1. create array longestIncSubseqLen, sequence ending with arr[i]
    2. create array longestDecSubseqLen, sequence starting with arr[i]
    3. create array longestBitonicSubseq 
    = longestIncSubseqLen + longestDecSubseqLen - 1
    Time Complexity: O(n^2) 
    Auxiliary Space: O(n)
    '''

    longestIncSubseqLen = [1 for num in array]
    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and longestIncSubseqLen[j] + 1 > longestIncSubseqLen[i]:
                longestIncSubseqLen[i] = longestIncSubseqLen[j] + 1

    longestDecSubseqLen = [1 for num in array]
    for i in range(len(array) - 1, -1, -1):
        currVal = array[i]
        for j in range(len(array) - 1, i, -1):
            prevVal = array[j]
            if currVal > prevVal and longestDecSubseqLen[j] + 1 > longestDecSubseqLen[i]:
                longestDecSubseqLen[i] = longestDecSubseqLen[j] + 1

    longestBitonicSubseqLen = []
    maxSeqIdx = 0
    for i in range(len(array)):
        longestBitonicSubseqLen.append(
            longestIncSubseqLen[i] +
            longestDecSubseqLen[i] - 1
        )

        if longestBitonicSubseqLen[i] >= longestBitonicSubseqLen[maxSeqIdx]:
            maxSeqIdx = i

    print(longestBitonicSubseqLen[maxSeqIdx])


longestIncreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
                              3, 11, 7, 15])
