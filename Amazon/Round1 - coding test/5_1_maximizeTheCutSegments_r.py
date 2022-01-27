def maximizeTheCutsHelper(n, x, y, z):
    if n == 0:
        return 0

    a, b, c = 0, 0, 0

    if x <= n:
        a = maximizeTheCutsHelper(n - x, x, y, z)
    if y <= n:
        b = maximizeTheCutsHelper(n - y, x, y, z)
    if z <= n:
        c = maximizeTheCutsHelper(n - z, x, y, z)

    return 1 + max(a, b, c)


def maximizeTheCuts(n, x, y, z):
    # code here
    print(maximizeTheCutsHelper(n, x, y, z))


maximizeTheCuts(5, 5, 3, 2)
