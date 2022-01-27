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
    Note in similar problem of - Find given sum in sorted array.
    Approach:
    We use two pointer, P1 - pointing smallest and P2 - pointing
    largest. If currSum > givenSum, move P2 to left, if currSum
    < givenSum, move P1 to right. If currSum == givenSum print
    solution and move both.

    P1 (left pointer) start at idx 0 | moves --> P1 += 1
    P2 (right pointer) start at idx N-1 | moves --> P2 -= 1

    So in current problem of - Find given sum in sorted and rotated
    array.
    Approach:
    P1 start at idx of smallest ele | moves --> P1 = (P1 + 1) % N
    P2 start at idx of largest ele | moves --> P2 = (P2 - 1 + N) % N
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
