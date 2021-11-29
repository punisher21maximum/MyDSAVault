def mainFunc(arr, rotation, givenIdx):
    '''
    Ques:
    Find element at a given index, after
    multiple right rotations.

    Approach:
    We take the effective rotations,
    that is sum(all right rotations)%n.
    We check the element to left,
    with same rotation.
    givenIdx 
    resultIdx = find element x positions left
    resultIdx = givenIdx - effectiveRotation
    '''
    n = len(arr)
    resultIdx = (n - givenIdx - rotation) % n
    print(resultIdx, arr[resultIdx])


arr = list(range(1, 11))

mainFunc(arr, rotation=5, givenIdx=0)
