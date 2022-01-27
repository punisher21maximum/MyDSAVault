def LRS(s1):

    DP = [[None for i in range(len(s1) + 1)] for j in range(len(s1) + 1)]

    # No common subseq in two empty strings
    DP[0][0] = 0

    # Empty string and string have 0 common subseq
    for col in range(1, len(s1) + 1):
        DP[0][col] = 0

    # String and empty string have 0 common subseq
    for row in range(1, len(s1) + 1):
        DP[row][0] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s1[i - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

    for r in DP:
        print(r)

    return DP[-1][-1]


s1 = "AGGTAB"
s1 = "GXTXAYB"
LRS(s1)
