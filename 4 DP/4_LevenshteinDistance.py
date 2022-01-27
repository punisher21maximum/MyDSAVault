def levenshteinDistance(str1, str2):
    '''
    Question: return min number of edit operations on str1 to be done
    to obtain str2. Operations - insert, substitute, delete.
    '''

    numOfEdits = [[i for i in range(len(str1) + 1)]
                  for j in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        numOfEdits[i][0] = i

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i-1] == str1[j-1]:
                currentNumOfEdits = numOfEdits[i-1][j-1]
            else:
                currentNumOfEdits = min(numOfEdits[i-1][j],
                                        numOfEdits[i][j-1],
                                        numOfEdits[i-1][j-1]) + 1

            numOfEdits[i][j] = currentNumOfEdits

    return numOfEdits[-1][-1]
