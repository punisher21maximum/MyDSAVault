def func2(weights, values, W, N, DP):
    """ """
    print(W, N)
    if W == 0:
        DP[W][N] = 0
    elif N == 0:
        DP[W][N] = float("inf")
    elif DP[W][N] is not None:
        return DP[W][N]
    elif weights[N - 1] <= W:
        DP[W][N] = min(
            func2(weights, values, W, N - 1, DP),
            values[N - 1] + func2(weights, values, W - weights[N - 1], N, DP),
        )
    else:
        DP[W][N] = func2(weights, values, W, N - 1, DP)
    # print(DP)
    return DP[W][N]


def func(costs, W):

    values = []
    weights = []
    for i in range(len(costs)):
        if costs[i] != -1:
            values.append(costs[i])
            weights.append(i + 1)
    N = len(values)

    DP = [[None for i in range(N + 1)] for j in range(W + 1)]

    print(values, weights, W, N)
    result = func2(weights, values, W, N, DP)
    for d in DP:
        print(d)

    return result if result != float("inf") else -1


print(func([10, -1, -1, -1, -1], 5))
