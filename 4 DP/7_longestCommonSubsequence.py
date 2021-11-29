def getLonger(str1, str2):
    if len(str1) >= len(str2):
        return str1
    return str2


def longestCommonSubsequence(str1, str2):

    sequences = [["" for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str1[j-1] == str2[i-1]:
                sequences[i][j] = sequences[i-1][j-1] + str1[j-1]
            else:
                sequences[i][j] = getLonger(
                    sequences[i-1][j], sequences[i][j-1])

    for r in sequences:
        print(r)
    return list(sequences[-1][-1])


longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
