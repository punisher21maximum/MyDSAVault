def binarySearch(array, leftIdx, rightIdx, targetEle):
    '''
    input - sorted array
    '''
    if leftIdx > rightIdx:
        print('Not found')
        return

    midIdx = leftIdx + (rightIdx - leftIdx) // 2

    if array[midIdx] == targetEle:
        print('found')
    elif targetEle < array[midIdx]:
        return binarySearch(array, leftIdx, midIdx - 1, targetEle)
    else:
        return binarySearch(array, midIdx + 1, rightIdx, targetEle)


array = [2, 3, 4, 10, 40]
binarySearch(array, 0, len(array) - 1, 10)
