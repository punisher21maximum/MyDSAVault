def func(arr):
    """ """
    if len(arr) == 0:
        if arr[0] >= 1:
            return 1
        else:
            return 0

    minJumps = 1
    idx = 0

    while idx + arr[idx] < len(arr) - 1:

        nextIdx = None
        for i in range(idx + 1, idx + arr[idx] + 1):
            if nextIdx is None:
                nextIdx = i
            elif i + arr[i] > nextIdx + arr[nextIdx]:
                nextIdx = i

        idx = nextIdx
        minJumps += 1

    return minJumps


print(func([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))
