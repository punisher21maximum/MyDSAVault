def main(a, ia):
    """
    Approach:
    Input:  a[]   = [50, 40, 70, 60, 90]
            ia[] = [3,  0,  4,  1,  2]
    Output: a[]   = [40, 60, 90, 50, 70]
            ia[] = [0,  1,  2,  3,   4]

    for i in range(len(ia)):
        while idx != ia[idx]:

            currVal = a[i]
            newIdx = ia[i]
            oldValAtNewIdx = a[newIdx]

            # replace value
            a[newIdx] = currVal
            ia[i] = i

            newIdx = ia[newIdx]
            targetValOld = a[ia[i]]
            a[ia[i]] = a[i]
    """

    for i in range(len(a)):
        while ia[i] != i:
            a[i], a[ia[i]] = a[ia[i]], a[i]
            ia[i], ia[ia[i]] = ia[ia[i]], ia[i]
