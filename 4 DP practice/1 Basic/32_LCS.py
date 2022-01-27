def LCSRecursive(s1, s2, len1, len2):

    if len1 == 0 or len2 == 0:
        return ""

    if s1[len1 - 1] == s2[len2 - 1]:
        return LCSRecursive(s1, s2, len1 - 1, len2 - 1) + s1[len1 - 1]
    else:
        return max(
            LCSRecursive(s1, s2, len1 - 1, len2),
            LCSRecursive(s1, s2, len1, len2 - 1),
            key=len,
        )


def LCS(s1, s2):
    """
    M*N space
    """

    DP = [[None for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]

    # No common subseq in two empty strings
    DP[0][0] = ""

    # Empty string and string have 0 common subseq
    for col in range(1, len(s1) + 1):
        DP[0][col] = ""

    # String and empty string have 0 common subseq
    for row in range(1, len(s2) + 1):
        DP[row][0] = ""

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                DP[i][j] = DP[i - 1][j - 1] + s1[j - 1]
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1], key=len)

    for r in DP:
        print(r)

    return DP[-1][-1]


def LCS2(s1, s2):
    """
    M*2 space
    """

    DP = [[None for i in range(len(s1) + 1)] for j in range(2)]

    # No common subseq in two empty strings
    DP[0][0] = ""

    # Empty string and string have 0 common subseq
    for col in range(1, len(s1) + 1):
        DP[0][col] = ""

    # String and empty string have 0 common subseq
    for row in range(1, 2):
        DP[row][0] = ""

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                DP[1][j] = DP[0][j - 1] + s1[j - 1]
            else:
                DP[1][j] = max(DP[0][j], DP[1][j - 1], key=len)

    for r in DP:
        print(r)

    return DP[-1][-1]


s1 = "AGGTAB"
s2 = "GXTXAYB"

print(LCSRecursive(s1, s2, len(s1), len(s2)))
