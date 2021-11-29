def mainFunc(arr):
    '''
    Ques:
    For an array there can be
    1. shift rotate left by N
    2. shift rotate right by M
    3. print idx1 to idx 2

    Approach:
    we find effective shift rotate,
    with direction.
    also we have mutiple quick roptations,
    so we use, array of 2N size
    with original array duplicated 
    twice in it.
    '''
