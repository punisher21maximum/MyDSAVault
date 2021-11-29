def mainFunc(arr, d):
    '''
    Ques:
    Print multiple left rotations based on,
    the input. In Time (N) | Space (1)

    Approach:
    For left rotation, our new first element
    is on right before rotation, in comparision 
    to original array.
    So if rotate by 3, our new first element
    is on index 4 (1 indexing).
    So based on input we decide our startIdx
    and print the n elements, after last
    we go to print from first.
    '''
    startIdx = d
    n = len(arr)
    for i in range(n):
        idx = (startIdx + i) % n
        print(arr[idx], end=' ')
    print()


arr = [1, 3, 5, 7, 9]
dArray = [1, 2, 3, 4]
for d in dArray:
    mainFunc(arr, d)
