'''
Modify 'd':
    d = (d % n) if d > 0 else (n - abs(d) % n)

Rotate array by 'd'
    Method1: Using Temp Array
    Time O(N) | Space O(d)
    Approach - 
    When we have to shift 'd' ele to left,
    we know the first 'd' ele will be moved to end
    and remaining will be shifted to left my 'd' units.

    So we put first 'd' ele in tempArray,
    shift remaining ele to left by 'd' units,
    and put ele at the end of array using tempArray.

    Method2: Rotate one by one
    Time O(N*d) | Space O(1)
    Approach - 
    1 rotation is like - put 1st ele in temp,
    shift all other by 1 unit,
    put ele in temp at last position.

    Repeat this d times.

    Method3: Reversal Algorithm
    Time O(N) | Space O(1)
    Approach - 
    To rotate an array by 'd', there are two parts
    in array, 1st d eles and rest of the array.
    Reverse(0 to d-1)
    Reverse(d to N-1)
    Reverse(o to N-1)

    Method4: Juggling Algo
    Time O(N) | Space O(1)
    Approach -
    Rotate ele in sets. First find hcf of arraySize and d.
    Number of sets equal to hcf. Rotate elements in sets,
    rotate 1st ele of each set, and so on.

Multiple Quick Rotations
    Method1: 2N array 
    Create a tempArr of size 2N, copy original arr
    in it twice.
    Keep startIdx at 0 and endIdx at N-1.
    Modify 'd'.
    Move both startIdx and endIdx by 'd', to right.
    Print array between startIdx and endIdx.

    Method2: Modular Arithmetic
    When moving right
        idx = (idx + 1) % N
    When moving left
        idx = (idx - 1 + N) % N

    Rotate right by 'd'
        startIdx = (startIdx + d) % N
        endIdx = (endIdx + d) % N
    Rotate lefy by 'd'
        startIdx = (startIdx - d + N) % N
        endIdx = (endIdx - d + N) % N
'''
