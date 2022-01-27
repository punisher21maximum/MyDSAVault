def reverseArr(arr, startIdx, endIdx):

    if endIdx > len(arr) - 1:
        print("end idx out of range")
        return arr

    numOfEle = endIdx - startIdx + 1
    for i in range(numOfEle // 2):
        arr[startIdx + i], arr[endIdx - i] = arr[endIdx - i], arr[startIdx + i]

    return arr


def mainFunc(arr, d, n):
    """
    Rotate array to right by d, If d is negative rotate left.
    Approach:
    Method4 - Reversal Algo Time O(N):
    rotate(arr[], d, n)
        reverse(arr[], 1, d) ;
        reverse(arr[], d + 1, n);
        reverse(arr[], 1, n);
    """
    d = (d % n) if d > 0 else (n - abs(d) % n)

    arr = reverseArr(arr, 0, d - 1)
    arr = reverseArr(arr, d, n - 1)
    arr = reverseArr(arr, 0, n - 1)

    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = -2
mainFunc(arr, d, n)
