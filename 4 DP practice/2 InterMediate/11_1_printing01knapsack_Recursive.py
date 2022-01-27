def func(W, weights, values, N, DP):
    """
    Same as - "10_01knapsack.py"

    Recursive

    Time O(N*W) | Space O(N*W)
    """
    print(N, W)
    if W == 0:
        DP[W][N] = 0
    elif N == 0:
        DP[W][N] = 0
    elif DP[W][N] is not None:
        return DP[W][N]
    elif weights[N - 1] <= W:
        DP[W][N] = max(
            values[N - 1] + func(W - weights[N - 1], weights, values, N - 1, DP),
            func(W, weights, values, N - 1, DP),
        )
    else:
        DP[W][N] = func(W, weights, values, N - 1, DP)

    return DP[W][N]


def printKnapsackItems(DP, weights, values, W, N):
    items = []
    r, c = W, N
    while DP[r][c] != 0:
        if DP[r][c] == DP[r][c - 1]:
            c -= 1
        else:
            items.append([weights[c - 1], values[c - 1]])
            c -= 1
            r -= weights[c - 1]
    print(items[::-1])


values = [6, 10, 12]
weights = [1, 2, 3]
W = 5
N = len(weights)
DP = [[None for i in range(N + 1)] for j in range(W + 1)]
print(func(W, weights, values, N, DP))
printKnapsackItems(DP, weights, values, W, N)
