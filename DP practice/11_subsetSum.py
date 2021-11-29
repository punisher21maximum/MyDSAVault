def subsetSum(array, targetSum, subset=[], idx=0):
    '''
    Recusrion
    '''
    if idx >= len(array):
        return False

    for i in range(idx, len(array)):
        if array[i] <= targetSum:
            targetSum -= array[i]
            subset.append(array[i])

            if targetSum == 0:
                return subset

            if subsetSum(array, targetSum, subset, i + 1):
                return True
            else:
                print('Not Possible')
                return False

    return subset


array = [3, 34, 4, 12, 5, 2]
targetSum = 9
print(subsetSum(array, targetSum))
