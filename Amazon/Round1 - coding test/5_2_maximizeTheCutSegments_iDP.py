def maximizeTheCuts(n, x, y, z):
    # code here
    DP = [-1] * (n + 1)
    DP[0] = 0

    for i in range(n + 1):
        if DP[i] == -1:
            continue
        if i + x <= n:
            DP[i + x] = max(DP[i + x], DP[i] + 1)
        if i + y <= n:
            DP[i + y] = max(DP[i + y], DP[i] + 1)
        if i + z <= n:
            DP[i + z] = max(DP[i + z], DP[i] + 1)

    return 0 if DP[n] == -1 else DP[n]


maximizeTheCuts(5, 5, 3, 2)
