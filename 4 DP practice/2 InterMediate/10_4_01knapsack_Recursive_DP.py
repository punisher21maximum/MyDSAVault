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


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
N = len(wt)
DP = [[None for i in range(N + 1)] for j in range(W + 1)]
print(func(W, wt, val, N, DP))
