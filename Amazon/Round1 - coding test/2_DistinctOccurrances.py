def sequenceCount(arr1, arr2):
    # Code here
    len1, len2 = len(arr1), len(arr2)

    DP = [[None for i in range(len2 + 1)] for j in range(2)]

    for i in range(len1 + 1):
        print(i, i % 2, ":", i - 1, (i - 1) % 2)
        for j in range(len2 + 1):
            if j == 0:
                DP[i % 2][j] = 1
            elif i == 0:
                DP[i % 2][j] = 0
            elif arr1[i - 1] == arr2[j - 1]:
                DP[i % 2][j] = DP[(i - 1) % 2][j] + DP[(i - 1) % 2][j - 1]
            else:
                DP[i % 2][j] = DP[(i - 1) % 2][j]

    for r in DP:
        print(r)
    print(DP[-1][-1])
    return DP[-1][-1]


sequenceCount(
    "geeksforgeeks",
    "ges",
)
