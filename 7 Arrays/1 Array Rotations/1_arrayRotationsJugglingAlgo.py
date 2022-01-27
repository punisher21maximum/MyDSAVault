def getHcf(a, b):
    if b == 0:
        return a
    return getHcf(b, a % b)


def mainFunc(arr, d, n):
    '''
    Rotate array to right by d, If d is negative rotate left.
    Approach:
    Method1 - Temp array:
    O(N) extra space

    Method2 - rotate one by one:

    Method3 - Juggling algorithm - Time O(N) | Space O(1):
    Rotate ele in sets. First find hcf of arraySize and d.
    Number of sets equal to hcf. Rotate elements in sets,
    rotate 1st ele of each set, and so on.
    '''
    d = (d % n) if d > 0 else (n - abs(d) % n)
    hcf = getHcf(d, n)

    for i in range(hcf):
        temp = arr[i]
        currIdx = i
        while True:
            nextIdx = (currIdx + d) % n
            if nextIdx == i:
                break
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx
        arr[currIdx] = temp

    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
mainFunc(arr, d, n)
