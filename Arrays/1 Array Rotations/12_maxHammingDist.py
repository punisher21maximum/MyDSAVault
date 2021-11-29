def maxHam(arr):
    '''
    Ques: max hamming dist is the count of number of
    ele diff in two arrays at corresponding position.

    Approach:
    Here note, we have to compare the original arr
    with each possible rotation (which is n).
    For "mutiple quick rotations" we use temp arr
    of size 2N with original arr duplicated twice in 
    it.
    '''

    arr2 = arr[:] * 2

    maxHam = 0
    for i in range(len(arr)):
        startIdx = i  # for current rotation
        currHam = 0
        for j in range(len(arr)):  # traverse both arr
            if arr[j] != arr2[startIdx + j]:
                currHam += 1
        maxHam = max(currHam, maxHam)

    return maxHam


arr = [2, 4, 6, 8]
print(maxHam(arr))
