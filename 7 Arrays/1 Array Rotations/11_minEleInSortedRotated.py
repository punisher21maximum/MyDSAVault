def modifiedBinarySearch(arr, l, r):
    '''
    sorted in inc order
    Approach Time O(logN):
    Note - for only smallest ele, it's prev is greater.
    We use modified binary search.
    Algo:
    Find mid, check if mid smallest. 
    if lastEle < mid than check in Right half
    else in leftHalf
    '''
    if len(arr) == 1:
        return arr[0]

    midIdx = l + (r - l) // 2

    if arr[midIdx-1] > arr[midIdx]:
        return arr[midIdx]
    elif arr[midIdx] > arr[r]:
        return modifiedBinarySearch(arr, midIdx + 1, r)
    else:  # arr[l] <= arr[midIdx]:
        return modifiedBinarySearch(arr, l, midIdx - 1)


arrs = [[5, 6, 1, 2, 3, 4],
        [1, 2, 3, 4],
        [1],
        [1, 2],
        [2, 1],
        [5, 6, 7, 1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6, 7],
        [2, 3, 4, 5, 6, 7, 8, 1],
        [3, 4, 5, 1, 2]
        ]
for arr in arrs:
    print(modifiedBinarySearch(arr, 0, len(arr) - 1))
