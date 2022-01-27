def LCSRecursive(s1, s2, s3, len1, len2, len3):

    if len1 == 0 or len2 == 0 or len3 == 0:
        return ""

    if s1[len1 - 1] == s2[len2 - 1] and s2[len2 - 1] == s3[len3 - 1]:
        return LCSRecursive(s1, s2, s3, len1 - 1, len2 - 1, len3 - 1) + s1[len1 - 1]
    else:
        return max(
            LCSRecursive(s1, s2, s3, len1 - 1, len2, len3),
            LCSRecursive(s1, s2, s3, len1, len2 - 1, len3),
            LCSRecursive(s1, s2, s3, len1, len2, len3 - 1),
            key=len,
        )


def LCS(s1, s2, s3):
    """
    M*N space
    """

    DP = [
        [[None for i in range(len(s3) + 1)] for j in range(len(s2) + 1)]
        for k in range(len(s1) + 1)
    ]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            for k in range(len(s3) + 1):
                if i == 0 or j == 0 or k == 0:
                    DP[i][j][k] = ""
                elif s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[k - 1]:
                    DP[i][j][k] = DP[i - 1][j - 1][k - 1] + s1[i - 1]
                else:
                    DP[i][j][k] = max(
                        DP[i - 1][j][k], DP[i][j - 1][k], DP[i][j][k - 1], key=len
                    )

    return DP[-1][-1][-1]


s1 = "AGGT12"
s2 = "12TXAYB"
s3 = "12XBA"

# print(LCSRecursive(s1, s2, s3, len(s1), len(s2), len(s3)))

print("lcs", LCS(s1, s2, s3))
