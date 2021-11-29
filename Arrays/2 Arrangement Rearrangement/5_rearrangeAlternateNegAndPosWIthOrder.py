def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def main(arr):
    '''
    Question: Given array with pos and neg, intergers.
    Rearrage as such, alternate pos and nef. Extra
    num at the end. Maintaining the order of 
    appearance.

    Approach:

    '''
    nextPosIdx, nextNegIdx, idx = 1, 1, 0
    n = len(arr)
    while idx < n:
        print('>>>', arr[idx])
        if (idx + 1) % 2 == 1:  # odd idx
            print('odd')
            if arr[idx] < 0:
                print(' ', 'neg')
                # search next posIdx
                nextPosIdx = max(nextPosIdx, idx)
                while nextPosIdx < n:
                    if arr[nextPosIdx] > 0:
                        break
                    nextPosIdx += 1
                if nextPosIdx >= n:
                    break
                arr = swap(arr, idx, nextPosIdx)
                nextNegIdx = min(nextNegIdx, nextPosIdx)
            posIdx = idx + 2
        else:  # even idx, should be neg
            print('even')
            if arr[idx] > 0:  # if pos
                print(' ', 'pos')
                # search next neg
                nextNegIdx = max(nextNegIdx, idx)
                while nextNegIdx < n:
                    if arr[nextNegIdx] < 0:
                        break
                    nextNegIdx += 1
                if nextNegIdx >= n:
                    break
                arr = swap(arr, idx, nextNegIdx)
                nextPosIdx = min(nextPosIdx, nextNegIdx)
            negIdx = idx + 2
        print(arr, idx, nextPosIdx, nextNegIdx)
        idx += 1

    print(arr)


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
main(arr)
