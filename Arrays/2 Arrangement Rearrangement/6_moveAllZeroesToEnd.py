def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def main(arr):
    '''
    Question: Move all zeroes to end.

    Approach:
    Use quicksort partition function, traverse
    array from last, find zeroes in from last
    to first and put them from last towards first
    '''
    idx = len(arr) - 1  # start from last
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr = swap(arr, i, idx)
            idx -= 1
    print(arr)


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
main(arr)
