def mainFunc(arr):
    '''
    Find max sum(i * arr[i])

    Note:
    Rj - Rj-1 = arrSum - n * arr[n-j]
    So Rj = Rj-1 + arrSum - n * arr[n-j]

    Approach:
    1. find 
    '''
    arrSum = sum(arr)
    n = len(arr)
    currSum = 0
    for i in range(len(arr)):
        currSum += i * arr[i]

    maxSum = currSum
    prevSum = currSum
    for i in range(1, n):
        currSum = prevSum + arrSum - n * arr[n - i]
        maxSum = max(currSum, maxSum)
        prevSum = currSum
