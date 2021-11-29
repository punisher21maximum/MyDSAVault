def merge(array, leftIdx, midIdx, rightIdx):
    '''
    merge func: merge two sorted arr, in sorted func
    '''

    leftArray = array[leftIdx: midIdx + 1]
    rightArray = array[midIdx + 1: rightIdx + 1]

    leftArrayIdx, rightArrayIdx, mergedArrayIdx = 0, 0, leftIdx
    while leftArrayIdx < len(leftArray) and rightArrayIdx < len(rightArray):
        if leftArray[leftArrayIdx] < rightArray[rightArrayIdx]:
            array[mergedArrayIdx] = leftArray[leftArrayIdx]
            leftArrayIdx += 1
        else:
            array[mergedArrayIdx] = rightArray[rightArrayIdx]
            rightArrayIdx += 1
        mergedArrayIdx += 1

    while leftArrayIdx < len(leftArray):
        array[mergedArrayIdx] = leftArray[leftArrayIdx]
        leftArrayIdx += 1
        mergedArrayIdx += 1

    while rightArrayIdx < len(rightArray):
        array[mergedArrayIdx] = rightArray[rightArrayIdx]
        rightArrayIdx += 1
        mergedArrayIdx += 1


def mergeSort(array, leftIdx, rightIdx):
    '''
    Time O(NlogN) | Space O(N)
    Algorithmic Paradigm: Divide and Conquer
    Sorting In Place: No in a typical implementation
    Stable: Yes 

    Adv:

    Dis:
    Extra memory O(N)
    It goes through the whole process even if the array is sorted.
    Slower comparative to the other sort algorithms for smaller tasks.
    '''
    if leftIdx >= rightIdx:
        return

    midIdx = leftIdx + (rightIdx - leftIdx) // 2

    mergeSort(array, leftIdx, midIdx)
    mergeSort(array, midIdx + 1, rightIdx)
    merge(array, leftIdx, midIdx, rightIdx)


array = [3, 7, 1, 33, -12, 4, 12, 99, -6]
mergeSort(array, 0, len(array) - 1)
print(array)
