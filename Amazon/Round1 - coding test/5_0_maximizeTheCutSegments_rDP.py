def maximizeTheCutsHelper(n, x, y, z, DP):
    if n == 0:
        return 0

    # print(n)
    if DP[n] != -1:
        return DP[n]

    a, b, c = 0, 0, 0

    if x <= n:
        a = maximizeTheCutsHelper(n - x, x, y, z, DP)
    if y <= n:
        b = maximizeTheCutsHelper(n - y, x, y, z, DP)
    if z <= n:
        c = maximizeTheCutsHelper(n - z, x, y, z, DP)

    DP[n] = 1 + max(a, b, c)

    return DP[n]


def maximizeTheCuts(n, x, y, z):
    # code here
    DP = [-1] * (n + 1)
    DP[0] = 0

    maximizeTheCutsHelper(n, x, y, z, DP)

    print(DP[n])


maximizeTheCuts(5, 5, 3, 2)
