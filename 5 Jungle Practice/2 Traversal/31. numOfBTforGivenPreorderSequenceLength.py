def getNumOfBTFromPreorderSequenceLength(N):
    '''
    Revise - Degree 3
    '''
    numOfBT = [0] * (N + 1)
    numOfBT[0] = numOfBT[1] = 1

    for i in range(2, N + 1):
        for j in range(i):
            numOfBT[i] += numOfBT[j] * numOfBT[i - 1 - j]

    print(numOfBT)


getNumOfBTFromPreorderSequenceLength(N=7)
