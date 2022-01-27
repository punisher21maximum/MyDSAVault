def func(costs, W):
    """
    Knapsack:
    Given - weights, values, W
    total value - maximise
    total weight - <= W
    item instances - unlimited (bounded)

    This Q:
    Given costs array, where costs[i] is cost of item and
    'i' is the weight of item. When costs[i] = -1 means
    item does not exist.

    Given - weights (indices), values (costs), W
    total value - minimise
    total weight - exact W
    item instances - unlimited (unbounded)

    Modify questions to make it similar to knapsack-
    1. values array - created from costs array, excluding
    -1 values.
    2. weights array - created from index of costs where
    i is not -1
    3. W

    """
    values = []
    weights = []
    for i in range(len(costs)):
        if costs[i] != -1:
            values.append(costs[i])
            weights.append(i + 1)
    N = len(values)
    print(values, weights, W, N)
    DP = [[None for i in range(N + 1)] for j in range(W + 1)]

    for n in range(N + 1):
        for w in range(W + 1):
            if w == 0:
                DP[w][n] = 0
            elif n == 0:
                DP[w][n] = float("inf")
            elif weights[n - 1] <= w:
                DP[w][n] = min(DP[w][n - 1], values[n - 1] +
                               DP[w - weights[n - 1]][n])
            else:
                DP[w][n] = DP[w][n - 1]

    for d in DP:
        print(d)

    return DP[W][N] if DP[W][N] != float("inf") else -1


print(func([10, -1, -1, -1, -1], 5))
