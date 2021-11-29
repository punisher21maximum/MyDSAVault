def partition(array, leftIdx, rightIdx):
    idx = leftIdx

    # pivot is rightIdx
    for i in range(leftIdx, rightIdx):
        if array[i] < array[rightIdx]:
            array[i], array[idx] = array[idx], array[i]
            idx += 1

    array[idx], array[rightIdx] = array[rightIdx], array[idx]

    return idx


def quickSort(array, leftIdx, rightIdx):
    '''
    Space O(1)

    Worst Case: Time O(N^2)
        When the partition process always picks greatest 
        or smallest element as pivot.

        Above pivot is last ele, worst case occurs when, 
        already sorted in inc or dec order.

    Best Case: Time O(logN)
        Partition process always picks the middle element 
        as pivot.

    Average Case: Time O(logN)

    Is QuickSort stable? 
        The default implementation is not stable. However any sorting algorithm can be made stable by considering indexes as comparison parameter. 

    Is QuickSort In-place? 
        As per the broad definition of in-place algorithm it qualifies as an in-place sorting algorithm as it uses extra space only for storing recursive function calls but not for manipulating the input. 
    '''
    if leftIdx >= rightIdx:
        return

    partitionIndex = partition(array, leftIdx, rightIdx)

    quickSort(array, leftIdx, partitionIndex - 1)
    quickSort(array, partitionIndex + 1, rightIdx)


array = [64, 25, 12, 22, 11, 99]
quickSort(array, 0, len(array) - 1)
print(array)
