def longestCommonSubsequenceLength(str1, str2, len1, len2):
    '''
    DP
    '''
    lcs = [[0 for i in range(len1+1)]
           for j in range(len2+1)]

    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if str1[j-1] == str2[i-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs[-1][-1]


def longestCommonSubsequence(str1, str2, len1, len2):
    '''
    DP
    '''
    lcs = [['' for i in range(len1+1)]
           for j in range(len2+1)]

    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if str1[j-1] == str2[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + str1[j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)

    for r in lcs:
        print(r)
    return lcs[-1][-1]


str1 = "ZXVVYZW"
str2 = "XKYKZPW"
print(longestCommonSubsequence(str1, str2, len(str1), len(str2)))
