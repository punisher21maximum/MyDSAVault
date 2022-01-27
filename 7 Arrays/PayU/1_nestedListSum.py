def getDepthSum(arr, depth=1, totalSum=0):
    '''
    Approach:
    we traverse the arr, if ele is value
    we add it to totalSum after multiplying
    by depth. if ele is nested list,
    we call func on it with curr depth + 1.
    '''
    for i in range(len(arr)):
        if isinstance(arr[i], int):
            totalSum += (arr[i] * depth)
        else:
            return getDepthSum(arr[i], depth+1, totalSum)

    return totalSum


print(getDepthSum([1, [4, [6]]]))
