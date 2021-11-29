def lcsOf3Length(str1, str2, str3, len1, len2, len3):
    '''
    Without-DP, Recursion 
    '''
    if len1 == 0 or len2 == 0 or len3 == 0:
        return 0

    if str1[len1 - 1] == str2[len2 - 1] and \
            str2[len2 - 1] == str3[len3 - 1]:
        return 1 + lcsOf3Length(str1, str2, str3, len1-1, len2-1, len3-1)
    else:
        return max(lcsOf3Length(str1, str2, str3, len1-1, len2, len3),
                   lcsOf3Length(str1, str2, str3, len1, len2-1, len3),
                   lcsOf3Length(str1, str2, str3, len1, len2, len3-1))


def lcsOf3(str1, str2, str3, len1, len2, len3):
    '''
    Without-DP, Recursion 
    '''
    if len1 == 0 or len2 == 0 or len3 == 0:
        return 0

    if str1[len1 - 1] == str2[len2 - 1] and \
            str2[len2 - 1] == str3[len3 - 1]:
        return 1 + lcsOf3(str1, str2, str3, len1-1, len2-1, len3-1)
    else:
        return max(lcsOf3(str1, str2, str3, len1-1, len2, len3),
                   lcsOf3(str1, str2, str3, len1, len2-1, len3),
                   lcsOf3(str1, str2, str3, len1, len2, len3-1))


str1 = 'AGGT12'
str2 = '12TXAYB'
str3 = '12XBA'

print(lcsOf3Length(str1, str2, str3, len(str1), len(str2), len(str3)))
print(lcsOf3(str1, str2, str3, len(str1), len(str2), len(str3)))
