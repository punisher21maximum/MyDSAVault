def func(arr):
    """
    Given -

    T O(N^2) | S O(N)
    """
    MSIS = arr[:]
    sequences = [None] * len(arr)
    MSISIdx = 0

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and MSIS[j] + arr[i] >= MSIS[i]:
                MSIS[i] = MSIS[j] + arr[i]
                sequences[i] = j

            if MSIS[i] > MSIS[MSISIdx]:
                MSISIdx = i

    print(MSIS[MSISIdx], buildSequence(arr, MSISIdx, sequences))


def buildSequence(arr, MSISIdx, sequences):
    sequence = []

    while MSISIdx is not None:
        sequence.append(arr[MSISIdx])
        MSISIdx = sequences[MSISIdx]

    return sequence[::-1]


arr = [1, 101, 2, 3, 100, 4, 5]
func(arr)
