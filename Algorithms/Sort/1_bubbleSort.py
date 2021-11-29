def bubbleSort(array, n):
    '''
    Approach: Time O(N^2) | Space O(1)
    Sorting in inc order. We have to sort n-1 elements.
    So first loop runs n-1 times, sorting n-1 eles.
    In 2nd for loop, we sort one ele in each iteration,
    we traverse from left to right, while comparing 
    two nbring ele, moving the greater to right, till
    end. Nowwe sort list of size n-1
    Next iteration, we traverse one idx less than before.
    We place another largest ele at end, sort list of
    size n-2.
    '''
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(array)


array = [64, 25, 12, 22, 11, 99]
bubbleSort(array, len(array))
