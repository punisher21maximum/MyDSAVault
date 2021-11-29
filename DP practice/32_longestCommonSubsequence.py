def longestCommonSubsequence(str1, str2, len1, len2):
    '''
    Recursion | O(n * 2n)
    '''
    if len1 == 0 or len2 == 0:
        return 0
    elif str1[len1 - 1] == str2[len2 - 1]:
        return 1 + longestCommonSubsequence(str1, str2, len1-1, len2-1)
    else:
        return max(longestCommonSubsequence(str1, str2, len1-1, len2),
                   longestCommonSubsequence(str1, str2, len1, len2-1))


str1 = "AGGTAB"
str2 = "GXTXAYB"
print(longestCommonSubsequence(str1, str2, len(str1), len(str2)))
