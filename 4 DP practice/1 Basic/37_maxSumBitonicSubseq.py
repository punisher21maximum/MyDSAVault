def func(arr):
    """
    Bi-tonic Subseq - first inc then dec

    Approach:
    1. find maxSumIncSubseq
    2. find maxSumDecSubseq
    3. find max(maxSumIncSubseq[i] + maxSumDecSubseq[i] - arr[i])
    """
    N = len(arr)

    maxSumIncSubseq = arr[:]
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j] and maxSumIncSubseq[j] + arr[i] >= maxSumIncSubseq[i]:
                maxSumIncSubseq[i] = maxSumIncSubseq[j] + arr[i]

    maxSumDecSubseq = arr[:]
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if arr[i] > arr[j] and maxSumDecSubseq[j] + arr[i] >= maxSumDecSubseq[i]:
                maxSumDecSubseq[i] = maxSumDecSubseq[j] + arr[i]

    maxSumBitonicVal = float("-inf")
    for i in range(N):
        maxSumBitonicVal = max(
            maxSumBitonicVal, maxSumIncSubseq[i] + maxSumDecSubseq[i] - arr[i]
        )

    print(maxSumIncSubseq)
    print(maxSumDecSubseq)
    print(maxSumBitonicVal)


func([1, 15, 51, 45, 33, 100, 12, 18, 9])
