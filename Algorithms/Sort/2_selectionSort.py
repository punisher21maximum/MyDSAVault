def selectionSort(array, n):
    '''
    Approach: Time O(N^2) | Space O(1)
    We find the idx of smallest ele in list of size n, 0 to n-1,
    swap it with startIdx of list, idx 0.
    Then we find idx of smallest ele in list of size n-1, 1 to n-1
    swap it with start of list, idx 1.
    '''
    for i in range(n - 1):
        minValIdx = i
        for j in range(i, n):
            if array[j] < array[minValIdx]:
                minValIdx = j
        array[i], array[minValIdx] = array[minValIdx], array[i]

    print(array)


array = [64, 25, 12, 22, 11]
selectionSort(array, len(array))
