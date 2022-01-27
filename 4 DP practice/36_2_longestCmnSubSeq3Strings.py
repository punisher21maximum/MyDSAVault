def lcsOf3Length(str1, str2, str3, len1, len2, len3):
    '''
    DP
    '''
    lcs = [[[0 for i3 in range(len3+1)]
            for i2 in range(len2+1)]
           for i1 in range(len1+1)]

    for i1 in range(len1+1):
        for i2 in range(len2+1):
            for i3 in range(len3+1):
                if i1 == 0 or i2 == 0 or i3 == 0:
                    lcs[i1][i2][i3] = 0
                elif str1[i1-1] == str2[i2-1] and str1[i1-1] == str3[i3-1]:
                    lcs[i1][i2][i3] = lcs[i1-1][i2-1][i3-1] + 1
                else:
                    lcs[i1][i2][i3] = max(lcs[i1-1][i2][i3],
                                          lcs[i1][i2-1][i3],
                                          lcs[i1][i2][i3-1])

    print(lcs[-1][-1][-1])


def lcsOf3(str1, str2, str3, len1, len2, len3):
    '''
    DP
    '''
    lcs = [[['' for i3 in range(len3+1)]
            for i2 in range(len2+1)]
           for i1 in range(len1+1)]

    for i1 in range(len1+1):
        for i2 in range(len2+1):
            for i3 in range(len3+1):
                if i1 == 0 or i2 == 0 or i3 == 0:
                    lcs[i1][i2][i3] = ''
                elif str1[i1-1] == str2[i2-1] and str1[i1-1] == str3[i3-1]:
                    lcs[i1][i2][i3] = lcs[i1-1][i2-1][i3-1] + str1[i1-1]
                else:
                    lcs[i1][i2][i3] = max(lcs[i1-1][i2][i3],
                                          lcs[i1][i2-1][i3],
                                          lcs[i1][i2][i3-1], key=len)

    print(lcs[-1][-1][-1])


str1 = 'AGGT12'
str2 = '12TXAYB'
str3 = '12XBA'

lcsOf3Length(str1, str2, str3, len(str1), len(str2), len(str3))
lcsOf3(str1, str2, str3, len(str1), len(str2), len(str3))
