def modifiedBinarySearch(arr, l, r, target):
    '''
    Find ele in sorted and rotated array.
    Approach:
    Method 1: Find the two subarrays, apply
    binarySearch on each.
    Method 2: Modify binarySearch, when
    searching in left and right halves,
    check in the half which is sorted,
    will find faster.
    '''
    if l > r:
        return -1

    midIdx = l + (r - l)//2
    midVal = arr[midIdx]

    if target == midVal:
        return midIdx
    elif arr[l] <= arr[midIdx]:  # if L is sorted
        if target >= arr[l] and target < arr[midIdx]:
            # if target in L
            return modifiedBinarySearch(arr, l, midIdx - 1, target)
        # if target in R
        return modifiedBinarySearch(arr, midIdx + 1, r, target)
    else:
        # if R is sorted
        if target > arr[midIdx] and target <= arr[r]:
            # if target in R
            return modifiedBinarySearch(arr, midIdx + 1, r, target)
        # if target in left
        return modifiedBinarySearch(arr, l, midIdx - 1, target)


def binarySearch(arr, l, r, target):
    if l > r:
        return -1

    midIdx = l + (r - l)//2
    midVal = arr[midIdx]

    if target == midVal:
        return midIdx
    elif target < midVal:
        return binarySearch(arr, l, midIdx - 1, target)
    else:
        return binarySearch(arr, midIdx + 1, r, target)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 0, len(arr) - 1, 11))
