def rearrangeArray(arr):
    '''
    Question:Given an array of n elements. Our task is to write 
    a program to rearrange the array such that elements at even 
    positions are greater than all elements before it and elements 
    at odd positions are less than all elements before it.

    Approach:
    Note:
    The resultant array, will be in inc order at even positions
    and dec order in odd positions.

    Arr2, copy of arr. sort arr2 in inc order. Now create two
    arrays, left and right. left is reversed first half of arr2,
    right is 2nd half of arr2. Merge arr taking ele alternately
    from left and right array.

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [5, 4, 3, 2, 1] [6, 7, 8, 9, 10]
    [5, 6, 4, 7, 3, 8, 2, 9, 1, 10]

    create arr2, copy of arr, sort arr2 in inc order.
    Now keep two pointers, l and r, to traverse arr2, from both sides.

    if lenn of arr is odd, last position is odd else even. 
    l, r = 0, n-1
    for i in range(n, 2):
        arr[i] = arr2[ceil(n/2) - i]
    for i in range(1, n, 2):
        arr[i] = arr2[ceil(n/2) + 1 + i]
    '''
