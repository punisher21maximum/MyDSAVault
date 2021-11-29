def heapify(array, startIdx, endIdx):

    print(startIdx)
    leftChildIdx = (startIdx * 2) + 1
    print(leftChildIdx)
    while leftChildIdx <= endIdx:
        if array[leftChildIdx] < array[startIdx]:
            array[startIdx], array[leftChildIdx] = array[leftChildIdx], array[startIdx]

        rightChildIdx = (startIdx * 2) + 2 if (startIdx * 2) + \
            2 <= endIdx else -1
        print(rightChildIdx)
        if rightChildIdx != -1:
            if array[rightChildIdx] < array[leftChildIdx]:
                array[leftChildIdx], array[rightChildIdx] = array[rightChildIdx], array[leftChildIdx]
                if array[leftChildIdx] < array[startIdx]:
                    array[leftChildIdx], array[startIdx] = array[startIdx], array[leftChildIdx]

        startIdx += 1
        leftChildIdx = (startIdx * 2) + 1


def heapSort(array):
    '''
    leftChildIdx = (idx * 2) + 1
    rightChildIdx = (idx * 2) + 2

    parent = (idx - 1) // 2

    lastChild = len(array) - 1
    lastParent = (lastChild - 1) // 2
    '''
    lastChild = len(array) - 1
    lastParent = (lastChild - 1) // 2
    for i in reversed(range(lastParent + 1)):
        print('a', array[i])
        heapify(array, i, len(array) - 1)
        print(array, array[i])
    # heapify(array, 0, len(array) - 1)


array = [12, 6, 13, 5, 11, 7]
heapSort(array)
print(array)
