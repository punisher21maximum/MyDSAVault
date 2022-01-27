def mainFunc(arr, rotation, givenIdx):
    '''
    Ques:
    Find element at a given index, after
    multiple right rotations.

    Approach:
    Modify d.

    For 'd' right rotation, find 'idx' d units to left
    from givenIdx
    resultIdx = (givenIdx - d + n) % n

    For 'd' left rotation, find 'idx' d units to right
    from givenIdx
    resultIdx = (givenIdx + d) % n
    '''
    n = len(arr)
    resultIdx = (n - givenIdx - rotation) % n
    print(resultIdx, arr[resultIdx])


arr = list(range(1, 11))

mainFunc(arr, rotation=5, givenIdx=0)
