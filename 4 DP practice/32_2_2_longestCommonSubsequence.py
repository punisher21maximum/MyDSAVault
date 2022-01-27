def longestCommonSubsequence(str1, str2, len1, len2):
    '''
    DP
    '''
    prevLcs = [0 for i in range(len1+1)]
    currLcs = [0 for i in range(len1+1)]

    for i in range(1, len2+1):
        prevLcs = currLcs
        currLcs = [0 for _ in range(len1+1)]
        for j in range(1, len1+1):
            if str1[j-1] == str2[i-1]:
                currLcs[j] = 1 + prevLcs[j-1]
            else:
                currLcs[j] = max(prevLcs[j], currLcs[j-1])

    return currLcs[-1]


str1 = "AGGTAB"
str2 = "GXTXAYB"
print(longestCommonSubsequence(str1, str2, len(str1), len(str2)))
