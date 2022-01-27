def insertionSort(array):
    """
    Approach:
    Time Complexity: O(n^2)
    Auxiliary Space: O(1)

    Sort list in inc order.
    We traverse the list, if we find ele GT prev ele,
    we move forward, but if ele if LT prev ele.
    We traverse from currIdx towards left, while the
    prev ele is LT smallerEle we found and idx >= 1
    and shift the eles to right. Than place ele
    at the idx.
    """
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            idx = i
            smallerVal = array[idx]

            while idx >= 1 and array[idx - 1] > smallerVal:
                array[idx] = array[idx - 1]
                idx -= 1
            array[idx] = smallerVal

    print(array)


array = [64, 25, 12, 22, 11, 99]
insertionSort(array)
