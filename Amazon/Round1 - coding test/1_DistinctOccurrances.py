def sequenceCount(arr1, arr2):
    # Code here
    len1, len2 = len(arr1), len(arr2)

    DP = [[None for i in range(len2 + 1)] for j in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if j == 0:
                DP[i][j] = 1
            elif i == 0:
                DP[i][j] = 0
            # elif j > i:
            #     DP[i][j] = 0
            elif arr1[i - 1] == arr2[j - 1]:
                # print("here", i, j)
                DP[i][j] = DP[i - 1][j] + DP[i - 1][j - 1]
            else:
                # print("--diff", i, j, arr1[i - 1], arr2[j - 1], DP[i][j - 1])
                DP[i][j] = DP[i - 1][j]

    for r in DP:
        print(r)
    print(DP[-1][-1])
    return DP[-1][-1]


sequenceCount(
    "geeksforgeeks",
    "ges",
)
