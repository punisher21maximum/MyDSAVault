def getIdxOfLargest(arr):

    largest = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            idx = i

    return idx


def mainFunc(arr, target, n):
    '''
    sorted inc order
    '''

    p2 = getIdxOfLargest(arr)
    p1 = (p2 + 1) % n

    while p1 != p2:
        currSum = arr[p1] + arr[p2]
        if currSum == target:
            print(p1, p2, '>', arr[p1], arr[p2])
            p1 = (p1 + 1) % n
            p2 = (p2 - 1 + n) % n
        elif currSum < target:
            p1 = (p1 + 1) % n
        elif currSum > target:
            p2 = (p2 - 1 + n) % n


arr = [11, 15, 6, 8, 9, 10]
target = 16
mainFunc(arr, target, len(arr))
