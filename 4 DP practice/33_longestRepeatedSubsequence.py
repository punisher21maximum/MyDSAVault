def longestCommonSubsequenceLength(str1, len1):
    '''
    Given one string, find LRS, indices of both subsequence
    should be different.
    '''
    lcs = [[0 for i in range(len1+1)]
           for j in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len1+1):
            if str1[j-1] == str1[i-1] and i != j:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs[-1][-1]


def longestCommonSubsequence(str1, len1):
    '''
    Given one string, find LRS, indices of both subsequence
    should be different.
    '''
    lcs = [['' for i in range(len1+1)]
           for j in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len1+1):
            if str1[j-1] == str1[i-1] and i != j:
                lcs[i][j] = str1[i-1] + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)

    print(lcs)
    return lcs[-1][-1]


str1 = 'AABEBCDD'
print(longestCommonSubsequence(str1, len(str1)))
