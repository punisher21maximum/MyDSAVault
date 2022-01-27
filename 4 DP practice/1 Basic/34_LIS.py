def LIS(arr):
    """
    Given - array, find longest inc subseq.

    T O(N^2) | S O(N)
    """
    lis = [1] * len(arr)
    sequences = [None] * len(arr)
    lisIdx = 0

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[j] + 1 >= lis[i]:
                lis[i] = lis[j] + 1
                sequences[i] = j

            if lis[i] > lis[lisIdx]:
                lisIdx = i

    print(buildSequence(arr, lisIdx, sequences))


def buildSequence(arr, lisIdx, sequences):
    sequence = []

    while lisIdx is not None:
        sequence.append(arr[lisIdx])
        lisIdx = sequences[lisIdx]

    return sequence[::-1]


arr = [10, 22, 9, 33, 21, 50, 41, 60]
LIS(arr)
