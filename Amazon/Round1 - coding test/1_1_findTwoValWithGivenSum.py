

def updateResult(resultVal, resultIdx,
                 newPotentialResultVal,
                 newPotentialResultIdx):

    if (newPotentialResultVal[0] > max(resultVal) or
            newPotentialResultVal[1] > max(resultVal)):
        resultVal = newPotentialResultVal
        resultIdx = newPotentialResultIdx

    return (resultVal, resultIdx)


def method1(array, K):  # Brute

    resultVal = [-1, -1]
    resultIdx = [-1, -1]

    for i in range(len(array)):
        for j in range(i, len(array)):
            if i != j and array[i] + array[j] == K:
                newPotentialResultVal = [array[i], array[j]]
                newPotentialResultIdx = [i, j]
                resultVal, resultIdx = updateResult(resultVal,
                                                    resultIdx,
                                                    newPotentialResultVal,
                                                    newPotentialResultIdx)

    print(resultIdx, [array[i] for i in resultIdx])


def updateResult2(resultIdx,
                  newPotentialResultIdx):

    resultVal = [array[idx] for idx in resultIdx]
    newPotentialResultVal = [array[idx] for idx in newPotentialResultIdx]

    if (newPotentialResultVal[0] > max(resultVal) or
            newPotentialResultVal[1] > max(resultVal)):
        resultIdx = newPotentialResultIdx

    return resultIdx


def method1_2(array, K):  # Brute

    resultIdx = [-1, -1]

    for i in range(len(array)):
        for j in range(i, len(array)):
            if i != j and array[i] + array[j] == K:
                newPotentialResultIdx = [i, j]
                resultIdx = updateResult2(resultIdx,
                                          newPotentialResultIdx)

    print(resultIdx, [array[i] for i in resultIdx])


def method2(array, K):  # Brute

    resultIdx = [-1, -1]
    hashTable = {array[i]: i for i in range(len(array))}

    for i in range(len(array)):
        remainingVal = K - array[i]
        if remainingVal in hashTable:
            newPotentialResultIdx = [i, hashTable[remainingVal]]
            resultIdx = updateResult2(resultIdx,
                                      newPotentialResultIdx)

    print(resultIdx, [array[i] for i in resultIdx])


def method3(array, K):  # Brute

    resultIdx = [-1, -1]
    array = sorted(array)

    leftIdx, rightIdx = 0, len(array) - 1
    while leftIdx < rightIdx:
        currSum = array[leftIdx] + array[rightIdx]
        if currSum < K:
            leftIdx += 1
        elif currSum > K:
            rightIdx -= 1
        else:
            newPotentialResultIdx = [leftIdx, rightIdx]
            resultIdx = updateResult2(resultIdx,
                                      newPotentialResultIdx)

            leftIdx += 1
            rightIdx -= 1

    print(resultIdx, [array[i] for i in resultIdx])


def mainFunc(array, K):
    '''
    Problem: Given array and integer K. Find values in array with given sum
    amd return idx, if >1 solutions, select the pair, which has max value.

    Approach:
    For each Method, Also update result, if a another solution, with higher
    value found.

    Method1 Brute Force Time (N^2):
    Two forloops, nested. Find if sum is equal to K. 

    Method2 HashTable Time O(N) | Space O(N):
    Creata a hashTable, set keys as values in array and value of keys as indices
    from array. For each value in array, we find (X - array[i]) in hashTable.

    Method3 Two pointers on sorted array :
    We sort the given array in increasing order, and keep two pointers, P1 at 
    start and P2 at the end. currVal if sum of value at P1 and P2. 
    If currVal < X then move P1 to right or if currVal > X then move P2 to left.
    If currVal equal to X, solution found, move P1 to right and P2 to left. 
    '''

    method1(array, K)
    method1_2(array, K)
    method2(array, K)
    method3(array, K)


array = [1, 4, 45, 6, 10, 8, 12, 4]
K = 16
mainFunc(array, K)
