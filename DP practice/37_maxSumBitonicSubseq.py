def longestIncreasingSubsequence(array):
    '''
    Bitonic sequence: first inc then dec 
    Algo:
    1. create array maxValueForIncSubseq, sum ending with arr[i]
    2. create array maxValueForDecSubseq, sum starting with arr[i]
    3. create array maxBitonicSubseq 
    = maxValueForIncSubseq + maxValueForDecSubseq - array[i]
    Time Complexity: O(n^2) 
    Auxiliary Space: O(n)
    '''

    maxValueForIncSubseq = array[:]
    for i in range(len(array)):
        currVal = array[i]
        for j in range(i):
            prevVal = array[j]
            if currVal > prevVal and maxValueForIncSubseq[j] + currVal > maxValueForIncSubseq[i]:
                maxValueForIncSubseq[i] = maxValueForIncSubseq[j] + currVal
    print(maxValueForIncSubseq)

    maxValueForDecSubseq = array[:]
    for i in range(len(array) - 1, -1, -1):
        currVal = array[i]
        for j in range(len(array) - 1, i, -1):
            prevVal = array[j]
            if currVal > prevVal and maxValueForDecSubseq[j] + currVal > maxValueForDecSubseq[i]:
                maxValueForDecSubseq[i] = maxValueForDecSubseq[j] + currVal
    print(maxValueForDecSubseq)

    sumOfMaxSumSubseq = float('-inf')
    for i in range(len(array)):
        sumOfMaxSumSubseq = max(sumOfMaxSumSubseq,
                                maxValueForIncSubseq[i] +
                                maxValueForDecSubseq[i] -
                                array[i])
    print(sumOfMaxSumSubseq)


longestIncreasingSubsequence([1, 15, 51, 45, 33,
                              100, 12, 18, 9])
