def factorial(N):
    if N in [0, 1]:
        return 1
    return N * factorial(N-1)


def numberOfWaysToTraverseGraph(width, height):

    numOfRights = width - 1
    numOfDowns = height - 1

    ways = factorial(numOfRights + numOfDowns) / \
        factorial(numOfRights) * factorial(numOfDowns)

    return ways
