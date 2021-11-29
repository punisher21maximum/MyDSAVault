def main(arr, index):
    '''
    Approach:
    Input:  arr[]   = [50, 40, 70, 60, 90]
            index[] = [3,  0,  4,  1,  2]
    Output: arr[]   = [40, 60, 90, 50, 70]
            index[] = [0,  1,  2,  3,   4]

    for i in range(len(index)):
        while idx != index[idx]:

            currVal = arr[i]
            newIdx = index[i]
            oldValAtNewIdx = arr[newIdx]

            # replace value
            arr[newIdx] = currVal
            index[i] = i 

            newIdx = index[newIdx]
            targetValOld = arr[index[i]]
            arr[index[i]] = arr[i]
    '''
